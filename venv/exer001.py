Nome
'''
nome = input('Qual é o seu nome? ')
sobre = input('E seu sobrenome?')
print('Olá {} {}, muito prazer!'.format(nome, sobre))
'''



#soma
'''
n1 = int(input('Informe o 1 numero: '))
n2 = int(input('Informe o 2 numero: '))
s = n1 + n2
m = n1 - n2
v = n1 * n2
d = n1 / n2
di = n1 // n2
ds = n1 % n2
print(' Soma = {}|\n Sub {}|\n Vez {}|\n Div {:.3}|'.format(s, m, v, d))
'''


#Propriedades
'''
sAlgo = input('Digite algo: ')
print('Propriedades sobre: {}'.format(sAlgo))
print(type(sAlgo))
print('É Alfa? {}'.format(sAlgo.isalpha()))
print('É Numerico? {:@^10}'.format(sAlgo.isnumeric()))
print('É Alphanumérico? {}'.format(sAlgo.isalnum()))
print('Só tem espaços? {}'.format(sAlgo.isspace()))
print('É Maiusculo? {}'.format(sAlgo.isupper()))
print('É minusculo? {}'.format(sAlgo.islower()))
print('É captalizado? {}'.format(sAlgo.istitle()))
'''





#exer005
'''
n = int(input('Digite um numero: '))
print('O seu susessor é {} e seu antessessor é {}!'.format(n+1, n-1))
'''

#exer006
'''
n = int(input('Digite um numero: '))
print('Seu dobro é {}, seu triplo é {} e sua raiz é {}'.format(n*2, n*3, n**(1/2)))
'''

#exer011
'''
a = float(input('Insira a altura da parede: '))
l = float(input('Insira o largura da parede: '))
t = (a*l)/2
print(' A parede possui {}m², portanto é necessário {} litros de tinta '.format(a*l, t))
'''


#exer012
'''
p = float(input('Informe o valor do produto: '))
d = float(input('Informe o desconto em %: '))
np = p * (1 - (d/100))
vd = p - np
print('Na liquidação de {}% de desconto, este produto, de R${} sai por R${:1.2f}, o valor do desconto é de R${:1.2f}'.format(d, p, np, vd))
'''

#exer013
'''
s = float(input('Informe o salário do funcionário: '))
print('Com o aumento de 15%, o salário deste funcionário passa a ser R${:1.2f}'.format(s*1.15))
'''


#teste de alteração via console para o git
