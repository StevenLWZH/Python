# 例外處理情境：轉換資料型態失敗
# 若輸入的資料格式不是數字，則無法轉換為數字，則請他重新輸入，直到成功
while True:
    data = input("請輸入數字:")
    try:
        number = int(data)  # 轉換資料可能會發生例外，因此放入try內
        break # 若輸入正確會進入try ，然後跳出無限迴圈
    except Exception: # 例外的總類，若正常則忽略Exception，若異常則進入Exception
        print("輸入格式錯誤，請重新再輸入")

number = number * 2
print(number)