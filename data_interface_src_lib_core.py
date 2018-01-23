"""
core data provisioning functions
"""
from mg_data_interface.src.configs.config import ALLOWED_PREFIXES
from mg_data_interface.src.configs.config import PROVISION_URL, BALANCE_URL,ME2U_URL
from mg_data_interface.src.configs.config import FREQUENCY
from mg_data_interface.src.configs.config import MESSAGES as messages
from mg_data_interface.src.configs.config import SOCIAL as social
from mg_data_interface.src.configs.config import KOZY_PACKAGE_ID as kozy_id
from mg_data_interface.src.configs.config import REGIONAL_ID as reg_id
from mg_data_interface.src.configs.config import SOCIAL_PKGS as social_pkgs
from mg_data_interface.src.configs.config import SOCIAL_FB_WEEKLY
from mg_data_interface.src.configs.config import SOCIAL_TW_WEEKLY
from mg_data_interface.src.configs.config import SOCIAL_WA_WEEKLY
from mg_data_interface.src.configs.config import UNLIMITED_ID
from mg_data_interface.src.configs.config import BONUSMEG250 
from mg_data_interface.src.configs.config import BONUSMEG500 
from mg_data_interface.src.configs.config import BONUSGIG1 
from mg_data_interface.src.configs.config import BONUSBUNDLES
from mg_data_interface.src.configs.config import NEWMSGBUNDLES
from mg_data_interface.src.configs.config import MY_MEG_10
from mg_data_interface.src.configs.config import VALIDITY as validity
from mg_data_interface.src.configs.config import DA_FACTOR
from mg_data_interface.src.configs.config import MSISDN_LENGTH
from mg_data_interface.src.configs.config import SUCCESS_HIT, FAIL_HIT
from mg_data_interface.src.lib.custom_loggers import twistd_logger as log
from mg_data_interface.src.configs.config import ACCOUNT_ID, AUTH_KEY
from mg_data_interface.src.configs.config import ROUTING_KEY
from mg_data_interface.src.configs.config import SERVICE_ID
from mg_data_interface.src.configs.config import NOW_SMS_EVENT_ID
from mg_data_interface.src.configs.config import RENEW_EVENT_ID
from mg_data_interface.src.configs.config import THIRD_DAY_SMS_EVENT_ID
from mg_data_interface.src.configs.config import DAY_OF_RENEWAL_EVENT_ID
from mg_data_interface.src.configs.config import SPECIAL_NUMBERS
from mg_data_interface.src.configs.config import DATA_USAGE
from mg_data_interface.src.configs.config import bonusMsgs
from mg_data_interface.src.configs.config import newMsgs
from aapcn.src.voice.config import service_class_check_packages
from mg_data_interface.src.lib.database_handler import DataCDR
from mg_data_interface.src.lib.con import generate_connection
from utilities.ucip.core import get_balance_and_date
from utilities.metrics.core import count
from utilities.sms.core import send_message
from utilities.common.client import Publisher
from utilities.db.core import get_connection

from ussd.services.common.language.core import getLanguage
from events.core.core import create_event as enqueue_active_events
from events.core.core import dequeue_active_events

from urllib2 import urlopen, Request
from urllib import urlencode
from ast import literal_eval
from datetime import datetime, timedelta

import traceback
import time
import random
import json
from time import strftime

res = generate_connection()


def convert_da_time(da_time):
    '''
    returns a date time object given a dedicated account time string
    '''
    da_time = da_time[:19]
    try:
        fmt = '%Y-%m-%dT%H:%M:%S'
        expiry_date = datetime.fromtimestamp(time.mktime( \
                time.strptime(str(da_time),fmt)))
    except OverflowError, e:
        expiry_date = datetime(9999, 12, 31, 0, 0)

    return expiry_date


def generate_air_tagging_params(resources, trans_type):
    '''
    generates a transaction_id for air transactions
    alongside other parameters required to tag transactions
    on air
    '''
    parameters = resources['parameters']
    parameters['externalData1'] = 'broad_band'
    #parameters['externalData1'] = 'data_bundle_renewal'
    parameters['externalData2'] = trans_type

    trans_id = random.randrange(1, 1000000000)
    trans_id = str(trans_id)
    parameters['transactionId'] = trans_id

    trans_id = random.randrange(1, 1000000000)
    trans_id = str(trans_id)
    parameters['transactionId'] = trans_id

    trans_id = random.randrange(1, 1000000000)
    trans_id = str(trans_id)
    parameters['transactionId'] = trans_id
    resources['parameters'] = parameters
    return resources

def generate_req_id():
    '''
    returns a request id
    '''
    return str(random.randrange(1, 10000000000))


def b_number_is_valid(b_number):
    '''
    validates the b number
    returns true or false
    '''
    resources = {}
    parameters = {}
    resources['parameters'] = parameters
    resources = generate_air_tagging_params(resources, "validate_number")
    resources['parameters']['msisdn'] = '261'+b_number[-9:]

    try:
        resp = get_balance_and_date(resources)
    except IOError, err:
        log('ERROR', "op|| b_number is valid %s " %(str(err)))
        return False
    except Exception, err:
        log('ERROR', "op|| b_number is valid %s " %(str(err)))
        return False
    else:
        log('INFO', "%s, IN resp code %s" %(str(resources['parameters']['msisdn']),str(resp['responseCode'])))
        if resp['responseCode'] == 0:
            return True
        else:
             return False

def process_me2u_request( params):
    '''
    enqueues a me2u request
    '''
    import traceback
    try:
        parameters = {}
        args = {}
        parameters['msisdn'] = params['msisdn']
        parameters['b_number'] = '261'+params['b_number']
        parameters['amount'] = params['amount']
        parameters['pin'] = params['pin']
        parameters['lang'] = params['lang']
        parameters['unit'] = params['package_id']


        params = urlencode(parameters)
        url = ME2U_URL
        resp = urlopen(Request(url, params))

    except IOError, err:
        error = 'operation: IO enqueue request, desc: \
                failed to submit me2u request %s: %s, error:%s'\
                % (parameters['msisdn'], parameters['b_number'], str(err))
        print error
        print traceback.format_exc()
        raise err

    except Exception, err:
        error = 'operation: n - enqueue request, desc: \
                failed to submit me2u request %s: %s, error: %s'\
                % (parameters['msisdn'], parameters['b_number'], str(err))
        print error
        raise err
    else:
        pass


def enqueue_provision_request(package, msisdn, b_msisdn, can_renew, is_web, is_night, r_key = ROUTING_KEY):
    '''
    enqueues a provisioning request
    '''
    import traceback
    flag_message_override = 'False'
    transaction_type = 'A'
    if package != "stop_auto":
        if b_msisdn == None:
            b_msisdn = msisdn
        else:
            transaction_type = 'B'
            b_msisdn = '261'+b_msisdn
        try:
            parameters = {}
            args = {}
            parameters['msisdn'] = msisdn
            parameters['b_msisdn'] = b_msisdn
            parameters['packageId'] = package
            parameters['authKey'] = AUTH_KEY
            parameters['accountId'] = ACCOUNT_ID
            parameters['transaction_type'] = transaction_type
            parameters['requestId'] = generate_req_id()
            parameters['flag_message_override'] = flag_message_override

            args['routing_key'] = r_key
            args['can_renew'] = can_renew
            if is_night:
                args['is_night'] = "True"
            else:
                args['is_night'] = 'False'

            print str(is_web) + "IS WEB"

            if is_web != None:
                req_id = is_web
                args['web_id'] = req_id

            parameters['args'] = str(args)
            
            params = urlencode(parameters)
            url = PROVISION_URL
            resp = urlopen(Request(url, params))

        except IOError, err:
            error = 'operation: IO enqueue request, desc: \
                    failed to submit provisioning request %s: %s, error:%s'\
                    % (msisdn, package, str(err))
            print error
            print traceback.format_exc()
            raise err
                    
        except Exception, err:
            error = 'operation: n - enqueue request, desc: \
                    failed to submit provisioning request %s: %s, error: %s'\
                    % (msisdn, package, str(err))
            print error
            raise err
        else:
            return (resp.info()).get('Transaction-Id')
    else:
        try:
            resp = disable_renewal(msisdn)
        except Exception, err:
            print traceback.format_exc()
        else:
            return resp

def enqueue_cc_provision_request(package, msisdn, cust_msisdn, can_renew, is_web, is_night, r_key = ROUTING_KEY):
    '''
    enqueues a provisioning request
    '''
    import traceback
    if package != "stop_auto":
        transaction_type = 'C'
        cust_msisdn = '261'+cust_msisdn[-9:]
        try:
            parameters = {}
            args = {}
            parameters['msisdn'] = msisdn
            parameters['b_msisdn'] = cust_msisdn
            parameters['packageId'] = package
            parameters['authKey'] = AUTH_KEY
            parameters['accountId'] = ACCOUNT_ID
            parameters['transaction_type'] = transaction_type
            parameters['requestId'] = generate_req_id()

            args['routing_key'] = r_key
            args['can_renew'] = can_renew
            if is_night:
                args['is_night'] = "True"
            else:
                args['is_night'] = 'False'

            print str(is_web) + "IS WEB"

            if is_web != None:
                req_id = is_web
                args['web_id'] = req_id
 
            parameters['args'] = str(args)
 
            params = urlencode(parameters)
            url = PROVISION_URL
            resp = urlopen(Request(url, params))
 
        except IOError, err:
            error = 'operation: IO enqueue request, desc: \
                    failed to submit provisioning request %s: %s, error:%s'\
                    % (msisdn, package, str(err))
            print error
            print traceback.format_exc()
            raise err
        except Exception, err:
            error = 'operation: n - enqueue request, desc: \
                    failed to submit provisioning request %s: %s, error: %s'\
                    % (msisdn, package, str(err))
            print error
            raise err
        else:
            return (resp.info()).get('Transaction-Id')
    else:
        try:
            resp = disable_renewal(msisdn)
        except Exception, err:
            print traceback.format_exc()
        else:
            return resp

def execute_provision_response(message, logger):
    '''
    determines if a message is aparty or bparty
    '''
    message = literal_eval(message)
    logger.info(message)
    message = json.loads(message)
    
    transaction_type = message['transaction_type']

    if transaction_type  == 'A' or transaction_type == 'a':
        return process_self(message, logger)
    else:
        return process_b_party(message, logger)

def process_self(message, logger):
    '''
    processes a self data response

    '''
    transaction_type = message['transaction_type']
    msisdn = str(message['msisdn']).strip()
    status = int(str(message['status']).strip())
    package_id = str(message['package_id'])
    flag_message_override = message['flag_message_override']

    body = message
    args = message['args']
    can_renew = 0
    is_night = False
    send_sms = 1

    rsrcs = {}
    rsrcs['msisdn'] = msisdn
    rsrcs['connections'] = res['connections']
    lang = check_language(rsrcs, logger)

    if 'can_renew' in args:
        can_renew = int(args['can_renew'])
        logger.info("renew: %s" % str(args['can_renew']))
    elif 'is_night' in args:
        is_night = str(args['is_night'])

    if 'send_sms' in args:
        send_sms = int(args['send_sms'])
        logger.info("send sms value: %s" % str(args['send_sms']))

    if package_id == UNLIMITED_ID:
        rsrcs = {}
        rsrcs['msisdn'] = msisdn
        rsrcs['connections'] = res['connections']
        lang = check_language(rsrcs, logger)
    
    if package_id in BONUSBUNDLES:
        rsrcs = {}
        rsrcs['msisdn'] = msisdn
        rsrcs['connections'] = res['connections']
        lang = check_language(rsrcs, logger)

    if package_id in NEWMSGBUNDLES:
        rsrcs = {}
        rsrcs['msisdn'] = msisdn
        rsrcs['connections'] = res['connections']
        lang = check_language(rsrcs, logger)
    
    if int(message['package_id']) != 0:
        if status == 5:
            logger.info(message)
            package_name = str(message['name'])
            logger.info('B4 data_usage')
            if package_id in DATA_USAGE:
                queue_msg = '%s| %s| %s' % (msisdn, package_name, package_id)
                rcs = {}
                rcs['parameters'] = {}
                rcs['parameters']['queue_name'] = 'mg_data_usage'
                Publisher(queue_msg, rcs)
            balance = message['balance']
           
            if 'volume' in balance:
                expiry = str(balance['volume']['expiry'])
                balance = str(balance['volume']['amount'])
            elif 'unlimited' in balance:
                expiry = str(balance['unlimited']['expiry'])
                balance = str(balance['unlimited']['amount'])
            elif 'regional' in balance:
                expiry = str(balance['regional']['expiry'])
                balance = str(balance['regional']['amount'])
            elif 'OTI' in balance:
                expiry = str(balance['OTI']['expiry'])
                balance = str(balance['OTI']['amount'])
            elif 'voice' in balance:
                expiry = str(balance['voice']['expiry'])
                balance = str(balance['voice']['amount'])
           
            balance = int(balance) / DA_FACTOR

            if balance == 0 or balance < 0:
                balance = '1'
            else:
                balance = str(balance)
                
        if status == 5:
            if expiry != 'False' or expiry !='false':
               try:
                   date = expiry.split('T')[0].split('-')
                   expiry_date = date[2]+'-'+date[1]+'-'+date[0]
                   metrics_name = package_name.replace(' ','_')
               except Exception, err:
                   expiry_date = (datetime.now()+timedelta(days=int(validity[package_id]))).replace(hour = 23, minute=59)
               else:
                   expiry_date = (datetime.now()+timedelta(days=int(validity[package_id]))).replace(hour = 23, minute =59)

            try:
                count(SUCCESS_HIT % 'self.'+metrics_name)
            except Exception:
                pass
            #Bonus Messages
            if package_id in BONUSBUNDLES:
                message = bonusMsgs[package_id][lang]
            elif package_id == BONUSMEG250:
                message = bonusMsgs['131'][lang]
            elif package_id == BONUSMEG500:
                message = bonusMsgs['132'][lang]
            elif package_id == BONUSGIG1:
                message = bonusMsgs['133'][lang]
            #End of Bonus Messages
            # elif package_id in NEWMSGBUNDLES:
            #    message = newMsgs[package_id][lang]
            elif is_night == 'True':
                message = messages['success_night'].safe_substitute(
                        expiry = expiry_date, data = package_name, code =social_pkgs[package_id])
            elif package_id == BONUSGIG1:
                message = bonusMsgs['133'][lang]
            #End of Bonus Messages
            elif package_id in NEWMSGBUNDLES:
                if package_id == '32':
                    hour = datetime.now().hour
                    if hour >= 0 and hour < 5:
                        message = newMsgs[package_id][2]
                    else:
                        message = newMsgs[package_id][1]
                elif package_id == '203':
                    hour = datetime.now().hour
                    if hour >= 0 and hour < 12:
                        message = newMsgs[package_id][lang]
                    else:
                        message = newMsgs['203-2'][lang]

                elif package_id =='396':
                    if 'parabole_nxt_month_expiry' in message:
                        message = newMsgs['PARABOLE_NXT_MONTH_EXPIRY'][lang]
                    else:
                        message = newMsgs[package_id][lang]

                else:
                    if package_id in ['209','211','213','215','217','218','219','399','401','405','421','422']:
                        from time import strftime
                        expiry_date = expiry_date.strftime('%Y-%m-%d %H:%M')
                        message = newMsgs[package_id][lang].safe_substitute(expiry = expiry_date)

                    elif package_id in ['376','377','378']:
                        message = newMsgs['M4M_DAILY'][lang]
                    
                    elif package_id in ['379','380','381']:
                        message = newMsgs['M4M_WEEKLY'][lang]
                    
                    elif package_id in ['382','383','384']:
                        message = newMsgs['M4M_MONTHLY'][lang]

                    elif package_id == '410':
                        message = newMsgs['LOW_COMBO_BUNDLE_500'][lang]

                    elif package_id == '411' and flag_message_override == True:
                        message = newMsgs['Ser@200_U&R'][lang]

                    elif package_id == '412' and flag_message_override == True:
                        message = newMsgs['Ser@500_U&R'][lang]

                    elif package_id == '413' and flag_message_override == True:
                        message = newMsgs['Ser@1000_U&R'][lang]
      
                    elif package_id == '418' and flag_message_override == True:
                        message = newMsgs['Ser@10000_Bogof'][lang]
    
                    elif package_id == '207' and flag_message_override == True:
                        message = newMsgs['Fun_Cool_Bogof'][lang]
        
                    elif package_id == '256' and flag_message_override == True:
                        message = newMsgs['Club_SMS_Mini_Bogof'][lang]
            
                    elif package_id == '251' and flag_message_override == True:
                        message = newMsgs['Club_SMS_Bogof'][lang] 

                    elif package_id == '411':
                        message = newMsgs['Ser@200'][lang]

                    elif package_id == '412':
                        message = newMsgs['Ser@500'][lang]

                    elif package_id == '413':
                        message = newMsgs['Ser@1000'][lang]

                    elif package_id == '4' and flag_message_override == True:
                        message = newMsgs['I-Ser@1000_U&R'][lang]
                    #start of data bonus SR6136197
                    elif package_id == '191' and flag_message_override == True:
                        message = newMsgs['I-Ser@600_U&R'][lang]

                    elif package_id == '240' and flag_message_override == True:
                        message = newMsgs['I-Ser@2000_U&R'][lang]

                    elif package_id == '6' and flag_message_override == True:
                        message = newMsgs['I-Ser@3000_U&R'][lang]

                    elif package_id == '8' and flag_message_override == True:
                        message = newMsgs['I-Ser@6000_U&R'][lang]

                    elif package_id == '9' and flag_message_override == True:
                        message = newMsgs['I-Ser@10000_U&R'][lang]

                    elif package_id == '11' and flag_message_override == True:
                        message = newMsgs['I-Ser@30000_U&R'][lang]

                    elif package_id == '14' and flag_message_override == True:
                        message = newMsgs['I-Ser@80000_U&R'][lang]

                    elif package_id == '15' and flag_message_override == True:
                        message = newMsgs['I-Ser@120000_U&R'][lang]
                    #End of data bonus

                    elif package_id == '4':
                        message = newMsgs['I-Ser@1000'][lang]

                    else:
                        message = newMsgs[package_id][lang]

            elif str(package_id) == MY_MEG_10 and flag_message_override == True:
                message = messages['success_I-Ser@200_U&R'][lang]
    
            elif str(package_id) == MY_MEG_10:
                message = messages['success_I-Ser@200'][lang]
            elif is_night == 'True':
                message = messages['success_night'].safe_substitute(
                message = newMsgs[package_id][lang])
            elif is_night == 'True':
                message = messages['success_night'].safe_substitute(
                        expiry = expiry_date, data = package_name)
            elif package_id in social:
                message = messages['social'].safe_substitute(
                        expiry = expiry_date, data = package_name, code =social_pkgs[package_id])
            elif package_id == kozy_id:
                message = messages['kozy']

            elif package_id == reg_id:
                message = messages['regional']

            elif package_id == UNLIMITED_ID:
                message = messages['unlimited_succ'][lang]
            elif package_id == SOCIAL_FB_WEEKLY:
                message = messages['success_fb_weekly'][lang]
            elif package_id == SOCIAL_TW_WEEKLY:
                message = messages['success_tw_weekly']
            elif package_id == SOCIAL_WA_WEEKLY:
                message = messages['success_wa_weekly']
            else:
                message = messages['success'].safe_substitute(
                        expiry = expiry_date, data = package_name)

        elif status == 7:
            if package_id == UNLIMITED_ID:
                message = messages['unlimited_unsucc'][lang]
            else:
                message = messages['insufficient_funds']
            count(FAIL_HIT % 'self.nofunds')

        elif status == 6:
            message = messages['conflicting_bundle']
            count(FAIL_HIT % 'self.conflicting')

        elif status == 9:
            if package_id in service_class_check_packages:
                message = messages['isBarred_FunAl'][lang]
            else:
                message = messages['is_barred']
            count(FAIL_HIT % 'self.isbarred')


        elif status == 12:
            message = messages['isBarred_MyMeg5']
            count(FAIL_HIT % 'self.isbarred')

        elif status == 13:
            if package_id in ['256']:
                message = messages['isBarred_alt_CLUBSMS'][lang]
                count(FAIL_HIT % 'self.isbarred')
            else:
                message = messages['isBarred_Not_whitelisted'][lang]
                count(FAIL_HIT % 'self.isbarred')

        elif status == 14:
            if package_id in ['194','195','203']:
                message = messages['isBarred_alt_FunAby'][lang]
                count(FAIL_HIT % 'self.isbarred')
            if package_id in ['225']:
                message = messages['isBarred_FunAl_time'][lang]
                count(FAIL_HIT % 'self.isbarred')
            else:
                message = messages['isBarred_alt_FunCool'][lang]
                count(FAIL_HIT % 'self.isbarred')

        #elif status == 17:
            #message = messages['isBarred_Mix500']
            #count(FAIL_HIT % 'self.isbarred')

        elif status == 18:
            message = messages['isBarred_Bundle200']
            count(FAIL_HIT % 'self.isbarred')

        else:
            if package_id == '399':
                message = messages['399-error'][lang]
            elif package_id == '401':
                message = messages['401-error'][lang]
            elif package_id == '405':
                message = messages['405-error'][lang]
            elif package_id == '410':
                message = messages['410-error'][lang]
            else:
                message = messages['error']
            count(FAIL_HIT % 'self.nofunds')
        logger.info(message)
        send_message(msisdn, message, logger, send_sms)

        '''
        having sent messages try create events
        '''
        if status == 5:
            if can_renew == 1:
                try:
                    create_events(body, logger)
                except Exception, err:
                    error = "no events created for %s " % msisdn
                    logger.error(error)
                    logger.error(str(traceback.format_exc()))
                else:
                    dump = "events for %s created" % msisdn
                    logger.info(dump)
    else:
        if message['balance']:
            expiry = str(message['balance']['volume']['expiry'])
            balance = str(message['balance']['volume']['amount'])
            balance = int(balance)/ DA_FACTOR
            date = expiry.split('T')[0].split('-')
            expiry_date = date[2]+'-'+date[1]+'-'+date[0]
            message = messages['balance'].safe_substitute(\
                    expiry = expiry_date, data = balance)
        else:
            message = messages['no_balance']

        logger.info(message)
        send_message(msisdn, message, logger, send_sms)

    if 'web_id' in args:
        '''
        insert request info into table
        '''
        db = DataCDR()
        db.insert_web_response(msisdn, args['web_id'], body, logger)
        
def process_b_party(message, logger):
    '''
    process an a party b party message

    '''
    msisdn = str(message['msisdn']).strip()
    status = int(str(message['status']).strip())
    b_msisdn = str(message['b_msisdn']).strip()
    package_id = str(message['package_id']).strip()
    send_sms = 1
    rsrcs = {}
    rsrcs['msisdn'] = msisdn
    rsrcs['connections'] = res['connections']
    lang = check_language(rsrcs, logger)

    if status == 5:
        package_name = str(message['name'])
        balance = message['balance']
        
        #expiry = str(message['balance']['volume']['expiry'])
        #balance = str(message['balance']['volume']['amount'])
        
        if 'volume' in balance:
            expiry = str(balance['volume']['expiry'])
            balance = str(balance['volume']['amount'])
        elif 'unlimited' in balance:
            expiry = str(balance['unlimited']['expiry'])
            balance = str(balance['unlimited']['amount'])
        elif 'regional' in balance:
            expiry = str(balance['regional']['expiry'])
            balance = str(balance['regional']['amount'])
        elif 'voice' in balance:
            expiry = str(balance['voice']['expiry'])
            balance = str(balance['voice']['amount'])
      
        balance = int(balance)/ DA_FACTOR

        if balance == 0 or balance < 0:
            balance = '1'
        else:
            balance = str(balance)

    if status == 5:
        if expiry != 'False':
            date = expiry.split('T')[0].split('-')
            expiry_date = date[2]+'-'+date[1]+'-'+date[0]
            metrics_name = package_name.replace(' ','_')
        else:
            expiry_date = (datetime.now()+timedelta(days=int(validity[package_id]) - 1)).replace(hour = 23, minute =59)
            expiry_date = expiry_date.strftime('%Y-%m-%d %H:%M')
        try:
            count(SUCCESS_HIT % 'b_party.'+metrics_name)
        except Exception:
            pass
        valid = validity[package_id]
        
        try:
            response = newMsgs[int(package_id)].safe_substitute(\
                b_msisdn = b_msisdn, data = package_name, days = valid)
            response_rec = messages['recipient']['success'].safe_substitute(\
                    benefactor = msisdn, data = package_name, balance = balance, expiry = expiry_date)
        except Exception:
            if package_id in ['220','254']:
                response = messages['subscriber_success_fun_ora'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_fun_ora'][lang].safe_substitute(benefactor = msisdn)
            elif package_id in ['207','255']:
                response = messages['subscriber_success_fun_cool'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_fun_cool'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '201':
                response = messages['subscriber_success_fun15'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_fun15'][lang].safe_substitute(benefactor = msisdn)
            elif package_id in ['197','199']:
                response = messages['subscriber_success_funPlus'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_funPlus'][lang].safe_substitute(benefactor = msisdn)
            elif package_id in ['222','223']:
                response = messages['subscriber_success_funRaitra'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_funRaitra'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '209':
                response = messages['subscriber_success_funRelax'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_funRelax'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '211':
                response = messages['subscriber_success_funExtra'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_funExtra'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '213':
                response = messages['subscriber_success_funUltra'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_funUltra'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '215':
                response = messages['subscriber_success_funMaxi'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_funMaxi'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '217':
                response = messages['subscriber_success_Mix1'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_Mix1'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '218':
                response = messages['subscriber_success_Mix2'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_Mix2'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '219':
                response = messages['subscriber_success_Mix3'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_Mix3'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '224':
                response = messages['subscriber_success_funAby'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_funAby'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '205':
                response = messages['subscriber_success_Bojo'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_Bojo'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '227':
                response = messages['subscriber_success_Boost1000'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_Boost1000'][lang].safe_substitute(benefactor = msisdn)
            elif package_id == '225':
                response = messages['subscriber_success_funAl'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_funAl'][lang].safe_substitute(benefactor = msisdn)
            elif package_id =='253':
                response = messages['subscriber_success_ArivoWeekday'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_ArivoWeekday'][lang].safe_substitute(benefactor = msisdn)
            elif package_id =='252':
                response = messages['subscriber_success_ArivoWeekend'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_ArivoWeekend'][lang].safe_substitute(benefactor = msisdn)
            elif package_id =='232':
                response = messages['subscriber_success_BoostWE'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_BoostWE'][lang].safe_substitute(benefactor = msisdn)
            elif package_id =='233':
                response = messages['subscriber_success_Boost500'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_Boost500'][lang].safe_substitute(benefactor = msisdn)
            elif package_id =='250':
                response = messages['subscriber_success_ifun'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_ifun'][lang].safe_substitute(benefactor = msisdn)
            elif package_id in ['376','377','378']:
                response = messages['subscriber_success_M4M_DAILY'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_M4M_DAILY'][lang].safe_substitute(benefactor = msisdn)
            elif package_id in ['379','380','381']:
                response = messages['subscriber_success_M4M_WEEKLY'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_M4M_WEEKLY'][lang].safe_substitute(benefactor = msisdn)
            elif package_id in ['382','383','384']:
                response = messages['subscriber_success_M4M_MONTHLY'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_M4M_MONTHLY'][lang].safe_substitute(benefactor = msisdn)
            elif package_id =='397':
                response = messages['subscriber_success_FB_7'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_FB_7'][lang].safe_substitute(benefactor = msisdn, expiry = expiry_date)
            elif package_id =='180':
                response = messages['subscriber_success_FB_4'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_FB_4'][lang].safe_substitute(benefactor = msisdn, expiry = expiry_date)
            elif package_id =='410':
                response = messages['subscriber_success_low_combo_bundle_500'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_low_combo_bundle_500'][lang].safe_substitute(benefactor = msisdn)
            elif package_id =='425':
                response = messages['subscriber_success_WA_30'][lang].safe_substitute(b_msisdn = b_msisdn)
                response_rec = messages['recipient_success_WA_30'][lang].safe_substitute(benefactor = msisdn, expiry = expiry_date)
            elif package_id in ['179','191','4','240','6','8','9','11','14','15']:
                response = messages['subscriber_success_data'][lang].safe_substitute(b_msisdn = b_msisdn, data = package_name, days = valid)
                response_rec = messages['recipient_success_data'][lang].safe_substitute(benefactor = msisdn, data = package_name, expiry = expiry_date)
            else:
                response = messages['subscriber']['success'].safe_substitute(b_msisdn = b_msisdn, data = package_name, days = valid)
                response_rec = messages['recipient']['success'].safe_substitute(benefactor = msisdn, data = package_name, balance = balance, expiry = expiry_date)
        logger.info(response)
        logger.info(response_rec)

        send_message(msisdn, response, logger)
        send_message(b_msisdn, response_rec, logger, send_sms)

    elif status == 7:
        response = messages['insufficient_funds']
        logger.info(response)
        count(FAIL_HIT % 'bparty.nofunds')
        send_message(msisdn, response, logger, send_sms)

    elif status == 6:
        response = messages['conflicting_bundle']
        logger.info(response)
        count(FAIL_HIT % 'bparty.conflicting')
        send_message(msisdn, response, logger, send_sms)

    elif status == 9:
        response = messages['is_barred']
        logger.info(response)
        count(FAIL_HIT % 'bparty.isbarred')
        send_message(msisdn, response, logger, send_sms)

    elif status == 12:
        response = messages['isBarred_MyMeg5']
        logger.info(response)
        count(FAIL_HIT % 'bparty.isbarred')
        send_message(msisdn, response, logger, send_sms)

    elif status == 13:
        response = messages['isBarred_Not_whitelisted'][lang]
        logger.info(response)
        count(FAIL_HIT % 'bparty.isbarred')
        send_message(msisdn, response, logger, send_sms)

    elif status == 14:
        if package_id in ['220','254']:
            response = messages['isBarred_past5pm'][lang]
            logger.info(response)
            count(FAIL_HIT % 'bparty.isbarred')
            send_message(msisdn, response, logger, send_sms)

    #elif status == 17:
        #response = messages['isBarred_Mix500']
        #logger.info(response)
        #count(FAIL_HIT % 'bparty.isbarred')
        #send_message(msisdn, response, logger)

    elif status == 18:
        response = messages['isBarred_Bundle200']
        logger.info(response)
        count(FAIL_HIT % 'bparty.isbarred')
        send_message(msisdn, response, logger, send_sms)

    else:
        response = messages['error']
        logger.info(response)
        count(FAIL_HIT % 'bparty.isbarred')
        send_message(msisdn, response, logger, send_sms)


def check_language(resources, logger):
    msisdn = resources['msisdn']
    try:
        language = getLanguage(resources)
        logger.info('%s-%s' % (msisdn, language))
    except Exception, err:
        error = 'error, failed checking langeage for:%s error: %s' % (msisdn, str(err))
        logger.error(error)
        return 'txt-3'
    else:
        return language

def create_events(message, logger):
    '''
    creates events
    1) creates an sms event
    2) creates a renewal event
    '''
    msisdn = str(message['msisdn']).strip()
    package_id = message['package_id'].strip()
    try:
        expiry = convert_da_time(str(message['balance']['volume']['expiry']))
    except ValueError, err:
        dbg = "no previous offers therefore no expiry for %s" % msisdn
        logger.debug(dbg)
        if int(validity[package_id]) == 1:
            expiry =(datetime.now()).replace(hour = 23, minute =59)
        else:
            expiry =(datetime.now()+timedelta(days=int(validity[package_id]))).replace(hour = 23, minute =59)
    
    freq = 0
    renw = 0

    parameters = {}
    parameters['msisdn'] = msisdn
    parameters['status'] = 0
    parameters['service_id'] = SERVICE_ID
    parameters['can_execute'] = 1
    parameters['parameters'] = '%s,%s,%s' % (str(package_id), str(freq), str(renw))

    try:
        #SMS event
        parameters['event_id'] = NOW_SMS_EVENT_ID
        parameters['execute_at'] = datetime.now() + timedelta(minutes = 1)
        res['parameters'] = parameters
        enqueue_active_events(res)
    except Exception, err:
        error = "failed creating sms event for msisdn || %s " % msisdn
        logger.error(error)

    else:
        dump = "created sms event for msisdn || %s" % msisdn
        logger.info(dump)
        
    try:
        #SMS event# 3rd day before renewal
        parameters['event_id'] = THIRD_DAY_SMS_EVENT_ID
        parameters['execute_at'] =  (expiry + timedelta(days = -3)).replace(hour= 8 )
        if msisdn in SPECIAL_NUMBERS:
            parameters['execute_at'] =  datetime.now() + timedelta(minutes = 1)
        res['parameters'] = parameters
        enqueue_active_events(res)
    except Exception, err:
        error = "failed creating 3rd day from renewal sms event for msisdn || %s " % msisdn
        logger.error(error)

    else:
        dump = "created 3rd day from renewal sms event for msisdn || %s" % msisdn
        logger.info(dump)
        
        
    try:
        #SMS event # day of renewal
        parameters['event_id'] = DAY_OF_RENEWAL_EVENT_ID
        parameters['execute_at'] = (expiry + timedelta(days = -1)).replace(hour= 8 )
        if msisdn in SPECIAL_NUMBERS:
            parameters['execute_at'] =  datetime.now() + timedelta(minutes = 1)
        res['parameters'] = parameters
        enqueue_active_events(res)
    except Exception, err:
        error = "failed creating day of renewal sms event for msisdn || %s " % msisdn
        logger.error(error)

    else:
        dump = "created day of renewal sms event for msisdn || %s" % msisdn
        logger.info(dump)



    try:
        #Renewal event
        parameters['event_id'] = RENEW_EVENT_ID
        # temporary for testing DONT FORGET FI REMOVE
        parameters['execute_at'] = (expiry+ timedelta(days=1)).replace(hour = 0, minute = 2)
        if msisdn in SPECIAL_NUMBERS:
            parameters['execute_at'] =  datetime.now() + timedelta(minutes = 15)
            res['parameters'] = parameters
        enqueue_active_events(res)
    except Exception, e:
        error = "failed creating renewal event for msisdn || %s " % str(parameters)
        logger.error(error)
        logger.error(res)
        logger.error(traceback.format_exc())
    else:
        info = "created renewal event successfully for msisdn || %s " % str(parameters)
        logger.info(info)

def disable_renewal(msisdn):
    '''
    disables renewal
    '''
    parameters = {}
    parameters['service_id'] = SERVICE_ID 
    parameters['msisdn'] = msisdn
    parameters['event_id'] = RENEW_EVENT_ID

    res['parameters'] = parameters
    try:
        resp = check_renew_status(res)
    except Exception, err:
        print traceback.format_exc()
    else:
        if resp:
            if resp[0]:
                try:
                    dequeue_active_events(res)
                except Exception, err:
                    error = "could not disable renewal for %s " % (msisdn)
                    print error
                else:
                    '''
                    send message
                    '''
                    message = messages['renewal_removed']
                    print message
                    send_message(msisdn, message)
                    return ("SUCCESS", resp[1])
            else:
                message = messages['no_renew']
                print message
                send_message(msisdn, message)
                return ("NO_RENEWAL", '0')


        else:
            message = messages['no_renew']
            print message
            send_message(msisdn, message)
            return ("NO_RENEWAL", '0')


def check_renew_status(resources):
    '''
    Function gets the latest event queued for a subscriber.
    The event should still be pending as  per service_id 
    and event_id
    '''
    results = False
    parameters = resources['parameters']
    msisdn = parameters['msisdn']
    service_id = parameters['service_id']
    event_id = parameters['event_id']

    sql = 'select * from service_events where msisdn = :msisdn \
            and can_execute = 1 and status = 0 and service_id = \
            :service_id and event_id = :event_id'
    params = {'msisdn':msisdn, 'service_id':service_id, 'event_id':event_id}
    try:
        connection = get_connection(resources)
        cursor = connection.cursor()
        cursor.execute(sql, params)
        records = cursor.fetchall()
        #log(resources, records, 'debug')
        count = cursor.rowcount
        if int(count) == 0:
            results = (False, 0)
        else:
            results = (True, records[0][3])
    except Exception, err:
        error = ' operation check_renew_status failed for %s, error:%s' % (
                msisdn, str(err))
        log(resources, error, 'error')
        #raise err
        return False
    else:
         return results
