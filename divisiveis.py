def numeros_divisiveis_por_7_e_multiplos_de_5(min, max):
    numeros = []
    for i in range(min, max+1):
        if i % 7 == 0 and i % 5 == 0:
            numeros.append(str(i))
    return ",".join(numeros)

# Entrada dos valores mínimos e máximos
minimo, maximo = map(int, input().split(','))

# Chamada da função e impressão dos resultados
resultado = numeros_divisiveis_por_7_e_multiplos_de_5(minimo, maximo)
print(resultado)
