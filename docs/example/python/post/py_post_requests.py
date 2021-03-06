# -*- coding: utf-8 -*-
"""
Iot dashboard POST example

iot-dashboard
IoT: Platform for Internet of Things

Iotdashboard source code is available under the MIT License

Online iot dashboard test and demo http://ihook.xyz

Online iot dashboard https://iothook.com

You can find project details on our project page https://iothook.com and wiki https://iothook.com
"""

import requests
import json

API_KEY = "c791e11-d9ab779"
url = 'http://localhost:8000/api/v1/datas/' + API_KEY

datas = {'name_id':'test','value':'66'}

auth=('iottestuser', 'iot12345**')

response = requests.post(url, data=datas, auth=auth)
print response
