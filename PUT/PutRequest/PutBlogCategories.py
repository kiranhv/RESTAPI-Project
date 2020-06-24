import requests as req
import json
import jsonpath
import POST

url = 'http://localhost:8888/api/blog/categories/10'

headers = {'content-type': 'application/json'}

file = open('C:/Automation Python/RESTAPI/PUT/PutRequestFile/PutRequest.json', 'r')
input_content = file.read()
request_json = json.loads(input_content)

response = req.put(url, data=json.dumps(request_json), headers=headers)
print(response.content)

assert response.status_code == 204

if response.status_code == 204:
   print("Put Success:", response.status_code)

if __debug__:
    if not response.status_code: raise AssertionError

file1 = open('C:/Automation Python/RESTAPI/PUT/PutResponseFile/PutResponse.json', 'w')
file1.write(response.text)

response_get = req.get("http://localhost:8888/api/blog/categories/")
print(response_get.content)

file2 = open('C:/Automation Python/RESTAPI/PUT/PutResponseFile/AfterPutResponse.json', 'w')
file2.write(response_get.text)

#json_text = json.loads(response.content)
#id  = jsonpath.jsonpath(json_text, 'id')
#print(id[0])