import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'E:\01_课题\01_TTM自由基X衍射成像\文章\文章数据\2_TTMCzP_Au_PSF_spetrum\film_ET.txt',sep = '\s+',encoding = 'gbk')
x = df.iloc[:,0]
y = df.iloc[:,1:]
plt.plot(x,y,label = df.columns[1:])
 # 画好图后对相关格式进行统一修改，因为是公用一个坐标
plt.xlabel('Wavelength (nm)', fontweight='bold',fontsize=16)
plt.ylabel('Extinction coefficient\n(10$^{{\scr 4}}$M$^{{\scr -1}}$cm$^{{\scr -1}}$)', fontweight='bold',fontsize=16)
# 设置图例位置
plt.legend(frameon=False , prop={'size': 14 ,'weight': 'bold'},loc = 'upper left') # 添加图标，说明每个折现对应什么
# 设置坐标轴范围
plt.xlim(350,900)  # 设置 x 轴范围为 100 到 300
plt.ylim(0,1.2)      # 设置 y1 轴范围为 0 到 2
# # 设置坐标轴的粗细
ax = plt.gca()
ax.spines['left'].set_linewidth(2)    # y 轴
ax.spines['top'].set_linewidth(2)    # 上方坐标轴
ax.spines['right'].set_linewidth(2)  # 右侧坐标轴
ax.tick_params(axis='both', which='major', width=2) 
# # 设置横坐标和纵坐标的刻度值为粗体
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(16) 

plt.show()