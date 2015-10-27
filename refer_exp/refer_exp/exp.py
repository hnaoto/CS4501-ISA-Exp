import os
os.system("pip install -q requests")

# same as  os.system, but more ideomatic
# unable to quiet
# import subprocess
# subprocess.call(["pip","install","-q", "requests"],, stdout=open(os.devnull, 'wb'))

import requests
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django import db
from main import models #TODO: import specific models from .models, to prevent having to retype models everytime
from django.core import serializers

from stuff import main
'''
def request(url):
  return requests.get(url)

def http_to_json(url):
  return requests.get(url).json
'''

#Done
#GET request from HTML to ModelAPI
#Returns a JSON containing username, id, and company.
def all_sellers():
  r = requests.get(r'^localhost:8001/api/v1/sellers/all$') 
  return main.all_sellers(r)

#Done
#GET request from HTML to ModelAPI
#Returns a JSON containing username, id, and company.
def all_buyers():
  r = requests.get(r'^localhost:8001/api/v1/buyers/all$') 
  return main.all_buyers(r)

#POST request from HTML to ModelAPI
#requies a username and password field
def log_in(username, password):
  info = {
  "username":username
  "password":password
  } 
  r = requests.post(r'^localhost:8001/api/v1/auth/login$', data = info)
  return main.log_in(r)

#POST request from HTML to ModelAPI
#requies a authenticator
def log_out(auth):
  info = {
  'authenticator':auth
  }
  r = requests.post(r'^localhost:8001/api/v1/auth/logout$', data = info)
  return main.log_out(r)

#still seems awkward
#POST request
#Contains buyer_u_id or seller_u_id or negotiation
#need to be valid IDs
#returns a transaction_id if valid
def create_transaction(request):
  return main.create_transaction(request)

#GET request
#user_id field
#how does front-end find user_id? From cookie?
def lookup_user(user_id):
  args = user_id
  r = requests.get(r'^localhost:8001/api/v1/users/(\d+)$')
  return main.lookup_user(r,args)

def view_all_transactions():
  r = requests.get(r'^localhost:8001/api/v1/transaction/all$') 
  return main.view_all_transactions(r)


#POST
#usertype, password fields
def create_user(usertype, username, password):
  info = {
  "usertype":usertype
  "username":username
  "password":password
  } 
  r = requests.post(r'^localhost:8001/api/v1/users/create$', data = info )
  return main.create_user(r)


