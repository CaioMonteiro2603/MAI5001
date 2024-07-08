class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        self.simplificar()

    def simplificar(self):
        gcd = self.mdc(self.numerador, self.denominador)
        self.numerador //= gcd
        self.denominador //= gcd

    def mdc(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, outra):
        novo_numerador = self.numerador * outra.denominador + outra.numerador * self.denominador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __sub__(self, outra):
        novo_numerador = self.numerador * outra.denominador - outra.numerador * self.denominador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __mul__(self, outra):
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __truediv__(self, outra):
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        return Fracao(novo_numerador, novo_denominador)

    def __eq__(self, outra):
        return self.numerador == outra.numerador and self.denominador == outra.denominador


# Função para ler e processar as operações
def processar_operacoes(entrada):
    operacoes = entrada.split()
    fracao1 = Fracao(*map(int, operacoes[0].split('/')))
    fracao2 = Fracao(*map(int, operacoes[1].split('/')))
    operador = operacoes[2]

    if operador == '+':
        resultado = fracao1 + fracao2
    elif operador == '-':
        resultado = fracao1 - fracao2
    elif operador == '*':
        resultado = fracao1 * fracao2
    elif operador == '/':
        resultado = fracao1 / fracao2
    elif operador == '==':
        resultado = fracao1 == fracao2
        return resultado

    return resultado

# Leitura da entrada
import sys
input = sys.stdin.read().strip()

# Processamento das operações
resultado = processar_operacoes(input)
print(resultado)
