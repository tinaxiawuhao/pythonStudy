import numpy as np
from matplotlib import pyplot as plt
import matplotlib

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.show()

 
# fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径，size 参数设置字体大小
zhfont1 = matplotlib.font_manager.FontProperties(fname="fonts/simkai.ttf", size=18)
font1 = {'color':'blue','size':20}
font2 = {'color':'darkred','size':15}
x = np.arange(1,11)
y =  2  * x +  5

# fontdict 可以使用 css 来设置字体样式
plt.title("20240524 - 测试", fontproperties=zhfont1, fontdict = font1, loc="left")
 
# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x 轴", fontproperties=zhfont1, loc="left")
plt.ylabel("y 轴", fontproperties=zhfont1, loc="top")
# 绘图标记
#plt.plot(x,y)
plt.plot(y, 'o:r',ms = 20, mec = 'y',mfc = '#4CAF50')
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
# 网格线
plt.grid() 
#plt.grid(axis='x') # 设置就在y轴方向显示网格线
#plt.grid(color = 'r', linestyle = '--', linewidth = 0.5)
plt.show()