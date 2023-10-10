# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):

    with open(fname, "r") as fich:
        for line in fich:
            item = line.strip().split(";")
            produtos[item[0]] = (item[1], item[2], item[3], item[4])
    return produtos


def registaCompra(produtos):
    car = dict()
    # cod[0] = pn(produto) e cod[1] = quantidade

    while True:

        cod = input("Code? ").split()  # CRIA UMA LISTA

        if cod == []:
            break

        p = cod[0]

        if p not in produtos:
            continue

        iva = float(produtos[p][3].strip('%\n')) / 100
        precofinal = round(float(produtos[p][2]) + float(produtos[p][2]) * iva, 2)

        car.setdefault(p, 0)

        try:
            car[p] += int(cod[1])
            qtd = int(cod[1])

        except:
            car[p] += 1
            qtd = 1

        # precofinal = precofinal * qtd
        # TRY EXCEPT PARA NÃO DAR ERRO NA QUANTIDADE
        print(produtos[p][0], qtd, precofinal)
    return car


def fatura(produtos, compra):
    #o argumento compra que passa para esta função é
    totalliquido = 0
    totalbruto = 0
    ivat = 0
    for i in compra.keys():
        pb = float(produtos[i][2])
        iva = produtos[i][3].split("%")[0]
        iva = float(int(iva)/100)
        qtd = compra[i]
        print(pb, iva, qtd)
        totalliquido += pb * qtd * (1+iva)
        totalbruto += pb *qtd
        ivat += totalliquido - totalbruto
        print("{:4d} {:31s}({:2f}%){:11.2f}".format(qtd, i, ivat, totalliquido))

    print("{:>41s}{:>11.2f}\n{:>41s}{:>11.2f}\n{:>41s}{:>11.2f}".format("Total Bruto:", totalbruto, "Total IVA:", ivat, "Total Liquido:",totalliquido))
def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)

    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            print(compra)
        elif op == "F":
            fatura(produtos,compra)
        elif op == "S":
            print("Caixa fechada")
            break
        else:
            print("Opção Inválida!")
        # Aqui pode acrescentar a compra a uma estrutura de dados adequada...
        # Acrescente outras opções aqui...

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])

