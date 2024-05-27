## Questão: Cálculo de Bônus com Entrada do Usuário

# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

# https://pt.stackoverflow.com/questions/66183/como-retornar-um-valor-no-formato-moeda-brasileiro-na-view-do-django

from datetime import datetime
import locale

#locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')  
nome_completo = str(input('Digite seu nome completo: '))
ano_bonus = datetime.now().year
salario = float(input('Digite o valor do seu salário: '))
premio = 1000.00

if salario <= 2000:
    percentual_bonus = 0.2
elif salario <= 5000:
    percentual_bonus = 0.3
else:
    percentual_bonus = 0.45

bonus_anual = ((salario + premio) * percentual_bonus)

print(f'Nome: {nome_completo}')
print(f'Salário: {locale.currency(salario)}')
print(f'Prêmio: {locale.currency(premio)}')
print(f'Porcentagem do bônus anual: {percentual_bonus * 100}%')
print(f'Bônus Anual: {locale.currency(bonus_anual)}')
