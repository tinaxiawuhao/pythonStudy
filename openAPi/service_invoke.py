# !-_-! coding=utf8 !-_-!

import time
import math
import random
import datetime
import calendar
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

'''
目的: 累计增加日调用数，得到微服务调用次数稳步增长的每日调用数据及曲线
start: 16352273
to: 20028329
avg:
    1、9月：日调用量平均3.2w
    2、10月：月调用量平均3.5w
    3、11月，月调用量平均3.8w
    4、12月，月调用量平均4.2w
'''


def getBetweenDay(month, year=2021, begin_date=None):
    date_list = []
    if begin_date:
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    else:
        begin_date = datetime.datetime(year,month,day=1)
    end_date = datetime.datetime(year, month, day=calendar.monthrange(year,month)[1])
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


def randoms_genner():
    d1 = np.random.randint(-300, -100, 10)
    d2 = np.random.randint(100, 300, 10)
    nums = []
    for i in d1: nums.append(i)
    for i in d2: nums.append(i)
    return nums


def do_random(avgs, dates, low, high):
    arrs = []
    result = dict()
    for k in dates:
        v = avgs * random.uniform(low, high)
        result[k] = math.ceil(v)
        arrs.append(math.ceil(v))
    return arrs


def hui_zong(a1, a2):
    for a in a2:
        a1.append(a)
    return a1


def gen_month(avgs, dates, low=None, high=None):
    date_lens = len(dates)
    # 方案1
    date1 = dates[: date_lens // 3]
    date2 = dates[date_lens // 3: date_lens // 3 + date_lens // 3]
    date3 = dates[date_lens // 3 + date_lens // 3:]
    arr1 = do_random(avgs, date1, 0.95, 1.03)
    arr2 = do_random(avgs, date2, 0.96, 1.07)
    arr3 = do_random(avgs, date3, 0.98, 1.10)
    arr = []
    arr = hui_zong(arr, arr1)
    arr = hui_zong(arr, arr2)
    arr = hui_zong(arr, arr3)
    t = 0
    for i in arr:
        t += i

    # 方案2
    # avgs = 37398
    #
    # arr = do_random(avgs, dates, low, high)


    # arr = hui_zong(arr, arr3)
    t = 0
    for i in arr:
        t += i

    print("月份: {}, 日平均调用: {}".format(dates[0].split("-")[1], t//len(dates)))
    return arr


def month():
    pass


def main(start, avg, m):
    times_start = start

    avg_12 = avg * 1000

    dates_12 = getBetweenDay(m)

    nums12 = gen_month(avg_12, dates_12)


    x = []
    x = hui_zong(x, dates_12)

    y = []
    y = hui_zong(y, nums12)

    plt.rcParams['savefig.dpi'] = 500  # 图片像素
    plt.rcParams['figure.dpi'] = 500  # 分辨率

    newy = []
    for index, value in enumerate(y):
        if index == 0:
            newy.append(value)
            continue
        if abs(y[index] - y[index-1]) < 800:
            continue
        if abs(y[index] - y[index-1]) >= 800 and abs(y[index] - y[index-1]) < 1500:
            if y[index] > y[index-1]:
                y[index] = y[index] - 800
            else:
                y[index] = y[index] + 800
        elif abs(y[index] - y[index-1]) >= 1500:
            if y[index] > y[index-1]:
                y[index] = y[index] - 1200
            else:
                y[index] = y[index] + 1200



    # plt.plot(x, y)
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y)
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    plt.xlabel("日期")
    plt.ylabel("日调用量")
    plt.xticks(rotation=270)

    plt.show()

    cha = []
    for i, v in enumerate(y):
        if i == 0:
            cha.append(0)
        if i == len(y)-1:
            break
        cha.append(y[i+1] - v)

    print("调用量每日较前一日波动:",cha)
    print("每日实际调用量: ", y)
    print(x)


if __name__ == "__main__":
    start, avg, m = 25441304, 43, 5
    start, avg, m = 26794973, 42, 6
    start, avg, m = 28066189, 41.5, 7
    start, avg, m = 29364987, 41, 8

    main(start, avg, m)
