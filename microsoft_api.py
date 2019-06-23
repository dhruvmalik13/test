#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 19:04:46 2017

@author: dhruvmalik
"""

import urllib.request
import requests
import json
import numpy as np
key = "94b7fad1b7eb4473bb53c126df03341f"
list_images=['https://s-media-cache-ak0.pinimg.com/564x/5a/bd/c0/5abdc0d5dc2a627132deb60164df2c83.jpg','https://s-media-cache-ak0.pinimg.com/564x/80/f1/a4/80f1a40212097f12e1bc4176f56c9626.jpg']
image_sample=r"/Users/dhruvmalik/Desktop/profile_pic.png"

with open( image_sample, 'rb' ) as f:
    data = f.read()
#urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)¶
url="https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"
headers = {
    
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
}
#print(data)
#data={"url":data }
#data = json.dumps({'name':'image_sample'})
#response = requests.request( 'POST', url, data=data, headers = headers,json=None )
json=None
params=None
print(data)
response = requests.request( 'post', url, json = json, data = data, headers = headers, params = params )
response=response.json()
print(response)

new_url=urllib(data="d",body={"data": api,"scores":"565"})   


#arams = urllib.urlencode({ "url": "http://example.com/picture.jpg"})
#data=urllib.request.Request(url,headers,str(body),"POST")
#response=[];
for i in range(1:1000):
	if(len(response) == 200):
		data=response
#for i in image_sample:
  #  body={"url": i}
   # response = requests.request( 'POST', url, json = body, headers = headers )
    #response=response.json()
    #response.append(response)
#response = requests.request( 'POST', url, ç, headers = headers )
#response=response.json()

#d=response[0]['scores']
#print(response[0]['scores'])

#response=urllib.request.Request('POST', url, data = body, headers = headers)
