def eh_divisivel(a, b):
    return a % b == 0

def main():
    import sys
    input = sys.stdin.read().strip()  # Lê toda a entrada e remove espaços em branco extras
    data = input.split('\n')  # Divide a entrada em linhas
    
    # Lê Min e Max da primeira linha, considerando vírgulas como separadores
    Min, Max = map(int, data[0].replace(',', ' ').split())

    # Lê x e y da segunda linha, considerando vírgulas como separadores
    x, y = map(int, data[1].replace(',', ' ').split())

    resultados = []
    
    for num in range(Min, Max + 1):
        if eh_divisivel(num, x) and eh_divisivel(num, y):
            resultados.append(num)
    
    if resultados:
        print(','.join(map(str, resultados)))

if __name__ == "__main__":
    main()
