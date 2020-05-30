import requests
import json
import os
import requests



AUTH_ENDPOINT='http://127.0.0.1:8000/api/auth/manual/'
ENDPOINT = "http://127.0.0.1:8000/api/local/"

headers1={
    'Content-Type' : 'application/json'
    }
data={
    'username':'ahsanali',
    'password':'ahsan',
    }
r=requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers1)
token=r.json()

print(token)


##
##headers={    
##    'Authorization':'JWT '+ token,
##    }
##data={
##    'content':'what\'s up'  
##    }
##rr=requests.put(ENDPOINT+str(15)+'/', data=data,headers=headers)
##print(rr.text)

'''

do_img(method='put',id=14,data={'user': 1, 'content':"akjdf;kjdhf"})


def do(method='get', data={},id='', is_json =True):
    headers={}
    if is_json:
        headers['content-type']='application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, headers=headers)
    print(r.text)
    return r


do(data={'id': 7})
do(method='delete', data={'id': 34})
do(method="put", data={'id': 6,'user':1,'content':'Using responses'})
do(method="post", data={'user':1,'content':'Using post'})
'''

'''
Create
Retreive/List
Update
Delete
'''
