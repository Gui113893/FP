def inputFloatList():
    lista = []
    while True:
        n = input("Digita um número(ENTER PARA TERMINAR): ")
        if n == "":
            break
        else:
            n = float(n)
            lista.append(n)
    return lista

def countLower(lst, v):
    count = 0
    for n in lst:
        if n < v:
          count += 1  
    return count

def minmax(lst):
    for i in range(0, len(lst)):
        if i == 0:
            maior = lst[i]
            menor = lst[i]
        else:
            if lst[i] > maior:
                maior = lst[i]
            elif lst[i] < menor:
                menor = lst[i]
    return maior, menor
        
def main():
    lista = inputFloatList()
    v_medio = (minmax(lista)[0] + minmax(lista)[1]) / 2
    c = countLower(lista, v_medio)

    print(f"Na lista {lista}, o valor médio entre o menor({minmax(lista)[1]}) e o maior({minmax(lista)[0]}) é de {v_medio} e existem {c} valores menores que ele")

if __name__ == "__main__":
    main()