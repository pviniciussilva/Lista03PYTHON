'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

    a. Tabuada de 5:
       5 X 1 = 5
       5 X 2 = 10
       ...
       5 X 10 = 50'''
num = int(input('Informe o número de qual tabuada você deseja: '))
print(f'Tabuada de {num}:')
for n in range(1, 11):
  print(f'{num} X {n} = {n * num}')