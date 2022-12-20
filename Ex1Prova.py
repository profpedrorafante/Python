print('Digite seu nome:')
nome = input()
sexo = input('Qual seu sexo(m/f):')
# se (sexo="f") e (sexo="F") entao
#  escreval("Você é do sexo feminino")
# senao
#
if (sexo == "f") and (sexo=="F"):
    print('Você é do sexo feminino')
elif(sexo=="m") and (sexo=="M"):
    print('Você é do sexo masculino')
else:
    print('Você digitou um valor de sexo inválido')


