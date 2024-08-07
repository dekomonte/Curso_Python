#Exercicio: Cálculo IMC

#Tabela Resultados
def resultado(imc):
    if imc < 17:
        print('Muito abaixo do peso')
    elif imc < 18.49:
        print('Abaixo do peso')
    elif imc < 24.99:
        print('Peso normal')
    elif imc < 29.99:
        print('Acima do peso')
    elif imc < 34.99:
        print('Obesidade I')
    elif imc < 39.99:
        print('Obesidade II (severa)')
    elif imc > 40:
        print('Obesidade III (eita!)')
    else:
        print('ERROR')


nome = input('Digite o nome: ')
peso = float(input('Digite o peso (kg): '))
h = float(input('Digite a altura (m): '))

imc = peso/(h ** 2)
resultado(imc)

