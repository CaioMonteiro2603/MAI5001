def soma_serie(n):
    if n == 0:
        return 0
    else:
        return (soma_serie(n-1) / 2) + 1

# Lendo o valor de n
n = int(input())

# Calculando a soma da série
resultado = soma_serie(n)

print(resultado)
