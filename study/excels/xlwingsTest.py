import xlwings as xws
import re

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
    eapis = "./file/apis.xlsx"
    eurls = "./file/url.xlsx"
    # 可以写成具体的电脑路径（默认为py程序的目录生成）
    results = "./file/xlwingResult.xlsx"
    vurlTitle = "虚拟url"
    rurlTitle = "真实url"


class Result:
    rapis = dict()
    rurls = dict()
    rtitle = list()


result = Result()


# 读取文件
def api_reader():
    # 创建应用
    # app = xws.App(visible=True, add_book=False)
    # 打开eapis数据表读取20210316的数据
    # wb = app.books.open(Config.eapis)
    wb = xws.Book(Config.eapis)
    sheet = wb.sheets["20210316"]
    # 读取全部数据
    result.rtitle = sheet.range("a1:e1").value
    list_value = sheet.range('A2:E5101').value

    for i in range(len(list_value)):
        # 使用Python的类库直接访问Excel的表单是很缓慢的，不要在Python的循环中引用sheet等Excel表单的单元格，
        # 而是要用List一次性读取Excel里的数据，在List内存中计算好了，然后返回结果
        item = {
            list_value[i][0]: {
                1: list_value[i][1],
                2: list_value[i][2],
                3: list_value[i][3],
                4: list_value[i][4]
            }
        }
        if result.rapis.get(list_value[i][0]):
            print(list_value[i][0])
        else:
            result.rapis.update(item)

    # 打开了就要关闭
    wb.close()
    # app.quit()


# 读取文件
def url_reader(vurlTitle, rurlTitle):
    # 创建应用
    # app = xws.App(visible=True, add_book=False)
    # 打开eurls数据表读取20210318的数据
    # wb = app.books.open(Config.eurls)
    wb = xws.Book(Config.eurls)
    sheet = wb.sheets["20210318"]
    # 读取全部数据
    result.rtitle.append(vurlTitle)
    result.rtitle.append(rurlTitle)
    list_value = sheet.range('A1:c5294').value

    for i in range(len(list_value)):
        # 使用Python的类库直接访问Excel的表单是很缓慢的，不要在Python的循环中引用sheet等Excel表单的单元格，
        # 而是要用List一次性读取Excel里的数据，在List内存中计算好了，然后返回结果
        data = reParsing(list_value[i][2])
        item = {
            list_value[i][0]: {
                1: list_value[i][1],
                2: data,
            }
        }
        if result.rurls.get(list_value[i][0]):
            print(item)
        else:
            result.rurls.update(item)

    # 打开了就要关闭
    wb.close()
    # app.quit()


def reParsing(text):
    if text is not None:
        data = re.findall(r'path\\{0,3}\":\\{0,3}\"([\/\w*\-\_\{\}]*)', text)
        return data
    return text


# 合并写入数据
def merge(results):
    # 应用方法 创建应用-工作簿-工作表-范围
    # add_book属性表示操作excel时是否新增一个excel文件，默认为true表示添加
    # 创建应用 visible操作过程是否显示
    # app = xws.App(visible=True, add_book=True)
    # 工作簿
    # wb = app.books.add()
    wb = xws.Book()
    # 工作表(不能使用中文命名)
    sheet = wb.sheets["sheet1"]

    for i in range(len(result.rtitle)):
        sheet.range('A1: G1').value = result.rtitle

    n = 1
    for k, value in result.rurls.items():
        n += 1
        va = result.rapis.get(k)
        if not va:
            continue
        datas = [k]
        # 获取apis信息
        for vai in range(1, len(va.keys()) + 1):
            datas.append(va.get(vai))
        # 获取url信息
        for vai in range(1, len(value.keys()) + 1):
            datas.append(value.get(vai))
        number = 'A' + str(n) + ': G' + str(n)
        sheet.range(number).value = datas

    # 关闭excel 保存excel
    wb.save(results)
    wb.close()
    # app.quit()


def main():
    # 读取api文件
    api_reader()
    # 读取url文件
    url_reader(Config.vurlTitle, Config.rurlTitle)
    # 合并
    merge(Config.results)


if __name__ == "__main__":
    main()
