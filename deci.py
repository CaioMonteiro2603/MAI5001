def decimal_para_ascii(numero):
    # Convertendo o número decimal para sua representação em bytes
    bytes_string = numero.to_bytes((numero.bit_length() + 7) // 8, 'big')

    # Convertendo cada byte em caractere ASCII
    ascii_string = bytes_string.decode('ascii', errors='replace')

    return ascii_string

# Solicitando ao usuário que digite o número de entrada
entrada = int(input())

# Convertendo o número de entrada para caracteres ASCII e exibindo a saída
saida = decimal_para_ascii(entrada)
print( saida)
