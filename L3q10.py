'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
if numero1 > numero2:
    while numero1 > numero2:
      numero1 -= 1
      print(numero1)
else:
    while numero2 > numero1:
      print(numero1)
      numero1 += 1
