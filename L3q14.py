'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''
totimpar = totpar = 0
for n in range(1, 11):
  num = int(input(f'Digite o {n}° número: '))
  if num % 2 == 1:
    totimpar += 1
  else:
    totpar += 1
print(f'O total de números ímpares foi {totimpar}')
print(f'E o total de números pares foi {totpar}')