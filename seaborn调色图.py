import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']#让中文的地方显示出来

#读取文件
df = pd.read_excel(r'C:/Users/dawei/Desktop/2.xlsx')
df.head()

#计算相关性系数
df_coor=df.corr()
df_coor.head()

# 设置画布大小，分辨率，和底色
plt.subplots(figsize=(9,9),dpi=1080,facecolor='w')

#annot为热力图上显示数据；fmt='.2f'为数据保留两位有效数字,square呈现正方形，vmax最大值为1
#cmap是改变色块的颜色，可以用的颜色代码见：https://matplotlib.org/3.3.3/tutorials/colors/colormaps.html
fig=sns.heatmap(df_coor,annot=True, vmax=1, square=True, cmap="RdBu", fmt='.2f')

fig


#以下步骤是加一个遮罩，在图片上去掉重复的相关系数，只显示一半的图片

# Compute the correlation matrix
corr = df.corr()

# Generate a custom colorma
cmap="RdBu"

# Generate a masking matrix
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Plot the heatmap
sns.heatmap(corr, mask=mask, cmap=cmap, annot=True, fmt='.2f', square=True)

# Show the plot
plt.show()




