# 5. Faça um programa que calcule o valor de desconto para um determinado produto,
# faça um Print Screen do código fonte do seu programa e também do programa em execução.

valor = float(input('Informe o valor do produto: '))
desconto = int(input('Informe o o valor(%) de desconto do produto: '))

print('Valor do produto R$', valor, '\n Valor de desconto ', desconto, '%', '\n')
print('Valor total com o desconto: R$', valor - (valor * (desconto / 100)))
