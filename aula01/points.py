# This program reads the coordinates of two points (x1,y1) and (x2,y2).
from math import dist


x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

# create tuples from coordinates
p1 = (x1, y1)
p2 = (x2, y2)

print("Point1:", p1)
print("Point2:", p2)

# Compute and print the distance between the points!

distancia = dist(p1, p2)

print(f"A distância entre {p1} e {p2} é de {distancia:.2f}")