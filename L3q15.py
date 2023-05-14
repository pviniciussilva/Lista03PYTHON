'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.'''
numero = 0
while numero < 90:
  print(numero)
  if numero == 3:
    numero = numero + (numero - 1)
    print(numero) 
  else:
    numero = numero + numero - 
  numero += 1
  print(numero)
  numero = numero + (numero - 1)'''
