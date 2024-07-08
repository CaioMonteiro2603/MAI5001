def create_rotor(offsets):
    return [(offset + i) % 26 for i, offset in enumerate(offsets)]

def rotate_rotor(rotor):
    return rotor[1:] + [rotor[0]]

def decrypt(letter, rotor1, rotor2, rotor3):
    index = ord(letter) - ord('a')
    index = rotor3[rotor2[rotor1[index]]]
    return chr(index + ord('a'))

contador1 = 0
contador2 = 0
rotor1 = []
rotor2 = []
rotor3 = []
mensagem = ""

print("Insira os deslocamentos para o rotor 1 (0-25):")
rotor1 = [int(x) for x in input().split()]

print("Insira os deslocamentos para o rotor 2 (0-25):")
rotor2 = [int(x) for x in input().split()]

print("Insira os deslocamentos para o rotor 3 (0-25):")
rotor3 = [int(x) for x in input().split()]

print("\nMensagem")

while True:
    try:
        mensagem = input("")
        nova_mensagem = ""
        
        for letra in mensagem:
            if letra.isalpha():
                nova_letra = decrypt(letra.lower(), rotor1, rotor2, rotor3)
                nova_mensagem += nova_letra
                rotor1 = rotate_rotor(rotor1)
                contador1 += 1
                if contador1 == 26:
                    rotor2 = rotate_rotor(rotor2)
                    contador1 = 0
                    contador2 += 1
                    if contador2 == 26:
                        rotor3 = rotate_rotor(rotor3)
                        contador2 = 0
            else:
                nova_mensagem += letra
        
        print("Mensagem decifrada:", nova_mensagem)
        break  # Saia do loop enquanto
    except KeyboardInterrupt:  # Lidar com Ctrl+C para interromper a execução
        print("Operação interrompida pelo usuário.")
        break
