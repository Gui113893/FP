# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle


t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
file = open("drawing.txt")
while True:
    linha = file.readline()

    linha = linha.rstrip()

    if linha == "":
        break

    if linha.isalpha():
        if linha=="UP":
            t.up()
        else:
            t.down()
    else:
        linha = linha.split()
        t.goto(int(linha[0]), int(linha[1]))
file.close()
# wait

turtle.Screen().exitonclick()

