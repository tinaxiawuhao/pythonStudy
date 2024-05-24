import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#创建包含时间序列的数据
df = pd.DataFrame(np.random.randn(8,4),index=pd.date_range('2/1/2020',periods=8), columns=list('ABCD'))
#柱状图：bar() 或 barh()
#直方图：hist()
#箱状箱：box()
#区域图：area()
#散点图：scatter()
#通过关键字参数kind可以把上述方法传递给 plot()。
df.plot(kind='box')
# 当使用 Pandas 的 DataFrame.plot() 方法时，默认情况下会使用 Matplotlib 库来生成图形。
plt.show()
