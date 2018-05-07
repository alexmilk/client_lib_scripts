import xml.etree.ElementTree as ET
import json
from pprint import pprint
from KalturaClient import *
from KalturaClient.Plugins.Core import *
from KalturaClient.Plugins.Core import KalturaFlavorAsset
# from utils import GetConfig
config = KalturaConfiguration(1666321)
config.serviceUrl = "http://www.kaltura.com/"
config.format = 2
client = KalturaClient(config)
secret = "dc944c90997c5217f52422332adc3c3d"
userId = 'alex.milkis@kaltura.com' 
partnerId = 1666321
expiry = 86400
ktype = KalturaSessionType.ADMIN
privs = "disableentitlement"
ks = client.generateSession(secret,userId,ktype,partnerId,expiry,privs)
client.setKs(ks)

# The formatValue function collapses the result object and contructs a new json one
def formatValue(val):
 if type(val) == list:
	if val == []:
	 return '[]'
	result = '[\n'
	for index in xrange(len(val)):
	 result += '%s => %s\n' % (index, formatValue(val[index]))
	result += ']'
	return result
 elif 'PROPERTY_LOADERS' in dir(val): # object
	result = '{\n'
	for key, value in vars(val).items():
	 result += '%s => %s\n' % (key, formatValue(value))
	result += '}'
	return result
 elif 'getValue' in dir(val):   # enum
	return val.getValue()
 else:
	return val

def testUpdate(name):
	# Create empty base entry object
	baseEntry = KalturaBaseEntry()
	# Define name argument to base entry object
	baseEntry.name = name
	baseEntry.type = "1"
	type = KalturaEntryType.MEDIA_CLIP
	# Save client add work to result object
	result = client.baseEntry.add(baseEntry, type)
	formattedResult = formatValue(result)
	print (formattedResult)
	return

entryName = input('Enter name: ')
testUpdate(entryName)