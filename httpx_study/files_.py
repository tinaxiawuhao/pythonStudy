import httpx

files = {'upload-file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel')}
r = httpx.post("https://httpbin.org/post", files=files)
print(r.text)

# 第一个元素是可选文件名，可以设置为​None ​。
# 第二个元素可以是类似文件的对象或字符串，它将以​ UTF-8 ​自动编码。
# 可选的第三个元素可用于指定要上载的文件的 MIME 类型。如果未指定，HTTPX 将尝试根据文件名猜测 MIME 类型，
# 未知文件扩展名默认为“​application/octet-stream​”。如果文件名显式设置为​None​，则 HTTPX 将不包含内容类型 MIME 标头字段。
files = {'upload-file': (None, 'text content', 'text/plain')}
r = httpx.post("https://httpbin.org/post", files=files)
print(r.text)

# 多文件
files = [('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
                      ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
r = httpx.post("https://httpbin.org/post", files=files)