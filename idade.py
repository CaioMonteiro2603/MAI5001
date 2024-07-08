def ler_data_nascimento():
    entrada = input()
    entrada = list(map(int,entrada.split('/')))
    dia = entrada[0]
    mes = entrada[1]
    ano = entrada[2]
    return dia,mes,ano

def transformar_data_dias(dia,mes,ano):
    ano_dias = ano*365
    mes_dias = mes*(365/12)
    total_dias = ano_dias + mes_dias + dia
    return total_dias

def calcula_idade(dia_nascimento,mes_nascimento,ano_nascimento):
    #Transformar a data atual em dias
    dias_atual = transformar_data_dias(4,4,2024)

    #Transformar a data de nascimento em dias
    dias_nascimento = transformar_data_dias(dia_nascimento,mes_nascimento,ano_nascimento)

    #calcular a diferença de dias entre a data atual e o nascimento
    diferenca_dias = dias_atual - dias_nascimento

    #Pegar a diferença de dias e dividir por 365 para ter em ano
    ano_nascimento = int(diferenca_dias/365)

    #Extrair a casa decimal para ter a quantidade de meses
    mes_nascimento_perc = (diferenca_dias/365) - ano_nascimento

    #Multiplicar o percentual pela quantidade d emeses no ano
    mes_nascimento = int(mes_nascimento_perc * 12)
    
    #Extrair a casa decimal para ter a quantidade de dias
    dia_nascimento_perc = (mes_nascimento_perc * 12) - mes_nascimento

    #Multiplicar o percentual pela quantidade de dias no mes
    dia_nascimento = int(dia_nascimento_perc * (365/12))+2 #Valor de Compensação 

    return dia_nascimento,mes_nascimento,ano_nascimento

def devolve_output(dia_nascimento,mes_nascimento,ano_nascimento):
    if dia_nascimento == 1:
        str_dia = 'dia'
    else: str_dia = 'dias'
    if mes_nascimento ==1:
        str_mes = 'mes'
    else: str_mes = 'meses'
    if ano_nascimento ==1:
        str_ano = 'ano'
    else: str_ano = 'anos'
    return print('{} {}, {} {} e {} {}'.format(ano_nascimento,str_ano,mes_nascimento,str_mes,dia_nascimento,str_dia))


#Algoritmo
#Ler data de nascimento
d,m,a = ler_data_nascimento()

#Calcular idade
d,m,a = calcula_idade(d,m,a)
#Devolve output
devolve_output(d,m,a)