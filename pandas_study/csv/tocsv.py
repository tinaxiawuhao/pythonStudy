import pandas as pd

data = {'Name': ['Smith', 'Parker'], 'ID': [101, 102], 'Language': ['Python', 'JavaScript']} 
info = pd.DataFrame(data) 
print('DataFrame Values:\n', info) 

#转换为csv数据
csv_data = info.to_csv() 
print('\nCSV String Values:\n', csv_data) 

# 保存csv文件
csv_data = info.to_csv("pandas_study/csv/pandas.csv",sep='|')