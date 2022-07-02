# 集合的運算
# s1={3,4,5}
# print(10 not in s1)
# s1={3,4,5}
# s2={4,5,6,7}
# s3=s1&s2 # & 就是交集的意思
# s3=s1|s2 # | 就是聯集的意思(符號在Enter的上方)
# s3=s1-s2 #差集的意思，指從s1中減去與s2中有重疊的部分，故剩下3
# s3=s1^s2 #反交集：取兩個集合中，不重疊的資料，故剩下3,6,7
# print(s3)
# s=set("Hello") # 把字串拆解為集合set(字串)
# print("H" in s)

#字典的運算：key-value的配對
# dic={"apple":"蘋果","bug":"蟲蟲"}
# dic["apple"]="小蘋果"
# print(dic["apple"])
# print("apple" in dic) # 判斷key是否存在
# dic={"apple":"蘋果","bug":"蟲蟲"}
# print(dic)
# del dic["apple"] # 刪除字典中的鍵值對(key-value pair)
# print(dic)
dic={x:x*2 for x in [3,4,5]} # 從列表的資料產生字典
print(dic)