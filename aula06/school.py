# Complete o programa!

# a)
def loadFile(fname, lst):
    file = open(fname)
    linha = file.readline()
    while True:
        linha = file.readline()
        if linha == "":
            break
        linha = linha.split("\t")
        lst.append((linha[0], linha[1], float(linha[5]), float(linha[6]), float(linha[7])))
            
    print("="*100)
    print(lst, end="\n")
    print("="*100)
    file.close()
    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    ...

# c) Crie a função printPauta aqui...
...

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    ...
    
    # mostrar a pauta
    ...


# Call main function
if __name__ == "__main__":
    main()


