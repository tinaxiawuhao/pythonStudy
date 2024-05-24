import requests

headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ2YWxpZGl0eVRpbWUiOiIyMTI0LTA1LTEzIDE1OjEwOjQyIiwic3ViIjoicnN1c2VyIiwiY29tcGFueUlkIjoyMjMsInVzZXJUeXBlIjoyLCJleHAiOjE3MTY2MDQxMjUsInVzZXJJZCI6MzQxLCJ1c2VyQ29kZSI6ImRlOGUxNmRhLWVhMDMtNDRjMC1hN2QzLTUxY2NjMGU1NjIyYSIsImVtYWlsIjoiIiwicmVhbG5hbWUiOiJyc3VzZXIifQ.SRMtBTGDgaOAjHs9-IiC6eyL1enbBpQRHFieHcaTS_o'}
# headers = {'Content-Type': 'application/json'}

payload = [10576]
r = requests.post('http://172.16.11.247:8080/api/tool/getModelInfoByChunkIds', json=payload, headers=headers)
# payload = {'key1': 'value1', 'key2': 'value2'}
# payload = (('key1', 'value1'), ('key1', 'value2'))
# r = requests.post('http://172.16.11.247:8080/api/tool/getModelInfoByChunkIds', data=payload, headers=headers)
# 返回数据
print(r.json())
# print(r.text())
# 响应状态码
print(r.status_code)
print(r.status_code == requests.codes.ok)
# 请求头
print(r.request.headers)
# 响应头
print(r.headers)


