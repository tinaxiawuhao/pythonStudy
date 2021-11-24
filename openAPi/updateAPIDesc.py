# !-_-! coding=utf8 !-_-!
import pymysql
import xlwings as xws


class Config:
    apis = "./file/test1.xlsx"


# 打开数据库连接，不指定数据库
conn = pymysql.connect(host="10.206.97.227", port=3329, user="app", passwd="V)4r28d4pRg-AEHa")
# conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456")
conn.select_db('ag_admin')
# 获取游标
cursor = conn.cursor()
# 修改语句
sql_update = "UPDATE ag_api SET description = %s WHERE idApi = %s"

results = []
des = []
des_add = []


def close_mysql():
    cursor.close()
    conn.close()
    print('sql执行成功')


# 读取文件
def desc_reader():
    # 创建应用
    # app = xws.App(visible=True, add_book=False)
    # 打开eapis数据表读取20210316的数据
    # wb = app.books.open(Config.eapis)
    wb = xws.Book(Config.apis)
    sheet = wb.sheets["sheet1"]
    # 读取全部数据
    list_value = sheet.range('A1:C8016').value
    for i in range(len(list_value)):
        # 插入数据
        value1 = list_value[i][0].strip()
        value2 = list_value[i][1].strip()
        value3 = str(list_value[i][2])
        try:
            # 执行SQL语句
            update_data = (value2 + "--开发者:" + str(value3), value1)
            cursor.execute(sql_update, update_data)
            # 提交到数据库执行
            conn.commit()
        except:
            # 发生错误时回滚
            conn.rollback()
        print("修改完成" + str(i))
    # 打开了就要关闭
    wb.close()
    # app.quit()


def main():
    # 读取desc文件
    desc_reader()
    close_mysql()


if __name__ == "__main__":
    main()
