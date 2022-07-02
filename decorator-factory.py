# 計算 1 + 2 +3 + ... + max 的裝飾器工廠
def calculateFactory(max):
    def calculate(callback):
        def run():
            total = 0
            for n in range(max+1):
                total += n
            callback(total)
        return run
    return calculate

@calculateFactory(100)
def show(result):
    print("結果是:", result)

@calculateFactory(10)
def showEnglish(result):
    print("Result is:", result)

show()
showEnglish()

# def myFactory(base): # 運用裝飾器工廠主要是可以接收額外的參數
#     def myDeco(cb):
#         def run():
#             print("裝飾器內的程式", base)
#             result = base * 2
#             cb(result)
#         return run
#     return myDeco

# @myFactory(3) # 使用裝飾器工廠需要加小括號，以此輸入參數
# def test(result):
#     print("普通函式的程式", result)

# test()