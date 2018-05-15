from KalturaClient.Plugins.Core import *
from KalturaClient.Plugins.Core import KalturaBaseEntry
# from utils import GetConfig
config = KalturaConfiguration(1068292)
config.serviceUrl = "http://www.kaltura.com/"
config.format = 2
client = KalturaClient(config)
secret = ""
userId = ""
partnerId = 1068292
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

entriesArray = []

def deleteEntries(id):
        # Perform baseEntry delete action
        result = client.baseEntry.delete(id)
        formattedResult = formatValue(result)
        print ("Deleted", id)
        return

for x in entriesArray:
        deleteEntries(x)
