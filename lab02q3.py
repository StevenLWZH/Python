from operator import add, mul, mod
def lambda_curry2(func):
    return lambda x : lambda y : func(x, y)
curried_add = lambda_curry2(add)
add_three = curried_add(3)
print(add_three(5))