"""
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

while(True):
    nome_usuario = input('Informe seu nome de usuário: ')
    senha_usuario = input('Informe sua senha: ')
    
    if nome_usuario != senha_usuario:
        break
    print('Senha inválida para este usuário')   