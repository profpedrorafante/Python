valor = float(input('Informe o valor do produto: '))
desconto = int(input('Informe o o valor(%) de desconto do produto: '))

print('Valor do produto R$', valor, '\n Valor de desconto ', desconto, '%', '\n')
print('Valor total com o desconto: R$', valor-(valor*(desconto/100)))