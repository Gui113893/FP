def countLetters(file):
    dicionario = {}
    with open(file) as file:
        for word in file:
            word = word.rstrip()
            for char in word:
                if char not in dicionario:
                    dicionario[char] = 1
                    
                else:
                    dicionario[char] +=1
    return dicionario





def main():
    letras = countLetters("wordlist.txt")
    letras2 = {}

    for key in sorted(letras.keys()):
        letras2[key] = letras[key]

    for key, value in letras2.items():
        print(f"{key}:{value}")

if __name__ == "__main__":
    main()