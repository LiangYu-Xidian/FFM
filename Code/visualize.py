import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import rcParams




# 2.绘制消融实验对比图

label_x = ["COAD","BRCA","GBM","PRAD","LUSC","KIRP","OSTE"]
data_1 = [0.8425,0.8289,0.8855,0.8489,0.8512,0.8491,0.9179]
data_2 = [0.7619,0.7540,0.8157,0.7666,0.7616,0.7601,0.8804]
data_3 = [0.8294,0.8118,0.8914,0.8313,0.8348,0.8356,0.9205]
data_4 = [0.7632,0.7363,0.8081,0.7641,0.7579,0.7590,0.8878]
data_5 = [0.7989,0.7622,0.8344,0.7991,0.7838,0.8032,0.8624]

val_x = range(len(label_x))

plt.figure(figsize=(9.5, 5))

plt.scatter(val_x,data_1,label="GraphBERT+T",c="royalblue",s=50)
plt.scatter(val_x,data_2,label="GraphBERT!+T",c="cornflowerblue",s=50)
plt.scatter(val_x,data_3,label="DrugBERT+T",c="seagreen",marker="^",s=50)
plt.scatter(val_x,data_4,label="DrugBERT!+T",c="mediumseagreen",marker="^",s=50)
plt.scatter(val_x,data_5,label="Only T",c="mediumpurple",marker="s",s=50)


plt.xticks(val_x,label_x)

plt.legend()
plt.ylabel("AUROC")
plt.xlabel("cancer")
plt.title("Ablation Performance")
plt.show()