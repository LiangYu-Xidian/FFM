
import xgboost as xgb
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer, make_column_selector


from sklearn.model_selection import StratifiedKFold,train_test_split,cross_val_score
from sklearn.metrics import auc, roc_curve
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn as sk
import random


def str_to_list(s):
    s = s.replace("[","")
    s = s.replace("]","")
    s = s.replace(" ","")
    l = s.split(",")
    l_v = []
    for e in l:
        l_v.append(float(e))
    return l_v

'''
PART1: 处理数据
'''
 
#读csv中的value数据得到转化为float的 id_list :df

tag = "drug"  # 取哪种embeding方式
if tag == "graph":
    d = 7
if tag == "drug":
    d = 8

file_pos = pd.read_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_final_guding/LUSC_lung.csv") 
file_neg = pd.read_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_final_guding/LUSC_lung_neg.csv") 
num = file_pos.shape[0]
num_neg = file_neg.shape[0]

#正样本
value_pos = []
for i in range(num):
    s_d = file_pos.iloc[i][d]
    s_t = file_pos.iloc[i][9]  
    l_d = str_to_list(s_d)
    # 1.
    l_t = str_to_list(s_t)
    l = l_d + l_t
    # l = l_d
    value_pos.append(l)
print("value_pos ok")

#负样本
value_neg = []
index_neg = []
while len(index_neg) < num:
    e = random.randint(0,num_neg-1)
    if e not in index_neg:
        index_neg.append(e)
for i in index_neg:
    s_d = file_neg.iloc[i][d]
    s_t = file_neg.iloc[i][9]  
    l_d = str_to_list(s_d)
    # 2.
    l_t = str_to_list(s_t)
    l = l_d + l_t
    # l = l_d
    value_neg.append(l)
print("value_neg ok")


#分出 value【二维】，label【一维】
value = value_pos + value_neg
label = [1]*num + [0]*num
print(len(value))
print(len(label))



'''
PART2: 训练集和测试集
'''

times = 0

x = value
y = label

X = np.array(x)
Y = np.array(y)


X_train, X_test , Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0, shuffle=True)#取出训练集和测试集

print(X_train)
print(Y_train)
print(X_test)
print(Y_test)
print(len(X_train))
print(len(Y_train))
print(len(X_test))
print(len(Y_test))

# ！！！！！！！！！！！！！！！！！！！！！！！交叉验证时
X_train = X
Y_train = Y

'''
PART3: 搜索最优参数
'''

clf = xgb.XGBClassifier()

    
# grid search 选择模型的超参数
param_grid = {
    "classifier__gamma": [0,0.05,0.1,0.3,0.5,0.6], 
    "classifier__reg_alpha": [0,0.01,0.05,0.5,1], # L1正则化权重项
    "classifier__reg_lambda": [0,0.1,0.5,1], # L2正则化权重项
    "classifier__n_estimators": [50,100,150,200,300], # 多少棵树
    "classifier__eta": [0.01,0.03,0.05,0.1,0,2,0.3], # 学习率
    "classifier__max_depth": [3,5,7,9,11,13,15,17,19,25], # 树的最大深度
    "classifier__colsample_bytree": [0.4,0.6,0.8,1], # 选择多少列构建一个树
    "classifier__min_child_weight": [1,2,3,4,5,6,7] # 叶子节点最小样本数目
}
# 构建grid search 模型， 10折交叉验证。
search = GridSearchCV(clf, param_grid, scoring="roc_auc", cv=10)
search.fit(X_train,Y_train)
print(search.best_score_)
print(search.best_params_)



