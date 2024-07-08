
def receber_input():
    entrada = input()

    entrada = entrada.split(',')
    altura = float(entrada[0])
    massa = float(entrada[1])

    return altura,massa

def calcular_peso(altura, massa):
    IMC = massa/(altura)**2
    return IMC

def calcular_multiplos_imcs():
    imcs = []
    while True:
        try:
            altura,massa = receber_input()
            imc = round(calcular_peso(altura, massa), 2)
            imcs.append(imc)
        except:
            break
    return imcs
    
def devolver_output(imcs):
    output = ['{:.2f}'.format(n) for n in imcs]
    print(*output)

imcs = calcular_multiplos_imcs()

devolver_output(imcs)

    