# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    x = open(fname)
    x.readline()
    for line in x:
        line = line.split("%\n")[0].split(";")
        line[-1] = int(line[-1]) / 100
        line[-2] = float(line[-2])
        produtos[line[0]] = tuple(line[1:])
    return produtos


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    dic = {}
    while 1:
        c = input("Code? ")
        if c == "":
            break
        a = c.split()
        if a[0] in produtos:
            if not a[0] in dic:
                dic[a[0]] = 0
            if len(a) == 1:
                dic[a[0]] += 1
                q = 1
            else:
                dic[a[0]] += int(a[-1])
                q = int(a[-1])
            p = round((produtos[a[0]][-1] + 1) * produtos[a[0]][-2] * q, 2)
            print(produtos[a[0]][0], q, p)
    return dic


def fatura(produtos, nfatura):
    """Imprime a fatura de uma dada compra."""
    while len(nfatura) > 0:
        f = int(input("Numero compra? "))
        if 0 < f <= len(nfatura):
            compra = nfatura[f - 1]
            tb = 0
            tiva = 0
            a = []
            for i in compra.keys():
                if not produtos[i][1] in a:
                    a.append(produtos[i][1])
            for n in a:
                print(n)
                for i in compra:
                    if produtos[i][1] == n:
                        p = round((produtos[i][-1] + 1) * produtos[i][-2] * compra[i], 2)
                        tb += produtos[i][-2] * compra[i]
                        tiva += (produtos[i][-1]) * produtos[i][-2] * compra[i]
                        iva = int(produtos[i][-1] * 100)
                        print("{:>4} {:<30s} ({:>2}%) {:>10}".format(compra[i], produtos[i][0], iva, p))
            print("{:>41} {:>10}".format("Total bruto:", round(tb, 2)))
            print("{:>41} {:>10}".format("Total IVA:", round(tiva, 2)))
            print("{:>41} {:>10}".format("Total liquido:", round(tb + tiva, 2)))
            break


def main(args):
    # produto guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)

    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    nfatura = []
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            nfatura.append(compra)
        elif op == "F":
            fatura(produtos, nfatura)
        elif op == "S":
            break

            # Aqui pode acrescentar a compra a uma estrutura de dados adequada...
        # Acrescente outras opções aqui...

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys

if __name__ == "__main__":
    main(sys.argv[1:])
