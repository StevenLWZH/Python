# Point 實體物件的設計：平面座標上的點
class Point: # Point 為類別名稱
    def __init__(self,x,y):
        self.x=x #self. 後面的x為屬性名稱
        self.y=y
# 建立第一個實體物件
p1=Point(3,4) # p1 為實體物件
print(p1.x,p1.y) # 需寫成實體物件(p1).屬性名稱(x)
# 建立第二個實體物件
p2=Point(5,6)
print(p2.x,p2.y)

# FullName 實體物件的設計：分開紀錄姓、名資料的全名
# class FullName: 
#     def __init__(self):  #較固定
#         self.first="Z.H."
#         self.last="Lai"
# name1=FullName()
# print(name1.first,name1.last)

class FullName:
    def __init__(self,first,last):  #較彈性
        self.first=first
        self.last=last
name1=FullName("Z.H.","Lai")
print(name1.first,name1.last)
name2=FullName("T.Y.","Lin")
print(name2.first,name2.last)