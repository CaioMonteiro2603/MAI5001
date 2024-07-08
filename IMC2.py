def calcular_imc(altura, peso):
    # Calculando o IMC
    imc = peso / (altura ** 2)
    
    # Classificando o IMC de acordo com a OMS
    classificacao = ""
    if imc < 18.5:
        classificacao = "Baixo peso"
    elif imc <= 24.9:
        classificacao = "Peso adequado"
    elif imc <= 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    return imc, classificacao

# Solicitando ao usuário que digite as alturas e os pesos
print()
entradas = [
    input(),
    input(),
    input(),
    input(),
    input(),
    input()
]

# Processando cada entrada
for entrada in entradas:
    altura, peso = map(float, entrada.split(','))
    
    # Calculando o IMC e classificando-o
    imc, classificacao = calcular_imc(altura, peso)
    
    # Exibindo o resultado
    print(f"{imc:.2f} {classificacao}")
