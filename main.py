# aqui eu importo random para eu conseguir escolher escolhas aleatorias tipo numeros simbolos etc 
import random

# aqui eu importo string para eu conseguir todas as strings uppercase / maiuscula e lowercase / minuscula
import string

# aqui eu pergunto quantos caracteres vai ter na sua senha tipo 5 = agaw5
caracteres = input("Quantos caracteres vai ter sua senha: ")

# aqui eu verifico se o caracteres e um digito / numero se for transforma em numero de verdade pois o input retorna uma string
if caracteres.isdigit():
    caracteres = int(caracteres)

    # a stringupper vale ABCDEFGH... todas as letras do alfabeto
    stringsUpper = string.ascii_uppercase

    # a stringlower vale abcdefgh... todas as letras do alfabeto
    stringsLower = string.ascii_lowercase

    # o numeros vale 12345... todos os numeros 1 a 10
    numeros = string.digits

    # os simbolos vale esses abaixo
    simbolos = "!@#$%^&*"

    # aqui a gente junta tudo para depois usar eles vai ficar tipo ABCDE.abcde.1234.#!@%
    todos = stringsUpper + stringsLower + numeros + simbolos

    # aqui a senha vale uma string vazia a entra uma escolha aleatoria do todos e junta aleatoriamente
    senha = "".join(random.choices(todos, k=caracteres))

    # aqui printa sua senha foi gerada : ai a senha formatada
    print(f"Sua senha gerada foi: {senha}")

else:
    # se nao for um numero printa digite um inteiro
    print("Digite um inteiro!")
