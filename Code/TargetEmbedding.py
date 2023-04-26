import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os




# # 1. 找到t1中每个靶标的邻居们得到 t_neigh
# global PPI
# global start
# global end
# PPI = pd.read_csv("D:/TASK3/Data/DiffExpress/interactome_no_selfcircle.csv")
# start = PPI.iloc[:,0].tolist()
# end = PPI.iloc[:,1].tolist()

# t1 = pd.read_csv("D:/TASK3/Data/DiffExpress/t1.csv")

# neighbors = []

# for i in range(t1.shape[0]):
#     print(i)
#     center = t1.iloc[i][1]
#     print(center)
#     neigh = []
#     for j in range(len(start)):
#         if str(start[j]) == str(center):
#             neigh.append(end[j])
#         if str(end[j]) == str(center):
#             neigh.append(start[j])
#     neigh = list(set(neigh))

#     neighbors.append(neigh)
#     print(neigh)

# t1["neighbors"] = neighbors

# t1.to_csv("D:/TASK3/Data/DiffExpress/t1_new.csv",index=False)
    
#---------------------------------------------------------------------------------------------------


#2.看一阶邻居分布情况, 并绘图

# t_neigh = pd.read_csv("D:/TASK3/Data/DiffExpress/t_neigh.csv")
# print(t_neigh)

# len_list = []
# for i in range(t_neigh.shape[0]):
#     s = t_neigh.iloc[i][2].replace("[","")
#     s = s.replace("]","")
#     s = s.replace(" ","")
#     l = s.split(",")
#     len_list.append(len(l))

# t_neigh["len_list"] = len_list


# len_list.sort()


# plt.figure(figsize=(30,12))   
# plt.title('Neighbor Distribution')
# plt.ylabel('Neighbour num')
# plt.xlabel('Target Index')

# sns.lineplot(x=[i+1 for i in range(len(len_list))] , y=len_list)
# sns.barplot(x=[i+1 for i in range(len(len_list))] , y=len_list)

# plt.show()

# t_neigh.to_csv("D:/TASK3/Data/DiffExpress/t1_new.csv",index=False)



#---------------------------------------------------------------------------------------------------

#2.计算子图密度，更新 t_neigh

# def Get_1_neigh_subgraph_density(samp,Network):
#     if len(samp) == 1:
#         density = 0.0
#     else :
#         samp = list(set(samp))
#         node = len(samp)
#         print("node:"+str(node))
#         edge = 0
#         for i in range (Network.shape[0]):
#             if (float(Network.iloc[i,0]) in samp) and (float(Network.iloc[i,1]) in samp) :
#                 edge = edge + 1
#         if node == 1:
#             density = 0.0
#         else:
#             # density = edge/node
#             density = (2*edge)/(node*(node-1))
#         print("edge:"+str(edge))
#         if(edge<node-1):
#             print("??????????????????????????????????????????????????????????????????????")
#             sys.exit(0)
#     return density


# t_neigh = pd.read_csv("D:/TASK3/Data/DiffExpress/t_neigh.csv")
# PPI = pd.read_csv("D:/TASK3/Data/DiffExpress/interactome_no_selfcircle.csv")
# density_list = []

# for i in range(t_neigh.shape[0]):
#     print(i)
#     s = t_neigh.iloc[i][2].replace("[","")
#     s = s.replace("]","")
#     s = s.replace(" ","")
#     l = s.split(",")
#     l.append(t_neigh.iloc[i][1])
#     sample = []
#     for e in l:
#         sample.append(float(e))
#     dens = Get_1_neigh_subgraph_density(sample,PPI)
#     density_list.append(dens)
#     print(dens)

# t_neigh["density_list"] = density_list

# t_neigh.to_csv("D:/TASK3/Data/DiffExpress/t1_new.csv",index=False)




#---------------------------------------------------------------------------------------------------

#3.得到单个靶标在特定癌症下的embedding，得到 T_XXXX

path = "D:/TASK3/Data/DiffExpress/diff_limma" ########
dirs = os.listdir(path)

for f in dirs:
    name = f.split("_")[0]
    print(f)
    file_in = pd.read_csv(path + "/" + f)
    values = file_in["logFC_max_min"]

    visit_target = []
    visit_value = []


    t_neigh = pd.read_csv("D:/TASK3/Data/DiffExpress/t_neigh.csv")
    embedding_list = []

    for i in range(t_neigh.shape[0]):
        print(i)
        # 中间的logFC，子图密度，300个一阶邻居，均值，方差
        t_embed = []
        media = str(t_neigh.iloc[i][1])
        s = t_neigh.iloc[i][2].replace("[","")
        s = s.replace("]","")
        s = s.replace(" ","")
        neighs = s.split(",")

        print("--------------------------------------")
        # 中间的logFC
        print(media)
        if media in visit_target:
            media_v = visit_value[visit_target.index(media)]
        else:
            for j in range(file_in.shape[0]):
                curr = str(int(file_in.iloc[j][0]))
                if str(media) == str(curr):
                    print(j)
                    media_v = values[j]
                    visit_target.append(media)
                    visit_value.append(media_v)
                    break
        t_embed.append(media_v)
        print(t_embed)

        #子图密度
        t_embed.append(t_neigh.iloc[i][4])
        print(t_embed)

        #300个一阶邻居
        n_300 = []
        for n in range(len(neighs)):
            neigh = neighs[n]
            if neigh in visit_target:
                neigh_v = visit_value[visit_target.index(neigh)]
            else:
                for j in range(file_in.shape[0]):
                    curr = str(int(file_in.iloc[j][0]))
                    if str(neigh) == str(curr):
                        neigh_v = values[j]
                        visit_target.append(neigh)
                        visit_value.append(neigh_v)
                        print(neigh_v)
                        break
            n_300.append(neigh_v)
        n_300 = n_300 + [0.0]*300
        obj_sort = sorted(n_300,reverse=True)
        t_embed = t_embed + obj_sort[:300]
        print(t_embed)

        # 均值，方差
        t_embed = t_embed + [np.mean(obj_sort[:300])] #mean
        t_embed = t_embed + [np.var(obj_sort[:300])] #var

        print(t_embed)
    
        embedding_list.append(t_embed)

    t_neigh["Embedding"] = embedding_list
    t_neigh.to_csv("D:/TASK3/Data/DiffExpress/T_" + str(name) + ".csv",index=False)


