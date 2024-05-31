```
pip freeze > requirements.txt
```

将项目依赖库进行导出。命令执行完成后会生成一个叫requirements.txt的文件

```
FROM python:3.12.3
ADD . /work
WORKDIR /work
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
CMD ["python","./yolo_study.py"]
```

```
docker build -t yolo:v8 .
```

通过docker打包
