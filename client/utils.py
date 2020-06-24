#!/usr/bin/python 
# -*- coding: utf-8 -*-

import hashlib
import requests
import json 
import sys 
import time 
import toml 

BASE_URL = "https://openplatform.symphonyprotocol.io"

def get_md5_Str(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    return m.hexdigest()

def post(sub_url, body):
    url = BASE_URL + sub_url
    try:
        resp = requests.post(url=url, json=body)
        print(resp.status_code)
        print(resp.text)
        if resp.status_code == 200:
            return json.loads(resp.text) 
    except:
        print(sys.exc_info()[0])
    return None

def get(sub_url):
    url = BASE_URL + sub_url
    try:
        resp = requests.get(url=url)
        print(resp.status_code)
        print(resp.text)
        if resp.status_code == 200:
            return json.loads(resp.text) 
    except:
        print(sys.exc_info()[0])
    return None 

def get_timestamp():
    t = time.time()
    return int(t)      

def get_toml_file(file_name):
    with open(file_name, 'r') as fi:
        text = fi.read()
        return text