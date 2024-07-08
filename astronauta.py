
import time

def andar_espiral(N,P):
    num = 1
    inicio = 0
    fim = N
    
    while inicio < fim:
        #Anda na borda superior
        for i in range(inicio, fim):
            #print(num,inicio,i)
            if num==P: return inicio , i
            num += 1
            
        #Anda na borda direita
        for i in range(inicio + 1, fim):
            #print(num,i , fim - 1)
            if num==P: return i , fim - 1
            num += 1
            
        #Anda na borda inferior
        for i in range(fim - 2, inicio - 1, -1):
            #print(num,fim - 1 , i)
            if num==P: return fim - 1 , i
            num += 1
               
        #Anda na borda esquerda
        for i in range(fim - 2, inicio, -1):
            #print(num,i , inicio)
            if num==P: return i , inicio
            num += 1

        inicio += 1
        fim -= 1

def main():

    parametros = input().split(" ")
    N = int(parametros[0])
    P = int(parametros[1])

    L = N * N
    if P > L:
        print(f"O astronauta ja saiu em missao ha {P - L} chamadas.")
        return
    
    i, j = andar_espiral(N,P)
    
    if P == L:
        print(f"O astronauta esta na posicao: {i} {j}\nPreste atencao, astronauta, chegou a sua vez!")
    else:
        print(f"O astronauta esta na posicao: {i} {j}\nAinda faltam {L - P} chamadas para a sua vez!")

if __name__ == "__main__":
    main()

time.sleep(0.8)