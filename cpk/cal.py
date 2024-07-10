import os

# 定义cpk的阈值
good_threshold = 1.0
excellent_threshold = 1.67

# 遍历文件夹中的所有txt文件
folder_path =  os.getcwd();
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # 假设cpk值在txt文件的特定行（例如倒数第二行）
        cpk_line = lines[-1].strip()  # 修改这里以匹配实际情况
        cpk_value = float(cpk_line.split(':')[1])  # 假设cpk值以"cpk=值"的形式存在
        
        # 根据cpk值分类
        if cpk_value >= excellent_threshold:
            result = '优秀'
        elif cpk_value >= good_threshold:
            result = '良好'
        else:
            result = '中等'
        
        # 将结果写入txt文件的最后一行
        with open(file_path, 'a') as file:
            file.write(f'/n评估结果: {result}')

print('处理完成')
