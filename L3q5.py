'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação'''
populacao1 = int(input('Digite a quantidade da 1° população: '))
porcentagem1 = float(input('Infor a taxa de crescimento da 1° população: '))
populacao2 = int(input('Digite a quantidade da 2° população: '))
porcentagem2 = float(input('Informe a taxa de crescimento da 2° população: '))
contador = 0
if populacao1 > populacao2:
  maior = populacao1
  menor = populacao2
else:
  maior = populacao2
  menor = populacao1
while (menor < maior):
  menor += menor * porcentagem1
  maior += maior * porcentagem2
  contador += 1
print(f'Passaram {contador} anos')
print(f'A quantidade da maior população atualmente é {maior}\nE a quantidade da menor população atualmente é {menor}')