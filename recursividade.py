def serie(n):
    if n == 0:
        return 0
    else:
        return (1 / (2 * n - 1)) - serie(n - 1)

def soma_serie(n):
    if n == 0:
        return 0
    else:
        return serie(n) + soma_serie(n - 1)

# Testando a função com o exemplo dado
n = 7
resultado = soma_serie(n)
print(resultado)
