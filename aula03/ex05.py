def max2(x, y):
    max = x
    if y > max:
        max = y
    
    return max

def max3(x, y, z):
    max = max2(max2(x, y), max2(y, z))
    return max




print(max2(4, 3))
print(max2(-3, -2))

print(max3(3, 5, 7))
print(max3(3, 7, 5))
print(max3(7, 5, 3))
print(max3(7, 3, 5))