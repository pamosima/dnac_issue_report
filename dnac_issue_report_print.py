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
from webexteamssdk import WebexTeamsAPI
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

dnac_username = os.getenv('dnacUsername')
dnac_password = os.getenv('dnacPassword')
dnac_base_url = os.getenv('dnacIP')
webex_token = os.getenv('webexToken')
webex_room_id = os.getenv('webexRoomId')

# Create a DNACenterAPI connection object; it uses DNA Center username and password, with DNA Center API version 1.2.10
# The base_url used by default is `from dnacentersdk.config import DEFAULT_BASE_URL`
dnac = DNACenterAPI(username=dnac_username,
                   password=dnac_password,
                   base_url=dnac_base_url,
                   version='2.3.3.0', 
                   verify=False,
                   debug=True)

webex = WebexTeamsAPI(access_token=webex_token)

issueP1=dnac.issues.issues(priority="p1", issueStatus="ACTIVE")
issueP2=dnac.issues.issues(priority="p2", issueStatus="ACTIVE")
issueP3=dnac.issues.issues(priority="p3", issueStatus="ACTIVE")
issueP4=dnac.issues.issues(priority="p4", issueStatus="ACTIVE")

occurrence = datetime.now().strftime('%d.%m.%Y %H:%M:%S')

output = str("")
output += str("Cisco DNA Center Issue Report\n")
output += str("Occurrence: "+occurrence+"\n")
output += str("---\n")
output += str("No of Issues: P1="+issueP1.totalCount+" P2="+issueP2.totalCount+" P3="+issueP3.totalCount+" P4="+issueP4.totalCount+"\n")
output += str("---\n")
output += str("List of P1 & P2 Issues:\n")
jsonIssueP1 = json.loads(json.dumps(issueP1))
p1issues = [(issue['priority'], issue['name']) for issue in jsonIssueP1['response']]
for issue in p1issues:
    output += str("{}: {}\n".format(issue[0], issue[1]))
    
jsonIssueP2 = json.loads(json.dumps(issueP2))
p2issues = [(issue['priority'], issue['name']) for issue in jsonIssueP2['response']]
for issue in p2issues:
    output += str("{}: {}\n".format(issue[0], issue[1]))
output += str("---")

print(output)


