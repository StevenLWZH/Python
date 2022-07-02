def is_prime(n):
    if n == 1 :
        return False
    count = 2
    while n > 1:
        if n == n:
            return True
        elif n % count == 0 :
            return False
        else:
            count += 1
print(is_prime(113))