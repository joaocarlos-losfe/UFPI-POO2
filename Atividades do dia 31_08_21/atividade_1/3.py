def salario_bruto(salario_hora, numero_de_horas):
    return (numero_de_horas * salario_hora) * 30

def imposto_renda(salario):
    return salario * (11 / 100)

def imposto_inss(salario):
    return salario * (8 / 100)

def imposto_sindicato(salario):
    return salario * (5 / 100)

def calcular_salario_liquido(salario):
    return salario - (imposto_renda(salario) + imposto_inss(salario) + imposto_sindicato(salario))

def mostrar_tabela(salario_bruto, ir, inss, sindicato, salario_liquido):
    print(f"+ Salario bruto: R${salario_bruto}")
    print(f"- IR: R${ir}")
    print(f"- INSS: R${inss}")
    print(f"- Sindicato: R${sindicato}")
    print(f"- Salario liquido: R${salario_liquido}")


if __name__ == "__main__":
    salario_hora = float(input("💸 Quanto ganha por hora ?: "))
    numero_de_horas = int(input("📅 Numero de horas que trabalha no mês?: "))

    salario = salario_bruto(salario_hora, numero_de_horas)

    mostrar_tabela(salario, imposto_renda(salario), imposto_inss(salario), imposto_sindicato(salario), calcular_salario_liquido(salario))
