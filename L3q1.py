'''1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido
'''


# nota = int(input('Digite um valor de 0 a 10: '))

# while( nota < 0 or nota > 10):
#     print('Valor inválido!!, Informe novamente:',end=' ')
#     nota = int(input())

while(True):
    nota = int(input('Digite um valor entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('Valor invalido!!', end=' ')
    else:
        break