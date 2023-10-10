def dateIsValid(year, month, day):
    #Verifica se os dados introduzidos na função são números inteiros 
    if (type(year) != int) or (type(month) != int) or (type(day) != int):  
        return False
    else:
 

        lista_dias = list(range(1, monthDays(year, month)+1))
        lista_meses = list(range(1, 13))
 

        if month in lista_meses and day in lista_dias:
            return True
        else:
            return False


print(dateIsValid(1980, 13, 3))