def tabuada(tabuada_de, comeca_por, termina_em):

    print(f"\nVou montar a tabuada de {tabuada_de} começando em {comeca_por} e terminando em {termina_em}")

    for x in range(comeca_por, termina_em + 1):
        print(f"{tabuada_de} X {x} = {tabuada_de * x}")


if __name__ == "__main__":
    tabuada_de = int(input("Montar a tabuda de: "))
    comeca_por = int(input("Começa por: "))
    termina_em = int(input("Termina em: "))

    tabuada(tabuada_de, comeca_por, termina_em)
    