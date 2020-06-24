import requests as req
import json
import jsonpath


response = req.delete("http://localhost:8888/api/blog/categories/100")

assert response.status_code == 204

if response.status_code == 204:
   print("Delete Success: No Content",response.status_code)

if __debug__:
   if not response.status_code: raise AssertionError


file1 = open('C:/Automation Python/RESTAPI/DELETE/DelResponseFile/DeleteResponse.json', 'w')
file1.write(response.text)

response_get = req.get("http://localhost:8888/api/blog/categories/")
print(response_get.content)

file2 = open('C:/Automation Python/RESTAPI/DELETE/DelResponseFile/AfterDeleteResponse.json', 'w')
file2.write(response_get.text)
