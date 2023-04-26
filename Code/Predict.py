import pandas as pd
import os


#---------------------------------------------------------------------------------------------------

#1.两两组合得到所有药物对

# file_in = pd.read_csv("./Data/CancerDC/DrugComb/d1_filtered.csv")
# D_r = []
# D_c = []
# T_r = []
# T_c = []
# S_r = []
# S_c = []
# SMILES = []
# name_list = []
# n = file_in.shape[0]
# for i in range(n-1):
#     index_r = i
#     for j in range(n-i-1):
#         index_c = j+i+1
#         print(str(n) + "--" +str(index_r) + "--" + str(index_c))
#         n1 = file_in.iloc[index_r][0]
#         n2 = file_in.iloc[index_c][0]
#         D_r.append(n1)
#         D_c.append(n2)
#         T_r.append(file_in.iloc[index_r][1])
#         T_c.append(file_in.iloc[index_c][1])
#         s1 = file_in.iloc[index_r][3]
#         s2 = file_in.iloc[index_c][3]
#         S_r.append(s1)
#         S_c.append(s2)
#         SMILES.append(s1+"?"+s2)
#         if n1 < n2:
#             name = n1+n2
#         else:
#             name = n2+n1
#         name_list.append(name)


# file_out = pd.DataFrame({"D_r":D_r,"D_c":D_c,"T_r":T_r,"T_c":T_c,"S_r":S_r,"S_c":S_c,"SMILES":SMILES,"name_list":name_list})

# file_out.to_csv("./Data/CancerDC/DrugComb/all_dpairs.csv",index=False)




#---------------------------------------------------------------------------------------------------

#2.拆文件
# file_in = pd.read_csv("./Data/CancerDC/DrugComb/all_dpairs.csv")

# n = file_in.shape[0]

# print(n)
# for k in range(28):
#     start = k*100000
#     end = (k+1)*100000
#     print(str(start) + " ~ " + str(end))
#     file_out = file_in[start:end]
#     file_out.to_csv("./Data/CancerDC/DrugComb/all_dpairs" + str(k) + ".csv")
# file_out = file_in[2800000:n]
# file_out.to_csv("./Data/CancerDC/DrugComb/all_dpairs28.csv")


#---------------------------------------------------------------------------------------------------

#2.寻找靶标
# path = "D:/TASK2/TASK2_py_code/all_pairs_new" ########
# #./Data/CancerDC/DrugComb/all_pairs_new

# dirs = os.listdir(path)

# t_info = pd.read_csv("D:/TASK3/Data/DiffExpress/T_embedding/T_PRAD.csv") ###1111#####
# #./Data/CancerDC/DrugComb/all_pairs_new/T_OSTE.csv

# t_name = t_info["ID"].tolist()
# t_value = t_info["Embedding"].tolist()

# for f in dirs:
#     file_in = pd.read_csv(path + "/" + f)

#     TargetEmbedding = []
#     for i in range(file_in.shape[0]):
#         print(f + str(i))
#         t_list = file_in.iloc[i][3].split(";") + file_in.iloc[i][4].split(";")
#         embed_ave = [0.0] * 304

#         count = 0.0
#         for t in t_list:
#             t = int(t)
#             if t in t_name:
#                 s = t_value[t_name.index(t)].replace("[","")
#                 s = s.replace("]","")
#                 s = s.replace(" ","")
#                 l = s.split(",")
#                 for j in range(304):
#                     embed_ave[j] = embed_ave[j] + float(l[j])
#                 count = count + 1.0
#         if count != 0.0:
#             # 求平均
#             for j in range(304):
#                 embed_ave[j] = embed_ave[j] / count
#         # 存储到list中
#         TargetEmbedding.append(embed_ave)

#     file_in["TargetEmbedding"] = TargetEmbedding

#     file_in.to_csv("D:/TASK3/Data/CancerDC/DrugComb/all_drug_pair/t_info/" + f ,index=False)
#     # D:/TASK3/Data/CancerDC/DrugComb/t_info




#---------------------------------------------------------------------------------------------------
#3.找全0的TargetEmbedding和重复的


# path = "D:/TASK3/Data/CancerDC/DrugComb/all_drug_pair/t_info"
# #D:/TASK3/Data/CancerDC/DrugComb/t_info

# dirs = os.listdir(path)

# train = pd.read_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/MGP-DR/PRAD_prostate.csv") ####1111####

# t_name = train["name_list"].tolist()

# for f in dirs:
#     file_in = pd.read_csv(path + "/" + f)

#     drop_list = []
#     n = file_in.shape[0]

#     for i in range(n):
#         print(f + str(i))

#         if file_in.iloc[i][8] in t_name:
#             drop_list.append(i)
#             continue
        
#         s = file_in.iloc[i][10].replace("[","")
#         s = s.replace("]","")
#         s = s.replace(" ","")
#         l = s.split(",")
#         if l[0] == "0.0":
#             drop_list.append(i)
    
#     print(len(drop_list))
#     print(drop_list)
#     file_out = file_in.drop(drop_list)
#     file_out.to_csv("D:/TASK3/Data/CancerDC/DrugComb/all_drug_pair/t_info2/" + f ,index=False)
    #D:/TASK3/Data/CancerDC/DrugComb/t_info






#---------------------------------------------------------------------------------------------------

#4.合文件
# path = "D:/TASK3/Data/CancerDC/DrugComb/all_drug_pair/t_info2" ########
# dirs = os.listdir(path)

# all_pairs = pd.DataFrame({"Unnamed: 0":[],"D_r":[],"D_c":[],"T_r":[],"T_c":[],"S_r":[],"S_c":[],"SMILES":[],"name_list":[],"DrugEmbedding":[],"TargetEmbedding":[]})

# for f in dirs:
#     print(f)
#     file_in = pd.read_csv(path + "/" + f)
#     all_pairs = all_pairs.append(file_in)

# print(all_pairs.shape[0])

# file_out = all_pairs.drop("Unnamed: 0",axis=1)
# file_out.to_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_pred/predict/OSTE.csv",index=False)#####






#---------------------------------------------------------------------------------------------------

#4. 统计样本总量、正样本量、取出每个文件的前10
path = "D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_pred/Result/PRAD" ###1111#####
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

    # 取出每个文件的前10
    valid_file = valid_file.append(file_in.head(10))

print(total_sample)
print(pos_sample)
valid_file.to_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_pred/Result/PRAD.csv",index=False)








