def calcular_operacao(entrada):
    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y if y != 0 else "Erro: divisão por zero",
                  '^': lambda x, y: x ** y if x != 0 or y != 0 else "Erro: base e expoente nulos"}
    
    for operador in operadores:
        if operador in entrada:
            num1, operador, num2 = entrada.partition(operador)
            num1 = int(num1)
            num2 = int(num2)
            
            resultado = operadores[operador](num1, num2)
            
            return resultado

# Entrada do usuário
entrada = input()

# Calcular o resultado da operação
resultado = calcular_operacao(entrada)
print(resultado)


