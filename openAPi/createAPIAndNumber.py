'''插入多条数据'''
import pymysql
import xlwings as xws
import uuid
import random
import datetime


# 速度很慢，没有成功结束
# 写入数据
# def xw_wirte():
#     # 应用方法 创建应用-工作簿-工作表-范围
#     # add_book属性表示操作excel时是否新增一个excel文件，默认为true表示添加
#     # 创建应用 visible操作过程是否显示
#     app = xws.App(visible=False, add_book=True)
#     # 工作簿
#     wb = app.books.add()
#     # 工作表(不能使用中文命名)
#     sht = wb.sheets["sheet1"]
#     # 范围（插入数据）options(transpose=True)竖着插入插入一列的两种方式
#     sht.range("a1").options(transpose=True).value = ["xlwings", "hello", "world", "beauteful", "friend"]
#     sht.range("b1").value = [[1], [2], [3], [4], [5]]
#     # 插入一行的两种方式
#     sht.range('A1').value = [1, 2, 3, 4, 5]
#     sht.range('A1').options(transpose=True).value = [[1], [2], [3], [4], [5]]
#
#     # 关闭excel 保存excel
#     wb.save("demo01.xlsx")
#     wb.close()
#     app.quit()


class Config:
    apis = "./file/test.xlsx"


# 打开数据库连接，不指定数据库
conn = pymysql.connect(host="10.206.97.227", port=3329, user="app", passwd="V)4r28d4pRg-AEHa")
# conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456")
conn.select_db('ag_admin')
# 获取游标
cur = conn.cursor()
# 另一种插入数据的方式，通过字符串传入值
sql = "INSERT INTO `ag_admin`.`ag_api`(`idApi`, `idTenant`, `idApiGroup`, `name`, `apiProtocol`, `path`, `httpMethod`, `description`, `parameter`, `paramDesc`, `hystrixConfig`, `logConfig`, `reqMediaType`, `procDef`, `remarks`, `code`, `version`, `timeout`, `available`, `cache`, `apiStatus`, `implMethod`, `releaseTime`, `accessLevel`, `pic`, `idDubboService`, `accessTimes`, `discard`, `envNo`, `owner`, `authMethod`, `authKey`, `createBy`, `createTime`, `updateBy`, `updateTime`, `storeStatus`, `publishType`, `approvalStatus`, `approvalRemark`) VALUES (%s, '7baf118f-5fc8-4e36-b93b-50f97fa96731', '3aceb073-0be3-4791-9399-39a9f359e2e3', %s, 'https', '/Z0HRBQ81/cloudapi/service/daily/qrcode/create/{content}', '[\"GET\"]', %s, '[{\"name\":\"content\",\"defaultValue\":\"\\\"\\\"\",\"required\":true,\"description\":\"文本或链接，格式举例 ： baidu.com\",\"paramPos\":\"PATH_PARAM\",\"type\":\"STRING\"}]', '[{\"name\":\"content\",\"defaultValue\":\"\\\"\\\"\",\"required\":true,\"description\":\"文本或链接，格式举例 ： baidu.com\",\"paramPos\":\"PATH_PARAM\",\"type\":\"STRING\"}]', '{\"circuitBreakerSleepWindowInMilliseconds\":5000,\"circuitBreakerErrorThresholdPercentage\":50,\"circuitBreakerRequestVolumeThreshold\":20}', '{\"withFullLog\":false,\"serverAddress\":\"http://127.0.0.1:8066/cfl/saveCmptFullLog\",\"connectTimeout\":2,\"queueSize\":100}', '', '{\"diagram\":{},\"process\":{\"aggregationGateways\":[],\"cmpts\":[{\"breakPoint\":false,\"customForm\":\"{\\\"timeout\\\":2000,\\\"mock\\\":true,\\\"implMethod\\\":\\\"restful\\\",\\\"serviceRes\\\":\\\"PROXY\\\",\\\"parameter\\\":\\\"{\\\\\\\"mappingParamDTOs\\\\\\\":[{\\\\\\\"bkdName\\\\\\\":\\\\\\\"content\\\\\\\",\\\\\\\"bkdParamPos\\\\\\\":\\\\\\\"PATH_PARAM\\\\\\\",\\\\\\\"defaultValue\\\\\\\":\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\\\\\\\\\"\\\\\\\",\\\\\\\"description\\\\\\\":\\\\\\\"文本或链接，格式举例 ： baidu.com\\\\\\\",\\\\\\\"name\\\\\\\":\\\\\\\"content\\\\\\\",\\\\\\\"paramPos\\\\\\\":\\\\\\\"PATH_PARAM\\\\\\\",\\\\\\\"required\\\\\\\":true,\\\\\\\"type\\\\\\\":\\\\\\\"STRING\\\\\\\"}],\\\\\\\"constParamDTOs\\\\\\\":[],\\\\\\\"customParamDTOs\\\\\\\":[]}\\\",\\\"name\\\":\\\"后端服务-NQNGIK\\\",\\\"code\\\":\\\"NQNGIK\\\",\\\"address\\\":\\\"[{\\\\\\\"address\\\\\\\":\\\\\\\"10.138.130.1\\\\\\\",\\\\\\\"port\\\\\\\":\\\\\\\"32015\\\\\\\",\\\\\\\"available\\\\\\\":true}]\\\",\\\"reqMediaType\\\":\\\"pass_through\\\",\\\"backendDetail\\\":\\\"{\\\\\\\"protocol\\\\\\\":\\\\\\\"http\\\\\\\",\\\\\\\"path\\\\\\\":\\\\\\\"/cloudapi/service/daily/qrcode/create/{content}\\\\\\\",\\\\\\\"httpMethod\\\\\\\":\\\\\\\"[\\\\\\\\\\\\\\\"GET\\\\\\\\\\\\\\\"]\\\\\\\"}\\\",\\\"apiReturn\\\":{\\\"mediaType\\\":\\\"pass_through\\\",\\\"example\\\":\\\"{ \\\\\\\"code\\\\\\\": 200, \\\\\\\"data\\\\\\\": success, \\\\\\\"msg\\\\\\\": \\\\\\\"数据调用成功\\\\\\\" }\\\",\\\"errMsg\\\":\\\"{ \\\\\\\"code\\\\\\\": 500, \\\\\\\"data\\\\\\\": fail, \\\\\\\"msg\\\\\\\": \\\\\\\"数据调用失败\\\\\\\" }\\\",\\\"backToClient\\\":true}}\",\"extraParas\":[{\"defaultValue\":\"0\",\"name\":\"retryCount\",\"description\":\"其值范围为0~2，默认为0，该值大于0且请求上游服务失败，系统将重新发起请求直到成功或者最大重试次数。\",\"title\":\"失败重试次数\",\"fieldType\":\"INTEGER\",\"regExp\":\"/^[0-2]$/\",\"required\":true},{\"defaultValue\":\"0\",\"name\":\"routeTimeout\",\"description\":\"路由组件执行超时时间（单位毫秒），默认为0，范围0~60000，该值大于0则采用该超时时间配置，如等于0则使用api的超时时间配置。\",\"title\":\"路由超时时间\",\"fieldType\":\"INTEGER\",\"regExp\":\"/^[1-5][0-9]{0,4}$|^0$|^60000$/\",\"required\":true}],\"id\":\"cmpt.node-AYM5D\",\"idCmptDef\":\"12294edb-e0ff-4c1b-b77f-ad0d1710f3a0\",\"name\":\"Restful路由组件\"},{\"breakPoint\":false,\"customForm\":\"{}\",\"extraParas\":[{\"defaultValue\":\"30\",\"name\":\"tokenExpireTime\",\"description\":\"配置Token认证过期时间,单位分钟\",\"title\":\"认证过期时间\",\"fieldType\":\"INTEGER\",\"regExp\":\"/^\\\\+?[1-9][0-9]*$/;\",\"required\":true}],\"id\":\"cmpt.node-3OURF\",\"idCmptDef\":\"d482c962-86db-4618-8790-2c1be532491c\",\"name\":\"JWT认证组件\"},{\"breakPoint\":false,\"customForm\":\"{}\",\"extraParas\":[],\"id\":\"cmpt.node-3EUNT\",\"idCmptDef\":\"f7898507-6e50-4c78-bad4-7d15c4a0e0ec\",\"name\":\"基于角色的鉴权组件\"}],\"endEvent\":{\"id\":\"end.node-249RA\"},\"parallelGateways\":[],\"scripts\":[],\"sequenceFlows\":[{\"conditionExpression\":\"\",\"id\":\"link.node-XWO3V\",\"name\":\"\",\"sourceRefId\":\"start.node-RCULZ\",\"targetRefId\":\"cmpt.node-3OURF\"},{\"conditionExpression\":\"\",\"id\":\"link.node-HHBAP\",\"name\":\"\",\"sourceRefId\":\"cmpt.node-3OURF\",\"targetRefId\":\"cmpt.node-3EUNT\"},{\"conditionExpression\":\"\",\"id\":\"link.node-NVI51\",\"name\":\"\",\"sourceRefId\":\"cmpt.node-3EUNT\",\"targetRefId\":\"cmpt.node-AYM5D\"},{\"conditionExpression\":\"\",\"id\":\"link.node-KBKTK\",\"name\":\"\",\"sourceRefId\":\"cmpt.node-AYM5D\",\"targetRefId\":\"end.node-249RA\"}],\"startEvent\":{\"id\":\"start.node-RCULZ\"}}}', '发布', 'c8522561bb424a4087c1790bf961842c', 1.1, 2000, 1, 0, 'published', 'restful', '2021-06-22 12:26:02', 'open', NULL, NULL, 00000000000000000000, 0, 1, '8af1aa1b-8600-491d-b232-96226f51a598', 'md5', 'C4F1BAC2D6CFF79247229D3C9BE26712', '8af1aa1b-8600-491d-b232-96226f51a598', '2021-06-01 12:24:43', '8af1aa1b-8600-491d-b232-96226f51a598', '2021-06-01 12:26:02', 'ready', 3, 0, NULL);"

conn2 = pymysql.connect(host="10.206.97.227", port=3329, user="app", passwd="V)4r28d4pRg-AEHa")
# conn2 = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456")
conn2.select_db('ag_monitor')
# 获取游标
cur2 = conn2.cursor()
sql2 = "INSERT INTO `ag_monitor`.`ag_cmpt_log`(`idLog`, `idTenant`, `idApi`, `idApiGroup`, `logTime`, `succeedCount`, `errorCount`, `totalReqSize`, `totalRespSize`, `avgGatewayTime`, `avgRouteTime`, `createTime`, `countSign`) VALUES (%s, '7baf118f-5fc8-4e36-b93b-50f97fa96731', %s, '3aceb073-0be3-4791-9399-39a9f359e2e3', %s, %s, %s, 546, 0, 0, 0, %s, b'1');"


def close_mysql():
    cur.close()
    cur2.close()
    conn.close()
    conn2.close()
    print('sql执行成功')


# 读取文件
def api_reader():
    # 创建应用
    # app = xws.App(visible=True, add_book=False)
    # 打开eapis数据表读取20210316的数据
    # wb = app.books.open(Config.eapis)
    wb = xws.Book(Config.apis)
    sheet = wb.sheets["sheet1"]
    # 读取全部数据
    list_value = sheet.range('A2:B8017').value
    number = 0
    logTime = datetime.datetime.now()
    logTime = (logTime + datetime.timedelta(days=4))
    idApis=[]
    for index in range(24):
        list = []
        time=logTime.strftime("%Y_%m_%d_%H_%M_%S")
        for i in range(len(list_value)):
            if (index == 0):
                # 插入数据
                value1=list_value[i][0].strip()
                value2=list_value[i][1].strip()
                if (len(value1) != 0 and len(value2) != 0):
                    # 添加api
                    idApi = str(uuid.uuid1())
                    idApis.append(idApi)
                    cur.execute(sql, (idApi, value1, value2))
            if(i >= 0 and i<100):
                tmp = (idApis[i] + "+" + time, idApis[i], time, random.randint(1, 4000), random.randint(0, 3), time)
            else:
                tmp = (idApis[i] + "+" + time, idApis[i], time, random.randint(1, 10), random.randint(0, 3), time)
            list.append(tmp)


        cur2.executemany(sql2, list)
        conn.commit()
        conn2.commit()
        logTime = (logTime + datetime.timedelta(days=-1))
        number = number + 1
        print("操作成功数" + str(number))

    # 打开了就要关闭
    wb.close()
    # app.quit()


def main():
    # 读取api文件
    api_reader()
    close_mysql()


if __name__ == "__main__":
    main()
