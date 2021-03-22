import xlrd, xlwt, re


class Config:
    eapis = "./file/apis.xlsx"
    eurls = "./file/url.xlsx"
    edoc = "./file/result.xls"
    vurl = "虚拟url"
    rurl = "真实url"


class Result:
    rapis = dict()
    rurls = dict()
    rtitle = list()


result = Result()


def api_reader():
    apis_book = xlrd.open_workbook(Config.eapis)
    apis_sheet = apis_book.sheet_by_name("20210316")

    result.rtitle = apis_sheet.row_values(0)
    row_len = apis_sheet.nrows
    for i in range(1, row_len):
        row = apis_sheet.row_values(i)
        if not row:
            continue
        item = {
            row[0]: {
                1: row[1],
                2: row[2],
                3: row[3],
                4: row[4]
            }
        }
        if result.rapis.get(row[0]):
            print(row)
        else:
            result.rapis.update(item)


def url_reader(kword, kword2):
    urls_book = xlrd.open_workbook(Config.eurls)
    urls_sheet = urls_book.sheet_by_index(0)

    result.rtitle.append(kword)
    result.rtitle.append(kword2)
    row_len = urls_sheet.nrows
    for i in range(0, row_len):
        row = urls_sheet.row_values(i)
        if not row:
            continue
        # 对真实url进行json解析
        data = jsonParsing(row[2])
        item = {
            row[0]: {
                1: row[1],
                2: data
            }
        }
        if result.rurls.get(row[0]):
            print(row)
        else:
            result.rurls.update(item)


def jsonParsing(text):
    data = re.findall(r'path\\{0,3}\":\\{0,3}\"([\/\w*\-\_\{\}]*)', text)
    return data


def merge(result_file):
    book = xlwt.Workbook()
    sheet = book.add_sheet('20210318')

    for i in range(len(result.rtitle)):
        sheet.write(0, i, result.rtitle[i])

    n = 1
    for k, value in result.rurls.items():
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

        for index in range(len(datas)):
            sheet.write(n, index, datas[index])
        n += 1

    book.save(result_file)


if __name__ == "__main__":
    api_reader()
    url_reader(Config.vurl, Config.rurl)
    merge(Config.edoc)
