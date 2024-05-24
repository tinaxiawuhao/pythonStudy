import httpx

headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ2YWxpZGl0eVRpbWUiOiIyMTI0LTA1LTEzIDE1OjEwOjQyIiwic3ViIjoicnN1c2VyIiwiY29tcGFueUlkIjoyMjMsInVzZXJUeXBlIjoyLCJleHAiOjE3MTY2MDQxMjUsInVzZXJJZCI6MzQxLCJ1c2VyQ29kZSI6ImRlOGUxNmRhLWVhMDMtNDRjMC1hN2QzLTUxY2NjMGU1NjIyYSIsImVtYWlsIjoiIiwicmVhbG5hbWUiOiJyc3VzZXIifQ.SRMtBTGDgaOAjHs9-IiC6eyL1enbBpQRHFieHcaTS_o'}
payload = [10576]

with httpx.Client(headers=headers) as client:
     headers = {'Content-Type': 'application/json'}
     r = client.post('http://172.16.11.247:8080/api/tool/getModelInfoByChunkIds',json=payload,headers=headers)
# 请求地址
print(r.request.url)
# 请求头
print(r.request.headers['Content-Type'])
print(r.request.headers['Authorization'])
# 返回值
print(r.json())
# 这将打印 Contnet-Type 中charset给定的字符集，或者打印“utf-8”
print(r.encoding)  

print("========================================")
headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ2YWxpZGl0eVRpbWUiOiIyMTI0LTA1LTEzIDE1OjEwOjQyIiwic3ViIjoicnN1c2VyIiwiY29tcGFueUlkIjoyMjMsInVzZXJUeXBlIjoyLCJleHAiOjE3MTY2MDQxMjUsInVzZXJJZCI6MzQxLCJ1c2VyQ29kZSI6ImRlOGUxNmRhLWVhMDMtNDRjMC1hN2QzLTUxY2NjMGU1NjIyYSIsImVtYWlsIjoiIiwicmVhbG5hbWUiOiJyc3VzZXIifQ.SRMtBTGDgaOAjHs9-IiC6eyL1enbBpQRHFieHcaTS_o'}
payload = [10576]
with httpx.Client(headers=headers) as client:
    headers = {'X-Api-Key': 'key'}
    # 设置单个请求超时
    request = client.build_request("POST", "http://172.16.11.247:8080/api/tool/getModelInfoByChunkIds",json=payload,headers=headers, timeout=10.0)
    # Don't send the API key for this particular request.
    del request.headers["X-Api-Key"]
    response = client.send(request)
    # 返回值
    print(response.json())


# Use a default 10s timeout everywhere.
client = httpx.Client(timeout=10.0)  
# Disable all timeouts by default.
client = httpx.Client(timeout=None)  

# 可以使用​Client​上的​limits​关键字参数控制连接池大小。它采用​httpx.Limits​的实例定义：

# ​max_keepalive_connections​，允许的保持活动状态连接数，或​None​始终允许。（默认值 20）
# ​max_connections​，允许的最大连接数，或​None​无限制。（默认值 100）
#吧​keepalive_expiry​，空闲保持活动状态连接的时间限制（以秒为单位），或​None​无限制。（默认值 5）
limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
client = httpx.Client(limits=limits)