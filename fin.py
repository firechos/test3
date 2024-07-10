import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '4月.xlsx'
df = pd.read_excel(file_path, header=None, skiprows=1, nrows=30)

means = df.mean(axis=1)
std_devs = df.std(axis=1, ddof=1)

grand_mean = means.mean()
mean_devs = std_devs.mean()
UCL_Xbar = grand_mean + 3 * (mean_devs / np.sqrt(df.shape[1]))
LCL_Xbar = grand_mean - 3 * (mean_devs / np.sqrt(df.shape[1]))

UCL_R = mean_devs * 2.114
LCL_R = 0

plt.figure(figsize=(12, 6))
plt.plot(means, marker='o', linestyle='-', color='b')
plt.axhline(grand_mean, color='r', linestyle='--')
plt.axhline(UCL_Xbar, color='g', linestyle='--')
plt.axhline(LCL_Xbar, color='g', linestyle='--')
plt.title('均值控制图')
plt.xlabel('指数')
plt.ylabel('均值')
plt.savefig('均值控制图.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(std_devs, marker='o', linestyle='-', color='b')
plt.axhline(mean_devs, color='r', linestyle='--')
plt.axhline(UCL_R, color='g', linestyle='--')
plt.axhline(LCL_R, color='g', linestyle='--')
plt.title('方差控制图')
plt.xlabel('指数')
plt.ylabel('标准差')
plt.savefig('方差控制图.png')
plt.show()
