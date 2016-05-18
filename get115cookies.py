#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import browsercookie
import re
import sys
reload(sys).setdefaultencoding("utf-8")
cj = browsercookie.chrome()
dict115 = cj._cookies[u'.115.com'][u'/']
cid = dict115['CID'].value
oefl = dict115['OOFL'].value
seid =  dict115['SEID'].value
uid = dict115['UID'].value
data  = {'cookies': {'CID': cid, 'OEFL': oefl, 'SEID': seid, 'UID': uid}}
import json
with open('/Users/kim/.115.cookies', 'w') as f:
  json.dump(data, f, ensure_ascii=False)
