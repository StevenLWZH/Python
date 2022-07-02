def num_eights(x):
    count = 0
    while x >= 1:
        x, mod = x // 10, x % 10
        if mod == 8 :
            count += 1
    return count
print(num_eights(88888888))