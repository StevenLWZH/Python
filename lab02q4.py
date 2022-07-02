def count_factors(n):
    i, count = 1, 0
    while n >= i : 
        if n % i == 0 :
            i += 1
            count += 1
        else:
            i += 1
    return count    

def count_primes(n):
    i, count = 1, 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count

def is_prime(n):
    return count_factors(n) == 2 # only factors are 1 and n

print(count_primes(20))