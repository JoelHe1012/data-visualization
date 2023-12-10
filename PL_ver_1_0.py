# 这段代码主要用来处理PL光谱
# 需求分析：
#   - 在作PL的时，我们需要将具有不同的x轴和y轴的曲线放在同一坐标系下面
#   - 需要对光谱的数据进行归一化
#   - 对初始版本的代码进行了优化，不再试图将所有的文件数据都整合到一个数据框中
#       而是用for循环，将每个文件数据直接作图

#导入需要的库
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from scipy.signal import find_peaks
import numpy as np

pl_folder_path = Path(r'path')
pl_files = list(pl_folder_path.glob('*.dx')) #获取该文件夹下所有的dx格式的文件，并以它们的路径为值创建list 
for file in pl_files:
    with file.open() as f:
        lines = f.readlines() # 打开文件，依行读取文件
    lines = lines[31:-1] #切片，删除前面的多行和最后一行
    lines.insert(0,f'{file.stem}_pl_Wavelength {file.stem}\n') # 将文件名加到首行,此处应用.insert(index,str)插入
    out_path = file.parent/f'df_{file.stem}.txt' # 创建一个新的路径对象
    out_path.touch() #按上面的路径，创建一个新的文档
    with out_path.open(mode = 'w') as f: # 打开新的空文档
        for row in lines:
            f.write(f'{row}') # 将处理好的文档依次写入新文档中
#以上，文件预处理完毕

# 下面的代码将对数据进行处理
df_pl_files = list(pl_folder_path.glob('df_*.txt')) # 会覆盖掉原来的变量，
pl_data_all =pd.DataFrame() #创建一个空的df
# 将文件夹下处理好的数据添加到数据框中
for file in df_pl_files:
    pl_data = pd.read_csv(file,sep=r'\s+', encoding = 'gbk') # 读取每个文件，然后创建一个临时DF
    pl_data['Normalized'] = (pl_data.iloc[:,1] - pl_data.iloc[:,1].min())/(pl_data.iloc[:,1].max() - pl_data.iloc[:,1].min()) #对发射强度归一化
    x = pl_data.iloc[:,0]
    y = pl_data['Normalized']
    peaks, _ = find_peaks(y, height=0.8)
    plt.plot(x,y,label = file.stem[3:])
     # 可以调整height参数以过滤掉较小的峰值
    
    print("Peaks found at positions:", x[peaks])
    # pl_data_all = pd.concat([pl_data_all,pl_data],axis=1) # 合并每个DF，得到数据,方便后续检查


# # 图片的完善与美化
# # 画好图后对相关格式进行统一修改，因为是公用一个坐标
plt.xlabel('Wavelength (nm)', fontweight='bold',fontsize=14)
plt.ylabel('Normalized PL Intensity\n(a. u.)', fontweight='bold',fontsize=16)
plt.title(None)
plt.legend(frameon=False , prop={'size': 16 ,'weight': 'bold'},loc = 'upper right') # 添加图标，说明每个折现对应什么
plt.grid(False)
plt.xlim(560, 820)  # 设置 x 轴范围为 100 到 300
plt.ylim(0, 1.3)      # 设置 y 轴范围为 0 到 1
# # 设置坐标轴的粗细
ax = plt.gca()
ax.spines['bottom'].set_linewidth(2)  # x 轴
ax.spines['left'].set_linewidth(2)    # y 轴
ax.spines['top'].set_linewidth(2)    # 上方坐标轴
ax.spines['right'].set_linewidth(2)  # 右侧坐标轴
ax.tick_params(axis='both', which='major', width=2) 
# # 设置横坐标和纵坐标的刻度值为粗体
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(16) 
# plt.show()


# # 这段代码用来输出新产生的df开头的文件
for file in df_pl_files:
    file.unlink()
