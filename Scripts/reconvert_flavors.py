import xml.etree.ElementTree as ET
import json
from pprint import pprint
from KalturaClient import *
from KalturaClient.Plugins.Core import *
from KalturaClient.Plugins.Core import KalturaFlavorAsset
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

flavorsArray = ["0_4nle3nek", "1_03bxm88q", "1_0447ddoy", "1_0f2d5r10", "1_0nnvo9mm", "1_1p6xe8la", "1_27rgnmzw", "1_2czky3s4", "1_2q3mwr54", "1_3z7617bn", "1_51c2hkmy", "1_526vitrz", "1_549p2ls8", "1_61adw7z3", "1_8iynz4xs", "1_8ul0t1p6", "1_8vse4qe4", "1_9gp3d17v", "1_9l5ilfp8", "1_awxdh1bj", "1_b0k1aee4", "1_b2a2h0mn", "1_bcdrwur6", "1_bfpflxin", "1_boufxuqz", "1_bqr56nl6", "1_cbsyca2x", "1_cmejxhq5", "1_cwjxrl9p", "1_dtbuotwh", "1_ezqibx2e", "1_f49e9ivk", "1_f4ip4v5w", "1_f9signq9", "1_fcrukk2l", "1_fn3y4yrk", "1_ggt2xh4z", "1_halg0bmf", "1_ic22okk3", "1_inqpytms", "1_irdgt3db", "1_iso2jxtd", "1_j4mfg1bb", "1_jdc51455", "1_kexlznff", "1_kujl62ph", "1_lnh6y60z", "1_lrif2j16", "1_mku7hwse", "1_ndj3je8x", "1_ody6a6x1", "1_ogmeegmp", "1_on5290ce", "1_qkhywg1y", "1_r05qeoqg", "1_stdxajbn", "1_t0c9wvcg", "1_tbum3hv7", "1_td8l74p8", "1_ts23wdwz", "1_vxhh6rbk", "1_wbzn9hb5", "1_wlq675ka", "1_xgem1bah", "1_yq54vub0", "1_ysp88ijt", "1_ywq9z1s1", "1_z8akf3oq", "1_06sjv6sn", "1_13nli6ku", "1_1gj93cdq", "1_26qyqyjz", "1_2pmr7zy8", "1_3fnrjsqo", "1_4rkd0hml", "1_67xqtwia", "1_92sujgir", "1_9ouw6h0g", "1_9zc8kk9u", "1_a8o7142a", "1_anre1rv9", "1_atz0yvc5", "1_b7rbr0f3", "1_bld8weew", "1_d3rc4rtk", "1_dcha7oht", "1_dzwe8dir", "1_e1lr9y6u", "1_fng1yqyo", "1_h8xhpc3u", "1_ihcmi6fv", "1_ishcb2ja", "1_k0wihqar", "1_mbrnlrfv", "1_n5zga0rv", "1_nbvzifm9", "1_onjpa3d2", "1_p9omb6ch", "1_svsqsb0c", "1_ufdjq8m7", "1_ufh2qt85", "1_uld3usjv", "1_xvuyuua2", "1_zepbyxao", "1_zljgf0o8"]

def reconvertFlavors(id):
	# Perform flavorAsset reconvert action
	result = client.flavorAsset.reconvert(id)
	formattedResult = formatValue(result)
	print ("Done", id)
	return

for x in flavorsArray:
	reconvertFlavors(x)