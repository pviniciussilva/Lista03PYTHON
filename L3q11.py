'''Altere o programa anterior para mostrar no final a soma dos números'''
numero1 = int(input('Digite um numero: ')) 
numero2 = int(input('Digite um numero: ')) 
soma = 0
if numero1 > numero2:
    while numero1 > numero2:
      soma += numero1
      numero1 -= 1
else:
    while numero2 > numero1:
      numero1 += 1
      soma += numero1
print(f'A soma entre os números informados é {soma}')
