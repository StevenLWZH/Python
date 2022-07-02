def wears_jacket_with_if(temp, raining):
    if temp < 60 or raining == True:
        return True
    else:
        return False

def wears_jacket(temp, raining):
        return temp < 60 or raining

print(wears_jacket(90, False))
print(wears_jacket(40, False))
print(wears_jacket(100, True))