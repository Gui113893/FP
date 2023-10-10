from tkinter import filedialog
import os

def fileSum(filename):
    soma = 0
    file = open(filename)
    while True:
        linha = file.readline()

        linha = linha.strip("\n")   

        if linha == "":
            break

        linha = float(linha)
        soma += linha

    file.close()
    return soma



def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):
    #name = input("File? ")                                  #A
    name = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(name)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


if __name__ == "__main__":
    main()

