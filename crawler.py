# 抓取 PTT 電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 Request 物件，附加 Request Headers 的資訊(讓程式的搜尋像一般使用者)
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

# 解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser") # 讓 BeautifulSoup 協助我們解析
titles=root.find_all("div",class_="title") # 尋找所有 class="title" 的 div 標籤
for title in titles:
    if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除)，就印出來
        print(title.a.string)