# 定義函式
# def multiply(n1,n2):
#     return n1*n2
# #呼叫函式
# value=multiply(3,4)+multiply(10,5) # (3*4)+(10*5)
# print(value)

# 程式的包裝：同樣的邏輯可以重複利用
def calcuate(max):
    sum=0
    for n in range(1,max+1):
        sum+=n
    print(sum)

calcuate(10)
calcuate(20)
# 定義後，要記得呼叫，定義才有效