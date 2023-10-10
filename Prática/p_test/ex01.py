# Calculadora de IMC
# Recebe o peso e a altura, calcula o IMC e imprime o resultado juntamente com a categoria
def IMC(peso, altura):
    #calcular IMC
    imc = peso / altura**2

    #classificar IMC e imprimir resultado
    if imc < 18.5:
        categoria = "Magro"
    elif imc < 25:
        categoria = "Saudável"
    elif imc < 30:
        categoria = "Forte"
    else:
        categoria = "Obeso"
    
    return imc, categoria

def main():
    # receber peso e altura
    peso = float(input("Digite o peso (em kilogramas): ")) 
    altura = float(input("Digite a altura (em metros): ")) 
    # para testar, use os valores 80 e 1.80 para peso e altura, respectivamente 
    # em que o resultado deve ser 24.69 e Saudável     
    print(f"{IMC(peso, altura)[0]:.2f}, {IMC(peso, altura)[1]}")   

if __name__ == "__main__":
    main()