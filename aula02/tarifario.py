duracao_inicial = int(input("Duração da chamada(s): "))

tarifario = 0.12 / 60

if duracao_inicial <= 60:
    custo = 0.12

else:
    tempo = duracao_inicial - 60
    custo = (tarifario * tempo) + 0.12

print(f"Uma chamada de {duracao_inicial}s tem um custo de {custo}€") 