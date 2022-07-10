import random
from time import sleep
n1 = input('Primeiro aluno: ')
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
print('O nome do aluno escolhido foi...')
print('PROCESSANDO...')
sleep(2)
print(f'{random.choice([n1, n2, n3, n4])}')