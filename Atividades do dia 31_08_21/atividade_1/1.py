def farenheit(farenheit):
    return (5 * (farenheit - 32)) / 9


if __name__ == "__main__":

    while(True):
        try:
            far = int(input("Temperatura em farenheit: "))
            celcius = farenheit(far)
            print("{:.1f}".format(celcius) + "° celcius\n")

        except:
            print("erro ao caclular...")
