def calcular_desconto(tipo_combustivel, litros):
    
    PRECO_ALCOOL = 3.45
    PRECO_GASOLINA = 4.53
    

    if tipo_combustivel == "A" or tipo_combustivel == 'a':
        if litros <= 20 and litros > 0:
            return (litros * PRECO_ALCOOL) -  ((litros * PRECO_ALCOOL) * (3 / 100))
        
        elif litros > 20 and litros >0:
            return (litros * PRECO_ALCOOL) -  ((litros * PRECO_ALCOOL) * (5 / 100))
        
        else:
            return 0


    elif tipo_combustivel == "G" or tipo_combustivel == "g":

        if litros <= 20 and litros > 0:
            return (litros * PRECO_GASOLINA) -  ((litros * PRECO_GASOLINA) * (4 / 100))
        
        elif litros > 20 and litros >0:
            return (litros * PRECO_GASOLINA) -  ((litros * PRECO_GASOLINA) * (6 / 100))
        
        else:
            return 0

    else:
        print("tipo de combustivel invalido...")


if __name__ == "__main__":
    tipo = input("entre com o tipo de cobustivel: G (Gasolina), A (Alcool): ")
    litros = float (input("Quantidade de litros: "))

    try:
        print("total a pagar: R${:.2f}".format(calcular_desconto(tipo, litros)))
    except:
        print("erro ao calcular")
