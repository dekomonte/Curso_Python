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
"""
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""

#==========Operadores Logicos==========
"""
and (e) 
or (ou) 
not (não)
and -> Todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
Também existe o tipo None que é usado para representar um não valor
"""

# Operador lógico "not" -> Usado para inverter expressões
# not True = False
# not False = True