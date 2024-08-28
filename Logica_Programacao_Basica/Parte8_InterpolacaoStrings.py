#==========Interpolacao==========
"""
Interpolação básica de strings -> Semelhante ao format
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))

nome2 = 'Andressa'
idade = 26
altura = 1.58
cargo = 'estagiária'

print('Meu nome é %s, sou %s, tenho %d e %.1f' % (nome2,cargo,idade,altura))

#==========Formatacao==========
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal

(Caractere)(><^)(quantidade) -> Preencher com char
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'HOJE'
print(f'{variavel}')
print(f'{variavel: >10}.') #Adiciona 10 caracteres na esquerda
print(f'{variavel: <10}.') #Adiciona 10 caracteres na direita
print(f'{variavel: ^10}.')


print(f'{8534.487364746:0=+10,.1f}')
#ChatGPT
"""
0: Preenche o espaço à esquerda do número com zeros, se necessário.
=: Coloca o sinal (+ ou -) logo após o preenchimento de zeros, antes do número em si.
+: Inclui o sinal positivo + para números positivos e o sinal negativo - para números negativos.
10: Especifica que a largura total do campo (incluindo o sinal, os dígitos e as vírgulas) será de 10 caracteres.
,: Usa a vírgula como separador de milhar.
.1f: Formata o número com uma casa decimal.
"""

print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

#==========Fatiamento==========
"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::] -> inicio, fim, passo
len() -> retorna a quantidade de caracteres da string
"""
variavel = 'Olá mundo' #Manipulacao de vetores
print(variavel[::-1])
print(len(variavel))