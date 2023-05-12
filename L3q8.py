'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''
soma = 0
for n in range(1, 6):
  numero = int(input(f'Informe o {n}° número: '))
  soma += numero 
print(f'A soma dos número informados é {soma}')