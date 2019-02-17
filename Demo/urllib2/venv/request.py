#enconding:utf-8

import sys
import json
from urllib import request

from bs4 import BeautifulSoup

url = "http://www.runoob.com/python/python-chinese-encoding.html"

request = urllib.request(url)
response = urllib.request.urlopen(request, timeout=30)
result = response.read()

print(result)