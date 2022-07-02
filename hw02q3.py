def missing_digits(n):
    count = 0
    if n < 10:
        return 0
    else:
        while n >= 10 :
            n , mod1= n // 10, n % 10 
            mod2 = n % 10
            if mod1 == mod2:
                func = mod1 - mod2
            else:
                func = mod1 - mod2 -1
            count += func
    return count   

print(missing_digits(1122))
    
        