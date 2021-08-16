import requests
import json

urls = [
    "http://10.138.228.199:31605/api/queryRAPModel.do?projectId=3"
]

def do_get(url):
    rsp = requests.get(url)
    if rsp.status_code != 200:
        print("get wrong when do url: {}".format(url))
        return
    return rsp.json()


def genner(jdata):
    info = jdata.get("modelJSON")
    print(info)



def main():
    for u in urls:
        jdata = do_get(u)
        genner(jdata)


if __name__ == "__main__":
    main()