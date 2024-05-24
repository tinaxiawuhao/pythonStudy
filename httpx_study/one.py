import httpx

# 要在请求中包含 URL 查询参数，请使用关键字：​params​
# params = {'key1': 'value1', 'key2': 'value2'}
# params = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = httpx.get('https://httpbin.org/get', params=params)


headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ2YWxpZGl0eVRpbWUiOiIyMTI0LTA1LTEzIDE1OjEwOjQyIiwic3ViIjoicnN1c2VyIiwiY29tcGFueUlkIjoyMjMsInVzZXJUeXBlIjoyLCJleHAiOjE3MTY2MDQxMjUsInVzZXJJZCI6MzQxLCJ1c2VyQ29kZSI6ImRlOGUxNmRhLWVhMDMtNDRjMC1hN2QzLTUxY2NjMGU1NjIyYSIsImVtYWlsIjoiIiwicmVhbG5hbWUiOiJyc3VzZXIifQ.SRMtBTGDgaOAjHs9-IiC6eyL1enbBpQRHFieHcaTS_o'}
payload = [10576]
r = httpx.post('http://172.16.11.247:8080/api/tool/getModelInfoByChunkIds', json=payload, headers=headers)
print(r.json())
print("============================================")
with httpx.stream("POST", "http://172.16.11.247:8080/api/tool/getModelInfoByChunkIds", json=payload, headers=headers) as r:
     for data in r.iter_bytes():
         print(data)