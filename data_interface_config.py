#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
config for the madagascar data interface

'''

from string import Template

HOST_NAME = __import__('socket').gethostname()

CWD = "/appussd/mg_data_interface/src/consumer"                           
LOG_NAME = "data_responselog-{}".format(HOST_NAME)
PID_FILE = '/appussd/mg_data_interface/src/consumer/data_prov_daemon-{}.pid'.format(HOST_NAME)
 
MEG_CWD = "/appussd/mg_data_interface/src/megfiftn_consumer"                       
MEG_LOG_NAME = "meg_responselog-{}".format(HOST_NAME)
MEG_PID_FILE = '/appussd/mg_data_interface/src/megfiftn_consumer/meg15_daemon-{}.pid'.format(HOST_NAME)


DEBUG = True
MIN_AMOUNT = 5
DA_FACTOR = 100
DA_ACTION = 'dedicatedAccountValueNew'
DA_ID = 8
WORKERS = 30
DEBUG = False

MAX_PURCHASES_PER_BLOCK = 2
BUY_KEYWORD = 'mix'
STOP_KEYWORD = 'stop'

SERVICE_ID = 2

NOW_SMS_EVENT_ID = 1
THIRD_DAY_SMS_EVENT_ID = 4
DAY_OF_RENEWAL_EVENT_ID = 5

RENEW_EVENT_ID = 2

MSISDN_LENGTH = 8

ALLOWED_PREFIXES = ['76','77','66','74','75','65','64']

 
BARRED_AFTERNOON_QUOTA = 91
BARRED_MORNING_QUOTA = 92
TIME_BARRED = 93
 

SPECIAL_NUMBERS = ['261330465390']
#SPECIAL_NUMBERS = ['22667102208','22667088086','22666201744','22666009090','22677717415','22677717390','22667125657','22677717378','22677717399','22677717392','22674345604','22666201745','22667088085','22675059211','22674437923','22667125657','22674344369','22674345604','22667125658']

PROVISION_URL =  "http://127.0.0.1:9002/submitProvision?"
BALANCE_URL =  "http://127.0.0.1:9002/submitProvision?"
ME2U_URL = "http://127.0.0.1:5550/provision?"
FREQUENCY  =  3

ACK = {}


ACK['txt-1'] = "Eto ampanatontosana ny fangatahanao. Mahandrasa kely azafady. Misaotra tompoko."
ACK['txt-2'] = "We have recieved your request, please wait as we process it"
ACK['postpaid'] = "Cher client vous n'etes pas autorise a acceder a ce service"
ACK['wrong_mix'] = "Raha mila fanampim-panazavana dia antsoy ny sampana mpikarakara ny mpanjifa. Misaotra tompoko"
ACK['wrong_class'] = "Tompoko, tsy tontosa ny fangatahanao. Ny tolotra RTA mix dia natokana ho an ny mpanjifa RTA Mobile.Misaotra tompoko"
ACK['wrong_rec'] = "Le nombre que vous avez envoyez n'est pas valide"
ACK['wrong_amount'] = "Le montant que vous envoyer n'est pas valide"
ACK['wrong'] = "demande meconnu"
ACK['non_gift_bundle'] = "Gifting is not allowed for this bundle"
ACK['not_allowed'] = "You are not allowed to access this service"

ACK_ME2U = {}
ACK_ME2U['txt-1'] = "We have recieved your request, please wait as we process it"
ACK_ME2U['txt-2'] = "Voaray ny fangatahanao. Miandrasa kely azafady. Misaotra tompoko"
ACK_ME2U['txt-3'] = "Votre demande et en cours de traitement. Veuillez patienter SVP"

MESSAGES = {}
MESSAGES['subscriber'] ={}
MESSAGES['subscriber']['same'] = "chere client vous ne pouvez pas ajoutez votre numero comme numero magique"
MESSAGES['subscriber']['is_barred'] = "Desole vous ne pouvez pas souscrire ce numero a numero magique"

#metrics
HITS = 'application.mg_data.hits.ussd'
INSERT_METRIC = 'application.mg_data.hits.ussd'
INSERT_CDR_METRIC = 'application.mg_data.hits.meg.cdrinsert'
UPDATE_CDR_METRIC = 'application.mg_data.hits.meg.trackerupdate'

SUCCESS_HIT = "application.internet.success.%s"
FAIL_HIT = "application.internet.fail.%s"

AUTH_KEY = 'modularP4ss'
ACCOUNT_ID = 'modular'
ROUTING_KEY = 'mg_data'
MEG_KEY = 'meg_fiftn'

MEG_QUEUES = {}
MEG_QUEUES['test'] = 'test_megfiftn_queue'
MEG_QUEUES['prod'] = 'megfiftn_queue'

QUEUES = {}
QUEUES['test'] = 'test_mg_data_interface_queue'
QUEUES['prod'] = 'mg_data_interface_queue'



#=============Start of double data promotion bundles==================
bonusMsgs = {}
bonusMsgs['131'] = {}
bonusMsgs['131']['txt-1'] = "You have successfully subscribed to MyMeg250.You have 250MB valid 7days and Bonus 250MB valid 7 days.Press *999*141# to check remaining balance"
bonusMsgs['131']['txt-2'] = "Tafiditra ny MyMeg250: 250Mo ampiasaina internet manankery 7andro sy bonus 250Mo manankery 7andro. Tsindrio ny *999*141# raha hijery ny Mo na Ko azo ampiasaina."
bonusMsgs['131']['txt-3'] = "L'offre MyMeg250 a ete effectue avec succes: 250Mo d internet valable 7jours et 250Mo de bonus internet valable 7jours. Consultation forfait, tapez *999*141#."

bonusMsgs['132'] = {}
bonusMsgs['132']['txt-1'] = "You have successfully subscribed to MyMeg500.You have 500MB valid 7days and Bonus 500MB valid 7 days.Press *999*141# to check remaining balance."
bonusMsgs['132']['txt-2'] = "Tafiditra ny MyMeg500: 500Mo ampiasaina internet manankery 7andro sy bonus 500Mo manankery 7andro. Tsindrio ny *999*141# raha hijery ny Mo na Ko azo ampiasaina."
bonusMsgs['132']['txt-3'] = "L'offre MyMeg500 a ete effectue avec succes: 500Mo d internet valable 7jours et 500Mo de bonus internet valable 7jours. Consultation forfait, tapez *999*141#."

bonusMsgs['133'] = {}
bonusMsgs['133']['txt-1'] = "You have successfully subscribed to MyGig1.You have 1GB valid 30days and Bonus 1GB valid 7 days.Press *999*141# to check remaining balance."
bonusMsgs['133']['txt-2'] = "Tafiditra ny MyGig1: 1Go ampiasaina internet manankery 30andro sy bonus 1Go manankery 7andro. Tsindrio ny *999*141# raha hijery ny Mo na Ko azo ampiasaina."
bonusMsgs['133']['txt-3'] = "L'offre MyGig1 a ete effectue avec succes: 1Go d internet valable 30jours et 1Go de bonus internet valable 7jours. Consultation forfait, tapez *999*141#."


#===========End of double data promotion bundles=====================
#===========Replacing temporary messgaes ===================
newMsgs = {}
newMsgs['32'] = {}
newMsgs['32'][1] = "Tafiditra ny MyMeg20Night: 20Mo ampiasaina internet @ 9ora alina-12ora alina. Tsindrion ny *999*103# ahafantaranao ny Kiloctet sy Megaoctet azo ampiasaina."
newMsgs['32'][2] = "Tafiditra ny MyMeg20Night: 20Mo ampiasaina internet @ 12ora alina-5ora maraina. Tsindrion ny *999*103# ahafantaranao ny Kiloctet sy Megaoctet azo ampiasaina."


newMsgs['33'] = {}
newMsgs['33']['txt-1'] = "You have succesfully subscribed to MyMeg50 Night: 50Mb valid for 1 night. Dial *999*103# to check remaining balance. Thank you."
newMsgs['33']['txt-2'] = "Tafiditra ny MyMeg50Night: 50Mo ampiasaina internet manankery 1alina. Tsindrion ny *999*103# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['33']['txt-3'] = "L'offre MyMeg50 Night a ete effectue avec succes: 50Mo valable 1 nuit. Tapez *999*103# pour consulter le forfait restant. Merci."

newMsgs['35'] = {}
newMsgs['35']['txt-1'] = "You have succesfully subscribed to MyMeg100 Night: 100Mb valid for 3 nights. Dial *999*103# to check remaining balance. Thank you."
newMsgs['35']['txt-2'] = "Tafiditra ny MyMeg100Night: 100Mo ampiasaina internet manankery 3alina. Tsindrion ny *999*103# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['35']['txt-3'] = "L'offre MyMeg100 Night a ete effectue avec succes: 100Mo valable 3 nuits. Tapez *999*103# pour consulter le forfait restant. Merci."

newMsgs['I-Ser@1000'] = {}
newMsgs['I-Ser@1000']['txt-1'] = "You are succesfully subscribed to I-Ser@1000:50Mb valid 1 day and 50Mb of BONUS to be used from 10pm to 04:59am.Press *999*114# to check remaining balance"
newMsgs['I-Ser@1000']['txt-2'] = "Tafiditra ny I-Ser@1000:ahazoana 50Mo ampisaina internet h@ 12ora alina sy BONUS 50Mo ampiasaina @ 10ora alina-5ora maraina.Megaoctet tavela:*999*114#"
newMsgs['I-Ser@1000']['txt-3'] = "La souscription a I-Ser@1000  a ete effectue avec succes:c est 50Mo utilisable 1 jour et un BONUS de 50Mo,valable de 22h a 04h59.Solde restant:*999*114#"

newMsgs['I-Ser@1000_U&R'] = {}
newMsgs['I-Ser@1000_U&R']['txt-1'] = "You are subscribed to I-Ser@1000 0+ I-Ser@1000 GIFT:100Mb valid 1 day and 100Mb of BONUS to be used from 10pm to 04:59am.Press *999*114# to check remaining balance"
newMsgs['I-Ser@1000_U&R']['txt-2'] = "Tafiditra ny I-Ser@1000 + I-Ser@1000 KADOA:100Mo azo ampisaina h@ 12ora alina sy BONUS 100Mo ampiasaina @10ora alina-5ora maraina. Megaoctet tavela:*999*114#"
newMsgs['I-Ser@1000_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@1000 + I-Ser@1000 CADEAU:100Mo utilisable 1 jour et un BONUS de 100Mo,valable de 22h a 04h59.Solde restant:*999*114#"

#=============Start of data bonus bundles=January16=SR6136197================
newMsgs['I-Ser@600_U&R'] = {}
newMsgs['I-Ser@600_U&R']['txt-1'] = "You are subscribed to I-Ser@600 + I-Ser@600 GIFT: 50Mb valid 1 day and 50Mb of BONUS to be used from 10pm to 05am. Press *999*114# to check remaining balance"
newMsgs['I-Ser@600_U&R']['txt-2'] = "Tafiditra ny I-Ser@600 + I-Ser@600 KADOA: 50Mo azo ampisaina hatr@ 12ora alina sy BONUS 50Mo ampiasaina @ 10ora alina-5ora maraina. Megaoctet tavela: *999*114# "
newMsgs['I-Ser@600_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@600 + I-Ser@600 CADEAU: 50Mo utilisable 1 jour et un BONUS de 50Mo, valable de 22h a 05h. Solde restant: *999*114#"

newMsgs['I-Ser@2000_U&R'] = {}
newMsgs['I-Ser@2000_U&R']['txt-1'] = "You are subscribed to I-Ser@2000 + I-Ser@2000 GIFT: 250Mb valid 1 day and 250Mb of BONUS to be used from 10pm to 05am. Press *999*114# to check remaining balance"
newMsgs['I-Ser@2000_U&R']['txt-2'] = "Tafiditra ny I-Ser@2000 + I-Ser@2000 KADOA: 50Mo azo ampisaina hatr@ 12ora alina sy BONUS 50Mo ampiasaina @ 10ora alina-5ora maraina. Megaoctet tavela: *999*114# "
newMsgs['I-Ser@2000_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@2000 + I-Ser@2000 CADEAU: 50Mo utilisable 1 jour et un BONUS de 50Mo, valable de 22h a 05h. Solde restant: *999*114#"

newMsgs['I-Ser@3000_U&R'] = {}
newMsgs['I-Ser@3000_U&R']['txt-1'] = "You are subscribed to I-Ser@3000 + I-Ser@3000 GIFT: 250Mb valid 7days and 250Mb of BONUS to be used from 10pm to 05am. Press *999*114# to check remaining balance"
newMsgs['I-Ser@3000_U&R']['txt-2'] = "Tafiditra ny I-Ser@3000 + I-Ser@3000 KADOA: 250Mo sy BONUS 250Mo ampiasaina @ 10ora alina-5ora maraina ary maharitra 7andro. Megaoctet tavela: *999*114# "
newMsgs['I-Ser@3000_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@3000 + I-Ser@3000 CADEAU: 250Mo utilisable 7 jours et un BONUS de 250Mo, valable de 22h a 05h. Solde restant: *999*114#"

newMsgs['I-Ser@6000_U&R'] = {}
newMsgs['I-Ser@6000_U&R']['txt-1'] = "You are subscribed to I-Ser@6000 + I-Ser@6000 GIFT: 550Mb valid 7days and 550Mb of BONUS to be used from 10pm to 05am. Press *999*114# to check remaining balance"
newMsgs['I-Ser@6000_U&R']['txt-2'] = "Tafiditra ny I-Ser@6000 + I-Ser@6000 KADOA: 550Mo sy BONUS 550Mo ampiasaina @ 10ora alina-5ora maraina ary maharitra 7andro. Megaoctet tavela: *999*114#"
newMsgs['I-Ser@6000_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@6000 + I-Ser@6000 CADEAU: 550Mo utilisable 7 jours et un BONUS de 550Mo, valable de 22h a 05h. Solde restant: *999*114#"

newMsgs['I-Ser@10000_U&R'] = {}
newMsgs['I-Ser@10000_U&R']['txt-1'] = "You are subscribed to I-Ser@10000 + I-Ser@10000 GIFT: 1Gb valid 7days and 1Gb of BONUS to be used from 10pm to 05am. Press *999*114# to check remaining balance"
newMsgs['I-Ser@10000_U&R']['txt-2'] = "Tafiditra ny I-Ser@10000 + I-Ser@10000 KADOA: 1Go sy BONUS 1Go ampiasaina @ 10ora alina-5ora maraina ary maharitra 7andro. Megaoctet tavela: *999*114# "
newMsgs['I-Ser@10000_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@10000 + I-Ser@10000 CADEAU: 1Go utilisable 7 jours et un BONUS de 1Go, valable de 22h a 05h. Solde restant: *999*114#"

newMsgs['I-Ser@30000_U&R'] = {}
newMsgs['I-Ser@30000_U&R']['txt-1'] = "You are subscribed to I-Ser@30000 + I-Ser@30000 GIFT: 4Gb valid 30days and 4Gb of BONUS to be used from 10pm to 05am. Press *999*114# to check remaining balance"
newMsgs['I-Ser@30000_U&R']['txt-2'] = "Tafiditra ny I-Ser@30000 + I-Ser@30000 KADOA: 4Go sy BONUS 4Go ampiasaina @ 10ora alina-5ora maraina ary maharitra 30andro. Megaoctet tavela: *999*114# "
newMsgs['I-Ser@30000_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@30000 + I-Ser@30000 CADEAU: 4Go utilisable 30jours et un BONUS de 4Go, valable de 22h a 05h. Solde restant: *999*114#"

newMsgs['I-Ser@80000_U&R'] = {}
newMsgs['I-Ser@80000_U&R']['txt-1'] = "You are subscribed to I-Ser@80000 + I-Ser@80000 GIFT: 12Gb valid 30days and 12Gb of BONUS to be used from 10pm to 05am. Press *999*114# to check remaining balance"
newMsgs['I-Ser@80000_U&R']['txt-2'] = "Tafiditra ny I-Ser@80000 + I-Ser@80000 KADOA: 12Go sy BONUS 12Go ampiasaina @ 10ora alina-5ora maraina ary maharitra 30andro. Megaoctet tavela: *999*114#  "
newMsgs['I-Ser@80000_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@80000 + I-Ser@80000 CADEAU: 12Go utilisable 30 jours et un BONUS de 12Go, valable de 22h a 05h. Solde restant: *999*114#"

newMsgs['I-Ser@120000_U&R'] = {}
newMsgs['I-Ser@120000_U&R']['txt-1'] = "You are subscribed to I-Ser@120000 + I-Ser@120000: 20Gb valid 30days and 20Gb of BONUS to be used from 10pm-05am. Press *999*114# to check remaining balance"
newMsgs['I-Ser@120000_U&R']['txt-2'] = "Tafiditra ny I-Ser@120000 + I-Ser@120000 KADOA: 20Go sy BONUS 20Go ampiasaina @ 10ora alina-5ora maraina ary maharitra 30andro. Megaoctet tavela: *999*114#   "
newMsgs['I-Ser@120000_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@120000 + I-Ser@120000 CADEAU: 20Go utilisable 30 jours et un BONUS de 20Go, valable de 22h a 05h. Solde restant: *999*114#"
#=============End of data bonus bundles==================

newMsgs['6'] = {}
newMsgs['6']['txt-1'] = "You are succesfully subscribed to I-Ser@3000:125Mb with 125Mb of BONUS to be used from 10pm to 04:59am.Validity 7days.Check remaining balance:*999*114#"
newMsgs['6']['txt-2'] = "Tafiditra ny I-Ser@3000:ahazoana 125Mo internet sy BONUS 125Mo ampiasaina @ 10ora alina-5ora maraina ary manankery 7 andro.Megaoctet tavela: *999*114#"
newMsgs['6']['txt-3'] = "La souscription a I-Ser@3000  a ete effectue avec succes:c est 125Mo avec BONUS 125Mo utilisable de 22h a 4h59.Validite 7 jours.Solde restant:*999*114#"

newMsgs['8'] = {}
newMsgs['8']['txt-1'] = "You are succesfully subscribed to I-Ser@6000:275Mb with 275Mb of BONUS to be used from 10pm to 04:59am.Validity 7days.Check remaining balance:*999*114#"
newMsgs['8']['txt-2'] = "Tafiditra ny I-Ser@6000:ahazoana 275Mo internet sy BONUS 275Mo ampiasaina @ 10ora alina-5ora maraina ary manankery 7 andro.Megaoctet tavela: *999*114#"
newMsgs['8']['txt-3'] = "La souscription a I-Ser@6000 a ete effectue avec succes:c est 275Mo avec BONUS 275Mo utilisable de 22h a 4h59.Validite 7 jours.Solde restant:*999*114#"

newMsgs['9'] = {}
newMsgs['9']['txt-1'] = "You are succesfully subscribed to I-Ser@10000:500Mb with 500Mb of BONUS to be used from 10pm to 04:59am.Validity 7days.Check remaining balance: *999*114#"
newMsgs['9']['txt-2'] = "Tafiditra ny I-Ser@10000:ahazoana 500Mo internet sy BONUS 500Mo ampiasaina @ 10ora alina-5ora maraina ary manankery 7 andro.Megaoctet tavela: *999*114#"
newMsgs['9']['txt-3'] = "La souscription a I-Ser@10000 a ete effectue avec succes:c est 500Mo avec BONUS 500Mo utilisable de 22h a 4h59.Validite 7 jours.Solde restant:*999*114#"

newMsgs['11'] = {}
newMsgs['11']['txt-1'] = "You are succesfully subscribed to I-Ser@30000:2Gb with 2Gb of BONUS to be used from 10pm to 04:59am.Validity 30days.Check remaining balance: *999*114#"
newMsgs['11']['txt-2'] = "Tafiditra ny I-Ser@30000:ahazoana 2Go internet sy BONUS 2Go ampiasaina @ 10ora alina-5ora maraina ary manankery 30 andro.Megaoctet tavela: *999*114#"
newMsgs['11']['txt-3'] = "La souscription a I-Ser@30000 a ete effectue avec succes:c est 2Go avec BONUS 2Go utilisable de 22h a 4h59.Validite 30 jours.Solde restant:*999*114#"

newMsgs['12'] = {}
newMsgs['12']['txt-1'] = "You have succesfully subscribed to MyGig2: 2Gb valid for 30 days. Dial *999*114# to check remaining balance. Thank you."
newMsgs['12']['txt-2'] = "Tafiditra ny MyGig2: 2Go ampiasaina internet manankery 30andro. Tsindrion ny *999*114# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['12']['txt-3'] = "L'offre MyGig2 a ete effectue avec succes: 2Go valable 30 jours. Tapez *999*114# pour consulter le forfait restant. Merci."

newMsgs['14'] = {}
newMsgs['14']['txt-1'] = "You are succesfully subscribed to I-Ser@80000:6Gb with 6Gb of BONUS to be used from 10pm to 04:59am.Validity 30days.Check remaining balance: *999*114#"
newMsgs['14']['txt-2'] = "Tafiditra ny I-Ser@80000:ahazoana 6Go internet sy BONUS 6Go ampiasaina @ 10ora alina-5ora maraina ary manankery 30 andro.Megaoctet tavela: *999*114#"
newMsgs['14']['txt-3'] = "La souscription a I-Ser@80000 a ete effectue avec succes:c est 6Go avec BONUS 6Go utilisable de 22h a 4h59. Validite 30 jours.Solde restant:*999*114#"

newMsgs['15'] = {}
newMsgs['15']['txt-1'] = "You are succesfully subscribed to I-Ser@120000:10Gb with 10Gb of BONUS to be used from 10pm to 04:59am.Validity 30days.Check remaining balance:*999*114#"
newMsgs['15']['txt-2'] = "Tafiditra ny I-Ser@120000:ahazoana 10Go internet sy BONUS 10Go ampiasaina @ 10ora alina-5ora maraina ary manankery 30 andro.Megaoctet tavela:*999*114#"
newMsgs['15']['txt-3'] = "La souscription a I-Ser@120000 a ete effectue avec succes:c est 10Go avec BONUS 10Go utilisable de 22h a 4h59.Validite 30 jours.Solde restant:*999*114#"


newMsgs['16'] = {}
newMsgs['16']['txt-1'] = "You have succesfully subscribed to MyGig30: 30Gb valid for 30 days. Dial *999*114# to check remaining balance. Thank you."
newMsgs['16']['txt-2'] = "Tafiditra ny MyGig30: 30Go ampiasaina internet manankery 30andro. Tsindrion ny *999*114# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['16']['txt-3'] = "L'offre MyGig30 a ete effectue avec succes: 30Go valable 30 jours. Tapez *999*114# pour consulter le forfait restant. Merci."

newMsgs['191'] = {}
newMsgs['191']['txt-1'] = "You are succesfully subscribed to I-Ser@600:25Mb valid 1 day and 25Mb of BONUS to be used from 10pm to 04:59am.Press *999*114# to check remaining balance"
newMsgs['191']['txt-2'] = "Tafiditra ny I-Ser@600:ahazoana 25Mo ampisaina internet h@ 12ora alina sy BONUS 25Mo ampiasaina @ 10ora alina-5ora maraina.Megaoctet tavela: *999*114#"
newMsgs['191']['txt-3'] = "La souscription a I-Ser@600 a ete effectue avec succes:c est 25Mo utilisable 1 jour et un BONUS de 25Mo,valable de 22h a 04h59.Solde restant: *999*114#"



newMsgs['19'] = {}
newMsgs['19']['txt-1'] = "Tafiditra ny tolotra Facebook manankery 1 andro. Tsindrion ny *999*36# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['19']['txt-2'] = "Tafiditra ny tolotra Facebook manankery 1 andro. Tsindrion ny *999*36# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['19']['txt-3'] = "Tafiditra ny tolotra Facebook manankery 1 andro. Tsindrion ny *999*36# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."


newMsgs['20'] = {}
newMsgs['20']['txt-1'] = "Tafiditra ny tolotra Twitter manankery 1 andro. Tsindrion ny *999*37# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['20']['txt-2'] = "Tafiditra ny tolotra Twitter manankery 1 andro. Tsindrion ny *999*37# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['20']['txt-3'] = "Tafiditra ny tolotra Twitter manankery 1 andro. Tsindrion ny *999*37# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."


newMsgs['21'] = {}
newMsgs['21']['txt-1'] = "Tafiditra ny Tolotra Whatsapp manankery 1 andro. Tsindrion ny *999*38# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['21']['txt-2'] = "Tafiditra ny Tolotra Whatsapp manankery 1 andro. Tsindrion ny *999*38# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
newMsgs['21']['txt-3'] = "Tafiditra ny Tolotra Whatsapp manankery 1 andro. Tsindrion ny *999*38# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."

newMsgs['119'] = {}
newMsgs['119']['txt-1'] = "Your subscription to Internet Mlay was performed with success, valid till 11:59PM. Thank you."
newMsgs['119']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny tolotra Internet Mlay, manakery hatramin ny 11:59 alina. Misaotra tompoko."
newMsgs['119']['txt-3'] = "Votre souscription a l'offre Internet Mlay a ete effectuee avec succes, valable jusqu a 23h59. Merci."

newMsgs['236'] = {}
newMsgs['236']['txt-1'] = "You are successfully subscribed to MyMeg5: 5Mb valid 1 day and 5Mb of BONUS to be used from 11:00pm to 05:59am. Press *999*114# to check remaining balance."
newMsgs['236']['txt-2'] = "Tafiditra ny MyMeg5: ahazoana 5Mo ampiasaina internet h@ 12ora alina sy BONUS 5Mo ampiasaina @ 11ora alina - 06ora maraina. Megaoctet  tavela: *999*114#."
newMsgs['236']['txt-3'] = "La souscription a MyMeg5 a ete effectuee avec succes: c est 5Mo utilisable 1 jour et un BONUS de 5Mo, valable de 23h a 05h59. Solde restant: *999*114#."

newMsgs['240'] = {}
newMsgs['240']['txt-1'] = "You are succesfully subscribed to I-Ser@2000:125Mb valid 1 day and 125Mb of BONUS to be used from 10pm to 04:59am.Press *999*114# to check remaining balance."
newMsgs['240']['txt-2'] = "Tafiditra ny I-Ser@2000:ahazoana 125Mo ampisaina internet h@ 12ora alina sy BONUS 125Mo ampiasaina @ 10ora alina-5ora maraina.Megaoctet tavela:*999*114#"
newMsgs['240']['txt-3'] = "La souscription a I-Ser@2000  a ete effectue avec succes:c est 125Mo utilisable 1 jour et un BONUS de 125Mo,valable de 22h a 04h59.Solde restant:*999*114#"

#newMsgs['420'] = {}
#newMsgs['420']['txt-1'] = "You are successfully subscribed to MyMeg5+: 5Mb valid 1 day and 5Mb of BONUS to be used from 11:00pm to 05:59am. Press *999*114# to check remaining balance."
#newMsgs['420']['txt-2'] = "Tafiditra ny MyMeg5+: ahazoana 5Mo ampiasaina internet h@ 12ora alina sy BONUS 75Mo ampiasaina @ 11ora alina - 06ora maraina. Megaoctet  tavela: *999*114#."
#newMsgs['420']['txt-3'] = "La souscription a MyMeg5+: a ete effectuee avec succes: c est 5Mo utilisable 1 jour et un BONUS de 75Mo, valable de 23h a 05h59. Solde restant: *999*114#."

#newMsgs['421'] = {}
#newMsgs['421']['txt-1'] = "You are successfully subscribed to MyMeg20: 20Mb valid 1 day and 20Mb of BONUS to be used from 11:00pm to 05:59am. Press *999*114# to check remaining balance."
#newMsgs['421']['txt-2'] = "Tafiditra ny MyMeg20: ahazoana 20Mo ampiasaina internet h@ 12ora alina sy BONUS 20Mo ampiasaina @ 11ora alina - 06ora maraina. Megaoctet  tavela: *999*114#."
#newMsgs['421']['txt-3'] = "La souscription a MyMeg20: a ete effectuee avec succes: c est 20Mo utilisable 1 jour et un BONUS de 75Mo, valable de 23h a 05h59. Solde restant: *999*114#."

#newMsgs['422'] = {}
#newMsgs['422']['txt-1'] = "You are successfully subscribed to MyMeg40: 40Mb valid 1 day and 40Mb of BONUS to be used from 11:00pm to 05:59am. Press *999*114# to check remaining balance."
#newMsgs['422']['txt-2'] = "Tafiditra ny MyMeg40: ahazoana 40Mo ampiasaina internet h@ 12ora alina sy BONUS 40Mo ampiasaina @ 11ora alina - 06ora maraina. Megaoctet  tavela: *999*114#."
#newMsgs['422']['txt-3'] = "La souscription a MyMeg40: a ete effectuee avec succes: c est 40Mo utilisable 1 jour et un BONUS de 40Mo, valable de 23h a 05h59. Solde restant: *999*114#."

#newMsgs['423'] = {}
#newMsgs['423']['txt-1'] = "You are successfully subscribed to MyMeg256: 256Mb valid 30 days and 256Mb of BONUS to be used from 11:00pm to 05:59am. Press *999*114# to check remaining balance."
#newMsgs['423']['txt-2'] = "Tafiditra ny MyMeg256: ahazoana 256Mo ampiasaina internet h@ 12ora alina sy BONUS 256Mo ampiasaina @ 11ora alina - 06ora maraina. Megaoctet  tavela: *999*114#."
#newMsgs['423']['txt-3'] = "La souscription a MyMeg256: a ete effectuee avec succes: c est 256Mo utilisable 30 jours et un BONUS de 256Mo, valable de 23h a 05h59. Solde restant: *999*114#."

#newMsgs['424'] = {}
#newMsgs['424']['txt-1'] = "You are successfully subscribed to MyMeg750: 750Mb valid 30 days and 750Mb of BONUS to be used from 11:00pm to 05:59am. Press *999*114# to check remaining balance."
#newMsgs['424']['txt-2'] = "Tafiditra ny MyMeg750: ahazoana 750Mo ampiasaina internet h@ 12ora alina sy BONUS 750Mo ampiasaina @ 11ora alina - 06ora maraina. Megaoctet  tavela: *999*114#."
#newMsgs['424']['txt-3'] = "La souscription a MyMeg750: a ete effectuee avec succes: c est 750Mo utilisable 30 jours et un BONUS de 750Mo, valable de 23h a 05h59. Solde restant: *999*114#."

newMsgs['242'] = {}
newMsgs['242']['txt-1'] = "You are successfully subscribed to MyGig2,5: 2Gb valid 30 days and 500Mb of BONUS to be used from 11pm to 05:59am. Press *999*114# to check remaining balance."
newMsgs['242']['txt-2'] = "Tafiditra ny MyGig2,5: ahazoanao 2Go ampiasaina mandritra ny 30 andro sy BONUS 500Mo ampiasaina @ 11ora alina-06 ora maraina. Megaoctet  tavela:*999*114#."
newMsgs['242']['txt-3'] = "La souscription a MyGig2,5 a ete effectuee avec succes: c est 2Go valable en 30 jours un BONUS de 500Mo, valable de 23h a 05h59. Solde restant: *999*114#."

newMsgs['244'] = {}
newMsgs['244']['txt-1'] = "You are successfully subscribed to MyGig15: 15Gb valid 30 days and 1Gb of BONUS to be used from 11pm to 05:59am. Press *999*114# to check remaining balance."
newMsgs['244']['txt-2'] = "Tafiditra ny MyGig15: ahazoanao 15Go ampiasaina mandritra ny 30 andro sy BONUS 1Go ampiasaina @ 11ora alina-06 ora maraina. Megaoctet  tavela:*999*114#."
newMsgs['244']['txt-3'] = "La souscription a MyGig15 a ete effectuee avec succes: c est 15Go valable en 30 jours un BONUS de 1Go, valable de 23h a 05h59. Solde restant: *999*114#."

newMsgs['197'] = {}
newMsgs['197']['txt-1'] = "Your subscription to FUN PLUS is successfully executed,offer valid till midnight.Thank you"
newMsgs['197']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUNPLUS,manankery hatr@ misasak alina.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['197']['txt-3'] = "Votre souscription a FUN PLUS est executee ,offre valable jusqu a minuit .Merci"


newMsgs['199'] = {}
newMsgs['199']['txt-1'] = "Your second subscription to FUN PLUS is successfully executed,offer valid till midnight.Thank you"
newMsgs['199']['txt-2'] = "Tontosa ny fampidiranao fanindroany ny FUNPLUS,manankery hatr@ misasak alina.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['199']['txt-3'] = "Votre deuxieme souscription a FUN PLUS est executee ,offre valable jusqu a minuit .Merc"


newMsgs['209'] = {}
newMsgs['209']['txt-1'] = Template("Your subscription to FUN RELAX is successfully executed,offer valid till $expiry.Thank you")
newMsgs['209']['txt-2'] = Template("Tontosa ny fangatahanao hampiasa ny FUN RELAX,manankery hatr@ $expiry.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko.")
newMsgs['209']['txt-3'] = Template("Votre souscription a FUN RELAX est executee ,offre valable jusqu a $expiry.Merci")


newMsgs['222'] = {}
newMsgs['222']['txt-1'] = "Your subscription to FUN RAITRA is successfully executed,offer valid till midnight.Thank you"
newMsgs['222']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN RAITRA,manankery hatr@ misasak alina.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['222']['txt-3'] = "Votre souscription a FUN RAITRA est executee ,offre valable jusqu a minuit .Merci"


newMsgs['223'] = {}
newMsgs['223']['txt-1'] = "Your second subscription to FUN RAITRA is successfully executed,offer valid on peak hours.Thank you"
newMsgs['223']['txt-2'] = "Tontosa ny fampidiranao fanindroany ny FUN RAITRA,manankery @ ora fialan tsasatra .Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['223']['txt-3'] = "Votre deuxieme souscription a FUN RAITRA est executee ,offre valable en heures creuses ce jour .Merci"


#newMsgs['250'] = {}
#newMsgs['250']['txt-1'] = "Tontosa ny fangatahanao hampiasa ny tolotra Daily Large Combo. Raha te hahafantatra ny ambim-bola Daily Large Combo, tsindrio *999*02#"
#newMsgs['250']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny tolotra Daily Large Combo. Raha te hahafantatra ny ambim-bola Daily Large Combo, tsindrio *999*02#."
#newMsgs['250']['txt-3'] = "Tontosa ny fangatahanao hampiasa ny tolotra Daily Large Combo. Raha te hahafantatra ny ambim-bola Daily Large Combo, tsindrio *999*02#."

newMsgs['250'] = {}
newMsgs['250']['txt-1'] = "You are now on I FUN , valid 24 hours.Thanks"
newMsgs['250']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny tolotra I-Fun. Tolotra manankery 24 ora .Misaotra tompoko"
newMsgs['250']['txt-3'] = "Vous etes maintenant sur I FUN ,valable 24 heures .Merci"


newMsgs['221'] = {}
newMsgs['221']['txt-1'] = "Your subscription to FUN FY is successfully executed,offer valid till midnight.Thank you"
newMsgs['221']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN FY,manankery hatr@ misasak alina.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['221']['txt-3'] = "Votre souscription a FUN FY est executee ,offre valable jusqu a minuit.Merc"

newMsgs['201'] = {}
newMsgs['201']['txt-1'] = "Your subscription to FUN 15 is successfully executed,offer valid on off peak hours.Thank you "
newMsgs['201']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN15,manankery @ ora fialan tsasatra.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['201']['txt-3'] = "Votre souscription a FUN 15 est executee ,offre valable en heures creuses .Merci"



newMsgs['211'] = {}
newMsgs['211']['txt-1'] = Template("Your subscription to FUN EXTRA is successfully executed,offer valid till $expiry.Thank you")
newMsgs['211']['txt-2'] = Template("Tontosa ny fangatahanao hampiasa ny FUN EXTRA,manankery hatr@ $expiry.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko.")
newMsgs['211']['txt-3'] = Template("Votre souscription a FUN EXTRA est executee ,offre valable jusqu a $expiry.Merci")


newMsgs['213'] = {}
newMsgs['213']['txt-1'] = Template("Your subscription to FUN ULTRA is successfully executed,offer valid till $expiry.Thank you")
newMsgs['213']['txt-2'] = Template("Tontosa ny fangatahanao hampiasa ny FUN ULTRA,manankery hatr@ $expiry.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko.")
newMsgs['213']['txt-3'] = Template("Votre souscription a FUN ULTRA est executee ,offre valable jusqu a $expiry.Merci")



newMsgs['215'] = {}
newMsgs['215']['txt-1'] = Template("Your subscription to FUN MAXI is successfully executed,offer valid till $expiry.Thank you")
newMsgs['215']['txt-2'] = Template("Tontosa ny fangatahanao hampiasa ny FUN MAXI,manankery hatr@ $expiry.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko.")
newMsgs['215']['txt-3'] = Template("Votre souscription a FUN MAXI est executee ,offre valable jusqu a $expiry.Merci")



newMsgs['217'] = {}
newMsgs['217']['txt-1'] = Template("Your subscription to MIX1 is successfully executed,offer valid till $expiry.Thank you")
newMsgs['217']['txt-2'] = Template("Tontosa ny fangatahanao hampiasa ny MIX1,manankery hatr@ $expiry.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko.")
newMsgs['217']['txt-3'] = Template("Votre souscription a MIX1 est executee ,offre valable jusqu a $expiry.Merci")


newMsgs['218'] = {}
newMsgs['218']['txt-1'] = Template("Your subscription to MIX2 is successfully executed,offer valid till $expiry.Thank you")
newMsgs['218']['txt-2'] = Template("Tontosa ny fangatahanao hampiasa ny MIX2,manankery hatr@ $expiry.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko.")
newMsgs['218']['txt-3'] = Template("Votre souscription a MIX2 est executee ,offre valable jusqu a $expiry.Merci")


newMsgs['219'] = {}
newMsgs['219']['txt-1'] = Template("Your subscription to MIX3 is successfully executed,offer valid till $expiry.Thank you")
newMsgs['219']['txt-2'] = Template("Tontosa ny fangatahanao hampiasa ny MIX3,manankery hatr@ $expiry.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko.")
newMsgs['219']['txt-3'] = Template("Votre souscription a MIX3 est executee ,offre valable jusqu a $expiry.Merci")

newMsgs['224'] = {}
newMsgs['224']['txt-1'] = "Your subscription to FUN ABY is successfully executed,offer valid till midnight.Thank you"
newMsgs['224']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN ABY ,manankery hatr@ misasak alina.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['224']['txt-3'] = "Votre souscription a FUN ABY est executee ,offre valable jusqu a minuit .Merci"


newMsgs['226'] = {}
newMsgs['226']['txt-1'] = "Your subscription to FUN450 is successfully executed,offer valid till midnight.Thank you"
newMsgs['226']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN450,manankery hatr@ 12 ora atoandro.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['226']['txt-3'] = "Your subscription to FUN450 is successfully executed,offer valid till midnight.Thank you"


newMsgs['194'] = {}
newMsgs['194']['txt-1'] = "Your subscription to FUN100 is successfully executed,offer valid till midnight.Thank you"
newMsgs['194']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN100,manankery hatr@ misasak alina.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['194']['txt-3'] = "Votre souscription a FUN100 est executee ,offre valable jusqu a minuit.Merci"

newMsgs['203'] = {}
newMsgs['203']['txt-1'] = "Your subscription to FUN &FRIENDLY is successfully executed,offer valid till midnight.Thank you"
newMsgs['203']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN &FRIENDLY,manankery hatr@ 12 ora atoandro.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['203']['txt-3'] = "Votre souscription a FUN &FRIENDLY est executee ,offre valable jusqu a midi .Merci"



newMsgs['203-2'] = {}
newMsgs['203-2']['txt-1'] = "Your subscription to FUN &FRIENDLY is successfully executed,offer valid till 5 pm.Thank you"
newMsgs['203-2']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN &FRIENDLY,manankery hatr@ 5 ora hariva.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['203-2']['txt-3'] = "Votre souscription a FUN &FRIENDLY est executee ,offre valable jusqu a 17 heures .Merci"


newMsgs['195'] = {}
newMsgs['195']['txt-1'] = "Your subscription to TAXI FUN is successfully executed,offer valid till 5 pm.Thank you"
newMsgs['195']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny TAXI FUN ,manankery hatr@ 5 ora hariva.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['195']['txt-3'] = "Votre souscription a TAXI FUN est executee ,offre valable jusqu a 17 heures.Merci"


newMsgs['220'] = {}
newMsgs['220']['txt-1'] = "Your subscription to FUN ORA is successfully executed,offer valid one hour.Thank you"
newMsgs['220']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN ORA,manankery adiny iray.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['220']['txt-3'] = "Votre souscription a FUN ORA est executee ,offre valable une heure .Merci"



newMsgs['205'] = {}
newMsgs['205']['txt-1'] = "Your subscription to BOJO is successfully executed,offer valid till midnight.Thank you"
newMsgs['205']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny BOJO ,manankery hatr@ misasak alina.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['205']['txt-3'] = "Votre souscription a BOJO est executee ,offre valable jusqu a minuit .Merci"

newMsgs['227'] = {}
newMsgs['227']['txt-1'] = "Your subscription is successfully executed,offer valid 24 hours.Thank you"
newMsgs['227']['txt-2'] = "Tontosa ny fangatahanao ,tolotra manankery 24 ora .Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['227']['txt-3'] = "Votre souscription est executee ,offre valable 24 heures.Merci"

newMsgs['228'] = {}
newMsgs['228']['txt-1'] = "Your subscription is successfully executed,offer valid 24 hours.Thank you"
newMsgs['228']['txt-2'] = "Tontosa ny fangatahanao ,tolotra manankery 24 ora .Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['228']['txt-3'] = "Votre souscription est executee ,offre valable 24 heures.Merci"

newMsgs['229'] = {}
newMsgs['229']['txt-1'] = "Your subscription is successfully executed,offer valid 24 hours.Thank you"
newMsgs['229']['txt-2'] = "Tontosa ny fangatahanao ,tolotra manankery 24 ora .Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['229']['txt-3'] = "Votre souscription est executee ,offre valable 24 heures.Merci"



newMsgs['230'] = {}
newMsgs['230']['txt-1'] = "Your subscription is successfully executed,offer valid 5 days.Thank you"
newMsgs['230']['txt-2'] = "Tontosa ny fangatahanao ,tolotra manankery 5 andro .Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['230']['txt-3'] = "Votre souscription est executee ,offre valable 5 jours .Merci"

newMsgs['231'] = {}
newMsgs['231']['txt-1'] = "Your subscription is successfully executed,offer valid 30 days.Thank you"
newMsgs['231']['txt-2'] = "Tontosa ny fangatahanao ,tolotra manankery 30 andro .Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko."
newMsgs['231']['txt-3'] = "Votre souscription est executee ,offre valable 30 jours .Merci"

newMsgs['234'] = {}
newMsgs['234']['txt-1'] = "Your subscription to Airtel 033 is successfully executed,offer valid till midnight. To check your balance, press *999#. Thank you"
newMsgs['234']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny AIRTEL 033, manankery hatr@ misasak alina. Fahana tavela:*999# .Misaotra tompoko"
newMsgs['234']['txt-3'] = "Votre souscription a Airtel 033 est executee ,offre valable jusqu a minuit. Consultation solde: *999#. Merci"

newMsgs['408'] = {}
newMsgs['408']['txt-1'] = "Tontosa ny fangatahanao ampiasa ny tolotra Bundle033 Mini afaka ampiasaina h@ 12ora alina. Misaotra tompoko"
newMsgs['408']['txt-2'] = "Tontosa ny fangatahanao ampiasa ny tolotra Bundle033 Mini afaka ampiasaina h@ 12ora alina. Misaotra tompoko"
newMsgs['408']['txt-3'] = "Tontosa ny fangatahanao ampiasa ny tolotra Bundle033 Mini afaka ampiasaina h@ 12ora alina. Misaotra tompoko"

'''
newMsgs['225'] = {}
newMsgs['225']['txt-1'] = "Your subscription to FUN AL is successfully executed. Enjoy UNLIMITED CALL to Airtel from 10 pm to 4 am. Thank you"
newMsgs['225']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny FUN AL, ahazoana antso airtel ILLIMITE manomboka @ 10 ora alina hatr@ 4 maraina.Misaotra tompoko."
newMsgs['225']['txt-3'] = "Votre souscription  a FUN AL est executee ,vous beneficiez d un appel ILLIMITE vers airtel de 22 heures  a 4 heures du matin.Merci"
'''
newMsgs['225'] = {}
newMsgs['225']['txt-1'] = "Your are now using FUN AL VACANCES:UNLIMITED call to airtel from 9 pm to 6 am .Thanks."
newMsgs['225']['txt-2'] = "Tafiditra FUN AL VACANCES ianao :antso airtel illimite manomboka amin ny 9 ora alina hatr@ 6 ora maraina.Misaotra tompoko."
newMsgs['225']['txt-3'] = "Vous etes sur FUN AL VACANCES, appels airtel ILLIMITE de 21h a 6 heures du matin.Merci."


newMsgs['207'] = {}
newMsgs['207']['txt-1'] = "You are on FUNCOOL and got Ar 1000 to call your friends at Ar 0 for first 20mn, airtel: Ar 1, other local network Ar 3. 2 SMS to Airtel for the price of one."
newMsgs['207']['txt-2'] = "Tafiditra FUNCOOL ianao: ahazoana Ar1000 hiantsoana Friends: Ar 0 - 20mn voalohany, airtel: Ar1, hafa: Ar3. Ankoatr izay, afaka mandefa SMS 2 @ vidin ny 1"
newMsgs['207']['txt-3'] = "Vous etes sur FUNCOOL: vous avez Ar1000 pour appeler vos Friends a Ar 0 les 20 premieres mn, airtel: Ar 1,autres reseaux: Ar 3. Et envoyer 2 SMS au prix d un"

newMsgs['Fun_Cool_Bogof'] = {}
newMsgs['Fun_Cool_Bogof']['txt-1'] = "You are on FunCoolPromo: Ar1000 + Ar1000 for Airtel calls at 1Ar-Other networks at 3Ar. 20Mn for Friends Calls and 2 SMS to airtel rated at the price of one."
newMsgs['Fun_Cool_Bogof']['txt-2'] = "Tafiditra ny FuncoolPromo: 1000Ar + 1000Ar hanaovana antso Airtel 1Ar-Hafa 3Ar. Ankoatr'izay misy 20Mn Friends ary afaka mandefa sms2 @ vidin ny1."
newMsgs['Fun_Cool_Bogof']['txt-3'] = "Vous etes souscrit a FunCoolPromo: 1000Ar + 1000Ar pour des appels Airtel a 1Ar - Autres a 3Ar. A part cela 20mn appel Friends et envoyez 2 SMS au prix d'un"

newMsgs['232'] = {}
newMsgs['232']['txt-1'] = "Your subscription is succesfully executed,you are now enjoying 7500 Ar for your airtel calls.Thank you"
newMsgs['232']['txt-2'] = "Tontosa ny fangatahanao .Nitombo avo 15 heny ny 500 Ar ka lasa 7500 Ar ahafahana miantso airtel .Manankery hatr@ misasak alina .Misaotra tompoko."
newMsgs['232']['txt-3'] = "Votre souscription est executee .Vous disposez de 7500 Ar d appels vers des numeros airtel ,valable jusqu a minuit.Merci"

newMsgs['233'] = {}
newMsgs['233']['txt-1'] = "Your subscription is succesfully executed,you are now enjoying 6000 Ar for your airtel calls.Thank you"
newMsgs['233']['txt-2'] = "Tontosa ny fangatahanao .Nitombo avo 12 heny ny 500 Ar ka lasa 6000Ar ahafahana miantso airtel .Manankery hatr@ misasak alina .Misaotra tompoko."
newMsgs['233']['txt-3'] = "Votre souscription est executee .Vous disposez de 6000 Ar d appels vers des numeros airtel ,valable jusqu a minuit.Merci"



newMsgs['251'] = {}
newMsgs['251']['txt-1'] = "Club SMS: You have received 100SMS, offer valid until 11:59 p.m. Thank you"
newMsgs['251']['txt-2'] = "Club SMS: Manana 100SMS ianao,manankery hatr@ 11:59 ora alina. Misaotra tompoko."
newMsgs['251']['txt-3'] = "Club SMS: Vous avez recu 100SMS , offre valable ce jour jusqu a 23h59. Merci"

newMsgs['Club_SMS_Bogof'] = {}
newMsgs['Club_SMS_Bogof']['txt-1'] = "Club SMS Promo: You have 100SMS + 100SMS GIFT and usable till 11:59pm"
newMsgs['Club_SMS_Bogof']['txt-2'] = "Club SMS Promo: Manana 100SMS + 100SMS KADOA ianao, manankery hatr@ 11:59 ora alina. Misaotra tompoko"
newMsgs['Club_SMS_Bogof']['txt-3'] = "Club SMS Promo: Vous avez recu 100SMS + 100SMS CADEAU, offre valable ce jour jusqu a 23h59. Merci"


newMsgs['256'] = {}
newMsgs['256']['txt-1'] = "Mini Club SMS: You have received 10SMS, offer valid until 11:59 p.m. Thank you"
newMsgs['256']['txt-2'] = "Mini Club SMS: Manana 10SMS ianao,manankery hatr@ 11:59 ora alina. Misaotra tompoko."
newMsgs['256']['txt-3'] = "Mini Club SMS: Vous avez recu 10SMS , offre valable ce jour jusqu a 23h59. Merci"

newMsgs['Club_SMS_Mini_Bogof'] = {}
newMsgs['Club_SMS_Mini_Bogof']['txt-1'] = "Mini Club SMS: Promo You have 10SMS + 10SMS GIFT and usable till 11:59pm"
newMsgs['Club_SMS_Mini_Bogof']['txt-2'] = "Mini Club SMS Promo: Manana 10SMS + 10SMS KADOA ianao, manankery hatr@ 11:59 ora alina. Misaotra tompoko"
newMsgs['Club_SMS_Mini_Bogof']['txt-3'] = "Mini Club SMS Promo: Vous avez recu 10SMS + 10SMS CADEAU, offre valable ce jour jusqu a 23h59. Merci"



newMsgs['235'] = {}
newMsgs['235']['txt-1'] = "Your subscription to FUN200 is successfully executed,offer valid till midnight.Thank you"
newMsgs['235']['txt-2'] = "Tontosa ny fangatahanao hampiasa FUN200,manankery hatr@ misasak alina. Madagasikara tanindrazako,Airtel tambazotrako"
newMsgs['235']['txt-3'] = "Votre souscription a FUN200 est executee ,offre valable jusqu a minuit.Merci"


newMsgs['253'] = {}
newMsgs['253']['txt-1'] = "Your subscription is succesfully executed,you are now enjoying 12000 Ar for your airtel calls.Thank you"
newMsgs['253']['txt-2'] = "Tontosa ny fangatahanao .Nitombo avo 12 heny ny 1000 Ar ka lasa 12000 Ar ahafahana miantso airtel .Manankery hatr@ misasak alina .Misaotra tompoko"
newMsgs['253']['txt-3'] = "Votre souscription est executee .Vous disposez de 12000 Ar d appels vers des numeros airtel ,valable jusqu a minuit.Merci"


newMsgs['252'] = {}
newMsgs['252']['txt-1'] = "Your subscription is succesfully executed,you are now enjoying 15000 Ar for your airtel calls.Thank you"
newMsgs['252']['txt-2'] = "Tontosa ny fangatahanao .Nitombo avo 15 heny ny 1000 Ar ka lasa 15000 Ar ahafahana miantso airtel .Manankery hatr@ misasak alina .Misaotra tompoko."
newMsgs['252']['txt-3'] = "Votre souscription est executee .Vous disposez de 15000 Ar d appels vers des numeros airtel ,valable jusqu a minuit.Merci"

newMsgs['257'] = {}
newMsgs['257']['txt-1'] = "You have subscribed to Airtel H@y. 150 MB usable for 1 day. *999*114*51# to know your balance"
newMsgs['257']['txt-2'] = "Tontosa ny fidiranao @ Airtel h@y: 150 Mo ampiasaina internet ao anatin ny 1 andro . Tsindrio *999*114*51# ahafahantaranao ny Megaoctet tavela"
newMsgs['257']['txt-3'] = "Vous avez souscrit a Airtel H@y. 150 Mo utilisable pendant 1jour. *999*114*51# pour connaitre votre solde"

newMsgs['258'] = {}
newMsgs['258']['txt-1'] = "You have subscribed to Airtel H@y. 350 MB usable for 5 days. *999*114*51# to check our balance"
newMsgs['258']['txt-2'] = "Tontosa ny fidiranao @ Airtel h@y: 350 Mo ampiasaina internet ao anatin ny 5 andro . Tsindrio *999*114*51# ahafahantaranao ny Megaoctet tavela"
newMsgs['258']['txt-3'] = "Vous avez souscrit a Airtel H@y. 350 Mo utilisable pendant 5 jours. *999*114*51# pour connaitre votre solde"

newMsgs['420'] = {}
newMsgs['420']['txt-1'] = "You have subscribed to Airtel H@y. 600 MB usable for 30 days. *999*114*51# to check your balance"
newMsgs['420']['txt-2'] = "Tontosa ny fidiranao @ Airtel h@y: 600 Mo ampiasaina internet ao anatin ny 30 andro . Tsindrio *999*114*51# ahafahantaranao ny Megaoctet tavela"
newMsgs['420']['txt-3'] = "Vous avez souscrit a Airtel H@y. 600 Mo utilisable pendant 30jours. *999*114*51# pour connaitre votre solde"

newMsgs['M4M_DAILY'] = {}
newMsgs['M4M_DAILY']['txt-1'] = "Your subscription is successfully executed. Enjoy the CALL, SMS and Internet of Airtel. Valid till 11:59 pm. Thank you"
newMsgs['M4M_DAILY']['txt-2'] = "Tontosa ny fangatahanao, Tolotra manankery hatr@11:59. Azo ampiasaina SMS, Internet ary antso mankany amin’ny tambazotra rehetra. Misaotra tompoko."
newMsgs['M4M_DAILY']['txt-3'] = "Votre souscription est executee, vous beneficiez d un appel, des SMS et linternet d Airtel. Valable jusqu a minuit. Merci"

newMsgs['M4M_WEEKLY'] = {}
newMsgs['M4M_WEEKLY']['txt-1'] = "Your subscription is successfully executed. Enjoy the CALL, SMS and Internet of Airtel. Offer valid 7 days. Thank you"
newMsgs['M4M_WEEKLY']['txt-2'] = "Tontosa ny fangatahanao, Tolotra manankery 7 andro. Azo ampiasaina SMS, Internet ary antso mankany amin’ny tambazotra rehetra. Misaotra tompoko."
newMsgs['M4M_WEEKLY']['txt-3'] = "Votre souscription est executee, vous beneficiez d un appel, des SMS et linternet d Airtel.  Offre valable 7 jours. Merci"

newMsgs['M4M_MONTHLY'] = {}
newMsgs['M4M_MONTHLY']['txt-1'] = "Your subscription is successfully executed. Enjoy the CALL, SMS and Internet of Airtel. Offer valid 30 days. Thank you"
newMsgs['M4M_MONTHLY']['txt-2'] = "Tontosa ny fangatahanao, Tolotra manankery 30 andro. Azo ampiasaina SMS, Internet ary antso mankany amin’ny tambazotra rehetra. Misaotra tompoko."
newMsgs['M4M_MONTHLY']['txt-3'] = "Votre souscription est executee, vous beneficiez d un appel, des SMS et linternet d Airtel.  Offre valable 30 jours. Merci"

newMsgs['Ser@200'] = {}
newMsgs['Ser@200']['txt-1'] = "You are subscribed to Ser@200. You have Ar 200 to make calls, SMS and for Internet connection. Calls to airtel are free from 10pm to 5am. Offer valid 1 day"
newMsgs['Ser@200']['txt-2'] = "Tontosa ny fidiranao ao @ Ser@200: Ar 200 hanaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 1 andro"
newMsgs['Ser@200']['txt-3'] = "Vous etes souscrit a Ser@200. Vous avez Ar 200 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 1 jour"

newMsgs['Ser@200_U&R'] = {}
newMsgs['Ser@200_U&R']['txt-1'] = "You are subscribed to Ser@200 + Ser@200 GIFT: Ar 400 for calls,SMS and for Internet connection.Calls to airtel are free from 10pm to 5am. Offer valid 1 day"
newMsgs['Ser@200_U&R']['txt-2'] = "Tafiditra ny Ser@200 miampy Ser@200 KADOA:400Ar anaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina-5ora maraina, manankery 1 andro"
newMsgs['Ser@200_U&R']['txt-3'] = "Vous etes souscrit a Ser@200+Ser@200 CADEAU:400Ar pour faire des appels,SMS ou Internet.L appel vers airtel est gratuit de 22h a 5h.Offre valable 1 jour"

newMsgs['Ser@500'] = {}
newMsgs['Ser@500']['txt-1'] = "You are subscribed to Ser@500. You have Ar 500 to make calls, SMS and for Internet connection. Calls to airtel are free from 10pm to 5am. Offer valid 1 day"
newMsgs['Ser@500']['txt-2'] = "Tontosa ny fidiranao ao @ Ser@500: Ar 500 hanaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 1 andro"
newMsgs['Ser@500']['txt-3'] = "Vous etes souscrit a Ser@500. Vous avez Ar 500 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 1 jour"

newMsgs['Ser@500_U&R'] = {}
newMsgs['Ser@500_U&R']['txt-1'] = "You are subscribed to Ser@500 + Ser@500 GIFT: Ar 1000 for calls, SMS and for Internet connection. Calls to airtel are free from 10pm to 5am. Offer valid 1day"
newMsgs['Ser@500_U&R']['txt-2'] = "Tafiditra ny Ser@500 miampy Ser@500 KADOA: Ar1000 hanaovana antso, SMS sy Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 1andro"
newMsgs['Ser@500_U&R']['txt-3'] = "Vous etes souscrit a Ser@500 + Ser@500 CADEAU: Ar 1000 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 1 jour"

newMsgs['Ser@1000'] = {}
newMsgs['Ser@1000']['txt-1'] = "You are subscribed to Ser@1000. You have Ar 1000 to make calls, SMS and for Internet connection. Calls to airtel are free from 10pm - 5am. Offer valid 1 day"
newMsgs['Ser@1000']['txt-2'] = "Tontosa ny fidiranao ao @ Ser@1000:Ar 1000 hanaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 1 andro"
newMsgs['Ser@1000']['txt-3'] = "Vous etes souscrit a Ser@1000. Vous avez Ar 1000 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 1 jour"

newMsgs['Ser@1000_U&R'] = {}
newMsgs['Ser@1000_U&R']['txt-1'] = "You are subscribed to Ser@1000 + Ser@1000 GIFT:Ar2000 for calls, SMS and for Internet connection. Calls to airtel are free from 10pm to 5am. Offer valid 1day"
newMsgs['Ser@1000_U&R']['txt-2'] = "Tafiditra ny Ser@1000 miampy Ser@1000 KADOA:Ar2000 hanaovana antso, SMS sy Internet.Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 1andro"
newMsgs['Ser@1000_U&R']['txt-3'] = "Vous etes souscrit a Ser@1000 + Ser@1000 CADEAU:Ar2000 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 1jour"

newMsgs['414'] = {}
newMsgs['414']['txt-1'] = "You are subscribed to Ser@1500. You have Ar 1500 to make calls, SMS and for Internet connection. Calls to airtel are free from 22pm - 5am. Offer valid 1 day"
newMsgs['414']['txt-2'] = "Tontosa ny fidiranao ao @ Ser@1500: Ar 1500 hanaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 1 andro"
newMsgs['414']['txt-3'] = "Vous etes souscrit a Ser@1500. Vous avez Ar 1500 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 1 jour"

newMsgs['415'] = {}
newMsgs['415']['txt-1'] = "You are subscribed to Ser@2000. You have Ar 2000 to make calls, SMS and for Internet connection. Calls to airtel are free from 22pm - 5am. Offer valid 7 days"
newMsgs['415']['txt-2'] = "Tontosa ny fidiranao ao @ Ser@2000: Ar 2000 hanaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 7 andro"
newMsgs['415']['txt-3'] = "Vous etes souscrit a Ser@2000. Vous avez Ar 2000 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 7 jours"

newMsgs['416'] = {}
newMsgs['416']['txt-1'] = "You are subscribed to Ser@3500. You have Ar 3500 to make calls, SMS and for Internet connection. Calls to airtel are free from 22pm - 5am. Offer valid 7 days"
newMsgs['416']['txt-2'] = "Tontosa ny fidiranao ao @ Ser@3500: Ar 3500 hanaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 7 andro"
newMsgs['416']['txt-3'] = "Vous etes souscrit a Ser@3500. Vous avez Ar 3500 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 7 jours"

newMsgs['417'] = {}
newMsgs['417']['txt-1'] = "You are subscribed to Ser@5000. You have Ar 5000 to make calls, SMS and for Internet connection. Calls to airtel are free from 22pm - 5am. Offer valid 7 days"
newMsgs['417']['txt-2'] = "Tontosa ny fidiranao ao @ Ser@5000: Ar 5000 hanaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 7 andro"
newMsgs['417']['txt-3'] = "Vous etes souscrit a Ser@5000. Vous avez Ar 5000 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 7 jours"

newMsgs['418'] = {}
newMsgs['418']['txt-1'] = "You are subscribed to Ser@10000. You have Ar10000 to make calls, SMS and for Internet connection. Calls to airtel are free from 22pm - 5am. Offer valid 30 days"
newMsgs['418']['txt-2'] = "Tontosa ny fidiranao ao @ Ser@10000: Ar 10000 hanaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 30 andro"
newMsgs['418']['txt-3'] = "Vous etes souscrit a Ser@10000. Vous avez Ar 10000 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 30 jours"

newMsgs['Ser@10000_Bogof'] = {}
newMsgs['Ser@10000_Bogof']['txt-1'] = "You are subscribed to Ser@10000 + Ser@10000 GIFT:Ar20000 for calls, SMS and Internet connection. Calls to airtel are free from 22pm to 5am. Offer valid 30days"
newMsgs['Ser@10000_Bogof']['txt-2'] = "Tafiditra ny Ser@10000 + Ser@10000 KADOA: Ar20000 hanaovana antso, SMS sy Internet.Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 30andro"
newMsgs['Ser@10000_Bogof']['txt-3'] = "Vous etes souscrit a Ser@10000 + Ser@10000 CADEAU: Ar20000 pour des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 30jours"

newMsgs['419'] = {}
newMsgs['419']['txt-1'] = "You are subscribed to Ser@20000. You have Ar20000 to make calls, SMS and for Internet connection. Calls to airtel are free from 22pm - 5am. Offer valid 30 days"
newMsgs['419']['txt-2'] = "Tontosa ny fidiranao ao @ Ser@20000: Ar 20000 hanaovana antso, SMS ary Internet. Maimaimpoana ny antso airtel @ 10ora alina - 5ora maraina, manankery 30 andro"
newMsgs['419']['txt-3'] = "Vous etes souscrit a Ser@20000. Vous avez Ar 20000 pour faire des appels, SMS ou Internet. L appel vers airtel est gratuit de 22h a 5h. Offre valable 30 jours"

newMsgs['396'] = {}
newMsgs['396']['txt-1'] = "Your request has been done with success, 100Gb valid for sharing till end of month, press *999*114*71# to check remaining balance. Thank you"
newMsgs['396']['txt-2'] = "Tontosa ny fangatahanao, 100Go azonao hozaraina h@ Faran ny volana. Tsindrion ny *999*114*71# hahafantaranao ny internet azonao zaraina. Misaotra tompoko"
newMsgs['396']['txt-3'] = "Votre demande a ete effectue avec succes, 100Go valide jusqu a la fin du mois, volume restant tapez *999*114*71#. Merci"

newMsgs['PARABOLE_NXT_MONTH_EXPIRY'] = {}
newMsgs['PARABOLE_NXT_MONTH_EXPIRY']['txt-1'] = "Your request has been done with success, 100Gb valid for sharing till end of next month, press *999*114*71# to check remaining balance. Thank you"
newMsgs['PARABOLE_NXT_MONTH_EXPIRY']['txt-2'] = "Tontosa ny fangatahanao, 100Go azonao hozaraina h@ faran ny volana manaraka. Tsindrion ny *999*114*71# hahafantaranao ny internet azonao zaraina."
newMsgs['PARABOLE_NXT_MONTH_EXPIRY']['txt-3'] = "Votre demande a ete effectuee avec succes, 100Go valide pour partage jusqu a la fin du mois prochain, volume restant tapez *999*114*71#. Merci"

newMsgs['LOW_COMBO_BUNDLE_500'] = {}
newMsgs['LOW_COMBO_BUNDLE_500']['txt-1'] = "Your request has been executed with success, offer valid for 1 day. Press *999*100*114# to check balance."
newMsgs['LOW_COMBO_BUNDLE_500']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny tolotra Mix500 maharitra 1andro, tsindrion ny *999*100*114# ahafantaranao ny antso sy Kilooctet azo ampiasaina"
newMsgs['LOW_COMBO_BUNDLE_500']['txt-3'] = "Votre demande a ete executee avec succes, offre valable 1 jour. Tapez *999*100*114# pour connaitre les forfaits restants."

newMsgs['397'] = {}
newMsgs['397']['txt-1'] = "You are succesfully subscribed to Facebook7 offer:250Mb valid 7 days.Press *999*47# to check remaining balance.Thank you"
newMsgs['397']['txt-2'] = "Tafiditra ny tolotra Facebook7:250Mo hanaovana Facebook manankery 7 andro.Tsindrion ny *999*47# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina"
newMsgs['397']['txt-3'] = "L'offre Facebook7 a ete effectue avec succes:250Mo valable 7jours.Tapez *999*47# pour consulter le forfait restant.Merci"

newMsgs['399'] = {}
newMsgs['399']['txt-1'] = Template("Your 5MB package is active and expire on $expiry. Press *999*338*100# for the remaining MB.Thank you")
newMsgs['399']['txt-2'] = Template("Tompoko, manana 5MB azo ampiasana h@ $expiry ianao. Tsindrio ny *999*338*100# ahafantaranao ny MB azonao ampiasaina.")
newMsgs['399']['txt-3'] = Template("Votre forfait de 5MB est active et expire le $expiry. Tapez *999*338*100# pour avoir le MB restant. Merci")

newMsgs['399-error'] = {}
newMsgs['399-error']['txt-1'] = "Your request is not executed. Press *338*100# OK. Cost: Ar6600. Thank you"
newMsgs['399-error']['txt-2'] = "Tsy tontosa ny fangatahanao. Tsindrio ny *338*100# raha hisafidy ampiasa io tolotra io. Sarany 6600 Ar. Misaotra tompoko"
newMsgs['399-error']['txt-3'] = "Votre demande n est pas executee. Tapez *338*100# OK pour vous souscrire a cette offre. Cout: Ar6600. Merci"

newMsgs['401'] = {}
newMsgs['401']['txt-1'] = Template("Your 30MB package is active and expire on $expiry. Press *999*338*103# for the remaining MB.Thank you")
newMsgs['401']['txt-2'] = Template("Tompoko, manana 30MB azo ampiasana h@ $expiry ianao. Tsindrio ny *999*338*103# ahafantaranao ny MB azonao ampiasaina.")
newMsgs['401']['txt-3'] = Template("Votre forfait de 30MB est active et expire le $expiry. Tapez *999*338*103# pour avoir le MB restant. Merci")

newMsgs['401-error'] = {}
newMsgs['401-error']['txt-1'] = "Your request is not executed. Press *338*103# OK. Cost: Ar24600. Thank you"
newMsgs['401-error']['txt-2'] = "Tsy tontosa ny fangatahanao. Tsindrio ny *338*103# raha hisafidy ampiasa io tolotra io. Sarany 24600 Ar. Misaotra tompoko"
newMsgs['401-error']['txt-3'] = "Votre demande n est pas executee. Tapez *338*103# OK pour vous souscrire a cette offre. Cout: Ar24600. Merci"

newMsgs['405'] = {}
newMsgs['405']['txt-1'] = Template("Your 30MB package is active and expire on $expiry. Press *999*338*101# for the remaining MB.Thank you")
newMsgs['405']['txt-2'] = Template("Tompoko, manana 30MB azo ampiasana h@ $expiry ianao. Tsindrio ny *999*338*101# ahafantaranao ny MB azonao ampiasaina.")
newMsgs['405']['txt-3'] = Template("Votre forfait de 30MB est active et expire le $expiry. Tapez *999*338*101# pour avoir le MB restant. Merci")

newMsgs['405-error'] = {}
newMsgs['405-error']['txt-1'] = "Your request is not executed. Press *338*101# OK. Cost: Ar31200. Thank you"
newMsgs['405-error']['txt-2'] = "Tsy tontosa ny fangatahanao. Tsindrio ny *338*101# raha hisafidy ampiasa io tolotra io. Sarany 31200 Ar. Misaotra tompoko"
newMsgs['405-error']['txt-3'] = "Votre demande n est pas executee. Tapez *338*101# OK pour vous souscrire a cette offre. Cout: Ar31200. Merci"

newMsgs['421'] = {}
newMsgs['421']['txt-1'] = Template("You have 5mn for outgoing call, 5mn for incoming call and  100Mb. Your package will expire on $expiry. Press *999*338*109# for the remaining balance. Thank you")
newMsgs['421']['txt-2'] = Template("Manana 5mn iantsoana ianao, 5mn handraisana antso ary 100Mo azo ampiasana hatr@ $expiry. Tsindrio ny *999*338*109# hamantarana ny ambina minitra sy Mo tavela")
newMsgs['421']['txt-3'] = Template("Votre forfait est active pour 5mn d appel sortant, 5mn entrant et 100 Mo. Ceci expirera le $expiry. Tapez *999*338*109# pour avoir le Mo restant. Merci")

newMsgs['422'] = {}
newMsgs['422']['txt-1'] = Template("You have 20mn for outgoing call, 20mn for incoming call and  250Mb. Your package will expire on $expiry. Press *999*338*110# for the remaining balance. Thank you")
newMsgs['422']['txt-2'] = Template("Manana 20mn iantsoana ianao, 20mn handraisana antso ary 250Mo azo ampiasana hatr@ $expiry. Tsindrio ny *999*338*110# hamantarana ny ambina minitra sy Mo tavela")
newMsgs['422']['txt-3'] = Template("Votre forfait est active pour 20mn d appel sortant, 20mn entrant et 250Mo. Ceci expirera le $expiry. Tapez *999*338*110# pour avoir le Mo restant. Merci")

newMsgs['421-error'] = {}
newMsgs['421-error']['txt-1'] = "Sorry, your request is not executed. Press *338*109# and then OK to subscribe to this offer. Cost : Ar 26500. Thank you"
newMsgs['421-error']['txt-2'] = "Miala tsiny, tsy tontosa ny fangatahanao. Tsindrio ny *338*109# raha hampiasa io tolotra io. Sarany: Ar  26500. Misaotra tompoko"
newMsgs['421-error']['txt-3'] = "Desole, votre demande n est pas executee. Tapez *338*109# puis OK pour vous souscrire a cette offre. Cout: Ar 26500. Merci"

newMsgs['410-error'] = {}
newMsgs['410-error']['txt-1'] = "Your request is not executed.  Thank you"
newMsgs['410-error']['txt-2'] = "Tsy tontosa ny fangatahanao.  Misaotra tompoko"
newMsgs['410-error']['txt-3'] = "Votre demande n est pas executee.  Merci"

newMsgs['425'] = {}
newMsgs['425']['txt-1'] = "Whatsapp offer is executed with success and valid 30 days. Check remaining balance press *999*46#"
newMsgs['425']['txt-2'] = "Tafiditra ny Tolotra Whatsapp manankery 30andro. Tsindrion ny *999*46# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina"
newMsgs['425']['txt-3'] = "L'offre whatsapp a ete executee avec succes et valable 30jours. Tapez *999*46# pour connaitre les volume restants"

newMsgs['426'] = {}
newMsgs['426']['txt-1'] = "You are subscribed to I-Ser@200 Promo:20Mb valid 1 day and 20Mb of BONUS to be used from 10pm to 04:59am.Press *999*114# to check remaining balance"
newMsgs['426']['txt-2'] = "Tafiditra ny I-Ser@200 Promo:20Mo ampisaina internet h@ 12ora alina sy BONUS 20Mo ampiasaina @ 10ora alina-5ora maraina.Megaoctet tavela: *999*114#"
newMsgs['426']['txt-3'] = "Vous etes souscrit a I-Ser@200 Promo:20Mo utilisable 1 jour et un BONUS de 20Mo,valable de 22h a 04h59.Solde restant:*999*114#"

#===========End of replacing temporary messgaes ===================

#====Names of above package ids==============
'''
tempMsgs = {}
tempMsgs[MyMeg 15][1]
tempMsgs[MyMeg 50][4]  
tempMsgs[MyMeg 100][6] 
tempMsgs[MyMeg 250][8]
tempMsgs[MyMeg 500][9]
tempMsgs[MyGig 1][11]
tempMsgs[MyGig 2][12]
tempMsgs[MyGig 5][14]
tempMsgs[MyGig 10][15]
tempMsgs[MyGig 30][16]
tempMsgs[Facebook][19]
tempMsgs[Twitter][20]
tempMsgs[Whatsapp][21]
tempMsgs[MyMeg 50(GIFT)][22]
tempMsgs[MyMeg 100(GIFT)][23]
tempMsgs[MyMeg 250(GIFT)][24]
tempMsgs[MyMeg 500(GIFT)][25]
tempMsgs[MyGig 1(GIFT)][26]
tempMsgs[MyGig 2GIFT)][27]
tempMsgs[MyGig 5(GIFT)][28]
tempMsgs[MyGig 10(GIFT)][30]
tempMsgs[MyGig 30(GIFT)][30]
tempMsgs[MyMeg 15 (GIFT)][121]
tempMsgs[Facebook (GIFT)][122]
tempMsgs[Twitter (GIFT)][123]
tempMsgs[Whatsapp (GIFT)][124]
tempMsgs[MyMeg 50(NIGHT)][33]
tempMsgs[MyMeg 100(NIGHT)][35]
tempMsgs[Regional][119]

'''
#====End of Names================================================================

MESSAGES['success'] = Template("Tontosa ny fangatahanao. Tsindrio ny *999*55# raha hijery ireo isa efa azonao @ Promo Mifety 55. Misaotra tompoko")

MESSAGES['success_15'] = "Tafiditra ny MyMeg15 ahazoanao 15Mo ampiasaina internet. Fijerena Mo tavela: tsindrio ny *999*114#. Misaotra tompoko"

MESSAGES['success_15_morn'] = "Tafiditra ny Mymeg15: 15Mo ampiasaina internet hatr@12 ora. Tsindrio ny *999*114# ahafantaranao ny Kilooctet sy ny megaoctet sisa azo ampiasaina."

MESSAGES['success_15_afte'] = "Tafiditra ny MyMeg15 ahazoanao 15Mo ampiasaina internet hatr@ 5 ora. Tsindrion ny *999*114# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."

MESSAGES['isBarred_MyMeg5'] = 'Tompoko tsy afaka mampiasa io tolotra io ianao, MyMeg10 ahazoana 10Mo @ sarany 200ar monja ary maharitra 1 andro. Tsindrio ny *114*41#'

MESSAGES['isBarred_Bundle200'] = 'Miala tsiny tompoko, tsy afaka mampiasa an io tolotra io ianao. Misaotra tompoko.'

MESSAGES['isBarred_Mix500'] = 'Miala tsiny tompoko, tsy afaka mampiasa an io tolotra io ianao. Misaotra tompoko.'

MESSAGES['success_15_french'] = "Votre demande a ete executee. Vous avez 15Mo d'internet. Tapez *999*114# pour connaitre les Mo restants.Merci"

MESSAGES['time_barred'] = "Ny fidirana amin io tolotra io dia misokatra hatramin ny 5 ora hariva ihany. Manasa anao hampiasa Mymeg 50 *114*4#. Misaotra tompoko."

MESSAGES['time_barred_french'] = "Cher client,votre demande n a pas ete executee. Vous pouvez souscrire a MyMeg15 de 8h-12h et de 13h-17h. Merci"

MESSAGES["time_barred_bparty"] = "Chere client, on ne peut pas pourchaser MyMeg15 pour votre ami parceque il est disponible seulement de 8h-12h et de 13h-17h Merci"

MESSAGES["morning_barred"] = "Tompoko, tsy tontosa ny fangatahanao. Manomboka amin ny 1ora-5ora no hahafahanao miditra indray amin ny MyMeg15 . Misaotra tompoko"
MESSAGES["morning_barred_french"] = "Cher client,v otre demande n a pas ete executee. Vous pouvez souscrire a nouveau de 13h jusqu a 17h. Merci"

MESSAGES["afternoon_barred"] = "Tompoko, tsy tontosa ny fangatahanao. Efa feno ny hahafahanao mampiasa io tolotra io androany. Misaotra tompoko "
MESSAGES["afternoon_barred_french"] = "Cher client,votre demande n a pas ete executee. Vous avez atteint le nombre de souscription autorise pour ce jour. Merci"

MESSAGES['success_night'] = Template("Tontosa ny fangatahanao. Ianao dia manana $data hanaovana internet. Tsindrio ny *999*103# ahafantaranao ny ambiny afaka ampiasainao. Misaotra tompoko")

MESSAGES['social'] = Template("Tontosa ny fangatahanao: 75Mo ho an ny $data manankery 1 andro. Tsindrio ny *999*$code# ahafantaranao ny ambina Kilooctet sy Megaoctet azo ampiasaina.")
MESSAGES['kozy'] = "Kozy Kozy: Manana 900 sec, 45 SMS sy 50 Mo ianao,manankery hatr@ 11:59 ora alina. Misaotra tompoko."
MESSAGES['regional'] = "Tontosa ny fangatahanao hampiasa ny tolotra Internet Mlay, manakery hatramin ny 11:59 alina. Misaotra tompoko"


MESSAGES['balance'] = Template('Ils vous reste $data qui expirera le $expiry.')
MESSAGES['no_balance'] = "vous n'avez pas un forfait en cours"

MESSAGES['ack'] = 'Request received, Check the confirmation messages and then restart the device before you start browsing'
MESSAGES['error'] = '''Tsy tontosa ny fangatahanao. Avereno afaka fotoana fohy azafady. Misaotra tompoko'''

MESSAGES['conflicting_bundle'] = 'Dear customer you are currently subscribed to another bundle. To purchase this bundle please exhaust your current bundle. Dial *544# to check your current bundle balance. Airtel.'

MESSAGES['subscriber'] = {}
MESSAGES['subscriber']['success'] = Template("Felicitations. Vous venez d'offrir avec succes $data valide pour $days jours au $b_msisdn.Naviguez vite et moins cher.Cliquez ici www.opera.com")

#MESSAGES['insufficient_funds'] = 'Dear customer you do not have sufficient funds to purchase this bundle. Please reload and try again. Airtel.'
#MESSAGES['insufficient_funds'] = "Vous n'avez pas assez de credit pour vous abonner. Merci de recharger votre compte"
#MESSAGES['insufficient_funds'] = "Desole! Vpus n'avez pas de credit pour souscrire a ce forfait. Veuillez recharger plus reessayer SVP!"

MESSAGES['insufficient_funds'] = 'Your current balance is insufficient to subscribe to this offer, please refill your account and submit your request. Thank you'
MESSAGES['insufficient_funds'] = "Miala tsiny, tsy ampy ny fahana ahafahanao mampiasa io tolotra io. Mampidira fahana ary avereno ny fangatahanao azafady. Misaotra tompoko"
MESSAGES['insufficient_funds'] = "Desole, votre credit est insuffisant pour effectuer cette requete. Veuillez recharger votre compte et renvoyer votre demande. Merci"

MESSAGES['recipient'] = {}
MESSAGES['recipient']['success'] = Template("Felicitations.le $benefactor vient de vous offrir $data valable jusqu'au $expiry.Naviquez vite et moins cher.Cliquez ici www.opera.com")
MESSAGES['is_barred'] = 'Tsy tontosa ny fangatahanao. Avereno afaka fotoana fohy azafady. Misaotra tompoko'
MESSAGES['renewal_removed'] = 'Votre renouvellement a ete desactive avec succes'
MESSAGES['no_renew'] = "Desole  vous n'avez pas de renouvellement active"
MESSAGES['tip'] = 'Press *131# to check your current balance before your start browsing. If balance still same, revise the process. Airtel'

MESSAGES['unlimited_succ'] = {}
MESSAGES['unlimited_succ']['txt-1']  = "Your subscription to the Unlimited Internet Offer was performed with success. Thank you"
MESSAGES['unlimited_succ']['txt-3'] = "Votre souscription a I offer Internet illimite a ete effectuee avec succes. Merci"
MESSAGES['unlimited_succ']['txt-2'] = "Tontosa ny fangatahanao hampiasa ny tolotra internet illimite. Misaotra tompoko"

MESSAGES['unlimited_unsucc'] = {}
MESSAGES['unlimited_unsucc']['txt-1'] = "Your subscription to the Unlimited Internet offer was rejected. Please refill your account and try later. Thank you"
MESSAGES['unlimited_unsucc']['txt-3'] = "Votre souscription a I offer internet Illimite a ete rejetee. Veuillez rajouter du credit a votre compte et reessayer plus tard. Merci"
MESSAGES['unlimited_unsucc']['txt-2'] = "Votre souscription a I offer internet Illimite a ete rejetee. Veuillez rajouter du credit a votre compte et reessayer plus tard. Merci"

MESSAGES['success_I-Ser@200'] = {}
MESSAGES['success_I-Ser@200']['txt-1'] = "You are succesfully subscribed to I-Ser@200:5Mb valid 1 day and 5Mb of BONUS to be used from 10pm to 04:59am.Press *999*114# to check remaining balance"
MESSAGES['success_I-Ser@200']['txt-2'] = "Tafiditra ny I-Ser@200:ahazoana 5Mo ampisaina internet h@ 12ora alina sy BONUS 5Mo ampiasaina @10ora alina-5ora maraina. Megaoctet tavela:*999*114# "
MESSAGES['success_I-Ser@200']['txt-3'] = "La souscription a I-Ser@200  a ete effectue avec succes:c est 5Mo utilisable 1 jour et un BONUS de 5Mo,valable de 22h a 04h59.Solde restant:*999*114# "

MESSAGES['success_I-Ser@200_U&R'] = {}
MESSAGES['success_I-Ser@200_U&R']['txt-1'] = "You are subscribed to I-Ser@200 + I-Ser@200 GIFT:10Mb valid 1 day and 10Mb of BONUS to be used from 10pm to 04:59am. Press *999*114# to check remaining balance"
MESSAGES['success_I-Ser@200_U&R']['txt-2'] = "Tafiditra ny I-Ser@200 + I-Ser@200 KADOA:10Mo azo ampisaina hatr@ 12ora alina sy BONUS 10Mo ampiasaina @10ora alina-5ora maraina. Megaoctet tavela: *999*114#"
MESSAGES['success_I-Ser@200_U&R']['txt-3'] = "Vous etes souscrit a I-Ser@200 + I-Ser@200 CADEAU:10Mo utilisable 1 jour et un BONUS de 10Mo,valable de 22h a 04h59. Solde restant:*999*114#"

MESSAGES['success_mymeg_10'] = "Tafiditra ny MyMeg10: 10Mo ampiasaina internet hatramin ny 12 ora. Tsindrion ny *999*114# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
MESSAGES['success_mymeg_10_morn'] = "Tafiditra ny MyMeg10 ahazoanao 10Mo ampiasaina internet hatr@ 12 ora. Tsindrio ny *999*114# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
MESSAGES['success_mymeg_10_afte'] = "Tafiditra ny MyMeg10 ahazoanao 10Mo ampiasaina internet hatr@ 5 ora. Tsindrion ny *999*114# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."

MESSAGES['success_fb_weekly'] = {}
MESSAGES['success_fb_weekly']['txt-1'] = "Facebook4 offer is executed with success and valid 4 days. Check remaining balance press *999*44#"
MESSAGES['success_fb_weekly']['txt-2'] = "Tafiditra ny tolotra Facebook4 manankery 4andro. Tsindrion ny *999*44# ahafantaranao ny kiloctet sy Megaoctet sisa azo ampiasaina"
MESSAGES['success_fb_weekly']['txt-3'] = "L'offre Facebook4 a ete executee avec succes et valable 4 jours. Tapez *999*44# pour connaitre les volumes restants"

MESSAGES['success_tw_weekly'] = "Tafiditra ny tolotra Twitter manankery 7 andro. Tsindrion ny *999*45# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."
MESSAGES['success_wa_weekly'] = "Tafiditra ny Tolotra Whatsapp manankery 7 andro. Tsindrion ny *999*46# ahafantaranao ny Kiloctet sy Megaoctet sisa azo ampiasaina."

MESSAGES['isBarred_alt_FunAby'] = {}
MESSAGES['isBarred_alt_FunAby']['txt-1']  = "Your subscription isn t executed,access is  open till 5 pm.Please use FUN ABY *100*23# .Thank you"
MESSAGES['isBarred_alt_FunAby']['txt-3'] = "Votre souscription n'est pas executee L'acces a cette offre est ouvert  jusqu a 17 heures.Veuillez utiliser FUN ABY *100*23# .Merci"
MESSAGES['isBarred_alt_FunAby']['txt-2'] = "Tsy tontosa ny fangatahanao.Ny fidirana @ io tolotra io dia  misokatra hatr@ 5 ora hariva .Ampiasao FUN ABY  *100*23#.Misaotra tompoko."


MESSAGES['isBarred_alt_FunCool'] = {}
MESSAGES['isBarred_alt_FunCool']['txt-1']  = "Your subscription isn t executed,access is  open till 5 pm.Please use FUN COOL *100*12# .Thank you"
MESSAGES['isBarred_alt_FunCool']['txt-3'] = "Votre souscription n est pas executee L'acces a cette offre est ouvert  jusqu a 17 heures.Veuillez utiliser FUN COOL *100*12# .Merci"
MESSAGES['isBarred_alt_FunCool']['txt-2'] = "Tsy tontosa ny fangatahanao.Ny fidirana @ io tolotra io dia  misokatra hatr@ 5 ora hariva .Ampiasao FUN COOL  *100*12#.Misaotra tompoko."

MESSAGES['isBarred_alt_CLUBSMS'] = {}
MESSAGES['isBarred_alt_CLUBSMS']['txt-1']  = "Dear customer,subscription to this offer is not available .Please use CLUB SMS.Press *100*2#. Cost Ar 500"
MESSAGES['isBarred_alt_CLUBSMS']['txt-3'] = "Cher client,cette offre n est pas disponible.Nous vous invitons a utiliser CLUB SMS. Tapez *100*2#.Cout Ar 500"
MESSAGES['isBarred_alt_CLUBSMS']['txt-2'] = "ialana tsiny tompoko, tsy misokatra io tolotra io.Manasa anao hampiasa CLUB SMS.Fidirana *100*2#. Sarany Ar 500"

MESSAGES['isBarred_FunAl'] = {}
MESSAGES['isBarred_FunAl']['txt-1']  = "Your current tarif plan does not allow you to access to this offer.Thanks"
MESSAGES['isBarred_FunAl']['txt-3'] = "Votre plan tarifaire actuel n a pas d acces a cette offre.Merci"
MESSAGES['isBarred_FunAl']['txt-2'] = "Tsy afaka mampiasa io tolotra io ny tarif ampiasainao.Misaotra tompoko"


MESSAGES['isBarred_FunAl_time'] = {}
MESSAGES['isBarred_FunAl_time']['txt-1']  = "Subscription not succesful.Time allowed is 10PM-4AM"
MESSAGES['isBarred_FunAl_time']['txt-3'] = "Subscription not succesful.Time allowed is 10PM-4AM"
MESSAGES['isBarred_FunAl_time']['txt-2'] = "Subscription not succesful.Time allowed is 10PM-4AM"


MESSAGES['isBarred_Not_whitelisted'] = {}
MESSAGES['isBarred_Not_whitelisted']['txt-1']  = "Dear customer,subscription to this offer is not available .Please use FUN COOL including free calls  to your friends number.Press *100*12#. Cost Ar 1000"
MESSAGES['isBarred_Not_whitelisted']['txt-3'] = "Cher client,cette offre n est pas disponible.Nous vous invitons a utiliser FUN COOL incluant des appels gratuits vers vos friends. Tapez *100*12#.Cout Ar 1000"
MESSAGES['isBarred_Not_whitelisted']['txt-2'] = "ialana tsiny tompoko, tsy misokatra io tolotra io.Manasa anao hampiasa FUN COOL misy antso friends maimaimpoana .Fidirana *100*12#. Sarany Ar 1000"

#isBarred_past5pm

MESSAGES['isBarred_past5pm'] = {}
MESSAGES['isBarred_past5pm']['txt-1']  = "Your subscription isnt executed,access is  open till 5 pm.Thank you"
MESSAGES['isBarred_past5pm']['txt-3'] = "Votre souscription n est pas executee L acces a cette offre est ouvert  jusqu a 17 heures .Merci"
MESSAGES['isBarred_past5pm']['txt-2'] = "Tsy tontosa ny fangatahanao.Ny fampiasana io tolotra io dia  misokatra hatr@ 5 ora hariva .Misaotra tompoko."


MESSAGES['subscriber_success_fun_ora'] = {}
MESSAGES['subscriber_success_fun_ora']['txt-1'] = Template("Your request to give FUN ORA to $b_msisdn is successfully executed,offer valid one hour.Thank you")
MESSAGES['subscriber_success_fun_ora']['txt-2'] = Template("Tontosa ny fanomezanao FUN ORA any @ laharana $b_msisdn manankery adiny iray.Madagasikara tanindrazako,airtel tambazotrako.Misaotra tompoko.")
MESSAGES['subscriber_success_fun_ora']['txt-3'] = Template("Votre demande d'offrir FUN ORA au numero $b_msisdn est executee ,offre valable une heure .Merci")


MESSAGES['subscriber_success_fun_cool'] = {}
MESSAGES['subscriber_success_fun_cool']['txt-1'] = Template("Your request to give FUN COOL to $b_msisdn is successfully executed .Offer valid 1 day.Thank you")
MESSAGES['subscriber_success_fun_cool']['txt-2'] = Template("Tontosa ny fanomezanao FUN COOL any @ laharana $b_msisdn. Manankery  1 andro.Misaotra tompoko")
MESSAGES['subscriber_success_fun_cool']['txt-3'] = Template("Votre demande d offrir FUN COOL au $b_msisdn est executee .Offre valable 1 jour .Merci")


MESSAGES['subscriber_success_fun15'] = {}
MESSAGES['subscriber_success_fun15']['txt-1'] = Template("You have succesfully made a FUN15 gift to $b_msisdn.Thanks.")
MESSAGES['subscriber_success_fun15']['txt-2'] = Template("Tontosa ny fangatahanao hanolotra FUN15 hoan ny $b_msisdn manankery @ ora fialan tsasatra na Alahady tontolo.Misaotra tompoko.")
MESSAGES['subscriber_success_fun15']['txt-3'] = Template("L'envoi de FUN15 vers le $b_msisdn FUN15 est reussi.Merci.")

MESSAGES['subscriber_success_funPlus'] = {}
MESSAGES['subscriber_success_funPlus']['txt-1'] = Template("Your request to give FUN PLUS to $b_msisdn is successfully executed .Thank you")
MESSAGES['subscriber_success_funPlus']['txt-2'] = Template("Tontosa ny fanomezanao FUN PLUS any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_funPlus']['txt-3'] = Template("Votre demande d offrir FUN PLUS au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_funRaitra'] = {}
MESSAGES['subscriber_success_funRaitra']['txt-1'] = Template("Your request to give FUN RAITRA to $b_msisdn is successfully executed .Thank you")
MESSAGES['subscriber_success_funRaitra']['txt-2'] = Template("Tontosa ny fanomezanao FUN RAITRA any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_funRaitra']['txt-3'] = Template("Votre demande d offrir FUN RAITRA au $b_msisdn est executee  .Merci")

MESSAGES['subscriber_success_funRelax'] = {}
MESSAGES['subscriber_success_funRelax']['txt-1'] = Template("Your request to give FUN RELAX to $b_msisdn is successfully executed .Thank you")
MESSAGES['subscriber_success_funRelax']['txt-2'] = Template("Tontosa ny fanomezanao FUN RELAX any @ laharana $b_msisdn .Misaotra tompoko")
MESSAGES['subscriber_success_funRelax']['txt-3'] = Template("Votre demande d offrir FUN RELAX au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_funExtra'] = {}
MESSAGES['subscriber_success_funExtra']['txt-1'] = Template("Your request to give FUN EXTRA to $b_msisdn is successfully executed .Thank you")
MESSAGES['subscriber_success_funExtra']['txt-2'] = Template("Tontosa ny fanomezanao FUN EXTRA any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_funExtra']['txt-3'] = Template("Votre demande d offrir FUN EXTRA au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_funUltra'] = {}
MESSAGES['subscriber_success_funUltra']['txt-1'] = Template("Your request to give FUN ULTRA to $b_msisdn is successfully executed .Thank you")
MESSAGES['subscriber_success_funUltra']['txt-2'] = Template("Tontosa ny fanomezanao FUN ULTRA any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_funUltra']['txt-3'] = Template("Votre demande d offrir FUN ULTRA au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_funMaxi'] = {}
MESSAGES['subscriber_success_funMaxi']['txt-1'] = Template("Your request to give FUN MAXI to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_funMaxi']['txt-2'] = Template("Tontosa ny fanomezanao FUN MAXI any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_funMaxi']['txt-3'] = Template("Votre demande d offrir FUN MAXI au $b_msisdn est executee .Merci")
   
MESSAGES['subscriber_success_Mix1'] = {}
MESSAGES['subscriber_success_Mix1']['txt-1'] = Template("Your request to give MIX1 to $b_msisdn is successfully executed .Thank you")
MESSAGES['subscriber_success_Mix1']['txt-2'] = Template("Tontosa ny fanomezanao MIX1 any @ laharana $b_msisdn.Misaotra tompoko")
MESSAGES['subscriber_success_Mix1']['txt-3'] = Template("Votre demande d offrir MIX1 au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_Mix2'] = {}
MESSAGES['subscriber_success_Mix2']['txt-1'] = Template("Your request to give MIX2 to $b_msisdn is successfully executed .Thank you")
MESSAGES['subscriber_success_Mix2']['txt-2'] = Template("Tontosa ny fanomezanao MIX2 any @ laharana $b_msisdn.Misaotra tompoko")
MESSAGES['subscriber_success_Mix2']['txt-3'] = Template("Votre demande d offrir MIX2 au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_Mix3'] = {}
MESSAGES['subscriber_success_Mix3']['txt-1'] = Template("Your request to give MIX3 to $b_msisdn is successfully executed .Thank you")
MESSAGES['subscriber_success_Mix3']['txt-2'] = Template("Tontosa ny fanomezanao MIX3 any @ laharana $b_msisdn.Misaotra tompoko")
MESSAGES['subscriber_success_Mix3']['txt-3'] = Template("Votre demande d offrir MIX3 au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_funAby'] = {}
MESSAGES['subscriber_success_funAby']['txt-1'] = Template("Your request to give FUN ABY to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_funAby']['txt-2'] = Template("Tontosa ny fanomezanao FUN ABY any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_funAby']['txt-3'] = Template("Votre demande d offrir FUN ABY au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_Bojo'] = {}
MESSAGES['subscriber_success_Bojo']['txt-1'] = Template("Your request to give BOJO to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_Bojo']['txt-2'] = Template("Tontosa ny fanomezanao BOJO any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_Bojo']['txt-3'] = Template("Votre demande d offrir BOJO au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_Boost1000'] = {}
MESSAGES['subscriber_success_Boost1000']['txt-1'] = Template("Your request to give BOOST 1000 to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_Boost1000']['txt-2'] = Template("Tontosa ny fanomezanao BOOST 1000 any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_Boost1000']['txt-3'] = Template("Votre demande d offrir BOOST 1000 au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_funAl'] = {}
MESSAGES['subscriber_success_funAl']['txt-1'] = Template("Your request to give FUN AL to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_funAl']['txt-2'] = Template("Tontosa ny fanomezanao FUN AL any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_funAl']['txt-3'] = Template("Votre demande d offrir FUN AL au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_ArivoWeekday'] = {}
MESSAGES['subscriber_success_ArivoWeekday']['txt-1'] = Template("Your request to give BOOST ARIVO to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_ArivoWeekday']['txt-2'] = Template("Tontosa ny fanomezanao BOOST ARIVO any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_ArivoWeekday']['txt-3'] = Template("Votre demande d offrir BOOST ARIVO au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_ArivoWeekend'] = {}
MESSAGES['subscriber_success_ArivoWeekend']['txt-1'] = Template("Your request to give BOOST ARIVO to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_ArivoWeekend']['txt-2'] = Template("Tontosa ny fanomezanao BOOST ARIVO any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_ArivoWeekend']['txt-3'] = Template("Votre demande d offrir BOOST ARIVO au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_BoostWE'] = {}
MESSAGES['subscriber_success_BoostWE']['txt-1'] = Template("Your request to give BOOST WEEK END to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_BoostWE']['txt-2'] = Template("Tontosa ny fanomezanao BOOST WEEK END any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_BoostWE']['txt-3'] = Template("Votre demande d offrir BOOST WEEK END au $b_msisdn est executee .Merci")

MESSAGES['subscriber_success_Boost500'] = {}
MESSAGES['subscriber_success_Boost500']['txt-1'] = Template("Your request to give BOOST 500 to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_Boost500']['txt-2'] = Template("Tontosa ny fanomezanao BOOST 500 any @ laharana $b_msisdn. Misaotra tompoko")
MESSAGES['subscriber_success_Boost500']['txt-3'] = Template("Votre demande d offrir BOOST 500 au $b_msisdn est executee .Merci")


MESSAGES['recipient_success_fun_ora'] ={}
MESSAGES['recipient_success_fun_ora']['txt-1'] = Template("You have received FUN ORA from $benefactor.You have 500s to call Airtel, valid one hour.Thank you")
MESSAGES['recipient_success_fun_ora']['txt-2'] = Template("Naharay  FUN ORA avy any @ $benefactor ianao. Noho izany, manana 500 s ianao hiantsoana airtel ao anatin'ny adiny iray.Misaotra tompoko")
MESSAGES['recipient_success_fun_ora']['txt-3'] = Template("Vous avez recu FUN ORA du $benefactor, et actuellement Vous disposez de 500s pour appeler des numéros airtel durant l' heure qui suit .Merci")

MESSAGES['recipient_success_fun_cool'] ={}
MESSAGES['recipient_success_fun_cool']['txt-1'] = Template("You got FUN COOL from $benefactor and have 1000 Ar to call Friends at 0Ar (max 20mn).Airtel 1Ar.Other local network 3Ar. 2 SMS are billed as only one")
MESSAGES['recipient_success_fun_cool']['txt-2'] = Template("Nahazo FUN COOL tany @ $benefactor ianao.Efa misy 1000 Ar.Iantsoana friends: 0Ar (hatr@ 20mn);Airtel 1Ar.Hafa 3 Ar. SMS 2 @ vidin ny 1.Manankery 1 andro")
MESSAGES['recipient_success_fun_cool']['txt-3'] = Template("Le $benefactor vous a offert FUN COOL avec 1000 Ar. Appels vers Friends 0Ar (maximum 20mn), Airtel 1Ar, autres 3 Ar. A part cela, envoyez 2 SMS au prix d un")


MESSAGES['recipient_success_fun15'] ={}
MESSAGES['recipient_success_fun15']['txt-1'] = Template("You have received a gift of FUNN15 from $benefactor.Valid 1 day and usable during offpeak  hours or whole day Sunday.Thanks")
MESSAGES['recipient_success_fun15']['txt-2'] = Template("Nandefasan ny $benefactor FUN15 maimaimpoana ianao iantsoana airtel @ ora fialan tsasatra na Alahady tontolo.")
MESSAGES['recipient_success_fun15']['txt-3'] = Template("Vous avez recu en cadeau FUN15 venant du $benefactor.Valable 1 jour et disponible pendant les heures creuses ou toute la journée de Dimanche .Merci")

MESSAGES['recipient_success_funPlus'] ={}
MESSAGES['recipient_success_funPlus']['txt-1'] = Template("You have received free FUN PLUS from $benefactor .Offer valid till midnight.Thank you ")
MESSAGES['recipient_success_funPlus']['txt-2'] = Template("Naharay  FUN PLUS maimaimpoana avy any @ $benefactor ianao . Manankery hatr@ misasak alina")
MESSAGES['recipient_success_funPlus']['txt-3'] = Template("Vous avez recu FUN PLUS gratuitement du $benefactor.Offre valable jusqu a minuit .Merci")

MESSAGES['recipient_success_funRaitra'] ={}
MESSAGES['recipient_success_funRaitra']['txt-1'] = Template("You have received free FUN RAITRA from $benefactor. Enjoy free calls to friends and family for 30 mn. Offer valid till midnight")
MESSAGES['recipient_success_funRaitra']['txt-2'] = Template("Naharay  FUN RAITRA  maimaimpoana avy any @ $benefactor ianao . Azonao iantsoana friends maimaimpoana hatr@ 30mn.Manankery 1 andro")
MESSAGES['recipient_success_funRaitra']['txt-3'] = Template("Vous avez recu FUN RAITRA  gratuitement du $benefactor .Vous beneficiez d appels gratuits vers Friends de 30mn.Offre valable jusqu a minuit")

MESSAGES['recipient_success_funRelax'] ={}
MESSAGES['recipient_success_funRelax']['txt-1'] = Template("You have received free FUN RELAX from $benefactor with UNLIMITED calls to FRIENDS, 50Mb and  all local calls.Valid 5 days")
MESSAGES['recipient_success_funRelax']['txt-2'] = Template("Naharay FUN RELAX maimaimpoana avy any @ $benefactor ianao.Misy antso FRIENDS maimaimpoana, antso rehetra eto an toerana, 50Mo.Manankery 5 andro")
MESSAGES['recipient_success_funRelax']['txt-3'] = Template("Vous avez recu FUN RELAX gratuitement du $benefactor avec des appels ILLIMITES vers FRIENDS, 50Mo et  appels tous operateurs .Valables 5jours")

MESSAGES['recipient_success_funExtra'] ={}
MESSAGES['recipient_success_funExtra']['txt-1'] = Template("You have received free FUN EXTRA from $benefactor with UNLIMITED calls to FRIENDS, 100Mb and all local calls.Valid 30 days")
MESSAGES['recipient_success_funExtra']['txt-2'] = Template("Naharay FUN EXTRA maimaimpoana avy any @ $benefactor ianao.Misy antso FRIENDS maimaimpoana, antso rehetra eto an toerana, 100Mo.Manankery 30 andro")
MESSAGES['recipient_success_funExtra']['txt-3'] = Template("Vous avez recu FUN EXTRA gratuitement du $benefactor avec des appels ILLIMITES vers FRIENDS, 100Mo et  appels tous operateurs .Valables 30jours")

MESSAGES['recipient_success_funUltra'] ={}
MESSAGES['recipient_success_funUltra']['txt-1'] = Template("You have received free FUN ULTRA from $benefactor with UNLIMITED calls to FRIENDS, 150Mb and  all local calls.Valid 30 days")
MESSAGES['recipient_success_funUltra']['txt-2'] = Template("Naharay FUN ULTRA maimaimpoana avy any @ $benefactor ianao.Misy antso FRIENDS maimaimpoana, antso rehetra eto an toerana, 150Mo.Manankery 30 andro")
MESSAGES['recipient_success_funUltra']['txt-3'] = Template("Vous avez recu FUN ULTRA gratuitement du $benefactor avec des appels ILLIMITES vers FRIENDS, 150Mo et  appels tous operateurs .Valables 30jours")

MESSAGES['recipient_success_funMaxi'] ={}
MESSAGES['recipient_success_funMaxi']['txt-1'] = Template("You have received free FUN MAXI from $benefactor with UNLIMITED calls to FRIENDS, 200Mb and 2hours to call locally. Valid 30 days")
MESSAGES['recipient_success_funMaxi']['txt-2'] = Template("Naharay FUN MAXI maimaimpoana avy any @ $benefactor ianao.Misy antso FRIENDS maimaimpoana sy 200Mo miampy antso 2h eto an toerana mandritry ny 30andro")
MESSAGES['recipient_success_funMaxi']['txt-3'] = Template("Vous avez recu FUN MAXI gratuitement du $benefactor avec des appels ILLIMITES vers FRIENDS,200Mo et 2h d appels tous operateurs .Valables 30jours")

MESSAGES['recipient_success_Mix1'] ={}
MESSAGES['recipient_success_Mix1']['txt-1'] = Template("You have received free MIX1 from $benefactor with UNLIMITED calls to FRIENDS, 300Mb and 3hours to call locally. Valid 30 days")
MESSAGES['recipient_success_Mix1']['txt-2'] = Template("Naharay MIX1 maimaimpoana avy any @ $benefactor ianao.Misy antso Friends ILLIMITES sy 300Mo miampy antso 3h eto an toerana mandritry ny 30andro")
MESSAGES['recipient_success_Mix1']['txt-3'] = Template("Vous avez recu MIX1 gratuitement du $benefactor avec des appels ILLIMITES vers FRIENDS, 300Mo et 3h d appels tous operateurs .Valables 30jours")

MESSAGES['recipient_success_Mix2'] ={}
MESSAGES['recipient_success_Mix2']['txt-1'] = Template("You have received free MIX2 from $benefactor with UNLIMITED calls to FRIENDS, 400Mb and 36000 Ar to call locally. Valid 30 days")
MESSAGES['recipient_success_Mix2']['txt-2'] = Template("Naharay MIX2 maimaimpoana avy any @ $benefactor ianao.Misy antso Friends ILLIMITES,400Mo miampy 36000Ar iantsoana eto an toerana mandritry ny 30andro")
MESSAGES['recipient_success_Mix2']['txt-3'] = Template("Vous avez recu MIX2 gratuitement du $benefactor avec des appels ILLIMITES vers FRIENDS, 400Mo et 36000 Ar d appels tous operateurs .Valables 30jours")

MESSAGES['recipient_success_Mix3'] ={}
MESSAGES['recipient_success_Mix3']['txt-1'] = Template("You have received free MIX3 from $benefactor with UNLIMITED calls to FRIENDS, 500Mb and 45000 Ar to call locally. Valid 30 days")
MESSAGES['recipient_success_Mix3']['txt-2'] = Template("Naharay MIX3 maimaimpoana avy any @ $benefactor ianao.Misy antso Friends ILLIMITES,500Mo miampy 45000Ar iantsoana eto an toerana mandritry ny 30andro")
MESSAGES['recipient_success_Mix3']['txt-3'] = Template("Vous avez recu MIX3 gratuitement du $benefactor avec des appels ILLIMITES vers FRIENDS, 500Mo et 45000 Ar d appels tous operateurs .Valables 30jours")

MESSAGES['recipient_success_funAby'] ={}
MESSAGES['recipient_success_funAby']['txt-1'] = Template("You have received free FUN ABY from $benefactor for your Airtel calls and for calls to other local network.Valid till midnight")
MESSAGES['recipient_success_funAby']['txt-2'] = Template("Naharay FUN ABY maimaimpoana avy any @ $benefactor ianao .Azonao iantsoana Airtel sy tambazotra hafa hatr@ misasak alina")
MESSAGES['recipient_success_funAby']['txt-3'] = Template("Vous avez recu FUN ABY gratuitement du $benefactor pour vos  appels vers Airtel et vers les autres operateurs locaux .Valables  jusqu a minuit")

MESSAGES['recipient_success_Bojo'] ={}
MESSAGES['recipient_success_Bojo']['txt-1'] = Template("You have received free BOJO from $benefactor with 999 seconds to call Airtel at 1 Ar/s .Valid till midnight")
MESSAGES['recipient_success_Bojo']['txt-2'] = Template("Naharay BOJO maimaimpoana avy any @ $benefactor ianao.Misy 999 segondra iantsoana Airtel. Ariary isa tsegondra ny antso.Manankery hatr@ misasak alina")
MESSAGES['recipient_success_Bojo']['txt-3'] = Template("Vous avez recu BOJO  gratuitement du $benefactor .Vous beneficiez de 999 sec d appels Airtel a 1 Ariary la seconde . Valables jusqu a minuit")

MESSAGES['recipient_success_Boost1000'] ={}
MESSAGES['recipient_success_Boost1000']['txt-1'] = Template("You have received free BOOST 1000 from $benefactor to call your relatives in Mada and abroad Offer valid till midnight")
MESSAGES['recipient_success_Boost1000']['txt-2'] = Template("Naharay BOOST 1000 maimaimpoana avy any @ $benefactor ianao.Azonao iantsoana ireo akaiky anao eto an toerana sy any ivelany. Manankery h@ misasak alina")
MESSAGES['recipient_success_Boost1000']['txt-3'] = Template("Vous avez recu BOOST 1000 gratuitement du $benefactor pour appeler vos proches a Mada et a l exterieur. Offre valable jusqu a minuit")

MESSAGES['recipient_success_funAl'] ={}
MESSAGES['recipient_success_funAl']['txt-1'] = Template("You have received free FUN AL from $benefactor. Enjoy UNLIMITED CALL to Airtel from 10pm to 4am")
MESSAGES['recipient_success_funAl']['txt-2'] = Template("Naharay FUN AL maimaimpoana avy any @ $benefactor ianao. Azonao iantsoana airtel ILLIMITE manomboka @ 10 ora alina hatr@ 4 maraina")
MESSAGES['recipient_success_funAl']['txt-3'] = Template("Vous avez recu FUN AL gratuitement du $benefactor.Vous beneficiez d un appel ILLIMITE vers airtel de 22 heures a 4 heures du matin.")
#ArivoWeekday

MESSAGES['recipient_success_ArivoWeekday'] ={}
MESSAGES['recipient_success_ArivoWeekday']['txt-1'] = Template("You have received free BOOST ARIVO from $benefactor .You are now enjoying 12000 Ar for your airtel calls ,valid till midnight")
MESSAGES['recipient_success_ArivoWeekday']['txt-2'] = Template("Naharay BOOST ARIVO maimaimpoana avy any @ $benefactor ianao.Misy 12000Ar iantsoana Airtel hatr@ misasak alina")
MESSAGES['recipient_success_ArivoWeekday']['txt-3'] = Template("Vous avez recu BOOST ARIVO gratuitement du $benefactor .Vous disposez de 12000 Ar d appels vers des numeros airtel ,valables jusqu a minuit")

MESSAGES['recipient_success_ArivoWeekend'] ={}
MESSAGES['recipient_success_ArivoWeekend']['txt-1'] = Template("You have received free BOOST ARIVO from $benefactor.You are now enjoying 15000 Ar for your airtel calls, valid till midnight")
MESSAGES['recipient_success_ArivoWeekend']['txt-2'] = Template("Naharay BOOST ARIVO maimaimpoana avy any @ $benefactor ianao.Misy 15000Ar iantsoana Airtel hatr@ misasak alina")
MESSAGES['recipient_success_ArivoWeekend']['txt-3'] = Template("Vous avez recu BOOST ARIVO gratuitement du $benefactor. Vous disposez de 15000 Ar d appels vers des numeros airtel ,valables jusqu a minuit")

MESSAGES['recipient_success_BoostWE'] ={}
MESSAGES['recipient_success_BoostWE']['txt-1'] = Template("You have received free BOOST WEEK END from $benefactor .You are now enjoying 7500 Ar for your airtel calls ,valid till midnight")
MESSAGES['recipient_success_BoostWE']['txt-2'] = Template("Naharay BOOST WEEK END maimaimpoana avy any @ $benefactor ianao. Lasa 7500 Ar ny 500 Ar ahafahana miantso airtel .Manankery hatr@ misasak alina")
MESSAGES['recipient_success_BoostWE']['txt-3'] = Template("Vous avez recu BOOST WEEK END gratuitement du $benefactor .Vous disposez de 7500 Ar d appels vers des numeros airtel ,valable jusqu a minuit")

MESSAGES['recipient_success_Boost500'] ={}
MESSAGES['recipient_success_Boost500']['txt-1'] = Template("You have received free BOOST 500 from $benefactor .You are now enjoying 6000 Ar for your airtel calls , valid till midnight")
MESSAGES['recipient_success_Boost500']['txt-2'] = Template("Naharay  BOOST 500 maimaimpoana avy any @ $benefactor ianao. Lasa 6000 Ar ny 500 Ar ahafahana miantso airtel .Manankery hatr@ misasak alina")
MESSAGES['recipient_success_Boost500']['txt-3'] = Template("Vous avez recu BOOST 500 gratuitement du $benefactor .Vous disposez de 6000 Ar d appels vers des numeros airtel ,valable jusqu a minuit")


MESSAGES['subscriber_success_ifun'] = {}
MESSAGES['subscriber_success_ifun']['txt-1'] = Template("Your request to give I FUN  to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_ifun']['txt-2'] = Template("Tontosa ny fanomezanao I FUN any @ laharana $b_msisdn. Misaotra tompoko.")
MESSAGES['subscriber_success_ifun']['txt-3'] = Template("Votre demande d offrir I FUN  au numero $b_msisdn est executee .Merci")


MESSAGES['recipient_success_ifun'] ={}
MESSAGES['recipient_success_ifun']['txt-1'] = Template("You got I FUN COOL from $benefactor .Thanks .")
MESSAGES['recipient_success_ifun']['txt-2'] = Template("Nahazo I FUN tany @ $benefactor ianao .Misaotra tompoko.")
MESSAGES['recipient_success_ifun']['txt-3'] = Template("Le $benefactor vous a offert I FUN  .Merci")

MESSAGES['subscriber_success_M4M_DAILY'] = {}
MESSAGES['subscriber_success_M4M_DAILY']['txt-1'] = Template("Your request to send a gift to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_M4M_DAILY']['txt-2'] = Template("Tontosa ny fangatahanao handefa tolotra any @ laharana $b_msisdn.Misaotra tompoko.")
MESSAGES['subscriber_success_M4M_DAILY']['txt-3'] = Template("Votre demande pour l'envoi de cette offre  au numero $b_msisdn est executee. Merci")

MESSAGES['recipient_success_M4M_DAILY'] ={}
MESSAGES['recipient_success_M4M_DAILY']['txt-1'] = Template("You got this offer including call to all local network,sms and internet from $benefactor,valid till midnight. Thanks")
MESSAGES['recipient_success_M4M_DAILY']['txt-2'] = Template("Naharay tolotra antso @ tambazotra rehetra,sms,internet tany @ $benefactor ianao,manankery hatr@ 11:59 alina .Misaotra tompoko")
MESSAGES['recipient_success_M4M_DAILY']['txt-3'] = Template("Le $benefactor vous a envoye cette offre incluant appel tous operateurs locaux,sms et internet ,valable jusqu a minuit. Merci")

MESSAGES['subscriber_success_M4M_WEEKLY'] = {}
MESSAGES['subscriber_success_M4M_WEEKLY']['txt-1'] = Template("Your request to send a gift to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_M4M_WEEKLY']['txt-2'] = Template("Tontosa ny fangatahanao handefa tolotra any @ laharana $b_msisdn.Misaotra tompoko.")
MESSAGES['subscriber_success_M4M_WEEKLY']['txt-3'] = Template("Votre demande pour l'envoi de cette offre  au numero $b_msisdn est executee. Merci")

MESSAGES['recipient_success_M4M_WEEKLY'] ={}
MESSAGES['recipient_success_M4M_WEEKLY']['txt-1'] = Template("You got this offer including call to all local network,sms and internet from $benefactor,valid 7 days. Thanks")
MESSAGES['recipient_success_M4M_WEEKLY']['txt-2'] = Template("Naharay tolotra antso @ tambazotra rehetra,sms,internet tany @ $benefactor ianao,manankery 7 andro.Misaotra tompoko")
MESSAGES['recipient_success_M4M_WEEKLY']['txt-3'] = Template("Le $benefactor vous a envoye cette offre incluant appel tous operateurs locaux,sms et internet ,valable 7 jours. Merci")

MESSAGES['subscriber_success_M4M_MONTHLY'] = {}
MESSAGES['subscriber_success_M4M_MONTHLY']['txt-1'] = Template("Your request to send a gift to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_M4M_MONTHLY']['txt-2'] = Template("Tontosa ny fangatahanao handefa tolotra any @ laharana $b_msisdn.Misaotra tompoko.")
MESSAGES['subscriber_success_M4M_MONTHLY']['txt-3'] = Template("Votre demande pour l'envoi de cette offre  au numero $b_msisdn est executee. Merci")

MESSAGES['recipient_success_M4M_MONTHLY'] ={}
MESSAGES['recipient_success_M4M_MONTHLY']['txt-1'] = Template("You got this offer including call to all local network,sms and internet from $benefactor,valid 30 days. Thanks")
MESSAGES['recipient_success_M4M_MONTHLY']['txt-2'] = Template("Naharay tolotra antso @ tambazotra rehetra,sms,internet tany @ $benefactor ianao,manankery 30 andro.Misaotra tompoko")
MESSAGES['recipient_success_M4M_MONTHLY']['txt-3'] = Template("Le $benefactor vous a envoye cette offre incluant appel tous operateurs locaux,sms et internet ,valable 30 jours. Merci")

MESSAGES['subscriber_success_FB_7'] = {}
MESSAGES['subscriber_success_FB_7']['txt-1'] = Template("You have successfully offered Facebook7(GIFT) to $b_msisdn and validty 7 Days. Thank you")
MESSAGES['subscriber_success_FB_7']['txt-2'] = Template("Tontosa ny fandefasanao Facebook7 Kado any @ $b_msisdn. Tolotra maharitra 7 andro. Misaotra tompoko")
MESSAGES['subscriber_success_FB_7']['txt-3'] = Template("Felicitations.Vous venez d'offrir avec succes Facebook7(GIFT) valide pour 7 jours au $b_msisdn.Naviguez vite et moins cher.Cliquez ici www.opera.com")

MESSAGES['recipient_success_FB_7'] ={}
MESSAGES['recipient_success_FB_7']['txt-1'] = Template("You have received Facebook7 (GIFT) from $benefactor and valid till $expiry.")
MESSAGES['recipient_success_FB_7']['txt-2'] = Template("Ianao dia naharay Facebook7 Kado avy any @ $benefactor. Tolotra afaka ampiasaina h@ $expiry.")
MESSAGES['recipient_success_FB_7']['txt-3'] = Template("Felicitations.Le $benefactor vient de vous offrir Facebook7(GIFT) valable jusqu au $expiry. Naviguez vite et moins cher. Cliquez ici www.opera.com")

MESSAGES['subscriber_success_FB_4'] = {}
MESSAGES['subscriber_success_FB_4']['txt-1'] = Template("You have successfully offered Facebook4(GIFT) to $b_msisdn and validty 4 Days. Thank you")
MESSAGES['subscriber_success_FB_4']['txt-2'] = Template("Tontosa ny fandefasanao Facebook4 Kado any @ $b_msisdn. Tolotra maharitra 4 andro. Misaotra tompoko")
MESSAGES['subscriber_success_FB_4']['txt-3'] = Template("Felicitations.Vous venez d'offrir avec succes Facebook4(GIFT) valide pour 4 jours au $b_msisdn.Naviguez vite et moins cher.Cliquez ici www.opera.com")

MESSAGES['recipient_success_FB_4'] ={}
MESSAGES['recipient_success_FB_4']['txt-1'] = Template("You have received Facebook4(GIFT) from $benefactor and valid till $expiry.")
MESSAGES['recipient_success_FB_4']['txt-2'] = Template("Ianao dia naharay Facebook4 Kado avy any @ $benefactor. Tolotra afaka ampiasaina h@ $expiry.")
MESSAGES['recipient_success_FB_4']['txt-3'] = Template("Felicitations.Le $benefactor vient de vous offrir Facebook4(GIFT) valable jusqu au $expiry. Naviguez vite et moins cher. Cliquez ici www.opera.com")

MESSAGES['subscriber_success_data'] = {}
MESSAGES['subscriber_success_data']['txt-1'] = Template("You have successfully offered $data(GIFT) to $b_msisdn and validt $days Day(s). Thank you")
MESSAGES['subscriber_success_data']['txt-2'] = Template("Tontosa ny fandefasanao $data Kado any @ $b_msisdn. Tolotra maharitra $days andro. Misaotra tompoko")
MESSAGES['subscriber_success_data']['txt-3'] = Template("Felicitations. Vous venez d'offrir avec succes $data(GIFT) valide pour $days jour(s) au $b_msisdn. Naviguez vite et moins cher. Cliquez ici www.opera.com")

MESSAGES['recipient_success_data'] = {}
MESSAGES['recipient_success_data']['txt-1'] = Template("You have received $data (GIFT) from $benefactor and valid till $expiry.")
MESSAGES['recipient_success_data']['txt-2'] = Template("Ianao dia naharay $data Kado avy any @ $benefactor. Tolotra afaka ampiasaina h@ $expiry.")
MESSAGES['recipient_success_data']['txt-3'] = Template("Felicitations. Le $benefactor vient de vous offrir $data(GIFT) valable jusqu au $expiry. Naviguez vite et moins cher. Cliquez ici www.opera.com")

MESSAGES['subscriber_success_low_combo_bundle_500'] = {}
MESSAGES['subscriber_success_low_combo_bundle_500']['txt-1'] = Template("Your request to send a gift to $b_msisdn is successfully executed.Thank you")
MESSAGES['subscriber_success_low_combo_bundle_500']['txt-2'] = Template("Tontosa ny fangatahanao handefa tolotra any @ laharana $b_msisdn.Misaotra tompoko.")
MESSAGES['subscriber_success_low_combo_bundle_500']['txt-3'] = Template("Votre demande pour l'envoi de cette offre  au numero $b_msisdn est executee. Merci")

MESSAGES['recipient_success_low_combo_bundle_500'] ={}
MESSAGES['recipient_success_low_combo_bundle_500']['txt-1'] = Template("You got this offer for Mix500 from $benefactor,valid till midnight. Thanks")
MESSAGES['recipient_success_low_combo_bundle_500']['txt-2'] = Template("Naharay tolotra antso @ Mix500 @ $benefactor ianao,manankery hatr@ 11:59 alina .Misaotra tompoko")
MESSAGES['recipient_success_low_combo_bundle_500']['txt-3'] = Template("Le $benefactor vous a envoye cette offre Mix500 ,valable jusqu a minuit. Merci")

MESSAGES['subscriber_success_WA_30'] = {}
MESSAGES['subscriber_success_WA_30']['txt-1'] = Template("Felicitations, vous venez d'offrir avec succes Whatsapp Monthly valide pour 30 jours au $b_msisdn. Naviguez vite et moins cher. Cliquez ici www.opera.com")
MESSAGES['subscriber_success_WA_30']['txt-2'] = Template("Felicitations, vous venez d'offrir avec succes Whatsapp Monthly valide pour 30 jours au $b_msisdn. Naviguez vite et moins cher. Cliquez ici www.opera.com")
MESSAGES['subscriber_success_WA_30']['txt-3'] = Template("Felicitations, vous venez d'offrir avec succes Whatsapp Monthly valide pour 30 jours au $b_msisdn. Naviguez vite et moins cher. Cliquez ici www.opera.com")

MESSAGES['recipient_success_WA_30'] ={}
MESSAGES['recipient_success_WA_30']['txt-1'] = Template("Felicitations, le $benefactor vient de vous offrir Whatsapp 30 valable jusqu au $expiry. Naviguez vite et moins cher, cliquez ici www.opera.com")
MESSAGES['recipient_success_WA_30']['txt-2'] = Template("Felicitations, le $benefactor vient de vous offrir Whatsapp 30 valable jusqu au $expiry. Naviguez vite et moins cher, cliquez ici www.opera.com")
MESSAGES['recipient_success_WA_30']['txt-3'] = Template("Felicitations, le $benefactor vient de vous offrir Whatsapp 30 valable jusqu au $expiry. Naviguez vite et moins cher, cliquez ici www.opera.com")


BUNDLES = {}
BUNDLES["4"] = "4"
BUNDLES["0"] = "0"
BUNDLES["6"] = "6"
BUNDLES["8"] = "8"
BUNDLES["9"] = "9"
BUNDLES["11"] = "11"
BUNDLES["12"] = "12"
BUNDLES["14"] = "14"
BUNDLES["15"] = "15"
BUNDLES["16"] = "16"
BUNDLES["32"] = "32"
BUNDLES["33"] = "33"
BUNDLES["35"] = "35"
BUNDLES["36"] = "19"
BUNDLES["37"] = "20"
BUNDLES["38"] = "21"
BUNDLES["40"] = "1"
BUNDLES["20"] = "58"
BUNDLES["41"] = "179"  #MyMeg10 Activation
BUNDLES["44"] = "180"  #Facebook Weekly Activation
BUNDLES["45"] = "181"  #Twitter Weekly Activation
BUNDLES["46"] = "182"  #Whatsapp Weekly Activation
BUNDLES["47"] = "191"  #MyMeg35 Activation
BUNDLES["2"] = "236"  #MyMeg5 Activation
BUNDLES["48"] = "240"  #MyMeg75 Activation
BUNDLES["49"] = "242"  #MyGig2.5 Activation
BUNDLES["50"] = "244"  #MyGig15 Activation
BUNDLES["51"] = "257"  #ISNA_DAILY Activation
BUNDLES["52"] = "258"  #ISNA_WEEKLY Activation
BUNDLES["100"] = "396"  #PARABOLE
BUNDLES["57"] = "397"  #Facebook_7
BUNDLES["53"] = "420"  #ISNA_MONTHLY Activation
BUNDLES["58"] = "425"  #Whatsapp Monthly Activation

#BUNDLES["55"] = "420"  #MyMeg5+ Activation
#BUNDLES["56"] = "421"  #MyMeg20 Activation
#BUNDLES["60"] = "422"  #MyMeg40 Activation
#BUNDLES["58"] = "423"  #MyMeg256 Activation
#BUNDLES["59"] = "424"  #MyMeg750 Activation

BUNDLES["100"] = "399"  #SmallDaily_5Mb
BUNDLES["103"] = "401"  #MediumDaily_30Mb
BUNDLES["101"] = "405"  #SmallWeekly_30Mb
BUNDLES["109"] = "421"  #ComboSmall15days
BUNDLES["110"] = "422"  #ComboLarge30days

#bonus bundles
BUNDLES["131"] = "131"
BUNDLES["132"] = "132"
BUNDLES["133"] = "133"

'''
BUNDLES["10"] = "17"
BUNDLES["11"] = "18"
BUNDLES["12"] = "19"
BUNDLES["13"] = "20"
BUNDLES["14"] = "21"
'''

B_BUNDLES = {}
B_BUNDLES["4"] = "22"
B_BUNDLES["0"] = "0"
B_BUNDLES["6"] = "23"
B_BUNDLES["8"] = "24"
B_BUNDLES["9"] = "25"
B_BUNDLES["11"] = "26"
B_BUNDLES["12"] = "27"
B_BUNDLES["14"] = "28"
B_BUNDLES["15"] = "29"
B_BUNDLES["16"] = "30"
B_BUNDLES["17"] = "36"
B_BUNDLES["20"] = "58"   #Data Unlimited GIFT Activation
B_BUNDLES["36"] = "19"   #Facebook GIFT Activation
B_BUNDLES["37"] = "20"   #Twitter GIFT Activation
B_BUNDLES["38"] = "21"   #Whatsapp GIFT Activation
B_BUNDLES["40"] = "1"    #MyMeg15 GIFT Activation
B_BUNDLES["41"] = "179"  #MyMeg10 GIFT Activation
B_BUNDLES["44"] = "180"  #Facebook Weekly GIFT Activation
B_BUNDLES["45"] = "181"  #Twitter Weekly GIFT Activation
B_BUNDLES["46"] = "182"  #Whatsapp Weekly GIFT Activation
B_BUNDLES["47"] = "191"  #MyMeg35 GIFT Activation
B_BUNDLES["2"] = "236"  #MyMeg5 GIFT Activation
B_BUNDLES["48"] = "240"  #MyMeg75 GIFT Activation
B_BUNDLES["49"] = "242"  #MyGig2.5 GIFT Activation
B_BUNDLES["50"] = "244"  #MyGig15 GIFT Activation
B_BUNDLES["57"] = "397"  #Facebook_7
B_BUNDLES["58"] = "425"  #Whatsapp Monthly GIFT Activation

#B_BUNDLES["55"] = "420"  #MyMeg5+ GIFT Activation
#B_BUNDLES["56"] = "421"  #MyMeg20 GIFT Activation
#B_BUNDLES["60"] = "422"  #MyMeg40 GIFT Activation
#B_BUNDLES["58"] = "423"  #MyMeg256 GIFT Activation
#B_BUNDLES["59"] = "424"  #MyMeg750 GIFT Activation

VALIDITY = {}
VALIDITY["4"] = "1"
VALIDITY["6"] = "3"
VALIDITY["8"] = "7"
VALIDITY["9"] = "7"
VALIDITY["11"] = "30"
VALIDITY["12"] = "30"
VALIDITY["14"] = "30"
VALIDITY["15"] = "30"
VALIDITY["16"] = "30"
VALIDITY["17"] = "1"
VALIDITY["19"] = "1"
VALIDITY["20"] = "1"
VALIDITY["21"] = "1"
VALIDITY["22"] = "1"
VALIDITY["23"] = "3"
VALIDITY["24"] = "7"
VALIDITY["25"] = "7"
VALIDITY["26"] = "30"
VALIDITY["27"] = "30"
VALIDITY["28"] = "30"
VALIDITY["29"] = "30"
VALIDITY["30"] = "30"
VALIDITY["31"] = "2"
VALIDITY["32"] = "2"
VALIDITY["33"] = "5"
VALIDITY["34"] = "7"
VALIDITY["35"] = "7"
VALIDITY["36"] = "1"
VALIDITY["1"] = "1"
VALIDITY["58"] = "30"
VALIDITY["63"] = "5"
VALIDITY["119"] = "30"
VALIDITY["179"] = "1"  #MyMeg10
VALIDITY["180"] = "4"  #Facebook Weekly
VALIDITY["181"] = "7"  #Twitter Weekly
VALIDITY["182"] = "7"  #Whatsapp Weekly
VALIDITY["191"] = "1"  #MyMeg35
VALIDITY["236"] = "1"  #MyMeg5
VALIDITY["240"] = "1"  #MyMeg75
VALIDITY["242"] = "30"  #MyGig2.5
VALIDITY["244"] = "30"  #MyGig15
VALIDITY["257"] = "1"  #ISNA_DAILY
VALIDITY["258"] = "5"  #ISNA_WEEKLY
VALIDITY["396"] = "30"  #PARABOLE
VALIDITY["397"] = "7"  #Facebook_7
VALIDITY["420"] = "30"  #ISNA_MONTHLY
VALIDITY["425"] = "30"  #Whatsapp Monthly

VALIDITY["399"] = "1"  #SmallDaily_5Mb
VALIDITY["401"] = "1"  #MediumDaily_30Mb
VALIDITY["405"] = "7"  #SmallWeekly_30Mb
VALIDITY["421"] = "15" #ComboSmall
VALIDITY["422"] = "30" #ComboLarge

VALIDITY["410"] = "1" #LOW COMBO BUNDLE 500

#VALIDITY["420"] = "1"  #MyMeg5+
#VALIDITY["421"] = "1"  #MyMeg20
#VALIDITY["422"] = "1"  #MyMeg40
#VALIDITY["423"] = "30"  #MyMeg256
#VALIDITY["424"] = "30"  #MyMeg750

#Voice Bundles
VALIDITY["250"] = "1"  #Daily_Large_combo
VALIDITY["221"] = "1"  #Fun & Fy
VALIDITY["201"] = "1"  #Fun15
VALIDITY["197"] = "1"  #Fun Plus
VALIDITY["199"] = "1"  #Fun Plus Extra
VALIDITY["209"] = "4"  #Fun Relax
VALIDITY["222"] = "1"  #Fun Raitra
VALIDITY["223"] = "1"  #Fun Raitra Extra
VALIDITY["211"] = "29"  #Fun Extra
VALIDITY["213"] = "29"  #Fun Ultra
VALIDITY["215"] = "29"  #Fun Maxi
VALIDITY["217"] = "29"  #MIX1
VALIDITY["218"] = "29"  #MIX2
VALIDITY["219"] = "29"  #MIX3
VALIDITY["224"] = "1"  #FUN ABY
VALIDITY["226"] = "1"  #FUN450
VALIDITY["194"] = "1"  #FUN100
VALIDITY["195"] = "1"  #TAXI FUN
VALIDITY["203"] = "1"  #FUN FRIENDLY
VALIDITY["220"] = "1"  #FUN ORA
VALIDITY["254"] = "1"  #FUN ORA
VALIDITY["205"] = "1"  #BOJO
VALIDITY["227"] = "1"  #BOOST 1000
VALIDITY["228"] = "1"  #BOOST 2000
VALIDITY["229"] = "1"  #BOOST 3000
VALIDITY["230"] = "1"  #BOOST 5000
VALIDITY["231"] = "30"  #BOOST 10000
VALIDITY["205"] = "1"  #BOJO
VALIDITY["225"] = "1"  #FUN AL
VALIDITY["207"] = "1"  #FUN COOL
VALIDITY["255"] = "1"  #FUN COOL
VALIDITY["232"] = "1"  #BOOST WE
VALIDITY["233"] = "1"  #BOOST 500
VALIDITY["251"] = "1"  #CLUBSMS
VALIDITY["256"] = "1"  #CLUBSMSMINI
VALIDITY["252"] = "1"  #BOOST1000WEEKEND
VALIDITY["253"] = "1"  #BOOST1000WEEKDAY
VALIDITY["235"] = "1"  #FUN200
VALIDITY["234"] = "1"  #BUNDLE33
VALIDITY["376"] = "1"  #M4M_DAILY_SMALL
VALIDITY["377"] = "1"  #M4M_DAILY_MEDIUM
VALIDITY["378"] = "1"  #M4M_DAILY_LARGE
VALIDITY["379"] = "7"  #M4M_WEEKLY_SMALL
VALIDITY["380"] = "7"  #M4M_WEEKLY_MEDIUM
VALIDITY["381"] = "7"  #M4M_WEEKLY_LARGE
VALIDITY["382"] = "30"  #M4M_MONTHLY_SMALL
VALIDITY["383"] = "30"  #M4M_MONTHLY_MEDIUM
VALIDITY["384"] = "30"  #M4M_MONTHLY_LARGE
VALIDITY["408"] = "1"  #BUNDLE33 MINI

VALIDITY["411"] = "1" #BUNDLE 200
VALIDITY["412"] = "1" #BUNDLE 500
VALIDITY["413"] = "1" #BUNDLE 1000
VALIDITY["414"] = "1" #BUNDLE 1500
VALIDITY["415"] = "7" #BUNDLE 2000
VALIDITY["416"] = "7" #BUNDLE 3500
VALIDITY["417"] = "7" #BUNDLE 5000
VALIDITY["418"] = "30" #BUNDLE 10000
VALIDITY["419"] = "30" #BUNDLE 20000

VALIDITY["426"] = "1"  #I-Ser@200 For mamo user

#bonus bundles
VALIDITY["131"] = "7"
VALIDITY["132"] = "7"
VALIDITY["133"] = "30"


KOZY_PACKAGE_ID = "17"
UNLIMITED_ID = "58"
REGIONAL_ID = "119"

#bonus bundles
BONUSMEG250 = "131"
BONUSMEG500 = "132"
BONUSGIG1 = "133"

BONUSBUNDLES = ['131','132','133']
NEWMSGBUNDLES = ['4','6','8','9','11','12','14','15','16','19','20','21','32','33','35','119','191','236','240','242','244','221','250','201','197','199','209','222','223','211','213','215','217','218','219','224','226','194','195','203','220','205','227','228','229','230','231','205','225','207','232','233','251','252','253','256','235','257','258','376','377','378','379','380','381','382','383','384','396','397','234','399','401','405','408','410','411','412','413','414','415','416','417','418','419','420','421','422','423','425','426']

DATA_USAGE = ['4', '6', '8', '9']

NON_GIFT_VOICE_BUNDLES = [194,195,226,221,203,235,234,248,249,408]

NIGHT_BUNDLES = ['31','32','33','34','35']
SOCIAL = ['19','20','21']

SOCIAL_PKGS = {}
SOCIAL_PKGS['19'] = '36'
SOCIAL_PKGS['20'] = '37'
SOCIAL_PKGS['21'] = '38'

MY_MEG_10 = '179'
SOCIAL_FB_WEEKLY = '180'
SOCIAL_TW_WEEKLY = '181'
SOCIAL_WA_WEEKLY = '182'

BILL_PLAN = {}
BILL_PLAN[8]  = {'bonus_offer_id': 1249, 'cost': 6000, 'refill_id': 'DP00', 'offer_id': 1018}  # MyMeg 250
BILL_PLAN[9]  = {'bonus_offer_id': 1248, 'cost': 10000, 'refill_id': 'DP01', 'offer_id': 1019} # MyMeg 500
BILL_PLAN[11] = {'bonus_offer_id': 1250, 'cost': 30000, 'refill_id': 'DP02', 'offer_id': 1021} # MyGig 1
