#Faça um programa que peça ao usuário para digitar um número inteiro,
#informe se este número é par ou ímpar. Caso o usuário não digite um número
#inteiro, informe que não é um número inteiro.

num = input("Digite um número inteiro: ")
p1 = int(num)
if p1 % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")

#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
#descrito, exiba a saudação apropriada.
#Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

hora = int(input("Digite uma hora (só números inteiros serão aceitos): "))

if hora >= 0 and hora < 12:
    print("Bom dia")
elif hora > 11 and hora < 18:
    print("Boa tarde")
else:
    print("Boa noite")

#Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
#menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
#Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

nome = input("Digite seu nome:")
tam_nome = len(nome)

if tam_nome < 4:
    print("Seu nome é curto")
elif tam_nome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")