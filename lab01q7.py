def double_eights(n):
    count = 0
    while n > 0 :
        n , mod = n // 10 , n % 10
        if mod == 8 :
            count += 1
    if count >= 2:
        return True
    else:
        return False
    
print(double_eights(1513855158))