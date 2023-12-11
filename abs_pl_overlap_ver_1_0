# 这段代码主要用于同时在一个坐标系中同时画吸收和发射的光谱图
# 对于吸收光谱，一般不归一化
# 发射光谱需要归一化
# 需要双y轴，左边的轴为吸收、右边的为发射
# 对abs_ver_1_0的画图方式进行优化，用for循环来画图，而不是整合成一个df

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
# from cycler import cycler
# import matplotlib as mpl

# 首先进行文件的预处理，将文件修改为我们想要的格式
abs_folder_path = Path(r'E:\01_课题\01_TTM自由基X衍射成像\文章\文章数据\1_PSF_TTM3PCz_TSCTAu2_absPL_CHCl3\PSF_Au_TTM3PCz_abs_CHCl3') # 输入要处理的吸收光谱文件所在文件夹的路径
pl_folder_path = Path(r'E:\01_课题\01_TTM自由基X衍射成像\文章\文章数据\1_PSF_TTM3PCz_TSCTAu2_absPL_CHCl3\PSF_Au_TTM3PCz_PL_CHCl3') # 发射光谱所在的文件夹路径
abs_files = list(abs_folder_path.glob('*.txt')) #获取abs文件夹下所有的txt格式的文件，并以它们的路径为值创建list
pl_files = list(pl_folder_path.glob('*.dx')) #获取pl文件夹下所有的dx格式的文件，并以它们的路径为值创建list 

# 预处理abs的文件
for file in abs_files:
    with file.open() as f:
        lines = f.readlines() # 打开文件，依行读取文件
    lines = lines[2:] #切片，删除前两行
    lines.insert(0,f'Wavelength,{file.stem}\n') # 将文件名加到首行,此处应用.insert(index,str)插入
    out_path = file.parent/f'df_{file.stem}.txt' # 创建一个新的路径对象
    out_path.touch() #按上面的路径，创建一个新的文档
    with out_path.open(mode = 'w') as f: # 打开新的空文档
        for row in lines:
            f.write(f'{row}') # 将处理好的文档依次写入新文档中

# 预处理pl的文件
for file in pl_files:
    with file.open() as f:
        lines = f.readlines() # 打开文件，依行读取文件
    lines = lines[31:-1] #切片，删除前面的多行和最后一行
    lines.insert(0,f'{file.stem}_pl_Wavelength {file.stem}\n') # 将文件名加到首行,此处应用.insert(index,str)插入
    out_path = file.parent/f'df_{file.stem}.txt' # 创建一个新的路径对象
    out_path.touch() #按上面的路径，创建新的文档
    with out_path.open(mode = 'w') as f: # 打开新的空文档
        for row in lines:
            f.write(f'{row}') # 将处理好的文档依次写入新文档中
# 创建一个图片，并设置双y轴
fig,ax1 = plt.subplots(figsize = (8,6))
ax2 = ax1.twinx()

# 处理吸收光谱，画图
# 依次导入每个文件为df格式，并作图
df_abs_files = list(abs_folder_path.glob('df_*.txt')) # 获取文件加下所有以df_开头的文件，即处理好的文件
for file in df_abs_files:
    abs_data = pd.read_csv(file, sep = ',', encoding = 'gbk') #读取每个文件，然后创建一个临时DF
    x = abs_data.iloc[:,0]
    y = abs_data.iloc[:,1]
    ax1.plot(x,y,label = file.stem[3:],linestyle = '--',linewidth = '3')
    # abs_data = pd.concat([abs_data,df],axis=1) # 合并每个DF，得到数据，这个可选择用来检查数据

# 处理发射光谱
# 依次导入每个文件为df格式，并作图
df_pl_files = list(pl_folder_path.glob('df_*.txt')) # 会覆盖掉原来的变量，读取所有以df_开头的txt文件
for file in df_pl_files:
    pl_data = pd.read_csv(file,sep=r'\s+', encoding = 'gbk') # 读取每个文件，然后创建一个临时DF
    pl_data['Normalized'] = (pl_data.iloc[:,1] - pl_data.iloc[:,1].min())/(pl_data.iloc[:,1].max() - pl_data.iloc[:,1].min()) #对发射强度归一
    x = pl_data.iloc[:,0] # 获取x轴的值
    y = pl_data['Normalized'] # 获取y轴的值
    ax2.plot(x,y,label = file.stem[3:],linewidth = '3') # 作图

# # 图片的完善与美化
# 设置线条颜色

# # 画好图后对相关格式进行统一修改，因为是公用一个坐标
ax1.set_xlabel('Wavelength (nm)', fontweight='bold',fontsize=16)
ax1.set_ylabel('Extinction coefficient\n(10$^{{\scr 4}}$M$^{{\scr -1}}$cm$^{{\scr -1}}$)', fontweight='bold',fontsize=16)
ax2.set_ylabel('Normalized PL Intensity\n(a. u.)', fontweight='bold',fontsize=16)
# 设置图例位置
ax1.legend(frameon=False , prop={'size': 14 ,'weight': 'bold'},loc = 'upper center') # 添加图标，说明每个折现对应什么
ax2.legend(frameon=False , prop={'size': 14 ,'weight': 'bold'},loc = 'upper right')
# 设置坐标轴范围
ax1.set_xlim(300,900)  # 设置 x 轴范围为 100 到 300
ax1.set_ylim(0,2)      # 设置 y1 轴范围为 0 到 2
ax2.set_ylim(0,1.2)
# # 设置坐标轴的粗细
ax1.spines['bottom'].set_linewidth(2)  # x 轴
ax1.spines['left'].set_linewidth(2)    # y 轴
ax1.spines['top'].set_linewidth(2)    # 上方坐标轴
ax1.spines['right'].set_linewidth(2)  # 右侧坐标轴
ax1.tick_params(axis='both', which='major', width=2) 
# # 设置横坐标和纵坐标的刻度值为粗体
for label in ax1.get_xticklabels() + ax1.get_yticklabels() + ax2.get_yticklabels():
    label.set_fontweight('bold')
    label.set_fontsize(16) 

# # plt.show()

# #最后，删除产生处理数据所产生的临时文件
for file in df_abs_files:
    file.unlink()
for file in df_pl_files:
    file.unlink()
# # 至此，关于紫外可见吸收光谱的处理程序第一个版本完成
# #  Congratulation !!!
