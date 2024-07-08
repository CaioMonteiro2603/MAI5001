def calcular_imc(altura, peso):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25:
        return "Peso adequado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Leitura da entrada
import sys
input = sys.stdin.read().strip()
linhas = input.split()
alturas_pesos = []

for linha in linhas:
    if linha.strip():  # Ignora linhas vazias
        try:
            altura, peso = map(float, linha.replace(' ', '').split(','))
            alturas_pesos.append((altura, peso))
        except ValueError:
            pass  # Ignora entradas malformadas

# Para cada par de altura e peso, calcula o IMC e imprime o resultado formatado
for altura, peso in alturas_pesos:
    imc = calcular_imc(altura, peso)
    classificacao = classificar_imc(imc)
    print(f"{imc:.2f} {classificacao}")
