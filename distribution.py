import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

file_path = '4月.xlsx' 
sheet_name = 'Sheet1'
data_column = '产量'

df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=[data_column], skiprows=range(1, 2), nrows=30)
data = df[data_column].dropna()  

plt.figure(figsize=(10, 6))
stats.probplot(data, dist="norm", plot=plt)
plt.title('Distribution Map(?)')
plt.xlabel('Theoretical')
plt.ylabel('Reality')
plt.grid(True)
plt.savefig(f'{data_column}_plot.png')
# plt.show()
