def gerar_jogos(lista): 
    return [(equipa1, equipa2) for equipa1 in lista for equipa2  in lista if equipa1 != equipa2]

def resultado(jogo):
    golos1 = int(input(f"Golos de {jogo[0]}: "))
    golos2 = int(input(f"Golos de {jogo[1]}: "))

    return (golos1, golos2)


def main():
    equipas = []
    while True:
        nome_equipa = input("Insere o nome de uma equipa(T para Terminar): ")
        if nome_equipa.upper() == "T":
            break
        else:
            equipas.append(nome_equipa)

    jogos = gerar_jogos(equipas)

    resultados = {}
    for jogo in jogos:
        resultados[jogo] = resultado(jogo)


if __name__ == "__main__":
    main()