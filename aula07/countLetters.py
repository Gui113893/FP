import sys

def countLetters(ficheiro):
    
    letras = {}

    with open(ficheiro, encoding="utf8") as f:
        for linha in f:
            for caracter in linha:
                if letras.get(caracter.lower()) == None and caracter.isalpha():
                    letras[caracter.lower()] = 1
                elif caracter.isalpha():
                    letras[caracter.lower()] += 1

    return letras

def main():

    ficheiro = sys.argv[1]
    dicionario_countLetters = countLetters(ficheiro)

    sorted_dicionario = dict(sorted(dicionario_countLetters.items()))

    for key, value in sorted_dicionario.items():
        print(key, value)

if __name__ == "__main__":
    main()
