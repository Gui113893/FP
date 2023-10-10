string = "p1;Ketchup;Mercearia Salgado;1.59;23%"

linha = string.split(";")

produtos = {}
produtos[linha[0]] = tuple(linha[i] for i in range(1, 5)) 

print(f"{2:>4d} {'cogumelos':<20s}({'23%':>3s}){13.98:10.2f}")
print(f"{2:>4d} {'ca':<20s}({'6%':>3s}){5.98:10.2f}")
print(f"{2:>4d} {'cara':<20s}({'6%':>3s}){1234.98:10.2f}")

print(f"{'Total Bruto:':>30s}{123.45:10.2f}")
print(f"{'Total Iva:':>30s}{123.45:10.2f}")
print(f"{'Total Liquido:':>30s}{123.45:10.2f}")
