# 抓取 PTT 八卦版的網頁原始碼(HTML)
import urllib.request as req
def getData(url): # 定義函式getData，給予參數url
    # 建立一個 Request 物件，附加 Request Headers 的資訊(讓程式的搜尋像一般使用者)
    request=req.Request(url, headers={
        "cookie":"over18=1",
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
    # 抓取上一個頁的連結
            print(title.a.string)
    nextLink=root.find("a",string="‹ 上頁") # 找到內文是 ‹ 上頁 a 標籤
    return nextLink["href"] # 抓取當中href後面的value，並回傳

# 主程序：抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3: #抓三頁的標題
    pageURL="https://www.ptt.cc"+getData(pageURL) # 後段為呼叫getData函式，並將pageURL傳入參數
    count+=1
# 後面迴圈的邏輯為：跑第一次時會跑line 25的網址，列表出標題後，最後還會return回傳上頁的網址，以此取代pageURL
# 接著會再跑第二次，但此時的pageURL，已經變成上頁的，因此可透過調整迴圈次數來決定搜索的頁面數。