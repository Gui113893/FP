x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input("number? "))
x4 = float(input("number? "))



maior = x1

if x2 > maior:
    maior = x2

elif x3 > maior:
    maior = x3

elif x4 > maior:
    maior = x4

print("Maior =",maior)