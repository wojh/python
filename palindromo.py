#53 - Programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input("Tecle a frase: ").strip()

frase_clear = frase.replace(" ", "")

esarf_clear = frase_clear[::-1]

if esarf_clear == frase_clear:
    print(f"SIM, '{frase}' é PALÍNDROMO")
else:
    print(f"NÃO, '{frase}' não é PALÍNDROMO")
