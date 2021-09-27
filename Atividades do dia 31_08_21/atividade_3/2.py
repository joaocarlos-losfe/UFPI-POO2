def fatorial(v):
    fat = 1  
    while (v > 1):  
        fat = fat * v 
        v -= 1 
    
    return fat

if __name__ == "__main__":

    valor = int(input("valor pra calcular o fatorial: "))

    print(fatorial(valor))
