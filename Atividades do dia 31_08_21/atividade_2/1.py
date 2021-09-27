def eh_triangulo(a, b, c):
    if ( a + b ) > c:
        return True
    elif (b + c) > a:
        return True
    elif ( a + c ) > b:
        return True
    else:
        return False

def tipo_triangulo(a, b, c):
    if eh_triangulo(a, b, c) and a == b and a == c:
        return "Equilatero"
    elif eh_triangulo(a, b, c) and (a == b and a != c ) or ( a == c and a != b):
        return "Isoceles"
    elif eh_triangulo(a, b, c) and (a != b and a != c) or (b != a and b != c) or (c != b and c != a):
        return "Escaleno"
    else:
        return "Não eh um triangulo"  
        

if __name__ == "__main__":
    a = int(input("lado a: "))
    b = int(input("lado b: "))
    c = int(input("lado c: "))

    try:
        print(tipo_triangulo(a,b,c))
    except:
        print("erro ao calcular...")