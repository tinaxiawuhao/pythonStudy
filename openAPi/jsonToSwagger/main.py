import os
import json
import requests
from operator import itemgetter


DIR_HTML = "./html"
DIR_JSON = "./json"
DIR_NODE = "./nodejs"
DIR_SWAG = "./swagger"


def get_html(html_url):
    pass


def html2json():
    pass


def reader(fi):
    f = open(fi, "r", encoding="utf8")
    cont = f.read()
    f.close()
    return cont


def name_parser(js):
    jss = js.split("\xa0")
    return jss[1].strip(".json")


def gen_tags(data):
    tags = list()
    for item in data:
        if not item:
            continue
        tag = dict()
        tag["name"] = item.get("name").replace("\xa0", " ")
        tag["description"] = item.get("name").replace("\xa0", " ")
        if not tag["name"]:
            continue
        tags.append(tag)
    return tags


def gen_info(data):
    return []


def gen_paths(datas):
    paths = dict()
    for item in datas:
        path_dict = dict()
        tag = item.get("name").replace("\xa0", " ")
        items = item.get("list")
        for data in items:
            tmp2 = dict()
            path = data.get("path").replace(".", "").replace("http://", "").replace(":", "/").replace("-", "_")
            method = data.get("method")
            tags = [tag]

            method_dict = dict()
            method_dict.update({"tags": tags})

            summary = data.get("title")
            method_dict.update({"summary": summary})
            method_dict.update({
                "authMethod": "md5",
                "authKey": 12345678,
                "publishType": 1,
                "apiLabelName": "基础接口",
            })

            if data.get("req_body_type") == "json":
                req_content_type = "application/json"
                method_dict.update({"consumes": [req_content_type]})
            if data.get("res_body_type") == "json":
                res_content_type = "application/json"
                method_dict.update({"produces": [res_content_type]})

            if "?" in path:
                path = path.split("?")[0]

            if not str(path).startswith("/"):
                path = os.path.join("/", path)

            # 取参数
            """
            {
                "name": "coupon",
                "desc": "",
                "type": "object",
                "no": 0
            },
            {
                "name": "condition",
                "desc": "---使用条件",
                "type": "string",
                "no": 1
            },
            {
                "name": "status",
                "desc": "---状态：1有效2无效",
                "type": "number",
                "no": 2
            }
            """
            req_query = data.get("req_query", [])
            req_query = sorted(req_query, key=itemgetter('no'))

            body_index = 0
            flag = False
            body = {"in": "body"}
            if req_query and len(req_query) > 0:
                parameters = list()
                for index, pitem in enumerate(req_query):
                    if not pitem:
                        continue
                    name = pitem.get("name")
                    if not name:
                        continue
                    param = dict()

                    type = pitem.get("type", "string")
                    if type == "":
                        type = "string"
                    if str(type).startswith("array<") and str(type).endswith(">"):
                        tmptype = str(type).rstrip(">").lstrip("array<")
                        type = "string" if tmptype=="object" else tmptype

                    no = pitem.get("no")
                    description = pitem.get("desc", "")


                    def parse_object_param():
                        param["name"] = name
                        param["description"] = description
                        schema = {"type": "object"}
                        properties = dict()
                        for i in range(index+1, len(req_query)-1):
                            pitem = req_query[i]
                            # if param["name"] == "farm":
                            #     print(pitem)
                            nname = pitem.get("name")
                            ptype = pitem.get("type", "string")
                            if ptype == "":
                                ptype = "string"
                            if str(ptype).startswith("array<") and str(ptype).endswith(">"):
                                tmptype = str(ptype).rstrip(">").lstrip("array<")
                                ptype = "string" if tmptype == "object" else tmptype
                            pdesc = pitem.get("desc", "")
                            if not str(pdesc).startswith("--"):
                                break
                            if name in ["pageSize", "pageNo", "page"]:
                                ptype = "integer"

                            properties.update({nname: {"type": ptype, "description": pdesc}})
                        schema.update({"properties": properties})
                        param.update({"schema": schema})

                    if type == "object":
                        parse_object_param()
                        if flag == False:
                            body.update(param)
                            body_index = len(parameters)
                            flag = True
                        else:
                            body_pa = parameters[body_index]
                            print(body_pa)
                            print(param)
                            body_index = -1
                        if body_index != -1:
                            parameters.append(body)
                    else:

                        if str(description).startswith("---"):
                            continue
                        param["name"] = name
                        param["description"] = description

                        if name in ["pageSize", "pageNo", "page"]:
                            param["type"] = "integer"
                            param["in"] = "query"
                        else:
                            param["type"] = type
                            param["in"] = "query"

                        if description == "放header里面就行":
                            param["in"] = "header"
                        if str(description).count("header")>0:
                            param["in"] = "header"

                        parameters.append(param)
                method_dict.update({"parameters": parameters})


            # 设置返回
            '''
                  responses:
                    '200':
                      description: A User object
                      content:
                        application/json:
                          schema:
                            type: object
                            properties:
                              id:
                                type: integer
                                description: The user ID.
                              username:
                                type: string
                                description: The user name.
            '''
            res_body = data.get("res_body")
            responses = {}
            if res_body and "array" in res_body:
                responses = dict()

                content = {}
                schema = {}
                properties = {}

                res_body = json.loads(res_body)
                pros = res_body.get("properties")
                for k, v in pros.items():
                    if not k:
                        continue
                    if not isinstance(v, dict):
                        continue
                    type = v.get("type")
                    desc = v.get("description")
                    if type == "number":
                        type = "integer"

                    if not type:
                        type = "object"
                    if not desc:
                        desc = ""
                    if str(type).startswith("array<") and str(type).endswith(">"):
                        tmptype = str(type).rstrip(">").lstrip("array<")
                        type = "string" if tmptype == "object" else tmptype

                    if type == "array":
                        tmp = {
                            k: {
                                "type": type,
                                "description": desc,
                                "items": {"type": "object"}
                            }
                        }
                    else:
                        tmp = {
                            k: {
                                "type": type,
                                "description": desc
                            }
                        }
                    properties.update(tmp)

                schema.update({
                    "type": "object",
                    "properties": properties
                })

                # content.update({"application/json": schema})

                responses.update({
                    "200": {
                        "description": "success",
                        "schema": schema
                    }
                })

            method_dict.update({"responses": responses})

            tmp2.update({str.lower(method): method_dict})
            paths.update({path: tmp2})

    return paths


def json_parser(js):
    cont = reader(js)
    data = {}
    try:
        data = json.loads(cont)
    except Exception as e:
        print(js, e)
        return

    swag_name = name_parser(js)

    swag_json = dict()
    swag_json["swagger"] = "2.0"
    swag_json["schemes"] = ["https", "http"]
    swag_json["host"] = "haiyouhetest-user.qingdao.cosmoplat.com"
    swag_json["basePath"] = "/"
    swag_json["info"] = {
        "title": swag_name,
        "version": "1.0"
    }

    tags = gen_tags(data)
    paths = gen_paths(data)

    swag_json.update({"tags": tags})
    swag_json.update({"paths": paths})

    f = open(os.path.join(DIR_SWAG, swag_name), "w", encoding="utf8")
    f.write(json.dumps(swag_json, ensure_ascii=False))
    f.close()


def json2swagger(jsons):
    for js in jsons:
        json_parser(js)


def get_all_jsons():
    files = os.listdir(DIR_JSON)
    files = [os.path.join(DIR_JSON, file) for file in files]
    return files


def main():
    jsons = get_all_jsons()
    json2swagger(jsons)


def demo():
    data = """{\"properties\":{\"code\":{\"type\":\"number\",\"description\":\"\"},\"msg\":{\"type\":\"string\",\"description\":\"\"},\"data\":{\"properties\":{\"pageSize\":{\"type\":\"number\",\"description\":\"每页几个\"},\"totalPage\":{\"type\":\"number\",\"description\":\"总页码\"},\"totalCount\":{\"type\":\"number\",\"description\":\"总个数\"},\"list|2\":{\"type\":\"array\",\"items\":{\"type\":\"object\",\"properties\":{\"id\":{\"type\":\"number\",\"description\":\"专题id\"},\"name\":{\"type\":\"string\",\"description\":\"专题名称\"}}}},\"currPage\":{\"type\":\"number\",\"description\":\"当前第几页\"}}}}}"}"""
    print(json.loads(data))


if __name__ == "__main__":
    main()
