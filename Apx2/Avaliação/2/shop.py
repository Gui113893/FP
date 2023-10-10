# Pode correr o programa sem argumentos:
#   python3 shop
# ou passando outros ficheiros de produtos como argumento:
#   python3 shop produtos1.txt ...

def loadDataBase(fname, produtos):
    f = open(fname, 'r')
    c = 1
    for x in f:
        if c == 1:
            c += 1
            continue
        a = x.split(';')
        produtos.update({a[0]: a[1:]})
    f.close()


def registaCompra(produtos, lista):
    d = {}
    for y in lista:
        codigo = y['codigo']
        quantidade = y['quantidade']
        if codigo in produtos:
            produtope = float(produtos[codigo][2]) * quantidade
            ivaproduto = float(produtos[codigo][2]) * quantidade * (
                        float(produtos[codigo][-1].replace('%\n', '')) / 100)
            print('Code? ', produtos[codigo][0], quantidade, round(produtope + ivaproduto, 2))
            if codigo in d:
                d[codigo] += quantidade
            else:
                d[codigo] = quantidade
        else:
            print('Code? ', end=" ")
    print('Code? ', end=" ")
    return d


def fatura(produtos, compra):
    h = {}
    bruto = 0
    iva = 0
    padding = ' '
    for codigo in compra:
        seccao = produtos[codigo][1]
        if seccao not in h:
            h[seccao] = []
        h[seccao].append({'quantidade': compra[codigo], 'taxa': produtos[codigo][-1], 'preço': produtos[codigo][-2],
                          'nome': produtos[codigo][0]})
    for seccao in h:
        print(seccao)
        for t in h[seccao]:
            taxa = float(t['taxa'].replace('%\n', ''))
            produtope = float(t['preço']) * t['quantidade']
            ivaproduto = float(t['preço']) * t['quantidade'] * (float(t['taxa'].replace('%\n', '')) / 100)
            print(
                f' {t["quantidade"] :{padding}>{3}} {t["nome"] :{padding}<{26}} ({taxa:2.0f}%) {produtope + ivaproduto:4.2f}')
            bruto += produtope
            iva += ivaproduto
    print(f'{"Total Bruto:" :{padding}>{37}} {bruto:>4.2f}')
    print(f'{"Total IVA:" :{padding}>{37}} {iva:>4.2f}')
    print(f'{"Total Liquido:" :{padding}>{37}} {bruto + iva:>4.2f}')


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
    w = []
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            list = []
            ciq = input()
            a = ciq.split()
            while len(a) > 0:
                b = {'codigo': a[0]}
                if len(a) > 1:
                    b.update(quantidade=int(a[1]))
                elif len(a) == 1:
                    b.update(quantidade=1)
                list.append(b)
                ciq = input()
                a = ciq.split()
            compra = registaCompra(produtos, list)
            w.append(compra)
        # Aqui pode acrescentar a compra a uma estrutura de dados adequada...
        # Acrescente outras opções aqui...
        elif op == 'F':
            i = input('Numero Compra? ')
            fatura(produtos, w[int(i) - 1])
        elif op == 'S':
            break

    print("Obrigado!")


# Não altere este código / Do not change this code
import sys

if __name__ == "__main__":
    main(sys.argv[1:])

