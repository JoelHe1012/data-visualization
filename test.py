import matplotlib.pyplot as plt
# import pandas as pd
# from pathlib import Path

from functions import abs_plot

fig = plt.figure(figsize = (16,10))
ax = fig.add_subplot(2,2,1)
abs_plot(r'E:\01_课题\02_TTM3RCz系列分子的合成与表征\原始数据\20230508abs',ax,(300,700),(0,0.5))
plt.show()