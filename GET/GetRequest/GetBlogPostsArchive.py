import json
import requests as req
import jsonpath as jp

#### Year ####

response = req.get('http://localhost:8888/api/blog/posts/archive/2020/?page=1&per_page=10')

file = open('C:/Automation Python/RESTAPI/GET/GetResponse/GetBlogPostsYearResponse.json', 'w')
file.write(response.text)

print('Response is: ', response.content)

assert response.status_code == 200

if response.status_code == 200:
   print("Get Year Success:", response.status_code)

if __debug__:
   if not response.status_code: raise AssertionError


######### Year and Month ############

response1 = req.get('http://localhost:8888/api/blog/posts/archive/2020/2/?page=1&per_page=10')

file1 = open('C:/Automation Python/RESTAPI/GET/GetResponse/GetBlogPostsYearMonthResponse.json', 'w')
file1.write(response1.text)

print('Response is: ', response1.content)

assert response1.status_code == 200

if response1.status_code == 200:
   print("Get Year and Month Success:", response1.status_code)

if __debug__:
   if not response1.status_code: raise AssertionError

######### Year , Month and Day ############

response2 = req.get('http://localhost:8888/api/blog/posts/archive/2020/2/5/?page=1&per_page=10')

file2 = open('C:/Automation Python/RESTAPI/GET/GetResponse/GetBlogPostsYearMonthDayResponse.json', 'w')
file2.write(response2.text)

print('Response is: ', response2.content)

assert response2.status_code == 200

if response2.status_code == 200:
   print("Get Year, Month and Day Success:", response2.status_code)

if __debug__:
   if not response2.status_code: raise AssertionError
