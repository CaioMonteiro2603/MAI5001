class Funcionario:
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def get_departamento(self):
        return self.departamento

    def set_nome(self, nome):
        self.nome = nome

    def set_salario(self, horas_trabalhadas):
        if horas_trabalhadas > 50:
            horas_extras = horas_trabalhadas - 50
            valor_horas_extras = horas_extras * (self.salario / 50)
            self.salario += valor_horas_extras

    def set_departamento(self, departamento):
        self.departamento = departamento

    def __str__(self):
        # Verifica se o salário tem valor decimal significativo
        if self.salario == int(self.salario):
            return f"{self.nome} {self.salario:.1f} {self.departamento}"
        else:
            return f"{self.nome} {self.salario:.1f} {self.departamento}"

def encontrar_funcionario(nome, funcionarios):
    for f in funcionarios:
        if f.get_nome() == nome:
            return f
    return None

def funcionario_com_maior_salario(funcionarios):
    return max(funcionarios, key=lambda f: f.get_salario())

def media_salarial(funcionarios):
    total_salario = sum(f.get_salario() for f in funcionarios)
    return total_salario / len(funcionarios)

# Leitura da entrada
import sys
input = sys.stdin.read().strip().split('\n')
num_funcionarios = int(input[0])
funcionarios = []

# Criar lista de funcionarios
for i in range(1, num_funcionarios + 1):
    nome, salario, departamento = input[i].split()
    salario = float(salario)
    funcionarios.append(Funcionario(nome, salario, departamento))

opcao = int(input[num_funcionarios + 1])

# Executar as opções fornecidas pelo usuário
if opcao == 1:
    nome, horas_trabalhadas = input[num_funcionarios + 2].split()
    horas_trabalhadas = int(horas_trabalhadas)
    funcionario = encontrar_funcionario(nome, funcionarios)
    if funcionario:
        funcionario.set_salario(horas_trabalhadas)
        print(funcionario)

elif opcao == 2:
    funcionario = funcionario_com_maior_salario(funcionarios)
    print(funcionario)

elif opcao == 3:
    nome, novo_departamento = input[num_funcionarios + 2].split()
    funcionario = encontrar_funcionario(nome, funcionarios)
    if funcionario:
        funcionario.set_departamento(novo_departamento)
        print(funcionario)

elif opcao == 4:
    media = media_salarial(funcionarios)
    print(f"{media:.2f}")
