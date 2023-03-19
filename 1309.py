dolar = (input())
casa_decimal = (input())

lendo_dolar = len(dolar)
for i in range(lendo_dolar):
    if lendo_dolar == 6:
        print(f"${dolar[:3]},{dolar[3:6]}.{casa_decimal*2}")