# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def find_number(key, dic):
    if dic.get(key) == None:
        print(f"Não existe contacto associado ao número: {key}")
    else:
        print(f"Nome associado ao número: {dic[key]}")

def filterPartName(contacts, partName):
    dicionario = {}
    for value in contacts.values():
        if partName in value:
            for key in contacts.keys():
                if contacts[key] == value:
                    dicionario[key] = value

    return dicionario

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            numero = input("Insira um número: ")
            nome = input("Insira um nome: ")
            contactos[numero] = nome
        elif op == "R":
            numero = input("Insira um número: ")
            contactos.pop(numero)
        elif op == "N":
            numero = input("Insira um número: ")
            find_number(numero, contactos)
        elif op == "P":
            partName = input("Indique parte do nome: ")
            print(filterPartName(contactos, partName))
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

