import pandas as pd
import os

#4. 统计样本总量、正样本量、取出每个文件的前10
path = "D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_pred/Result/GBM" ###1111#####
dirs = os.listdir(path)

total_sample = 0
pos_sample = 0
valid_file = pd.DataFrame({"Unnamed: 0":[],"D_r":[],"D_c":[],"T_r":[],"T_c":[],"S_r":[],"S_c":[],"SMILES":[],"name_list":[],"DrugEmbedding":[],"TargetEmbedding":[],"predict_score":[]})

for f in dirs:
    print(f)
    file_in = pd.read_csv(path + "/" + f)

    # 样本总量
    n = file_in.shape[0]
    total_sample = total_sample + n

    #正样本量
    count = 0
    predict_score = file_in["predict_score"].tolist()
    for i in range(n):
        if float(predict_score[i]) > 0.5:
            count = count + 1
        else:
            break
    pos_sample = pos_sample + count

print(total_sample)
print(pos_sample)