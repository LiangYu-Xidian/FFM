import imp
import numpy as np
import pandas as pd
import math
import os
import random


#1. 过滤NAN

# file_in = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\summary_v_1_5.csv')
# print(file_in.shape)
# print(file_in.head(10))

# drop_list = []

# for i in range(file_in.shape[0]):
#     print(i) 
#     if (str(type(file_in.iloc[i][2])) == "<class 'float'>") & (str(file_in.iloc[i][2]) == "nan"):
#         drop_list.append(i)

# print(drop_list)

# file_out = file_in.drop(drop_list)
# print(file_out.shape)
# print(file_in.shape)

# file_out.to_csv('D:\TASK3\Data\CancerDC\DrugComb\summary_filtered.csv')

#-------------------------------------------------------------------------------------------------------------------------

#2. 取出所有药物

# file_in = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\summary_filtered.csv')
# print(file_in.shape)
# print(file_in.head(10))

# d_row = file_in["drug_row"].to_list()
# d_col = file_in["drug_col"].to_list()
# d_row_t = file_in["drug_row_target_name"].to_list()
# d_col_t = file_in["drug_col_target_name"].to_list()
# D = d_row + d_col
# T = d_row_t + d_col_t

# file_out = pd.DataFrame({"drug":D, "target":T})
# print(file_out.shape)
# file_out = file_out.drop_duplicates()
# print(file_out.shape)
# file_out.to_csv('D:\TASK3\Data\CancerDC\DrugComb\\all_drug.csv')


#-------------------------------------------------------------------------------------------------------------------------

#3. 映射drugbank ID

# file_in = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\\all_drug.csv')
# drug_info = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\drug_info.csv')
# print(file_in.shape)
# # file_in = file_in.head(30)

# DrugBank = []
# SMILES = []

# for i in range(file_in.shape[0]):
#     print(i)
#     drug = str(file_in.iloc[i][0]).lower()
#     print(drug)
#     flag = 0
#     for j in range(drug_info.shape[0]):
#         name = str(drug_info.iloc[j][1]).lower()
#         if drug == name:
#             flag = 1
#             DrugBank.append(drug_info.iloc[j][0])
#             SMILES.append(drug_info.iloc[j][3])
#             break;
#     if flag == 0:
#         DrugBank.append("NULL")
#         SMILES.append("NULL")

# file_in["DrugBank"] = DrugBank
# file_in["SMILES"] = SMILES

# print(file_in)
# file_in.to_csv('D:\TASK3\Data\CancerDC\DrugComb\\all_drug_new.csv')




#-------------------------------------------------------------------------------------------------------------------------

#4. 分文件
# file_in = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\\all_target.csv')
# n = file_in.shape[0]
# print(file_in)

# count = 0
# f = 1

# drug = []
# target = []
# CID = []
# SMILES = []
# for i in range(n):
#     drug.append(file_in.iloc[i][0])
#     # target.append(file_in.iloc[i][1])
#     count = count + 1
#     if(count == 100 or i == n-1):
#         file_out = pd.DataFrame({"T":drug})
#         file_out.to_csv('D:\TASK3\Data\CancerDC\DrugComb\\all_target_' + str(f) +'.csv',index=False)
        
#         drug = []
#         target = []
#         CID = []
#         SMILES = []
#         count = 0

#         f = f + 1

        
#-------------------------------------------------------------------------------------------------------------------------

#5. 取靶标信息
# file_in = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\d1.csv')
# n = file_in.shape[0]
# print(file_in.head(10))

# target = []

# for i in range(n):
#     if file_in.iloc[i][1] != "\\N" :
#         targets = file_in.iloc[i][1].split(";")
#         for t in targets:
#             t = t.strip()
#             target.append(t)

# print(len(target))
# target = list(set(target))
# print(len(target))

# file_out = pd.DataFrame({"target":target})
# file_out.to_csv('D:\TASK3\Data\CancerDC\DrugComb\\all_target.csv')



#-------------------------------------------------------------------------------------------------------------------------

#5. 整合靶标信息为ez_id
# file_in = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\d1.csv')

# # file_in = file_in.head(5)

# t_info = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\\t1.csv')
# drugbank_info = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\drug_target.csv')
# DB_id = drugbank_info["drug"].to_list()
# DB_t = drugbank_info["targets"].to_list()

# n = file_in.shape[0]
# m = t_info.shape[0]


# all_target = []

# for i in range(n):
#     print(i)
#     if file_in.iloc[i][1] != "\\N" :
#         id_now = ""
#         targets = file_in.iloc[i][1].split(";")
#         ID = file_in.iloc[i][2]

#         for t in targets:
#             t = t.strip()
#             for j in range(m):
#                 if t == t_info.iloc[j][0]:
#                     id_now =  id_now + t_info.iloc[j][1] + ";"
#                     break
#                 else:
#                     id_now =  id_now + ""

#         if ID.find("D") == True:
#             pos = DB_id.index(ID)
#             id_now = id_now + DB_t[pos]
        
#         id_new = ";".join(list(set(id_now.split(";"))))
#         print(id_new)
#         all_target.append(id_new)
#     else:
#         all_target.append("NULL")



# file_in["T"] = all_target

# file_in.to_csv('D:\TASK3\Data\CancerDC\DrugComb\d1_new.csv')



#-------------------------------------------------------------------------------------------------------------------------

#6. 整理数据格式（;）
# file_in = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\d1.csv')

# all_target = []

# for i in range(file_in.shape[0]):
#     print(i)
#     s = file_in.iloc[i][1]
#     l = s.split(";")
#     new_l = []
#     for e in l:
#         if e != "":
#             new_l.append(e)
#     new_s = ";".join(new_l)
#     all_target.append(new_s)


# file_in["target"] = all_target

# file_in.to_csv('D:\TASK3\Data\CancerDC\DrugComb\d1_new.csv')



#-------------------------------------------------------------------------------------------------------------------------

#7. 去除不在PPI中的靶标

# file_in = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\d1.csv')
# PPI = pd.read_csv('D:\TASK3\Data\DiffExpress\interactome_no_selfcircle.csv')
# PPI_L = list(set(PPI["0"].to_list() + PPI["1"].to_list()))
# ppi = []
# for p in PPI_L:
#     ppi.append(str(p))

# all_target = []

# for i in range(file_in.shape[0]):
#     print(i)
#     s = file_in.iloc[i][1]
#     l = s.split(";")
#     new_l = []
#     for e in l:
#         if str(e) in ppi:
#             new_l.append(e)
#     new_s = ";".join(new_l)
#     print(new_s)
#     all_target.append(new_s)


# file_in["T"] = all_target

# file_in.to_csv('D:\TASK3\Data\CancerDC\DrugComb\d1_filtered.csv')


#-------------------------------------------------------------------------------------------------------------------------

#8. 循环读数据处理tissue
# drug_info = pd.read_csv('D:\TASK3\Data\CancerDC\DrugComb\d1_filtered.csv')
# d_list = drug_info["drug"].tolist()
# t_list = drug_info["T"].tolist()
# s_list = drug_info["SMILES"].tolist()

# path = "D:\TASK3\Data\CancerDC\DrugComb\\tissue\curr"
# dirs = os.listdir(path)
# for f in dirs:
#     print(f)
#     file_in = pd.read_csv(path + "\\" + f)
#     D_r = []
#     D_c = []
#     T_r = []
#     T_c = []
#     S_r = []
#     S_c = []
#     SMILES = []

#     for i in range(file_in.shape[0]):
#         d_r = file_in.iloc[i][0]
#         d_c = file_in.iloc[i][1]
#         if (str(d_r) in d_list) and (str(d_c) in d_list):
#             D_r.append(d_r)
#             D_c.append(d_c)
#             r_index = d_list.index(d_r)
#             c_index = d_list.index(d_c)
#             T_r.append(t_list[r_index])
#             T_c.append(t_list[c_index])
#             r_index = d_list.index(d_r)
#             s_r = s_list[r_index]
#             s_c = s_list[c_index]
#             S_r.append(s_r)
#             S_c.append(s_c)
#             SMILES.append(s_r+"?"+s_c)
    
#     file_out = pd.DataFrame({"D_r":D_r,"D_c":D_c,"T_r":T_r,"T_c":T_c,"S_r":S_r,"S_c":S_c,"SMILES":SMILES})
#     file_out.to_csv("D:\TASK3\Data\CancerDC\DrugComb\\tissue\\new\\" + f,index=False)



#-------------------------------------------------------------------------------------------------------------------------

#9. 循环读数据生成负样本（neg）

# drug_info = pd.read_csv('./Data/CancerDC/DrugComb/d1_filtered.csv')
# d_list = drug_info["drug"].tolist()
# t_list = drug_info["T"].tolist()
# s_list = drug_info["SMILES"].tolist()

# path = "./Data/CancerDC/DrugComb/tissue/all_info" ########
# dirs = os.listdir(path)

# for f in dirs:
#     dict_drug = []
#     dict_relate = []
#     print(f)
#     file_in = pd.read_csv(path + "/" + f)
#     D_r = file_in["D_r"].tolist()
#     D_c = []
#     T_r = file_in["T_r"].tolist()
#     T_c = []
#     S_r = file_in["S_r"].tolist()
#     S_c = []
#     SMILES = []

#     for i in range(file_in.shape[0]):
#         print(i)
#         d_r = file_in.iloc[i][0]  # 固定的药物
#         s_r = file_in.iloc[i][4]
#         d_c_old = file_in.iloc[i][1] # 要换的药物


#         # 找出与d_r相关的所有药物
#         relate = []
#         if(d_r in dict_drug):
#             iiindex = dict_drug.index(d_r)
#             relate = dict_relate[iiindex]
#         else:
#             for j in range(file_in.shape[0]):
#                 d1 = file_in.iloc[j][0]
#                 d2 = file_in.iloc[j][1]
#                 if(str(d1) == str(d_r)):
#                     relate.append(d2)
#                 if(str(d2) == str(d_r)):
#                     relate.append(d1)
#             dict_drug.append(d_r)
#             dict_relate.append(relate)
        
#         relate_set = set(relate)

#         print(dict_drug)

#         d_set = list(set(d_list) - relate_set) # 药物集

#         random_index = random.randint(0,len(d_set)-1)

#         d_c = d_set[random_index] # 取出药物
#         D_c.append(d_c)

#         c_index = d_list.index(d_c) # 取出原list中的索引 
#         t_c = t_list[c_index] 
#         T_c.append(t_c)
#         s_c = s_list[c_index]
#         S_c.append(s_c)
#         SMILES.append(s_r+"?"+s_c)
    
#     file_out = pd.DataFrame({"D_r":D_r,"D_c":D_c,"T_r":T_r,"T_c":T_c,"S_r":S_r,"S_c":S_c,"SMILES":SMILES})
#     file_out.to_csv("./Data/CancerDC/DrugComb/tissue/curr/neg/" + f,index=False)


#-------------------------------------------------------------------------------------------------------------------------

#10. 添加name_list寻找重复组合
# file_in = pd.read_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/ADD_aaa/COAD_large_intestine_neg.csv")

# names = []
# for i in range(file_in.shape[0]):
#     name1 = file_in.iloc[i][0]
#     name2 = file_in.iloc[i][1]
#     if name1 < name2:
#         name = name1 + name2
#     else:
#         name = name2 + name1
#     names.append(name)
# file_in["name_list"] = names
# file_in.to_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/COAD_large_intestine_neg.csv",index = False)

#-------------------------------------------------------------------------------------------------------------------------

#11. 根据name_list删除重复组合
file_in = pd.read_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/ADD_aaa/BRCA_breast_neg.csv")

drop_list = []
exist_list = []
for i in range(file_in.shape[0]):
    name = file_in.iloc[i][10]
    name = str(name)
    if name in exist_list:
        drop_list.append(i)
    else:
        exist_list.append(name)

file_in = file_in.drop(drop_list)
    
file_in.to_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/COAD_large_intestine_neg.csv",index = False)