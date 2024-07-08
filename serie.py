def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)

def formatted_harmonic_sum(n):
    return round(harmonic_sum(n), 3)

# Leitura da entrada
n = int(input())

# Calcula a soma harmônica e imprime o resultado formatado
print(formatted_harmonic_sum(n))
