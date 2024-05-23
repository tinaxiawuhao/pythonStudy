import pandas as pd

#创建DataFrame数据
info_website = pd.DataFrame({'name': ['编程狮', 'W3Cschool', '微学苑', '92python'],
     'rank': [1, 2, 3, 4],
     'language': ['PHP', 'C', 'PHP','Python' ],
     'url': ['w3cschool.cn', 'm.w3cschool.cn', 'www.weixueyuan.com','www.92python.com' ]})

# 创建ExcelWriter对象
with pd.ExcelWriter('pandas_study/result/website.xlsx', engine='openpyxl') as writer:
    info_website.to_excel(writer, sheet_name='Sheet1', index=False)
    print('输出成功')
    


