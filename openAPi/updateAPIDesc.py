# !-_-! coding=utf8 !-_-!
import pymysql
import xlwings as xws


class Config:
    apis = "./file/test1.xlsx"


# 打开数据库连接，不指定数据库
# conn = pymysql.connect(host="10.206.97.227", port=3329, user="app", passwd="V)4r28d4pRg-AEHa")
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456")
conn.select_db('ag_admin')
# 获取游标
cur = conn.cursor()
# 查询语句
sql = "SELECT idApi,description FROM ag_api"

results =[]
des = []
des_add = []

def close_mysql():
    cur.close()
    conn.close()
    print('sql执行成功')

def select_api():
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        print("查询完成")
    except:
        print("Error: unable to fecth data")


# 读取文件
def desc_reader():
    # 创建应用
    # app = xws.App(visible=True, add_book=False)
    # 打开eapis数据表读取20210316的数据
    # wb = app.books.open(Config.eapis)
    wb = xws.Book(Config.apis)
    sheet = wb.sheets["sheet1"]
    # 读取全部数据
    list_value = sheet.range('A2:B8019').value


    # 打开了就要关闭
    wb.close()
    # app.quit()

def append_desc():
    # SQL 更新语句
    for api in results:
        sql = "UPDATE ag_api SET description = "".join(row[1].split()) + des_add WHERE idApi = api[0]"
        try:
            # 执行SQL语句
            cur.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 发生错误时回滚
            conn.rollback()
    print("插入完成")

def main():
    select_api()
    # 读取desc文件
    desc_reader()
    close_mysql()


if __name__ == "__main__":
    main()
