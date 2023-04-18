'''Faça um programa que leia e valide as seguintes informações:
    a. Nome: maior que 3 caracteres;
    b. Idade: entre 0 e 150;
    c. Salário: maior que zero;
    d. Sexo: 'f' ou 'm';
    e. Estado Civil: 's', 'c', 'v', 'd';'''

nome = input('nome: ')
while(len(nome) < 3):
    print('nome invalido digite novamente')
    nome = input('nome: ')
Idade = int(input('Iforme sua idade: '))
while(Idade < 0 or Idade > 150):
    print('Idade invalida digite novamente')
    Idade = int(input('Iforme sua idade: '))
Salario = float(input('Iforme seu salario: '))
while(Salario < 0):
    print('Salario invalido digite novamente')
    Salario = float(input('Iforme seu salario: '))
Sexo = input('Digite seu sexo "f" ou "m": ').lower()
while(Sexo != 'f' and Sexo != 'm'):
    print('Sexo invalido digite novamente')
    Sexo = input('Digite seu sexo "f" ou "m": ').lower()
Estado_civil = input('Digite seu estado civil "s", "c", "v", "d": ').lower()
while(Estado_civil not in ["s", "c", "v", "d"]):
    print('Estado civil invalido digite novamente')
    Estado_civil = input('Digite seu estado civil "s", "c", "v", "d": ').lower()