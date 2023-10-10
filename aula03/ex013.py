def mdc(a, b):
    r = a % b
    
    if r == 0:
        return b
    elif r > 0:
        return mdc(b, r)

print(mdc(12, 20))