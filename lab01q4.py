def falling(n, k):
    
    if k == 0 :
        return 1
    else:
        k -= 1
        return n * falling(n-1, k)

print(falling(4,3))