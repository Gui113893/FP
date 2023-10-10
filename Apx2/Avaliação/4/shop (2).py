def loadDataBase(fname, produtos):
    """Lê dados do ficheiro fname e atualiza/acrescenta a informação num
    dicionário de produtos com o formato {código: (nome, secção, preço, iva), ...}.
    """
    with open(fname, 'r' ) as file:
        next(file)
        for linha in file:
            linha= linha.strip('\n')
            l = linha.split(";")
            produtos[l[0]] = (l[1],l[2],l[3],l[4].strip("%"))

    return produtos


def registaCompra(produtos):
    """Lê códigos de produtos (ou códigos e quantidades),
    mostra nome, quantidade e preço final de cada um,
    e devolve dicionário com {codigo: quantidade, ...}
    """
    
    lista={}
    while True:
        pdt = input('Code? ').strip()
        pdt = pdt.split()

        if pdt ==[]:
            break
        if pdt[0] not in produtos: 
            continue
        if pdt[0] not in produtos: continue

        if len(pdt) == 1:
            pdt.append(1)
        
        prf = float(produtos[pdt[0]][2]) + float(produtos[pdt[0]][2])*float(produtos[pdt[0]][3])/100

        lista.setdefault(pdt[0],0)
        lista[pdt[0]] += float(pdt[1])
        print(produtos[pdt[0]][0],pdt[1],"{:.2f}".format(prf*float(pdt[1])))

    return(lista)



def fatura(produtos, compra,m):

    compra=compra[int(m)]

    TB= 0
    TI=0
    s ={}

    for r in compra.keys():

        p =  produtos[r][1]
        if p not in s.keys():
            s[p] = dict()
        pt = produtos[r][0]
        s[p][pt] = [produtos[r][3],compra[r],produtos[r][2]]
        
   
    for p in s.keys():
        print(p)
        for pt in s[p].keys():
               
            PB =float(s[p][pt][2])
            Q = int( s[p][pt][1])
            IVA = float(s[p][pt][0])

            TB += PB*Q
            TI += IVA/100*PB*Q
            P_IVA =(PB+PB*IVA/100)*Q

       

            print('{:>12} {:<24} {:>12} {:>12}'.format(Q,pt, '(' +'{:>2}'.format(str(round(IVA)))+'%)',round(P_IVA,2)))
        
    print('{:>50} {:>12}'.format('Total Bruto:', round(TB,2)))
    print('{:>50} {:>12}'.format('Total IVA:', round(TI,2)))
    print('{:>50} {:>12}'.format('Total Liquido:', round(TB +TI,2)))

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
    compra = dict()
    n = 0
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula

        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            n += 1
            compra[n] = registaCompra(produtos)
        if op == "F":
            m = int(input("Numero compra? "))
            fatura(produtos, compra, m)
        if op == "S":
            break
            
    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])
