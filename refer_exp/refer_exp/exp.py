'''
import os
os.system("pip install -q requests")
import requests


# same as  os.system, but more ideomatic
# unable to quiet
# import subprocess
# subprocess.call(["pip","install","-q", "requests"],, stdout=open(os.devnull, 'wb'))
'''

'''
def request(url):
  return requests.get(url)

def http_to_json(url):
  return requests.get(url).json
'''

#import requests
import urllib.request
import urllib.parse
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django import db
from django.core import serializers
from elasticsearch import Elasticsearch
from kafka import SimpleProducer, KafkaClient
#from stuff import main


#GET request from HTML to ModelAPI
#Returns a JSON containing username, id, and company.
def all_sellers(request):
  # r = requests.get(r'^localhost:8001/api/v1/sellers/all$') 
  req = urllib.request.Request(r'^localhost:8001/api/v1/buyers/all$')
  resp_json = urllib.request.urlopen(req).read().decode('utf-8')  
  resp = json.loads(resp_json)
  return resp

#GET request from HTML to ModelAPI
#Returns a JSON containing username, id, and company.
def all_buyers(request):
  # r = requests.get(r'^localhost:8001/api/v1/buyers/all$') 
  req = urllib.request.Request(r'^localhost:8001/api/v1/sellers/all$')
  resp_json = urllib.request.urlopen(req).read().decode('utf-8')  
  resp = json.loads(resp_json)
  return resp

#POST request from HTML to ModelAPI
#requies a username and password field
''''
def log_in(request, username, password):
  if request.method != 'POST':
      return _error_response(request, "must make POST request")
  post_data = {
  "username":username,
  "password":password
  } 
  post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
  req = urllib.request.Request(r'^localhost:8001/api/v1/auth/login$', data=post_encoded, method='POST')
  resp_json = urllib.request.urlopen(req).read().decode('utf-8')
  resp = json.loads(resp_json)
  return JsonResponse(resp)
  

  
'''

#POST request from HTML to ModelAPI
#requies a authenticator
def log_out(auth):
  if request.method != 'POST':
        return _error_response(request, "must make POST request")
  if 'authenticator' not in request.POST:
         return _error_response(request, "missing auth")
  post_data = {
  "authenticator" : request.POST['authenticator']}
 
  post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
  req = urllib.request.Request(r'^localhost:8001/api/v1/auth/logout$', data=post_encoded, method='POST')
  resp_json = urllib.request.urlopen(req).read().decode('utf-8')
  resp = json.loads(resp_json)
  return JsonResponse(resp)
  '''
  info = {
  'authenticator':auth
  }
  r = requests.post(r'^localhost:8001/api/v1/auth/logout$', data = info)
  return main.log_out(r)
  '''

#still seems awkward
#POST request
#Contains buyer_u_id or seller_u_id or negotiation
#need to be valid IDs
#returns a transaction_id if valid
def create_transaction(request):
  if request.method != 'POST':
        return _error_response(request, "must make POST request")
  if 'buyer_u_id' not in request.POST or 'seller_u_id' not in request.POST or 'negotiation' not in request.POST:
        return _error_response(request, "missing required fields")
  post_data = {
  "buyer_u_id" : request.POST['buyer_u_id'], 
  "seller_u_id" : request.POST['seller_u_id'],
  "negotiation" : request.POST['negotiation']}
 
  post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
  req = urllib.request.Request(r'^localhost:8001/api/v1/transaction/create$', data=post_encoded, method='POST')
  resp_json = urllib.request.urlopen(req).read().decode('utf-8')
  resp = json.loads(resp_json)
  return JsonResponse(resp)


#GET request
#user_id field
#how does front-end find user_id? From cookie?
def lookup_user(request, user_id):
  if  request.method !='GET':
        return _error_response(request, "must make GET request")
  param_encoded = urllib.parse.urlencode(request.GET.get('user_id','')).encode('utf-8')  
  req = urllib.request.Request(r'^localhost:8001/api/v1/buyers/all$'+param_encoded)
  resp_json = urllib.request.urlopen(req).read().decode('utf-8')
  resp = json.loads(resp_json)
  return JsonResponse(resp)
  '''
  args = user_id
  r = requests.get(r'^localhost:8001/api/v1/users/(\d+)$')
  return main.lookup_user(r,args)
  '''
'''
def view_all_transactions():
  r = requests.get(r'^localhost:8001/api/v1/transaction/all$') 
  return main.view_all_transactions(r)
'''

#POST
#usertype, password fields
#expected to contain
def create_user(request):
  if request.method != 'POST':
        return _error_response(request, "must make POST request")
  if 'usertype' not in request.POST:
        return _error_response(request, "Usertype is not found")
  if 'password' not in request.POST or 'username' not in request.POST:
        return _error_response(request, "missing fields for Basic User")
  post_data = {
  "usertype":request.POST['usertype'],
  "username":request.POST['username'],
  "password":request.POST['password']
  } 
  post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
  req = urllib.request.Request(r'^localhost:8001/api/v1/users/create$', data=post_encoded, method='POST')
  resp_json = urllib.request.urlopen(req).read().decode('utf-8')
  resp = json.loads(resp_json)
  return JsonResponse(resp)

  '''
  info = {
  "usertype":usertype
  "username":username
  "password":password
  } 
  r = requests.post(r'^localhost:8001/api/v1/users/create$', data = info )
  return main.create_user(request)
  '''






####UPDATES###### 
##search for companies and search for notes



#Rewrite log in
#Tested 
def log_in(request):
	if request.method != 'POST':
		return _error_response(request, "must make POST request")
	post_data = {
	"username":request.POST['username'],
	"password":request.POST['password']
	} 
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://models:8000/api/v1/auth/login', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	if resp["ok"] is True:
		return _success_response(request, resp["resp"])
	else:
		return _error_response(request, resp["error"])





#Create company 
#Tested
def create_company(request):
	if request.method != 'POST':
		return _error_response(request, "must make POST request")
	if 'name' not in request.POST or 'description' not in request.POST:
		return _error_response(request, "missing fields")
	
	values = { 
						"name" : request.POST['name'],
						"description" : request.POST['description'],
	}
	data = urllib.parse.urlencode(values).encode('utf-8')
	req = urllib.request.Request('http://models:8000/api/v1/company/create', data=data, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	if resp["ok"] is True:
		#es_add is a temporay helper function adding listing to ES directly without working with kafka 
		es_add_company_listing(request, resp["resp"]["company_id"])
		return _success_response(request, resp["resp"])
	else:
		return _error_response(request, resp["error"])


#Serarch compnay 
#url http://localhost:8002/api/v1/company/search?q=
#Tested
def search_company(request):
	if request.method!= 'GET':
		return _error_response(request, "must make GET request")	
	es = Elasticsearch(['es'])
	es.indices.refresh(index="company_index")
	resp = es.search(index='company_index', body={'query': {'query_string': {'query': request.GET.get('q', '')}}, 'size': 10})
	if resp['timed_out'] is True:
		return _error_response(request, "search service is down.")
	if resp['hits']['total'] is 0:
		return _success_response(request, "No matched results found.")
	data = []
	for s in resp['hits']['hits']:
			data.append(s['_source'])
	return _success_response(request, data)







#Csreate note
#Tested
def create_note(request):
	if request.method!= 'POST':
		return _error_response(request, "must make POST request")
	if 'authenticator' not in request.POST or 'title' not in request.POST or 'details' not in request.POST:
		return _error_response(request, "missing fields")
	
	values = { 
						"authenticator" : request.POST['authenticator'],
						"title" : request.POST['title'],
						"details": request.POST['details']
	}
	data = urllib.parse.urlencode(values).encode('utf-8')


	req = urllib.request.Request('http://models:8000/api/v1/note/create', data=data, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	if resp["ok"] is True:
		kafka = KafkaClient('kafka:9092')
		producer = SimpleProducer(kafka)
		note_new_listing = {
		"title" : request.POST['title'], 
		"details": request.POST['details'],
		"id": resp["resp"]["id"]
		}
		producer.send_messages(b'note-listings-topic', json.dumps(note_new_listing).encode('utf-8'))
	  		#es_add is a temporay helper function adding listing to ES directly without working with kafka 
		#es_add_note_listing(request, resp["resp"]["id"], resp["resp"]["username"])
		return _success_response(request, resp["resp"])
	else:
		return _error_response(request, resp["error"])






#url http://localhost:8002/api/v1/note/search?q=
def search_note(request):
	if request.method!= 'GET':
		return _error_response(request, "must make GET request")	
	es = Elasticsearch(['es'])
	es.indices.refresh(index="note_index")
	resp = es.search(index='note_index', body={'query': {'query_string': {'query': request.GET.get('q', '')}}, 'size': 10})
	if resp['timed_out'] is True:
		return _error_response(request, "search service is down.")
	if resp['hits']['total'] is 0:
		return _success_response(request, "No matched results found.")
	data = []
	for s in resp['hits']['hits']:
			data.append(s['_source'])
	return _success_response(request, data)


	

#Helper
def es_add_note_listing(request, id, username):
	es = Elasticsearch(['es'])
	note_new_listing = {'title': request.POST['title'], 'details': request.POST['details'], 'username': username, 'id': id}
	es.index(index='note_index',doc_type='listing' , id=note_new_listing['id'], body=note_new_listing)
	es.indices.refresh(index="note_index")

def es_add_company_listing(request, id):
	es = Elasticsearch(['es'])
	company_new_listing = {'name': request.POST['name'], 'description': request.POST['description'], 'id': id}
	es.index(index='company_index',doc_type='listing' , id=company_new_listing['id'], body=company_new_listing)
	es.indices.refresh(index='company_index')



def _error_response(request, error_msg):
    return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request, resp=None):
    if resp:
        return JsonResponse({'ok': True, 'resp': resp})
    else:
        return JsonResponse({'ok': True})

