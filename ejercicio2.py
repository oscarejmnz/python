def generar_numeros_impares(n = 100):
    impares = []

    contador = 0
    numero = 0

    while contador < n:
        if bin(numero) == 1 :
            impares.append(numero)
            contador += 1
        
        numero += 1

    return impares