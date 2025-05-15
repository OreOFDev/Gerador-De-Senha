# Importei os modulos random string time e pyperclip usando um metodo de importar varios modulos em uma linha
import random as r,string as s,time as t, pyperclip as p 

# c = caracteres / pergunto quantos caracteres a pessoa quer
c = input("Quantos caracteres voce deseja na sua senha: ")

# tente
try:
    # trasnforma o c em int
    c = int(c)

    # criei a variavel senha que é igual a nada
    senha = ""

    # criei a variavel simbolos que eu mesmo escolhi eles
    simbolos = "!@#$%&*"

    # criei as variaveis de numeros letras minusculas e maiusculas usando o modulo s = string que eu importei no comeco
    numeros = s.digits
    letrasMinusculas = s.ascii_lowercase
    letrasMaiusculas = s. ascii_uppercase

    # criei a variavel tudo que vai ser igual a todas as variaveis anteriores exemplo: !@#$%&*0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    tudo = simbolos + numeros + letrasMinusculas + letrasMaiusculas 

    # faco um for com o range de c = caracteres
    for i in range(c):

        # ai ele vais somando ate dar os caracteres que a pessoa pediu
        senha += r.choice(tudo)
    
    # printo gerando senha para ficar mais profissional
    print("Gerando Senha Aguarde...")

    # deixo o codigo parar por 1.5 segundos para realmente parecer que ta gerando
    t.sleep(1.5)

    # printo a senha
    print(f"A Sua Senha Gerada É {senha}")

    # pergunto se quer copiar e deixo na variavel co = copiar  e transformo em lowercase
    co = input("Deseja copiar a senha? (s/n): ").lower()

    # se co for igual a s copio a senha
    if co == "s":
        p.copy(senha)

    # senao so passo / o codigo so para
    else:
        pass
     
# se la no comeco dar erro para transformar o c em int ele vai dar esse erro de ValueError e passar
except ValueError:
    pass
