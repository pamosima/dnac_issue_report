#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Cisco DNA Center Issue Report Console Script.

Copyright (c) 2023 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Patrick Mosimann"
__email__ = "pamosima@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2023 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import json
import http.client
import base64
import os
from dnacentersdk import DNACenterAPI
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

dnac_username = os.getenv('dnacUSERNAME')
dnac_password = os.getenv('dnacPASSWORD')
dnac_base_url = os.getenv('dnacIP')

ecall_username = os.getenv('ecallUSERNAME')
ecall_password = os.getenv('ecallPASSWORD')


# Create a DNACenterAPI connection object; it uses DNA Center username and password, with DNA Center API version 1.2.10
# The base_url used by default is `from dnacentersdk.config import DEFAULT_BASE_URL`
api = DNACenterAPI(username=dnac_username,
                   password=dnac_password,
                   base_url=dnac_base_url,
                   version='2.3.3.0', 
                   verify=False,
                   debug=True)
issueP1=api.issues.issues(priority="p1", issueStatus="ACTIVE")
issueP2=api.issues.issues(priority="p2", issueStatus="ACTIVE")
issueP3=api.issues.issues(priority="p3", issueStatus="ACTIVE")
issueP4=api.issues.issues(priority="p4", issueStatus="ACTIVE")

occurrence = datetime.now().strftime('%d.%m.%Y %H:%M:%S')

authorization = base64.b64encode(f"{ecall_username}:{ecall_password}".encode('ascii')).decode('ascii')

client = http.client.HTTPSConnection("rest.ecall.ch")
headers = {
    'Authorization': 'Basic ' + authorization,
    'Content-Type': 'application/json'
}

message = f"""{{ 
    "channel": "sms",
    "from": "0041763373989",
    "to": "0041763373989",
    "content": {{
        "type": "Text",
        "text": "Cisco DNA Center Issue Report from {occurrence} No of Issues: P1={issueP1.totalCount} P2={issueP2.totalCount} P3={issueP3.totalCount} P4={issueP4.totalCount}" 
    }}
}}"""

client.request("POST", "/api/message", message, headers)

res = client.getresponse()
print(res.read().decode("utf-8"))
