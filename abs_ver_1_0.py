# 这段代码主要用来将处理后的紫外可见吸收光谱的数据转换为图
# 这是关于紫外可见吸收光谱数据处理的第一个版本
# 唯一需要输入的地方是将文件夹路径赋值给folder_path
# Ver1_0版本说明：
# 基础功能：将一个文件下的所有的紫外可见吸收光谱的txt文件转换为图，所有的图都是共用一个坐标系

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# 首先进行文件的预处理，将文件修改为我们想要的格式
folder_path = Path(r'E:\test') # 输入要处理的文件所在文件夹的路径
files = list(folder_path.glob('*.txt')) #获取该文件夹下所有的txt格式的文件，并以它们的路径为值创建list

for file in files:
    with file.open() as f:
        lines = f.readlines() # 打开文件，依行读取文件
    lines = lines[2:] #切片，删除前两行
    lines.insert(0,f'Wavelength,{file.stem}') # 将文件名加到首行,此处应用.insert(index,str)插入
    out_path = file.parent/f'df_{file.stem}.txt' # 创建一个新的路径对象
    out_path.touch() #按上面的路径，创建一个新的文档
    with out_path.open(mode = 'w') as f: # 打开新的空文档
        for row in lines:
            f.write(f'{row}\n') # 将处理好的文档依次写入新文档中
#以上，文件预处理完毕

# 下面的代码将对数据进行处理
df_files = list(folder_path.glob('df_*.txt')) # 会覆盖掉原来的变量，
abs_data =pd.DataFrame() #创建一个空的df

# 将文件夹下处理好的数据添加到数据框中
for file in df_files:
    df = pd.read_csv(file, sep = ',', encoding = 'gbk') #读取每个文件，然后创建一个临时DF
    abs_data = pd.concat([abs_data,df],axis=1) # 合并每个DF，得到数据
abs_data = abs_data.loc[:,~abs_data.columns.duplicated()] #这个语法比较复杂，用来删除重复列
# 至此，数据处理完成

# 定义x与y轴，然后用for循环画图，所有的折线都公用一个坐标
x = abs_data['Wavelength']
# y1 = abs_data['Tp-Au-2']
# y2 = abs_data['TTM3PCz']
abs_intensity = abs_data.iloc[:,1:] #一个临时变量
for col in abs_intensity.columns:
    y = abs_intensity[col]
    plt.plot(x, y, marker=None, linestyle='-',linewidth=3, label = col) #对每个y轴进行作图
    
# 画图也可以选如下方式：
# 挨个指定y坐标，然后画图
# plt.plot(x, y1, marker=None, linestyle='-',linewidth=3, label = 'Tp-Au-2')
# plt.plot(x, y2, marker=None, linestyle='-',linewidth=3, label = 'TTM3PCz')

# 图片的完善与美化
# 画好图后对相关格式进行统一修改，因为是公用一个坐标
plt.xlabel('Wavelength (nm)', fontweight='bold',fontsize=16)
plt.ylabel('Absorption', fontweight='bold',fontsize=16)
plt.title(None)
plt.legend(frameon=False , prop={'size': 16 ,'weight': 'bold'}) # 添加图标，说明每个折现对应什么
plt.grid(False)
plt.xlim(350, 700)  # 设置 x 轴范围为 100 到 300
plt.ylim(0, 0.5)      # 设置 y 轴范围为 0 到 1
# 设置坐标轴的粗细
ax = plt.gca()
ax.spines['bottom'].set_linewidth(2)  # x 轴
ax.spines['left'].set_linewidth(2)    # y 轴
ax.spines['top'].set_linewidth(2)    # 上方坐标轴
ax.spines['right'].set_linewidth(2)  # 右侧坐标轴
ax.tick_params(axis='both', which='major', width=2) 
# 设置横坐标和纵坐标的刻度值为粗体
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(16)
# plt.show()
# 最后，删除新创建的df_*.txt文件，如不删除，会产生大量的重复文件
for file_to_delete in df_files:
    file_to_delete.unlink()
    print(f"{file_to_delete} 已被删除。")
# 至此，关于紫外可见吸收光谱的处理程序第一个版本完成
#  Congratulation !!!
            


