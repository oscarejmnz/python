def generar_numeros_primos(n = 100):
    primos = []

    contador = 0
    numero = 0

    while contador < n:
        if numero % contador == 0 :
            primos.append(numero)
            contador += 1
        
        numero += 1

    return primos