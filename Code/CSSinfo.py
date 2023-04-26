import pandas as pd
import numpy as np
from pyrsistent import b
from regex import B
from sqlalchemy import false;

import math


# ------------------处理源数据中不合规矩的行-----------------
# i=0;
# f_out = open("D:/TASK3/Data/doses_CssSyn2020_source.txt", "a")


# with open("D:/TASK3/Data/doses_CssSyn2020_1.txt","r") as f:
#     for line in f:
#         i = i + 1
#         print(i)
#         line = line.replace(",","/")
#         f_out.write(line)

# f_out.close()



# --------------------------读入数据------------------------------

# file_in = pd.read_csv("D:/TASK3/Data/doses_CssSyn2020_source.txt",error_bad_lines=False)
# print(file_in.shape)

# drug1 = []
# drug2 = []
# css = []

# for i in range(file_in.shape[0]):
#     print(i)
#     row = file_in.iloc[i][0]
#     row_list = row.split("|")
#     drug1.append(row_list[1].replace("\"",""))
#     drug2.append(row_list[2].replace("\"",""))
#     css.append(row_list[len(row_list)-1].replace("\"",""))

# drug_pair = pd.DataFrame({"drug1":drug1,"drug2":drug2,"css":css})
# drug_pair = drug_pair.drop_duplicates()
# print(drug_pair)

# drug_pair.to_csv("D:/TASK3/Data/drug_pair.csv",index=false)





# --------------------------css合并后的药物对------------------------------
file_in = pd.read_csv("D:/TASK3/Data/drug_pair.csv",error_bad_lines=False)

print(file_in.shape)

# 删去具有NAN的行
drop_list = []

for i in range(file_in.shape[0]):
    print(i)
    if file_in.iloc[i][1] is np.nan or file_in.iloc[i][2] is np.nan:
        drop_list.append(i)

file_in = file_in.drop(drop_list)
print(file_in.shape)

# 合并数值
means = file_in['css'].groupby([file_in['drug1'], file_in['drug2']]).mean()
print(means)
means.to_csv("D:/TASK3/Data/drug_pair_single.csv",index=false)
