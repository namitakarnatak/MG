#!/usr/bin/env python


from data_provisioning.src.common.core import log
from utilities.logging.core import log
from utilities.db.core import get_connection as getConnections
from utilities.memcache.core import MemcacheHandler
from data_provisioning.src.configs.core import SPECIAL_PRICE_BUNDLES,whatsapp_monthly_bundle_price
import traceback
from aapcn.src.voice.core import subscription_check,is_weekend,is_whitelisted,voice_offer_deletion
from aapcn.src.voice.config import (voice_bundles_to_be_recorded,
        offer_deletion_packages, whitelisting_packages,
        retailer_packages_check,weekend_check_packages,offer_id_check_ser500,offer_id_check_ser1000,promo_offer_id_check_bundle200,offer_id_check_funcool,
        offer_id_check_ser10000,offer_id_check_clubsmsmini,offer_id_check_clubsms)
from aapcn.src.volume.config import (mymeg10_flag_check,mymeg50_flag_check,whatsapp_monthly_flag_offer_id,offer_id_check_iser600,offer_id_check_iser2000,
        offer_id_check_iser3000,offer_id_check_iser6000,offer_id_check_iser10000,offer_id_check_iser30000,offer_id_check_iser80000,offer_id_check_iser120000)
from data_provisioning.src.core.config import (product_name_iser600,product_name_iser2000,product_name_iser3000,product_name_iser6000,product_name_iser10000,
        product_name_iser30000,product_name_iser80000,product_name_iser120000)

def debug(txt):
    from config import debug
    if debug:
        txt = 'DEBUG: %s' %(str(txt))
        return txt

def dealer_is_whitelisted(resources, msisdn):
    '''
    checks whether a number is whitelisted
    as a me2u dealer
    '''
    trans_id = resources['parameters']['transactionId']
    sql = '''select msisdn, active from dealer_me2u_whitelist
          where msisdn = :msisdn'''
    con = getConnections(resources)
    cursor = con.cursor()
    try:
        cursor.execute(sql, {'msisdn':msisdn})
        details = cursor.fetchall()
    except Exception, err:
        log(resources, traceback.format_exc(), 'error')
        return False
    else:
        if details:
            info = "trans_id: %s, msisdn: %s, dealer dets: %s" %(
                    trans_id, msisdn, str(details))
            log(resources, info, 'debug')
            active = details[0][1]
            if int(active) ==1:
                return True
            else:
                return False
        else:
            return False

def determine_param(func):
    '''
    a decorator that returns a new parameter
    that changes based on a particular condition
    Right now, return the price of a bundle dependent on whether 
    the msisdn is whitelisted
    '''
    def __inner(resources):
        package_id = resources['parameters']['packageId']
        trans_id = resources['parameters']['transactionId']
        msisdn  = resources['parameters']['msisdn']

        resources = func(resources)

        if package_id in SPECIAL_PRICE_BUNDLES:
            if dealer_is_whitelisted(resources, msisdn):
                new_price = SPECIAL_PRICE_BUNDLES[package_id]
                info = "trans_id: %s msisdn: %s NEW PRICE: %s, package_id: %s" %(
                        trans_id, msisdn, str(new_price), package_id)
                log(resources, info, 'debug')
                resources['parameters']['price'] = new_price

        return resources
    return __inner


@determine_param
def getPackageDetails(resources):
    ''' retrieves the packageId,cost and other details from a DB call '''
    packageId = resources['parameters']['packageId']
    transaction_id = resources['parameters']['transactionId']
    sql = '''
          select table1.offer_id, table3.package_category_name, table1.volume,
          table1.validity, table2.package_cost, table2.package_name, table2.refill_id, 
          table2.trans_amount, table1.uc, table1.ut from new_provisioning_packages table1,
          new_packages table2, provision_package_category table3 where 
          table2.provisioning_packages_id = table1.id and table2.id =:packageId 
          and table3.id=table1.package_category_id '''
    sql = sql.strip()
    try:
        cache_key = 'package_details_%s' % str(packageId)
        details = MemcacheHandler().get( cache_key )
        log( resources, '%s - packageDetails from cache - %s' % (transaction_id, details), 'debug' )
        
        if not details:
            log(resources, "get package details: cache miss!! package_id %s" % (packageId), 'debug')
            log(resources, "fetching from DB", 'debug')
            connection = getConnections(resources)
            log(resources, "got connection", 'debug')
            cursor = connection.cursor()
            cursor.execute(sql,{'packageId':packageId})
            details = cursor.fetchall()
            # put in cache
            try:
                MemcacheHandler().set(cache_key, details)
            except Exception, err:
                caching_err = 'error on caching - %s' % (str(err))
                log( resources, caching_err, 'error' )
                pass

            cursor.close()
    except Exception,e:
        error = ('operation: getPackageDetails, Desc: Could not fetch package details' +
                'for packageID:%s,Error:%s' %(str(packageId),str(e)))
        error = e
        log(resources, error, 'error')
        try:
            cursor.close()
        except:
            pass
        raise e

    else:
        if details:
            log(resources, str(details), 'debug')
            try:
                packageDetails = {}
                packageDetails['offer_id'] = details[0][0]
                packageDetails['package_category_name']= details[0][1]
                try:
                    packageDetails['data_volume'] =  int(details[0][2])
                except Exception, err:
                    packageDetails['data_volume'] =  details[0][2]
                packageDetails['data_validity'] =  details[0][3]
                packageDetails['package_cost'] = details[0][4]
                packageDetails['package_name'] = details[0][5]
                packageDetails['refill_id'] = details[0][6]
                packageDetails['trans_amount'] = details[0][7]
                packageDetails['uc'] = details[0][8]
                packageDetails['ut'] = details[0][9]

                resources['parameters']['packageDetails'] = packageDetails
                parameters = resources['parameters']
                parameters['validity'] = packageDetails['data_validity']
                parameters['package_category_name'] = packageDetails['package_category_name']
                parameters['volume'] = packageDetails['data_volume']
                parameters['offer_id'] = packageDetails['offer_id']
                parameters['cost'] = '%s' %str(packageDetails['package_cost'])
                parameters['price'] = parameters['cost']
                parameters['package_name'] = packageDetails['package_name']
                parameters['refill_id'] = packageDetails['refill_id']
                parameters['trans_amount'] = packageDetails['trans_amount']
                parameters['uc'] = packageDetails['uc']
                parameters['ut'] = packageDetails['ut']
                parameters['externalData2'] = parameters['package_name']
                if 'external_Data1' in parameters:
                    parameters['externalData1'] = parameters['external_Data1']
                if 'external_Data2' in parameters:
                    parameters['externalData2'] = parameters['external_Data2']

                resources['parameters'] = parameters
                log(resources, resources, 'info')
            except Exception,e:
                error = ('operation GetPackageDetails, Desc: error inserting details into '+ 
                        'a dict,Error:%s' %(str(e)))
                log(resources, str(traceback.format_exc()), 'error')
                print error
        else:
            resources['provisionStatus'] = '-1'
            resources['desc'] = 'No such Package'
    log(resources, resources['parameters'], 'debug')
    return resources


def check_bill_plan_whitelist(resources, msisdn):
    '''
    checks whether a number is whitelisted
    for testing reduces rates billing plan
    '''
    trans_id = resources['parameters']['transactionId']
    sql = '''select msisdn from bill_plan_whitelist_test
          where msisdn = :msisdn'''
    con = getConnections(resources)
    cursor = con.cursor()
    try:
        cursor.execute(sql, {'msisdn':msisdn})
        details = cursor.fetchall()
        cursor.close()
    except Exception, err:
        cursor.close()
        log(resources, traceback.format_exc(), 'error')
        return False
    else:
        if len(details) > 0:
            info = ("trans_id: %s, msisdn: %s is whitelisted for reduced rate billing" % (trans_id, msisdn))
            log(resources, info, 'debug')
            return True
        else:
            return False

def billSubscriber(resources):
    from utilities.data_ucip.core import bill_subscriber
    from utilities.data_ucip.core import get_offers
    from mg_data_interface.src.configs.config import BILL_PLAN
    from config import bonus
    parameters = resources['parameters']
    packageId = resources['parameters']['packageId']
    msisdn = resources['parameters']['msisdn']

    if 'args' in parameters:
        if 'is_renew' in (parameters['args']):
            log(resources, "is_renew", 'info')
            parameters['externalData1'] = parameters['package_name'] + '_autorenewal'
            parameters['externalData2'] = 'auto_renewal' + '_' + parameters['beneficiary']
        elif 'can_renew' in (parameters['args']):
            args = parameters['args']
            if args['can_renew'] == '1':
                parameters['externalData1'] = parameters['package_name'] + '_autorenewal'
                parameters['externalData2'] = 'auto_renewal' + '_' + parameters['beneficiary']
            else:
                parameters['externalData1'] = parameters['package_name']
                parameters['externalData2'] = 'oneoff' + '_' + parameters['beneficiary']

        elif parameters['transaction_type'] == 'B':
            parameters['externalData1'] = parameters['package_name']
            parameters['externalData2'] = 'oneoff'+ '_'+  parameters['beneficiary']

        else:
            parameters['externalData1'] = parameters['package_name']
            parameters['externalData2'] = 'oneoff' + '_' + parameters['beneficiary']

    if parameters.has_key('external_Data1'):
       parameters['externalData1'] = parameters['external_Data1']
    if parameters.has_key('external_Data2'):
       parameters['externalData2'] = parameters['external_Data2']

    if 'my_meg_20_night_tag' in parameters:
        parameters['externalData1'] = (parameters['externalData1']).replace(parameters['package_name'], parameters['my_meg_20_night_tag'])
    
    if int(parameters['price']) > 0:
        #whitelisted = check_bill_plan_whitelist(resources, msisdn)
        if int(packageId) in BILL_PLAN:
            resp = get_offers(resources)
            if resp['responseCode'] == 0:
                offer_information = resp['offerInformation']
                bill_plan = BILL_PLAN[int(packageId)]
                cost = bill_plan['cost']
                bonus_offer_id = bill_plan['bonus_offer_id']
                # offer_id  = bill_plan['offer_id']
                # refill_id = bill_plan['refill_id']
                offer_found = False
                for offer in offer_information:
                    if offer['offerID'] == bonus_offer_id:
                        offer_found = True
                        break
                if offer_found and bonus:
                    resources['parameters']['price'] = str(cost)
                    # resources['parameters']['offer_id'] = offer_id
                    # resources['parameters']['refill_id'] = refill_id
                    resources['parameters']['externalData1'] = parameters['package_name'] + '_promo'
                    resources['parameters']['externalData2'] = 'oneoff' + '_' + parameters['beneficiary']
                    resp = bill_subscriber(resources)
                    info_msg = 'REDUCED PACKAGE COST: %s: %s, %s, bill_plan: %s' % (str(msisdn), str(resources['parameters']['transactionId']), str(resp['responseCode']), str(bill_plan))
                    log(resources, info_msg, 'info')
                    msg = 'BILLING: %s, %s' % (msisdn, str(resp))
                    log(resources, msg, 'info')
                    if resp['responseCode'] == 0:
                        return True
                    else:
                        return False
                else:
                    resp = bill_subscriber(resources)
                    info_msg = 'BILLING NORMAL PRICE:: %s-%s-%s' % (msisdn, str(resources['parameters']['transactionId']),
                            str(resp['responseCode']))
                    log(resources, info_msg, 'info')
                    msg = 'BILLING: %s, %s' % (msisdn, str(resp))
                    log(resources, msg, 'info')
                    if resp['responseCode'] == 0:
                        return True
                    else:
                        return False
            else:
                resp = bill_subscriber(resources)
                info_msg = 'BILLING NORMAL PRICE:: %s-%s-%s' % (msisdn, str(resources['parameters']['transactionId']),
                        str(resp['responseCode']))
                log(resources, info_msg, 'info')
                msg = 'BILLING: %s, %s' % (msisdn, str(resp))
                log(resources, msg, 'info')
                if resp['responseCode'] == 0:
                    return True
                else:
                    return False
        else:
            resp = bill_subscriber(resources)
            info_msg = 'BILLING NORMAL PRICE:: %s-%s-%s' % (msisdn, str(resources['parameters']['transactionId']),
                    str(resp['responseCode']))
            log(resources, info_msg, 'info')
            msg = 'BILLING: %s, %s' % (msisdn, str(resp))
            log(resources, msg, 'info')
            if resp['responseCode'] == 0:
                return True
            else:
                return False
    else:
        return True

def processRequest(resources):
    '''processes the provisioning request for the given subscriber'''
    from data_provisioning.src.configs.core import status
    from json import dumps
    from utilities.metrics.core import beat
    from aapcn.src.common.core import get_data_profile
    from aapcn.src.voice.core import is_whitelisted

    transactionId = resources['parameters']['transactionId']
    transaction_type = resources['parameters']['transaction_type']

    if transaction_type =='C':
        msisdn = resources['parameters']['b_msisdn']
        benefactor = msisdn
        log(resources, "CC INITIATED-BENEFACTOR msisdn: %s" % (str(benefactor)), 'info')
        beneficiary = resources['parameters']['b_msisdn']
        log(resources, "CC INITIATED-BENEFICIARY msisdn: %s" % (str(beneficiary)), 'info')
        cc_msisdn = resources['parameters']['msisdn']
        resources['parameters']['cc_msisdn'] = cc_msisdn

    else:
        msisdn = resources['parameters']['msisdn']
        benefactor = msisdn
        log(resources, "BENEFACTOR msisdn: %s" % (str(benefactor)), 'info')

        beneficiary = resources['parameters']['b_msisdn']
        log(resources, "BENEFICIARY msisdn: %s" % (str(beneficiary)), 'info')


    #add a parameter  a mssisdn just because
    resources['parameters']['a_msisdn'] = benefactor

    '''
    1) always bill the benefactor
    2) always provision the beneficiary
    '''
    #make the beneficiary to be the main msisdn
    resources['parameters']['msisdn'] = beneficiary

    resources['parameters']['benefactor'] = benefactor
    resources['parameters']['beneficiary'] = beneficiary

    packageId = resources['parameters']['packageId']
    parameters = resources['parameters']
    resources['parameters'] = parameters
    if int(packageId) != 0:
        resources = getPackageDetails(resources)
        packageDetails = resources['parameters']['packageDetails']
        packageCategoryName = packageDetails['package_category_name'] 
        group = packageCategoryName
        packageName = resources['parameters']['package_name']
        log(resources, packageName, 'debug')
        if packageCategoryName == 'volume':
            from aapcn.src.volume.core import provisionBundle,checkConflictingBundles,getBalance,is_barred,is_barred_MyMeg5,is_bonus_offer_bundle_check
        elif packageCategoryName == 'router':
            from aapcn.src.routers.core import provisionBundle,checkConflictingBundles,getBalance,is_barred
        elif packageCategoryName == 'meg_15':
            from aapcn.src.meg_fifteen.core import provisionBundle,checkConflictingBundles,getBalance,is_barred
        elif packageCategoryName == 'fun':
            from aapcn.src.sacc_fun.core import provisionBundle,checkConflictingBundles,getBalance,is_barred
            log(resources, 'loaded sacc module', 'debug')
        elif packageCategoryName == 'unlimited':
            from aapcn.src.unlimited.core import provisionBundle,checkConflictingBundles,getBalance,is_barred

        elif packageCategoryName == 'telescopic':
            from aapcn.src.telescopic.core import (provisionBundle, checkConflictingBundles, getBalance,
                    check_subscription_time, update_package_details, telescopic_subscription_limit, is_barred)
            getBalance(resources)
            update_package_details(resources)
        elif packageCategoryName == 'regional':
            from aapcn.src.regional.core import provisionBundle,checkConflictingBundles,getBalance,is_barred
        elif packageCategoryName == 'OTI':
            from aapcn.src.oti.core import provisionBundle,checkConflictingBundles,getBalance,is_barred
        elif packageCategoryName == 'voice':
            from aapcn.src.voice.core import provisionBundle,checkConflictingBundles,getBalance,is_barred,is_time_barred,voice_offer_deletion,is_whitelisted,is_barred_Bundle200,is_bonus_bundle_check

        resources = getBalance(resources)
        log(resources, 'get balance done','debug')

        conflicting_bundle = checkConflictingBundles(resources)
        log(resources, 'conflicting: %s msisdn: %s bundle: %s' % (str(conflicting_bundle)
            ,beneficiary,
            packageName),'debug')

        is_barred = is_barred(resources)
        log(resources, 'is barred: %s msisdn: %s bundle: %s' % (str(is_barred)
            ,beneficiary,
            packageName),'debug')
        
            
        within_time_limits = True
        if packageCategoryName == 'telescopic':
            within_time_limits = check_subscription_time(resources)

        exceeded_subscription = False
        if packageCategoryName == 'telescopic':
            exceeded_subscription = telescopic_subscription_limit(resources)

        my_meg5_barred = False
        if parameters['package_name'] == 'MyMeg 5':
            my_meg5_barred = is_barred_MyMeg5(resources)
            log(resources, 'MyMeg 5 barred: %s msisdn: %s' % (str(my_meg5_barred),beneficiary),'debug')

        #mix500_barred = False
        #if parameters['package_name'] == 'Mix500':
            #mix500_barred = is_barred_Mix500(resources)
            #log(resources, 'Mix500 barred: %s msisdn: %s' % (str(mix500_barred),beneficiary),'debug')

        if parameters['package_name'] == 'Whatsapp_Monthly':
            whatsapp_monthly_bonus = is_bonus_offer_bundle_check(resources,whatsapp_monthly_flag_offer_id)
            log(resources, 'Whatsapp Monthly barred: %s msisdn: %s' % (str(whatsapp_monthly_barred),beneficiary),'debug')
            package_id = resources['parameters']['packageId']
            if package_id in whatsapp_monthly_bundle_price and whatsapp_monthly_bonus == True:
               whatsapp_new_price = whatsapp_monthly_bundle_price[package_id]
               resources['parameters']['price'] = whatsapp_new_price
               log(resources, 'Whatsapp Monthly bundle NEW PRICE: %s msisdn: %s package_id:%s' % (str(whatsapp_new_price),beneficiary,package_id),'debug')

        bundle200_barred = False
        if parameters['package_name'] == 'Ser@200':
            bundle200_barred = is_barred_Bundle200(resources)
            log(resources, 'Ser@200 barred: %s msisdn: %s' % (parameters['flag_message_override'],beneficiary),'debug')
            if bundle200_barred == False:
                parameters['flag_message_override'] = is_bonus_bundle_check(resources,promo_offer_id_check_bundle200)
                log(resources, 'Ser@200 Bonus Allowed: %s msisdn: %s' % (parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == 'Ser@500':
            parameters['flag_message_override'] = is_bonus_bundle_check(resources,offer_id_check_ser500)
            log(resources, 'Ser@500 Bonus Allowed: %s msisdn: %s' % (parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == 'Ser@1000':
            parameters['flag_message_override'] = is_bonus_bundle_check(resources,offer_id_check_ser1000)
            log(resources, 'Ser@1000 Bonus Allowed: %s msisdn: %s' % (parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == 'FUN COOL':
            parameters['flag_message_override'] = is_bonus_bundle_check(resources,offer_id_check_funcool)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == 'Ser@10000':
            parameters['flag_message_override'] = is_bonus_bundle_check(resources,offer_id_check_ser10000)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == 'ClubSMS-Mini':
            parameters['flag_message_override'] = is_bonus_bundle_check(resources,offer_id_check_clubsmsmini)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == 'ClubSMS':
            parameters['flag_message_override'] = is_bonus_bundle_check(resources,offer_id_check_clubsms)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == 'I-Ser@200':
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,mymeg10_flag_check)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == 'I-Ser@1000':
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,mymeg50_flag_check)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == product_name_iser600:
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,offer_id_check_iser600)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == product_name_iser2000:
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,offer_id_check_iser2000)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == product_name_iser3000:
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,offer_id_check_iser3000)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == product_name_iser6000:
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,offer_id_check_iser6000)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == product_name_iser10000:
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,offer_id_check_iser10000)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == product_name_iser30000:
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,offer_id_check_iser30000)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == product_name_iser80000:
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,offer_id_check_iser80000)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')

        if parameters['package_name'] == product_name_iser120000:
            parameters['flag_message_override'] = is_bonus_offer_bundle_check(resources,offer_id_check_iser120000)
            log(resources, '%s Bonus Allowed: %s msisdn: %s' % (parameters['package_name'],parameters['flag_message_override'],beneficiary),'debug')


        voice_time_barred = False
        whitelisted = True
        if packageCategoryName == 'voice':
            voice_time_barred = is_time_barred(resources)
            if int(packageId) in whitelisting_packages:
                whitelisted = is_whitelisted(resources)
                log(resources, 'MSISDN: %s is Whitelisted for %s - %s' % (beneficiary,str(resources['parameters']['package_name']),str(whitelisted)),'debug')


        if (is_barred == False) and within_time_limits and (my_meg5_barred == False) and (bundle200_barred == False) and (voice_time_barred == False) and whitelisted:
            if (is_barred == False) and exceeded_subscription == False:
                if (conflicting_bundle == False):
                    #JUST BEFORE WE BILL WE ENSURE THE MSISDN IS SET BACK TO THE BENEFACTOR
                    resources['parameters']['msisdn'] = benefactor
                    
                    if int(packageId) == 32: # MyMeg20Night
                        from datetime import datetime
                        hour = datetime.now().hour
                        if hour >= 0 and hour < 5:
                            (resources['parameters'])['my_meg_20_night_tag'] = 'MyMeg 20 NIGHT 2'
                        else:
                            (resources['parameters'])['my_meg_20_night_tag'] = 'MyMeg 20 NIGHT 1'

                    if billSubscriber(resources):
                        (resources['parameters'])['packageName'] = packageName
                        #HAVING BILLED THE BENEFACTOR, WE RESET THE MSISDN TO THE BENEFICIARY FOR PROVISIONING
                        resources['parameters']['msisdn'] = beneficiary
                        #VOICE OFFER DELETION ALWAYS SUCCEEDS
                        if (int(packageId) in offer_deletion_packages) and voice_offer_deletion(resources):
                            try:
                                resources = provisionBundle(resources)
                            except Exception, err:
                                log(resources, traceback.format_exc(), 'error')
                                try:
                                    refill_response = resources['parameters']['refill_resp']
                                except Exception, KeyError:
                                    refill_response = None

                                if refill_response is not None:
                                    # Response code 0 added incase refill exception is due to updateUcUt failure
                                    if str(resources['parameters']['refill_resp']) in ['100','999','0']:
                                        (resources['parameters'])['status'] = status['IN_defined_refill_error']
                                    else:
                                        (resources['parameters'])['status'] = status['Undefined_refill_error']
                                else:
                                    (resources['parameters'])['status'] = status['Undefined_refill_error']

                            else:
                                (resources['parameters'])['status'] = status['successfullyProvisioned']
                                try:
                                    metric_name = packageName.replace(' ','_')
                                    beat('application.internet.%s' %metric_name)
                                except Exception, err:
                                    pass
                        else:
                            try:
                                resources = provisionBundle(resources)
                            except Exception, err:
                                log(resources, traceback.format_exc(), 'error')
                                try:
                                    refill_response = resources['parameters']['refill_resp']
                                except Exception, KeyError:
                                    refill_response = None

                                if refill_response is not None:
                                    # Response code 0 added incase refill exception is due to updateUcUt failure
                                    if str(resources['parameters']['refill_resp']) in ['100','999','0']:
                                        (resources['parameters'])['status'] = status['IN_defined_refill_error']
                                    else:
                                        (resources['parameters'])['status'] = status['Undefined_refill_error']
                                else:
                                    (resources['parameters'])['status'] = status['Undefined_refill_error']

                            else:
                                (resources['parameters'])['status'] = status['successfullyProvisioned']
                                try:
                                    metric_name = packageName.replace(' ','_')
                                    beat('application.internet.%s' %metric_name)
                                except Exception, err:
                                    pass

                    else:
                        (resources['parameters'])['status'] = status['insufficientFunds']
                else:
                    resources['parameters']['status'] = status['packageConflict']
            else:
                resources['parameters']['status'] = status['exceed_sub_limit']
        else:
            if my_meg5_barred:
                resources['parameters']['status'] = status['isBarred_MyMeg5']
            #elif mix500_barred:
                #resources['parameters']['status'] = status['isBarred_Mix500']
            elif bundle200_barred:
                resources['parameters']['status'] = status['isBarred_Bundle200']
            elif not within_time_limits or is_barred:
                resources['parameters']['status'] = status['isBarred']
            elif voice_time_barred:
                resources['parameters']['status'] = status['voice_time_restriction']
            #elif not offer_deleted:
            #    resources['parameters']['status'] = status['error']
            elif not whitelisted:
                resources['parameters']['status'] = status['not_whitelisted']
            else:
                resources['parameters']['status'] = status['time_restriction']

    else:
        resources['parameters']['package_name'] = 'balance'
        resources['parameters']['package_category_name'] = 'volume'
        try:
            #from aapcn.src.volume.core import getBalance
            resources = get_data_profile(resources)
            #resources = getBalance(resources)
        except Exception, err:
            log(resources, traceback.format_exc(), 'error')
            (resources['parameters'])['status'] = status['error']
        else:
            (resources['parameters'])['status'] = status['successfullyProvisioned']

    #HAVING GOTTEN OUR RESPONSE WE RESET THINGS TO THE WAY THEY WERE
    if resources['parameters']['transaction_type'] == 'C':
        resources['parameters']['msisdn'] = cc_msisdn
    else:
        resources['parameters']['msisdn'] = benefactor
    resources['parameters']['b_msisdn'] = beneficiary

    parameters = resources['parameters']
    transactionId = parameters['transactionId']
    info = json_dump(resources)['parameters']['resp']
    log(resources, "Final resources:%s"%str(info), 'info')
    resp = dumps(json_dump(resources)['parameters']['resp'],default=date_handler)
    response = '%s' %(str(resp))
    return response

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def json_dump (resources):
    '''gets parameters from resources
    and creates a json
    '''
    parameters = resources['parameters']
    balance_info = parameters['balance']
    msisdn = parameters['msisdn']
    b_msisdn = parameters['b_msisdn']
    status = parameters['status']
    transaction_id = parameters['transactionId']
    packageId = parameters['packageId']
    transaction_type = parameters['transaction_type'] 
    name = parameters['package_name']
    args = parameters['args']
    flag_message_override = parameters['flag_message_override']
    try:
        refill_resp = parameters['refill_resp']
    except Exception, KeyError:
        refill_resp = 'None'

    if 'parabole_nxt_month_expiry' in parameters:
        parabole_nxt_month_expiry = parameters['parabole_nxt_month_expiry']
        resp = {'msisdn': msisdn,
                'status': status,
                'b_msisdn': b_msisdn,
                'package_id': packageId,
                'transactionId' : transaction_id,
                'transaction_type': transaction_type,
                'args':args,
                'name':name,
                'balance' : balance_info,
                'parabole_nxt_month_expiry':parabole_nxt_month_expiry,
                'Refill_resp':refill_resp}

    else:
        resp = {'msisdn': msisdn,
                'status': status,
                'b_msisdn': b_msisdn,
                'package_id': packageId,
                'transactionId' : transaction_id,
                'transaction_type': transaction_type,
                'args':args,
                'name':name,
                'balance' : balance_info,
                'Refill_resp':refill_resp,
                'flag_message_override' : flag_message_override}
    parameters['resp'] = resp
    return resources

def new_bill_plan(resources, packageId, msisdn):
    from utilities.data_ucip.core import bill_subscriber
    from utilities.data_ucip.core import get_offers
    from mg_data_interface.src.configs.config import BILL_PLAN
    whitelisted = check_bill_plan_whitelist(resources, msisdn)
    if int(packageId) in BILL_PLAN and whitelisted:
        resp = get_offers(resources)
        if resp['responseCode'] == 0:
            offer_information = resp['offerInformation']
            bill_plan = BILL_PLAN[int(packageId)]
            cost = bill_plan['cost']
            offer_id = bill_plan['offer_id']
            for offer in offer_information:
                if offer['offerID'] == offer_id:
                    resources['parameters']['price'] = str(cost)
                    resp = bill_subscriber(resources)
                    info_msg = 'REDUCED PACKAGE COST: %s: %s, %s, bill_plan: %s' % (str(msisdn), str(resources['parameters']['transactionId']), str(resp['responseCode']), str(bill_plan))
                    log(resources, info_msg, 'info')
                    if resp['responseCode'] == 0:
                        return True
                    else:
                        return False
        else:
            return False

