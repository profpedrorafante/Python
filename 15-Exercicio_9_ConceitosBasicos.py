# 9. Elabore um programa que permita a entrada de dois valores, x e y, troque seus valores entre si e então exiba os novos resultados.


x = int(input('Informe um número inteiro(x): '))
y = int(input('Informe um número inteiro(y): '))
print('O valor de x agora é: ', x)
print('O valor de y agora é: ', y)
print('\n')

troca = x
x = y
y = troca
print('O valor de x agora é: ', x)
print('O valor de y agora é: ', y)
