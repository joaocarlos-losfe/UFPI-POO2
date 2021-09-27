def calcular_exesso(peso_peixe):
    if peso_peixe > 50:
        return  peso_peixe - 50;
    else:
        return 0

def calcular_multa(excesso):
    if(excesso > 0):
        return excesso * 4
    else:
        return 0

def mostrar_mensagem(multa, excesso):
    if multa == 0:
        print("não pagará multa ✅")
    else:
        print(f"⚠️ excesso de peso de {excesso}. pagará uma multa de R${multa}")
    


if __name__ == "__main__":

    while True:
        try:
            peso_peixe = float(input("⚖️ Entre com o peso do peixe: "))
            excesso = calcular_exesso(peso_peixe)
            multa = calcular_multa(excesso)
            mostrar_mensagem(multa, excesso)
        
        except:
            print('erro ao calcular. digitou um número float ?')


