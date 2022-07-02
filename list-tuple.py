# 有序可變動列表 List
# grades=[12,60,15,70,90]
# grades[1:4]=[] #連續刪除列表中從編號1到編號4(不包括)的資料
# grades[0]=55 #放到列表中的第一個位置
# grades=grades+[12,33]
# length=len(grades) #取得列表的長度
#練習二
# data=[[3,4,5],[6,7,8]]
# data[0][0:2]=[5,5,5] # 把數字3跟4換成三個5
# print(data[0])

#有序不可變動列表 Tuple
data=(3,4,5)
data[0]=5 # 錯誤：因Tuple的資料不可變動
print(data)