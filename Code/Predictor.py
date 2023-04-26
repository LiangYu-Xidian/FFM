
import xgboost as xgb



from sklearn.model_selection import StratifiedKFold,train_test_split,cross_val_score
from sklearn.metrics import auc, roc_curve
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn as sk
import random
import time
import os

start = time.time()


#读csv中的value数据得到转化为float的 id_list :df
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
PART1: 处理训练数据
'''

file_train = pd.read_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_pred/train/PRAD_prostate.csv") ##111######

#分出 value【二维】，label【一维】
#训练样本
value_train = []
label_train = []
for i in range(file_train.shape[0]):
    s_d = file_train.iloc[i][7]
    s_t = file_train.iloc[i][9]  
    l_d = str_to_list(s_d)
    l_t = str_to_list(s_t)
    l = l_d + l_t
    value_train.append(l)
    label_train.append(int(file_train.iloc[i][11]))
print("value_train ok")



'''
PART2: 训练集打包
'''
x = value_train
y = label_train

X = np.array(x)
Y = np.array(y)

X_train = X
Y_train = Y



'''
PART3: 训练分类器
'''
clf = xgb.XGBClassifier()
clf.fit(X,Y)



'''
PART3: 预测
'''
path = "D:/TASK3/Data/CancerDC/DrugComb/all_drug_pair/PRAD"  ##222######

dirs = os.listdir(path)
for f in dirs:
    print(f)
    file_predict = pd.read_csv(path + "/" + f)

    #预测样本
    value_pred = []
    for i in range(file_predict.shape[0]):   
        s_d = file_predict.iloc[i][9]
        s_t = file_predict.iloc[i][10]  
        l_d = str_to_list(s_d)
        l_t = str_to_list(s_t)
        l = l_d + l_t
        value_pred.append(l)
    print("value_pred ok")

    pred_proba = clf.predict_proba(value_pred)
    print(len(pred_proba))

    #取出为1的概率
    predict_score = []
    for proba in pred_proba:
        predict_score.append(proba[1])
    
    file_predict["predict_score"] = predict_score
    file_out = file_predict.sort_values(by=["predict_score"],ascending=False)
    file_out.to_csv("D:/TASK3/Data/CancerDC/DrugComb/tissue/curr/Samples_pred/Result/PRAD/"+f,index=False)  ##333######

end = time.time()
print(end-start)


