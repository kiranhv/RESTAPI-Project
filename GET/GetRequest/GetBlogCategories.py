import json
import requests as req
import jsonpath as jp

response = req.get('http://localhost:8888/api/blog/categories/')

file = open('C:/Automation Python/RESTAPI/GET/GetResponse/GetResponse.json', 'w')
file.write(response.text)

print('Response is: ', response.content)

assert response.status_code == 200

if response.status_code == 200:
   print("Get Success:", response.status_code)

if __debug__:
   if not response.status_code: raise AssertionError


######### Get request with ID ############

response1 = req.get('http://localhost:8888/api/blog/categories/1068')

file1 = open('C:/Automation Python/RESTAPI/GET/GetResponse/GetResponsewithID.json', 'w')
file1.write(response1.text)

print('Response is: ', response1.content)

assert response1.status_code == 200

if response1.status_code == 200:
   print("Get with ID Success:", response1.status_code)

if __debug__:
   if not response1.status_code: raise AssertionError
