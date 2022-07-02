# 定義一個裝式器，計算 1 + 2 + ... + 50 的總和
def count(callback):
    def run():
        # 裝式器想要執行的程式碼
        result = 0
        for n in range(51):
            result += n
        # print(result) # 印出 1 + 2 + ... + 50 的總和
        # 把計算結果透過參數傳到被裝飾的普通函式中
        callback(result)
    return run

# 使用裝飾器
@count
def show(n):
    print("計算結果:", n)

@count
def showEnglish(n):
    print("Result is:", n)

show()
showEnglish()

# # 定義裝飾器
# def testDecorator(callback):
#     def innerFunc(): # 定義內部函式
#         print("裝飾器中的程式碼")
#         callback(3) # 這個回呼函式，其實就是被裝飾的普通函式
#     return innerFunc

# # 使用裝飾器
# @testDecorator
# def decoratedFunc(data):
#     print("普通函式的程式碼", data)

# decoratedFunc()