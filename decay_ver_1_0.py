# 这是用来处理寿命衰减曲线的代码

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 首先输入文件夹所在路径
lifetime_folder = Path(r'E:\1_TTM闪烁体\TTM自由基X衍射成像\文章\文章数据\寿命')
file = lifetime_folder/'A-740nm.dat'
# 文件预处理
# 删除前两行，然后插入列名lifetime\tcounts
with file.open() as f:
    lines = f.readlines()
lines = lines[2:]
lines.insert(0,f'lifetime\tcounts\n')
out_path = file.parent/f'df_{file.stem}.txt'
out_path.touch()
with out_path.open('w') as f:
    for row in lines:
        f.write(row)
decay_data = pd.read_csv(out_path,sep='\t',encoding = 'gbk', engine='python')
x = decay_data.iloc[:,0] * (10**6)
y = decay_data.iloc[:,1]

plt.semilogy(x,y)   

