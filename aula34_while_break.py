"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print('Seu nome é {}'.format(nome))

    if nome == 'sair':
        break

print('Acabou')