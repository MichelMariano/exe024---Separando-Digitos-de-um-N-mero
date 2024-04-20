# Faça um programa que leia de 0 à 9999 e mostre na tela cada um dos digitos separdos.

# Exemplo:
# Digite um número: 1834
# unidade: 4
# dezenas: 3
# centenas: 8
# milhar: 1

num = int(input('Informe um Número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {} '.format(num))
print('Unidade: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))
