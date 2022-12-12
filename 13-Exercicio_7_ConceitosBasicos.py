# 7. Elabore um programa que calcule quantas notas de 50, 10 e 1 são
# necessárias para se pagar uma conta cujo valor é fornecido.
valorConta = int(input("Digite o valor da conta: "))

#Calcular Quantas notas de 50
quantidadeNotas50 = valorConta//50 # // no python retorna so a divisão inteira
valorRestante = valorConta - (quantidadeNotas50*50)

#Calcular Quantas notas de 10
quantidadeNotas10 = valorRestante//10
valorRestante = valorRestante - (quantidadeNotas10*10)

#Calcular Quantas notas de 1
quantidadeNotas1 = valorRestante//1
valorRestante = valorRestante - (quantidadeNotas1*1)


print('Para pagar a conta de: ', valorConta , '\n',
      'Vamos usar: ', quantidadeNotas50, ' notas de R$50,00\n'
                    , quantidadeNotas10, ' notas de R$10,00\n'
                    , quantidadeNotas1, 'notas de R$1,00')