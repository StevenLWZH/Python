# 網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8") # 取得台大網站的原始碼(HTML、CSS、JS)
# print(data)
import sys
sys.path.append(modules) # 在模組的搜尋路徑列表中【新增路徑】
print(sys.path) #印出模組的搜尋路徑列表


import urllib.request as request #因要做網路連線，所以需載入此模組
import json # 為了解析json，因此載入json模組
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組，處理 json 資料格式
# print(data)

# 將公司名稱列表出來
clist=data["result"]["results"] #需先觀察API資料，當中觀察到result和results為一個列表，因此提前面
with open("company.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n") #藉由上面的results找出key-value
