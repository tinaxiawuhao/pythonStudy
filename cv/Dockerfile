FROM python:3.12.3
ADD . /work
WORKDIR /work
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
CMD ["python","yolo_study.py"]