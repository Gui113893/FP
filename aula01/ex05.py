import math

a = float(input("Cateto A (cm): "))
b = float(input("Cateto B (cm): "))

h = math.sqrt( (a**2) + (b**2) )

angulo_graus = (math.acos(a/h) * 180) / math.pi

print(f"A hipotenusa do triângulo retângulo é de {h:.2f}cm\nO ângulo entre o cateto A e a Hipotenusa é de {angulo_graus:.2f}º")

