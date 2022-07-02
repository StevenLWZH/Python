# Point 實體物件的設計：平面座標上的點
# class Point: # Point 為類別名稱
#     def __init__(self,x,y):
#         self.x=x #self. 後面的x為屬性名稱
#         self.y=y
#     # 定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5
# p=Point(3,4)
# p.show() # 呼叫實體方法 / 函式
# p.distance(0,0) # 計算座標 3,4 和座標 0,0 之間的距離
# result=p.distance(0,0)
# print(result)

# File 實體物件的設計：包裝檔案讀取的程式
class File:
    # 初始化函式
    def __init__(self,name):
        self.name=name
        self.file=None # 尚未開啟檔案：初期是None
    # 定義實體方法
    def open(self): 
        self.file=open(self.name,mode="r",encoding="utf-8")    
    def read(self):
        return self.file.read()
# 讀取第一個檔案
f1=File("company.txt") #利用變數f1代表實體方法
f1.open() # 呼叫
data=f1.read() # 讀取
print(data)
# 讀取第二個檔案
f2=File("新增路徑.txt")
f2.open()
data=f2.read()
print(data)