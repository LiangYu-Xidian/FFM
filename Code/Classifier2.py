from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import  AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import BaggingClassifier
import xgboost as xgb



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

file_pos = pd.read_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_final_guding/OSTE_bone.csv") 
file_neg = pd.read_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_final_guding/OSTE_bone_neg.csv") 
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
    # l = l_d + l_t
    l = l_d
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
    # l = l_d + l_t
    l = l_d
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

X_train = X
Y_train = Y

'''
PART3: 训练分类器
'''

pre_all = []
re_all = []
f1_all = []
auc_all = []

# clf = svm.SVC(decision_function_shape='ovo',gamma='auto')
# clf = RandomForestClassifier()
clf = xgb.XGBClassifier()


for time in range(10):
    k_fold = StratifiedKFold(n_splits=10,shuffle=True)
    precision = cross_val_score(clf, X_train, Y_train, cv=k_fold, scoring = 'precision')
    recall = cross_val_score(clf, X_train, Y_train, cv=k_fold, scoring = 'recall')
    f1 = cross_val_score(clf, X_train, Y_train, cv=k_fold, scoring = 'f1')
    roc_auc = cross_val_score(clf, X_train, Y_train, cv=k_fold, scoring = 'roc_auc')
    print(time+1)
    print(precision)
    print("precision:"+str(precision.mean()))
    print("recall:"+str(recall.mean()))
    print("f1:"+str(f1.mean()))
    print("roc_auc:"+str(roc_auc.mean()))
    pre_all.append(precision.mean())
    re_all.append(recall.mean())
    f1_all.append(f1.mean())
    auc_all.append(roc_auc.mean())
print("--------------------------------------------------------------------")
# print("precision:")
# print(pre_all)
# print("recall:")
# print(re_all)
# print("f1:")
# print(f1_all)
# print("roc_auc:")
# print(auc_all)


Result = pd.DataFrame({"pre_all":pre_all,"re_all":re_all,"f1_all":f1_all,"auc_all":auc_all})
Result.to_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Result/xgboost/DrugBert/OSTE_bone.csv")

print("precision_ave:"+str(np.mean(pre_all)))
print("recall_ave:"+str(np.mean(re_all)))
print("f1_ave:"+str(np.mean(f1_all)))
print("auc_ave:"+str(np.mean(auc_all)))
