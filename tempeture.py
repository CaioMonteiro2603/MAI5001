def celsius_to_fahrenheit(celsius):
    fahrenheit = 9 * celsius / 5 + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273
    return kelvin

entrada = input().split()
temperatura = float(entrada[0])
escala = entrada[1]

if escala == "C":
    fahrenheit = celsius_to_fahrenheit(temperatura)
    kelvin = celsius_to_kelvin(temperatura)
    print("{:.1f} F".format(fahrenheit) if fahrenheit % 1 != 0 else "{:.0f} F".format(fahrenheit))
    print("{:.1f} K".format(kelvin) if kelvin % 1 != 0 else "{:.0f} K".format(kelvin))
else:
    print("Escala de temperatura inválida")
