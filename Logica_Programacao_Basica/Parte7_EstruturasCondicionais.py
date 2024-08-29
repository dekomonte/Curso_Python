#==========Estrutura Condicional==========
entrada = input("A luz deveria ser apagada?")

if entrada == 'sim':
    print("Ufa!")
elif entrada == 'nao':
    print("SAI DAQUI!!")
else:
    print("Triste")

print("FORA DO BLOCO")


#==========Operadores de Comparacao==========

#OP                          Exemplo (True)
#>       maior               2 > 1
#>=      maior ou igual      2 >= 2
#<       menor               1 < 2
#<=      menor ou igual      2 <= 2
#==      igual               'a' == 'a'
#!=      diferente           'a' != 'b'


#==========Operadores Logicos==========

#and (e)
#or (ou)
#not (não)
#and -> Todas as condições precisam ser verdadeiras
#None -> Usado para representar um não valor

# Operador lógico "not" -> Usado para inverter expressões
# not True = False
# not False = True

# Operadores in e not in
# in -> "está em"
# not in -> "não está em"
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
print(10 * '-')
nome = 'Otávio'

#Consigo acessar pelos índices + e -
print(nome[2])
print(nome[-4])

print('vio' in nome)
print('zero' in nome)

print('vio' not in nome)
print('zero' not in nome)

#Exemplo - String
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')


#Flag -> Marcar um local
#None -> não valor
#is e is not -> é ou não é (tipo, valor, identidade)
#id -> identidade
