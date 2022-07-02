# 隨機模組
import random

# 隨機選取
# data=random.choice([1,5,6,10,20]) #隨機選取1筆
# data=random.sample([1,5,6,10,20],3) #隨機選取3筆
# print(data)

# 隨機調換順序(洗牌的概念)
# data=[1,5,8,20]
# random.shuffle(data)
# print(data)

# 隨機取得亂數
# data=random.random() # 0 ~ 1 之間的隨機亂數
# data=random.uniform(60,100) # 60 ~ 100 之間的隨機亂數
# print(data)

# 取得常態分配亂數
# 平均數 100 ，標準差 10
# data=random.normalvariate(100,10)
# print(data)

# 統計模組
import statistics as stat 
# data=stat.mean([1,4,5,8]) # 算平均
# data=stat.median([1,4,5,8]) # 算中位數
data=stat.stdev([1,4,5,8]) # 算標準差
print(data)