# openplatform_client

Examples:

1. create client:
```
client = sym.SymClient()
```

2. create company and user, 
```
client = sym.SymClient()
client.register('test_company', 'test_user', 'test_pwd')
```

3. after create a user, need to login before other actions
```
client = sym.SymClient()
client.login('test_user', 'test_pwd')
```

4. view company_id after login if you need company_id
```
client = sym.SymClient()
client.login('test_user', 'test_pwd')
company_id = client.get_comapny_id()
print(company_id)
```

5. upload data toml schema, return schema_id which will be used in next steps
```
client = sym.SymClient()
client.login('test_user', 'test_pwd')
schema_id = client.upload_data_label_schema('../openplatform/tools/test.toml')
print(schema_id)
```

6. use buffer data, 1273600184722538496 is the buffer schema_id, "2020-05-01" is the start query date, "2020-06-30" is the end query date, 0 is the cursor index, if records during query are more than 100, then each query will return 100 maximun records, when query more than 100 records in the same query period, the cursor will be next data start index, the "next_cursor" will be returned in result body.
```
client = sym.SymClient()
client.login('test_user', 'test_pwd')
data = client.request_buffer_data(1273600184722538496, "2020-05-01", "2020-06-30", 0)
print(data)
```

7. upload data label, 1275804353319559168 is the data label schema_id, {} is the label item dict
```
client = sym.SymClient()
client.login('test_user', 'test_pwd')
client.push_data_label(1275804353319559168, {})
```

8. upload model label schema
```
client = sym.SymClient()
client.login('test_user', 'test_pwd')
schema_id = client.upload_model_label_schema('../openplatform/tools/test.toml')
print(schema_id)
```

9. get data labels, same as get buffer data
```
client = sym.SymClient()
client.login('test_user', 'test_pwd')
res = client.request_data_label(1275004877172531200, "2020-05-01", "2020-06-30", 0)
print(res)
```

10. get model labels, same as get buffer data
```
client = sym.SymClient()
client.login('test_user', 'test_pwd')
res = client.request_model_label(1275012792373637120, "2020-05-01", "2020-06-30", 0)
print(res)
```

11. upload model label
```
client = sym.SymClient()
client.login('test_user', 'test_pwd')
res = client.push_model_label( 1275012792373637120, {"test":"item"})
print(res)
```