# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
import memcache
def hello(request):
    return HttpResponse("Hello world")
def hello1(request):
    return HttpResponse("Hello world")    
def api(request):
	#read main memcache info
	main_info_json='{"host":"127.0.0.1","port":"41000"}'
	main_info_obj=json.loads(main_info_json)
	main_mc = memcache.Client(['%s:%s' % (main_info_obj['host'] , main_info_obj['port'])])
	#read site info from main memcache
	site_info_json=main_mc.get(request.get_host())
	site_info_obj=json.loads(site_info_json)
	if site_info_json:
		#get table
		try:
			request_table=request.GET['table']	
		except Exception, e:
			return HttpResponse('{"error":"no table!"}')	
		if request.GET['table']=='member':
			return HttpResponse('{"error","site %s not avaliable!"}' % request.get_host() ) 
		else:
			site_mc = memcache.Client(['%s:%s' % (site_info_obj['dataMemcache']['host'] , site_info_obj['dataMemcache']['port'])])
			site_title = site_info_obj['dataMemcache']['title']
			#get action
			try:
				request_action=request.GET['action']
			except Exception, e:
				#raise e
				request_action=''
			#make key	
			str1='%s_%s_%s_%s' % (site_title,request_table,request_action,'')
			#if 
			response=site_mc.get(str1.encode('utf-8'))
			if response:
				return HttpResponse(response)
			else:
				return HttpResponse('{"error":"table %s no data!"}' % request_table)
	else:
		return HttpResponse('{"error","site %s not avaliable!"}' % request.get_host() ) 

	#obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6,7)}]
	#encodedjson = json.dumps(obj)
	#main_mc.set(request.get_host(),encodedjson)
	#encode json
	
	#print repr(obj)
	#re encodedjson
	return HttpResponse(main_mc.get(request.get_host()))    
def memcache_testbuilder(request):
	#read main memcache info
	main_info_json='{"host":"127.0.0.1","port":"41000"}'
	main_info_obj=json.loads(main_info_json)
	main_mc = memcache.Client(['%s:%s' % (main_info_obj['host'] , main_info_obj['port'])])
	#read site info from main memcache
	obj = {
	"name":u"北京信息科技大学",
	"site":"api.bistu.edu.cn:40000",
	"dataMemcache":{
		"host":"127.0.0.1",
		"port":"41000",
		"title":"bistu",
	},
	"UserServer":{
		"host":"127.0.0.1",
		"port":"40500",
	},
	"UserMemcache":{
		"host":"127.0.0.1",
		"port":"41000",
		"title":"user",
	}

	}
	encodedjson = json.dumps(obj)
	status=main_mc.set(obj['site'],encodedjson)
	obj = [
	{
	"id": "1",
	"buildingName": u"小营校区一教",
	"buildingCode": "0101"
	},
	{
	"id": "2",
	"buildingName": u"小营校区空调",
	"buildingCode": "0104"
	},
	{
	"id": "3",
	"buildingName": u"清河校区二教",
	"buildingCode": "0302"
	},
	{
	"id": "4",
	"buildingName": u"健翔桥校区二教",
	"buildingCode": "0202"
	}
	]
	encodedjson = json.dumps(obj)
	status=main_mc.set("bistu_building__",encodedjson)
	obj = [
	{
	"id": "1",
	"buildingName": u"小营校区一教",
	"buildingCode": "0101"
	},
	{
	"id": "4",
	"buildingName": u"健翔桥校区二教",
	"buildingCode": "0202"
	}
	]
	encodedjson = json.dumps(obj)
	status=main_mc.set("bistu_building_list_",encodedjson)
	#encode json
	
	#print repr(obj)
	#re encodedjson
	return HttpResponse(status)    
