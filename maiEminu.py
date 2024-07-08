def contar_maiusculas_minusculas(frase):
    maiusculas = 0
    minusculas = 0
    
    for caractere in frase:
        if caractere.isalpha():
            if caractere.isupper():
                maiusculas += 1
            elif caractere.islower():
                minusculas += 1
    
    return maiusculas, minusculas

frase = input()
maiusculas, minusculas = contar_maiusculas_minusculas(frase)
print("Maiúsculas:", maiusculas)
print("Minúsculas:", minusculas)
