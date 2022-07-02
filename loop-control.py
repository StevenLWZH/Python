# break 簡易的範例
# n=0
# while n<5:
#     if n ==3:
#         break
#     print(n) # 印出迴圈中結束後的n
#     n+=1
# print("最後的n:",n)

# continue 的簡易範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     print(x)
#     n+=1
# print("最後的n:",n) #最後n為2，表示只跑兩次迴圈，因為0,2整除，被跳過

# #else 的簡易範例
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum) #印出0加到10的總和

# 綜合範例：找出整數平方根
# 輸入 9，得到 3
# 輸入 11，得到【沒有】整數的平方根
n=input("請輸入一個正整數:")
n=int(n) #將使用者輸入的正整數，轉換成數字
for i in range(n): # i 從 0 ~ n-1
    if i*i==n:
        print("整數平方根:",i)
        break # 用 break 強制結束迴圈時，不會執行 else 區塊
else:
    print("沒有整數平方根")
