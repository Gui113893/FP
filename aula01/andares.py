andares = int(input("Digita o número de andares: "))

moradores = int(input("Digita o número de moradores por andar: "))

distancia_metros_dia = 0

for i in range(1 , andares+1):
    distancia_metros_dia += ((moradores*4) * (3*i))

distancia_km_ano = (distancia_metros_dia * 365) / 1000

print(f"Num prédio de {andares} andares e {moradores} moradores por andar, o elevador percorrerá {distancia_km_ano}km no fim de 1 ano.")