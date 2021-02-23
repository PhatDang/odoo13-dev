#!/usr/bin/python3
import json
import requests
import base64


url = 'http://localhost:8069'
username = 'admin'
password = 'admin'


# =============================================================


print('\n 1. Login in Odoo and get access tokens:')
r = requests.post(
    url + '/api/auth/get_tokens',
    headers={'Content-Type': 'text/html; charset=utf-8'},
    data=json.dumps({
        'username': username,
        'password': password,
    }),
    # verify = False      # for TLS/SSL connection
)
print(r.text)
access_token = r.json()['access_token']


print("\n 2. report - Call method 'get_pdf' (with parameters):")
r = requests.get(
    url + '/api/report/get_pdf',
    headers={
        'Content-Type': 'text/html; charset=utf-8',
        'Access-Token': access_token
    },
    data=json.dumps({
        "report_name":  "account.report_invoice",
        "ids":          [3],  # for Odoo v12/v11/v9/v8
        # "docids":       [3],  # for Odoo v10
    }),
    # verify = False      # for TLS/SSL connection
)
print(r.text[:500] + '\n...')


print("\n 3. Decoding to PDF format:")
pdf = base64.decodestring(eval(r.text))
print(pdf[:500] + '\n...')


# Obtain a final PDF file
# f = open('OUT.pdf', 'w')
# f.write(pdf)
# f.close()
