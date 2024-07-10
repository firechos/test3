import pandas as pd
import matplotlib.pyplot as plt

file_path = '4月.xlsx'  
df = pd.read_excel(file_path)

columns_to_plot = ['产量','切割','毛刺','开孔','上色','挂链','合模']

for column in columns_to_plot:
    
    plt.figure()
    df[column].plot(kind='hist', bins=20, edgecolor='black', title=f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    
    image_path = f'{column}_histogram.png'
    plt.savefig(image_path)
    plt.close()
