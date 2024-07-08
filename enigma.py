def rotor_mapping(rotor):
    """
    Cria um dicionário de mapeamento de rotores para decifração.
    """
    mapping = {}
    for i in range(len(rotor)):
        mapping[chr(i + ord('a'))] = chr(rotor[i] + ord('a'))
    return mapping

def decrypt_message(message, rotors):
    """
    Decifra a mensagem utilizando os rotores fornecidos.
    """
    rotor1 = rotor_mapping(rotors[0])
    rotor2 = rotor_mapping(rotors[1])
    rotor3 = rotor_mapping(rotors[2])
    
    decrypted_message = []
    for char in message:
        if char.isalpha():
            if char.islower():
                decrypted_char = rotor3[rotor2[rotor1[char]]]
            else:  # se for maiúscula
                decrypted_char = rotor3[rotor2[rotor1[char.lower()]]].upper()
            decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(char)
    
    return ''.join(decrypted_message)

# Função para ler os rotores do input de uma vez só
def read_rotors_input():
    import sys
    input = sys.stdin.read
    lines = input().strip().split('\n')
    
    rotors = []
    for line in lines[1:]:  # ignora a primeira linha com "Rotores:"
        rotor_input = line.strip().split()
        rotor = [int(num) for num in rotor_input]
        rotors.append(rotor)
    
    return rotors

# Função para ler a mensagem criptografada do input
def read_encrypted_message():
    import sys
    input = sys.stdin.read
    return input().strip()

# Leitura dos rotores
rotors = read_rotors_input()

# Leitura da mensagem criptografada
encrypted_message = read_encrypted_message()

# Decifra a mensagem
decrypted_message = decrypt_message(encrypted_message, rotors)

# Imprime a mensagem decifrada
print(decrypted_message)