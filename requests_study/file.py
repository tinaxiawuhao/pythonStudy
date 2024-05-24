import requests

url = 'http://httpbin.org/post'
# files = {'file': open('report.xls', 'rb')}
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
# 显式地设置文件名，文件类型和请求头
#files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

r = requests.post(url, files=files)
r.text