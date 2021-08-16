import requests

url = "http://10.138.228.199:31605/api/queryRAPModel.do?projectId=3"
# url = "https://open.cosmoplat.com:443/api/checkHealth?name=attack"
# url = "https://openapi-uat.app.cosmoplat.com:443/5A7KNP97/v3/api/checkHealth?name=attack"
# url = "http://10.138.130.29:50448/api/checkHealth?name=attack"
# url = "https://openapi-uat.app.cosmoplat.com/5A7KNP97/v3/api/checkHealth?name=attack"


# headers = {"api_gateway_auth_token": "rg2eDZlVENSRqnFcwpOjAwxMbc4j5oppnQBdwRjrtnmD+8eCcPqO89HMrBcdfu1Mdok2UkqQpWJcJy59N8OA-LNKIXaFLl7rKR3xSKmvoJKD0XI8nBv7OEfpGbvmFvYWd72obHg6q3iWPofrOvblTljZ89dpCsTgglmpoGawcLC+8KqPvNH7+E2Qf0eQy0yv"}

# url = "http://seeseeu.top"
rsp = requests.get(url, allow_redirects=False)

# print(rsp.headers)
print(rsp.text)
# print(rsp.status_code)

