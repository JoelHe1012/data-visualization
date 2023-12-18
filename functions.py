# 将绘制吸收光谱的代码写成一个函数
# 该函数要实现以下功能：
# 导入一个包含紫外吸收光谱数据文件的路径，然后对该目录下所有的txt文件作图（一个路径参数）
# 为方便和不同的图片组合，因此还需要一个坐标轴参数
# 坐标轴范围应该是可调的，因此需要两个元组作为参数传进去
# 该函数仅仅用来绘制紫外可见吸收光谱，因此，其他部分应该是固定的

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# 定义绘制吸收光谱的函数
def abs_plot(path,axes,xlim,ylim):
    '''
    1.用来绘制紫外可见吸收光谱，可以把一个文件目录下所有txt格式的文件绘制成紫外可见吸收光谱
    2.所有的折线都在同一坐标轴下面
    :param path: 路径
    :param axes: 坐标轴
    :param xlim: x轴范围
    :param ylim: y轴范围
    :return: 返回一张图
    '''
# 首先进行文件的预处理，将文件修改为我们想要的格式
    folder_path = Path(path) # 获取要处理的文件所在文件夹的路径
    files = list(folder_path.glob('*.txt')) #获取该文件夹下所有的txt格式的文件，并以它们的路径为值创建list
    for file in files:
        with file.open() as f:
            lines = f.readlines() # 打开文件，依行读取文件
        lines = lines[2:] #切片，删除前两行
        lines.insert(0,f'Wavelength,{file.stem}/n') # 将文件名加到首行,此处应用.insert(index,str)插入
        out_path = file.parent/f'df_{file.stem}.txt' # 创建一个新的路径对象
        out_path.touch() #按上面的路径，创建一个新的文档
        with out_path.open(mode = 'w') as f: # 打开新的空文档
            for row in lines:
                f.write(f'{row}\n') # 将处理好的文档依次写入新文档中
    # 下面的代码将对数据进行处理
    df_files = list(folder_path.glob('df_*.txt'))
    for file in df_files:
        abs_data = pd.read_csv(file, sep = ',', encoding = 'gbk')
        x = abs_data.iloc[:,0]
        y = abs_data.iloc[:,1]
        axes.plot(x,y,label = file.stem[3:],linestyle = '--',linewidth = '3')
        print('画图完成')
    # # 画好图后对相关格式进行统一修改，因为是公用一个坐标
    axes.set_xlabel('Wavelength (nm)',fontsize=18)
    axes.set_ylabel('Extinction coefficient\n(10$^{{\scr 4}}$M$^{{\scr -1}}$cm$^{{\scr -1}}$)',fontsize=16)
    axes.set_title(None)
    axes.legend(frameon=False , prop={'size': 18})    # 添加图标，说明每个折现对应什么
    axes.grid(False)
    axes.set_xlim(xlim)  # 设置 x 轴范围为 100 到 300
    axes.set_ylim(ylim)      # 设置 y 轴范围为 0 到 1
    axes.spines[:].set_linewidth(3)
    axes.tick_params(axis='both', which='major', width=2)
    # # 设置横坐标和纵坐标的刻度值为粗体
    for label in axes.get_xticklabels() + axes.get_yticklabels():
        label.set_fontsize(16)
    # 最后，删除新创建的df_*.txt文件，如不删除，会产生大量的重复文件
    for file_to_delete in df_files:
        file_to_delete.unlink()
        print(f"{file_to_delete} 已被删除。")


