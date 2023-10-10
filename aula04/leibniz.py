def leibnizPi4(n):
    soma = 0
    for i in range(0, n+1):
        soma += ((-1)**i)/(2*i +1)
    
    return soma

def main():
    n = int(input("Digita o número de termos: "))
    print(f"A soma de {n} primeiros termos da série de Leibniz é de {leibnizPi4(n)}")

main()