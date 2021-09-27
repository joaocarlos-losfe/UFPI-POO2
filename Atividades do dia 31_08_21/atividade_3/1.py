def calcular_potencia(base, expoente):
    pot = 1
    for x in range (expoente):
        pot *= base
        
    return pot

if __name__ == "__main__":

    base = int(input("base: "))
    expoente = int (input("expoente: "))

    pot = calcular_potencia(base, expoente)

    print(pot)