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


import urllib.request
import urllib.parse
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django import db
#from main import models #TODO: import specific models from .models, to prevent having to retype models everytime
from django.core import serializers
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
  info = {
  "username":username
  "password":password
  } 
  r = requests.post(r'^localhost:8001/api/v1/auth/login$', data = info)
  return main.log_in(r)
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

#Helper
def _error_response(request, error_msg):
    return JsonResponse({'ok': False, 'error': error_msg})

def _success_response(request, resp=None):
    if resp:
        return JsonResponse({'ok': True, 'resp': resp})
    else:
        return JsonResponse({'ok': True})

