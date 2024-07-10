import pandas as pd
import numpy as np

file_path = '4月.xlsx'
sheet_name = 'Sheet1'
data_column = '合模'

df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=[data_column])
data = df[data_column].dropna()

mean = np.mean(data)
std_dev = np.std(data)

LSL = 0
USL = 5

cpk = min((mean - LSL) / (3 * std_dev), (USL - mean) / (3 * std_dev))

output_file = f'{data_column}_cpk.txt'

with open(output_file, 'w') as file:
    file.write(f'上限: {LSL:.4f}\n')
    file.write(f'下限: {USL:.4f}\n')
    file.write(f'Cpk: {cpk:.4f}\n')

