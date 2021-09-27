def fatorial(v):

    if v > 0:
        max_fat = 0;
        fat = 1 

        if v > 16:
            max_fat = 16
        else:
            max_fat = v

        while (max_fat > 1):  
            fat = fat * max_fat 
            max_fat -= 1 
        
        return fat
    else:
        print("numero negativo")
        return 0

if __name__ == "__main__":

    while True:
        valor = int(input("valor pra calcular o fatorial: "))
        print(fatorial(valor))