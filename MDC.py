def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Entrada do usuário
a, b = map(int, input().split())

# Calcular o MDC
resultado = mdc(a, b)
print(resultado)
