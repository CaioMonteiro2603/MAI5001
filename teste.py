import math

def s1(x, n):
    soma = 0
    sinal = 1
    for i in range(1, 2 * n + 1, 2):
        termo = (x ** i) / math.factorial(i)
        soma += sinal * termo
        sinal *= -1
    return soma

def s2(x, n):
    def termo(i):
        return (-1) ** i * (x ** (2 * i)) / math.factorial(2 * i)

    def serie_recursiva(i, soma=0):
        if i == n:
            return soma
        else:
            return serie_recursiva(i + 1, soma + termo(i))

    return serie_recursiva(0)


x, n = map(float, input().split())

# Convertendo n para inteiro
n = int(n)

resultado_s1 = s1(x, n)
resultado_s2 = s2(x, n)

print("{:.3f}".format(resultado_s1))
print("{:.3f}".format(resultado_s2))
