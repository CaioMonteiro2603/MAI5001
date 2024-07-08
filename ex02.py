import math

class Complexo:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complexo(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complexo(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.imag * other.real + self.real * other.imag
        return Complexo(real_part, imag_part)
    
    def __truediv__(self, other):
        r_squared = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / r_squared
        imag_part = (self.imag * other.real - self.real * other.imag) / r_squared
        return Complexo(real_part, imag_part)
    
    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
    
    def __str__(self):
        return f"{self.real:.2f}{'+' if self.imag >= 0 else ''}{self.imag:.2f}i"

# Função para calcular o resultado das operações
def calcular_operacoes(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == 'abs':
        return abs(num1), abs(num2)
    elif op == '==':
        return num1 == num2
    else:
        return None

# Entrada das operações e números complexos
entrada = input().split()
num1 = Complexo(*map(float, input().split(',')))
num2 = Complexo(*map(float, input().split(',')))

# Iteração sobre as operações e impressão dos resultados
for op in entrada:
    resultado = calcular_operacoes(op, num1, num2)
    if isinstance(resultado, tuple):
        print(f"{op}:{resultado[0]:.2f}")
        print(f"{op}:{resultado[1]:.2f}")
    elif resultado is not None:
        print(f"{op}:{resultado}")
