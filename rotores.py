def decode_char(char, rotor):
    if char.isalpha():
        if char.isupper():
            base = ord('A')
        else:
            base = ord('a')
        index = ord(char) - base
        decoded_index = rotor[index]
        return chr(decoded_index + base)
    else:
        return char

def decode_message(message, rotors):
    decoded_message = ""
    rotor1, rotor2, rotor3 = rotors
    for char in message:
        decoded_char = char
        decoded_char = decode_char(decoded_char, rotor1)
        decoded_char = decode_char(decoded_char, rotor2)
        decoded_char = decode_char(decoded_char, rotor3)
        decoded_message += decoded_char
    return decoded_message

rotors = []

# Lendo os valores dos rotores
for _ in range(3):
    rotor = list(map(int, input().split()))
    rotors.append(rotor)

# Lendo a mensagem cifrada
message = input().strip()

# Decodificando a mensagem
decoded_message = decode_message(message, rotors)

# Imprimindo a mensagem decodificada
print(decoded_message)
