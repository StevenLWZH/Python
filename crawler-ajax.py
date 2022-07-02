# 抓取 KKDAY 的文章資料
import urllib.request as req
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=8cc91f0f13a9694aa1f072738e7f5b6c"
# 建立一個 Request 物件，附加 Request Headers 的資訊(讓程式的搜尋像一般使用者)
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 根據觀察，取得的資料是 JSON 格式
# print(data)

# 解析 JSON 格式的資料，取得每篇文章的標題
import json
data=json.loads(data) # 把原始的 JSON 資料解析成字典/列表的表示形式

# 取得 JSON 資料中的文章標題
posts=data["data"]["top_products"]["prod_list"] # 縮小資料範圍
for keys in posts: 
    print(keys["name"]) 