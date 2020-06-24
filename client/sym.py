#!/usr/bin/python 
# -*- coding: utf-8 -*-
from .utils import get_md5_Str, get, post, get_timestamp, get_toml_file
import json

class SymClient:
    company_id = ""
    secret = ""

    def __init__(self):
        pass

    def get_comapny_id(self):
        return self.company_id

    def register(self, company_name, user_name, password):
        """regieter company.

        :param company_name: company name.
        :param user_name: user name.
        :param password: password.
        """
        body = {
            "name": company_name,
            "user_name": user_name,
            "pwd": get_md5_Str(password)
        }
        data = post('/auth/register', body)
        if data is not None and data['code'] == 200:
            self.company_id = data['result']['id']
            self.secret = data['result']['secret']
        else:
            raise Exception('register failure')

    def login(self, user_name, password):
        body = {
            "user_name": user_name,
            "pwd": get_md5_Str(password)
        }
        data = post('/auth/login', body)
        if data is not None and data['code'] == 200:
            self.company_id = data['result']['id']
            self.secret = data['result']['secret']
        else:
            raise Exception('login failure')

    def upload_data_label_schema(self, toml_file):
        toml_dict = get_toml_file(toml_file)
        body = {
            'toml': toml_dict
        }
        print(body)
        url = '/data/schema?id={id}&ts={ts}&sign={sign}'.format(id=self.company_id, ts=get_timestamp(), sign="testsign")
        data = post(url, body)
        if data is None:
            raise Exception('upload_data_label_schema failure')
        elif data['code'] != 200:
            raise Exception('upload_data_label_schema failure')
        else:
            return data['result']['schema_id']

    def request_buffer_data(self, schema_id, start_date, end_date, cursor):
        url = '/buffer/pull?id={id}&ts={ts}&sign={sign}'.format(id=self.company_id, ts=get_timestamp(), sign='testsign')
        body = {
            "schema_id": schema_id,
            "scope": {
                "start_date": start_date,
                "end_date": end_date,
                "cursor": cursor
            }
        }
        data = post(url, body)
        if data is not None and data['code'] == 200:
            return data['result']['items'], data['result']['next_cursor']
        else:
            raise Exception('request_buffer_data failure')

    def push_data_label(self, schema_id, data_dict):
        body = {
            "schema_id": schema_id,
            "data": data_dict
        }
        url = '/data/push?id={id}&ts={ts}&sign={sign}'.format(id=self.company_id, ts=get_timestamp(), sign="testsign")
        resp = post(url, body)
        if resp is not None and resp['code'] == 200:
            return 'success'
        else:
            raise Exception('push_data_label failure')

    def upload_model_label_schema(self, toml_file):
        toml_dict = get_toml_file(toml_file)
        body = {
            'toml': toml_dict
        }
        print(body)
        url = '/label/schema?id={id}&ts={ts}&sign={sign}'.format(id=self.company_id, ts=get_timestamp(), sign="testsign")
        data = post(url, body)
        if data is None:
            raise Exception('upload_model_label_schema failure')
        elif data['code'] != 200:
            raise Exception('upload_model_label_schema failure')
        else:
            return data['result']['schema_id']

    def request_data_label(self, schema_id, start_date, end_date, cursor):
        url = '/data/pull?id={id}&ts={ts}&sign={sign}'.format(id=self.company_id, ts=get_timestamp(), sign='testsign')
        body = {
            "schema_id": schema_id,
            "scope": {
                "start_date": start_date,
                "end_date": end_date,
                "cursor": cursor
            }
        }
        data = post(url, body)
        if data is not None and data['code'] == 200:
            return data['result']['items'], data['result']['next_cursor']
        else:
            raise Exception('request_data_label failure')

    def request_model_label(self, schema_id, start_date, end_date, cursor):
        url = '/label/pull?id={id}&ts={ts}&sign={sign}'.format(id=self.company_id, ts=get_timestamp(), sign='testsign')
        body = {
            "schema_id": schema_id,
            "scope": {
                "start_date": start_date,
                "end_date": end_date,
                "cursor": cursor
            }
        }
        data = post(url, body)
        if data is not None and data['code'] == 200:
            return data['result']['items'], data['result']['next_cursor']
        else:
            raise Exception('request_model_label failure')

    def push_model_label(self, schema_id, data_dict):
        body = {
            "schema_id": schema_id,
            "data": data_dict
        }
        url = '/label/push?id={id}&ts={ts}&sign={sign}'.format(id=self.company_id, ts=get_timestamp(), sign="testsign")
        resp = post(url, body)
        if resp is not None and resp['code'] == 200:
            return 'success'
        else:
            raise Exception('push_data_label failure')