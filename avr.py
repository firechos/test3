import pandas as pd

pd.options.display.float_format = '{:.4f}'.format

file_path = '4月.xlsx'  
df = pd.read_excel(file_path)

mean_values = df.iloc[1:31, :].mean()
range_values = df.iloc[1:31, :].max() - df.iloc[1:31, :].min()
variance_values = df.iloc[1:31, :].var()

result = pd.DataFrame({
    '平均值': mean_values,
    '极差': range_values,
    '方差': variance_values
}).round(4)

output_file = 'task1.xlsx'
result.to_excel(output_file, index=False)
