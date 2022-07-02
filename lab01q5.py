def sum_digits(y):
    sum = 0
    while y > 0:
         y, x = y // 10, y % 10
         sum += x
    return sum

print(sum_digits(4224))