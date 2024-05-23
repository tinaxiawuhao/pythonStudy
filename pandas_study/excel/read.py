import pandas as pd
#读取excel数据
df = pd.read_excel('pandas_study/result/website.xlsx', engine='openpyxl')
# 遍历字典df的值，就可以观察所有读到的数据：
print(df.head())
