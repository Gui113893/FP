# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    with open(fname) as ficheiro:
        ficheiro.readline()
        for linha in ficheiro:
            linha = linha.strip().split(";")
            produtos[linha[0]] = (linha[1], linha[2], float(linha[3]), float(linha[4].strip("%"))/100)

def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    dados_compra = {}
    while True:
        codigo_quantidade = input("Code? ").split()
        
        if len(codigo_quantidade) == 0:
            return dados_compra
        
        codigo = codigo_quantidade[0]

        if codigo in produtos:

            if len(codigo_quantidade) == 2:
                quantidade = int(codigo_quantidade[1])
            else:
                quantidade = 1
            
            preco = calcular_preco(produtos, codigo, quantidade)
            print(f"{produtos[codigo][0]}  {quantidade}  {preco:.2f}")

            if dados_compra.get(codigo) == None:
                dados_compra[codigo] = quantidade
            else:
                dados_compra[codigo] += quantidade
    
def fatura(produtos, compra):
    """Imprime a fatura de uma dada compra."""
    seccao = ""
    total_bruto = total_iva = total_liquido = 0
    for codigo, quantidade in compra.items():

        total_bruto += produtos[codigo][2] * quantidade
        total_iva += produtos[codigo][2] * produtos[codigo][3] * quantidade
        total_liquido += calcular_preco(produtos, codigo, quantidade)

        if seccao != produtos[codigo][1]:
            seccao = produtos[codigo][1]
            print(f"{seccao}")
        
        print(f"{quantidade:>4d} {produtos[codigo][0]:<25s}({str(int(produtos[codigo][3]*100)):>2s}%){calcular_preco(produtos, codigo, quantidade):10.2f}") 

    print(f"{'Total Bruto:':>35s}{total_bruto:10.2f}")
    print(f"{'Total IVA:':>35s}{total_iva:10.2f}")
    print(f"{'Total Liquido:':>35s}{total_liquido:10.2f}")

def calcular_preco(produtos, codigo, quantidade):
    """Função auxiliar de cálculo"""
    return (produtos[codigo][2] + produtos[codigo][2] * produtos[codigo][3]) * quantidade    

def main(args):
    produtos = {}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)
    
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    n_compra = 0
    compras = {}

    repetir = True
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            n_compra += 1
            # Esta opção regista os produtos de uma compra e guarda-os num dicionário do tipo, compras = {n_compra: {codigo : quantidade}}
            compras[n_compra] = registaCompra(produtos)
        elif op == "F":
            n = int(input("Numero compra? "))
            fatura(produtos, compras[n])
        elif op == "S":
            break

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])

