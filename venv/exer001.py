#Nome
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

#exer007
'''
m1 = float(input('Digite a nota do M1: '))
m2 = float(input('Digite a nota do M2: '))
print('A média final deste aluno é de: {}'.format((m1+m2)/2))
'''

#exer008
'''
m = float(input('Digite o comprimento em metros: '))
print('Este comprimento equivale a {} cm e a {} milimetros.'.format((100*m), (1000*m)))
'''

#exer009
'''
n = int(input('Digite um numero para saber sua tabuada: '))
print('{} x 1 = {}'.format(n, (n*1)))
print('{} x 2 = {}'.format(n, (n*2)))
print('{} x 3 = {}'.format(n, (n*3)))
print('{} x 4 = {}'.format(n, (n*4)))
print('{} x 5 = {}'.format(n, (n*5)))
'''

#exer010
'''
r = float(input('Quantos reais o você possue na carteira? '))
d = float(input('Qual a cotação atual do dollar? '))
print('Com R${} é possivel comprr US${:.2f} :)'.format(r, (r/d)))
'''

#exer011
'''
a = float(input('Insira a altura da parede: '))
l = float(input('Insira o largura da parede: '))
t = (a*l)/2
print(' A parede possui {:.2f}m², portanto é necessário {:.2f} litros de tinta '.format(a*l, t))
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

#exer014
'''
c = float(input('Informe a temperatura em ºC: '))
f = (c * (9/5)) + 32
print('{:.2f} ºC na escala de Fahrenheit equivale a {:.2f} ºF.'.format(c, f))
'''

#exer015
'''
d = int(input('Por quantos dias este carro foi alugado? '))
km = float(input('Quantos Kms foram rodados?' ))
print('O valor total do aluguel deste carro foi de {:.2f}'.format((d*60)+(km*0.15)))
'''

#exer016
'''
import math

n = float(input('Informe um numero: '))
i = math.trunc(n)
print('A parte inteira de {} é de {}'.format(n, i))
'''

#exer017
'''
import math

co = float(input('Informe o cateto oposto: '))
ca = float(input('informe o cateto adjacente: '))
h = math.hypot(co,ca)
print('a Hipotenusa de {} e {} é igual a {:.2f}'.format(co, ca, h))

'''

#exer018

import math
'''
ang = float(input('Informe um algulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Seno = {} \nCoseno = {} \nTangente = {}'.format(sen, cos, tan))
'''

#exer019
'''
import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
sor = random.randr
print('O aluno sorteado foi o {}'.format(sor))
'''