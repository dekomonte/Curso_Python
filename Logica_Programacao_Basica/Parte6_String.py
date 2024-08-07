#==========Strings==========

nome = 'Andressa'
sobrenome = 'Monteiro'
altura = 1.58687

#Formatacao com f-string
linha_1 = f'{nome} {sobrenome} tem {altura:.3f}'
print(linha_1)

#Formatacao com format
linha_2 = '{} {} tem {:.3f}'.format(nome, sobrenome, altura)
linha_3 = '{0} {1} tem {2:.3f}'.format(nome, sobrenome, altura)

print(linha_2)
print(linha_3)