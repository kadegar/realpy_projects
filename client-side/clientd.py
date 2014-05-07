#submitting to a web form

import requests

url='http://httpbin.org/post'
data={'fname':'Frederick','lname':'the Great'}

r=requests.post(url,data=data)

print r.content
