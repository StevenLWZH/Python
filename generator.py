# 建立生成器函式
# def test():
#     print("階段一")
#     yield 3
#     print("階段二")
#     yield 5

# 呼叫並回傳生成器
# gen = test() # 使 gen 為生成器

# 搭配 for 迴圈中使用 (搭配迴圈才能提取當中的資料)
# for data in gen:
#     print(data)

def generateEven(maxnumber):
    number = 0
    while number <= maxnumber:
        yield number
        number += 2

evenGenerator = generateEven(55)
for data in evenGenerator:
    print(data)