def generar_numeros_pares(n = 100):
    pares = []

    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        
        numero += 1

    return pares