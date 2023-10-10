def media():
    soma = tot = 0
    while True:
        n = input("Digite um número real (ENTER PARA PARAR): ")
        if n == "":
            break
        v = float(n)
        tot += 1
        soma += v
    
    if tot != 0: 
        media = soma / tot
        return media

def main():
    print(media())

main()