# Nome
'''
nome = input('Qual é o seu nome? ')
sobre = input('E seu sobrenome?')
print('Olá {} {}, muito prazer!'.format(nome, sobre))
'''

# soma
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

# Propriedades
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

# exercicio 005
'''
n = int(input('Digite um numero: '))
print('O seu susessor é {} e seu antessessor é {}!'.format(n+1, n-1))
'''

# exercicio 006
'''
n = int(input('Digite um numero: '))
print('Seu dobro é {}, seu triplo é {} e sua raiz é {}'.format(n*2, n*3, n**(1/2)))
'''

# exercicio 007
'''
m1 = float(input('Digite a nota do M1: '))
m2 = float(input('Digite a nota do M2: '))
print('A média final deste aluno é de: {}'.format((m1+m2)/2))
'''

# exercicio 008
'''
m = float(input('Digite o comprimento em metros: '))
print('Este comprimento equivale a {} cm e a {} milimetros.'.format((100*m), (1000*m)))
'''

# exercicio 009
'''
n = int(input('Digite um numero para saber sua tabuada: '))
print('{} x 1 = {}'.format(n, (n*1)))
print('{} x 2 = {}'.format(n, (n*2)))
print('{} x 3 = {}'.format(n, (n*3)))
print('{} x 4 = {}'.format(n, (n*4)))
print('{} x 5 = {}'.format(n, (n*5)))
'''

# exercicio 010
'''
r = float(input('Quantos reais o você possue na carteira? '))
d = float(input('Qual a cotação atual do dollar? '))
print('Com R${} é possivel comprr US${:.2f} :)'.format(r, (r/d)))
'''

# exercicio 011
'''
a = float(input('Insira a altura da parede: '))
l = float(input('Insira o largura da parede: '))
t = (a*l)/2
print(' A parede possui {:.2f}m², portanto é necessário {:.2f} litros de tinta '.format(a*l, t))
'''

# exercicio 012
'''
p = float(input('Informe o valor do produto: '))
d = float(input('Informe o desconto em %: '))
np = p * (1 - (d/100))
vd = p - np
print('Na liquidação de {}% de desconto, este produto, de R${} sai por R${:1.2f}, o valor do desconto é de R${:1.2f}'.format(d, p, np, vd))
'''

# exercicio 013
'''
s = float(input('Informe o salário do funcionário: '))
print('Com o aumento de 15%, o salário deste funcionário passa a ser R${:1.2f}'.format(s*1.15))

'''

# exercicio 014
'''
c = float(input('Informe a temperatura em ºC: '))
f = (c * (9/5)) + 32
print('{:.2f} ºC na escala de Fahrenheit equivale a {:.2f} ºF.'.format(c, f))
'''

# exercicio 015
'''
d = int(input('Por quantos dias este carro foi alugado? '))
km = float(input('Quantos Kms foram rodados?' ))
print('O valor total do aluguel deste carro foi de {:.2f}'.format((d*60)+(km*0.15)))
'''

# exercicio 016
'''
import math

n = float(input('Informe um numero: '))
i = math.trunc(n)
print('A parte inteira de {} é de {}'.format(n, i))
'''

# exercicio 017
'''
import math

co = float(input('Informe o cateto oposto: '))
ca = float(input('informe o cateto adjacente: '))
h = math.hypot(co,ca)
print('a Hipotenusa de {} e {} é igual a {:.2f}'.format(co, ca, h))

'''

# exercicio 018
'''
import math
ang = float(input('Informe um algulo qualquer: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Seno = {} \nCoseno = {} \nTangente = {}'.format(sen, cos, tan))
'''

# exercicio 019
'''
import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
sor = [a1, a2, a3, a4]
print('O aluno sorteado foi o {}'.format(random.choice(sor)))
'''

# exercicio 020
'''
import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
sor = [a1, a2, a3, a4]
#print(sor)
a = random.choice(sor)
sor.remove(a)
b = random.choice(sor)
sor.remove(b)
c = random.choice(sor)
sor.remove(c)
d = sor[0]
print('f1 = {} \nf2 = {} \nf3 = {} \nf4 = {}'.format(a, b, c, d))
'''

# exercicio 020_2
'''
from random import shuffle

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
sor = [a1, a2, a3, a4]
sor.sort()
print(sor)
shuffle(sor)
print(sor)
'''

# exercicio 021

#import playsound
# cond = str(input('Deseja tocar a musica?(s/N) '))


# Fedora baixar libs: playsound, pycairo, pyGoObject
'''
 if cond == 's':
    audio = r'/home/luiz/Música/guitar.mp3'
    playsound.playsound(audio)

# win10
  '''
#audio = r'C:\Users\Zanetti\Downloads\metal-guitar-11.mp3'
#playsound.playsound(audio)


# exercicio 022
'''
n = str(input('Insira o nome completo: '))
n = n.strip()
letras = len(n) - n.count(' ')

print("""Maisculo: {}

Minusculo: {}

Nº de letras: {}

Letras 1º nome: {}""".format(n.upper(), n.lower(), letras, n.find(' ')))
'''

# exercicio 023
'''
ni = int(input('Digite um numero: '))
u = ni // 1 % 10
d = ni // 10 % 10
c = ni // 100 % 10
m = ni // 1000 % 10

print("Un: {} \nDe: {} \nCe: {} \nMi: {}".format(u, d, c, m))
'''

# exercicio 24
'''
cid = str(input('Cidade: ')).strip()

if cid[:5].upper() == 'SANTO':
    print('O nome da cidade começa com Santo')
else:
    print('O nome da cidade Não começa com Santo')
'''

# exercicio 25
'''
nome = str(input('Nome: ')).strip()
if 'SILVA' in nome.upper():
    print('Este nome possue Silva.')
else:
    print('Não possue Silva')
'''

# exercicio 26
'''
nome = str(input('Nome: ')).strip()
na = nome.upper().count('A')
pa = nome.upper().find('A')
ua = nome.rfind('a')
print('Numeros de A: {}'.format(na))
print('Posição do 1º A: {}'.format(pa))
print('Posição do ultimo A: {}'.format(ua))
'''

# exercicio 27
'''
nome = str(input('Nome: '))
nome = nome.strip()
lnome = nome.split()
print(lnome[0])
print(lnome[len(lnome)-1])

'''

# exercicio 28
'''
from random import randint
from time import sleep
num = int(input('Pense em um numero entre 0 e 5: '))
if num == randint(0, 5):
    sleep(2)
    print('Ganhou')
else:
    sleep(2)
    print('Perdeu')
'''

# exercicio 29
'''
from random import randint

vel = randint(50, 120)
print('Radar: Velocidade lida - {} Km/h'.format(vel))
if vel > 80:
    mul = (vel - 80) * 7.00
    print('Velocidade acima do limite de 80 Km/h')
    print('Valor da multa a ser paga: R${:.2f}'.format(mul))
'''

# exercicio 30
'''
n = int(input('Digite um numero inteiro: '))
if (n % 2) == 0:
    print('{} é par.'.format(n))
else:
    print('{} é impar.'.format(n))
'''

# exercicio 31
'''
v = float(input("Quantos Km's de viagem? "))
p = 0.5
if v > 200:
    p = 0.45
print('Valor da passagem: R$ {:.2f}'.format(v*p))
'''

# exercicio 32
'''
a = int(input('Digite o ano: '))
print('Este é bisexto.') if (a % 4) == 0 else print('Não é bisexto')
'''

# exercicio 33
'''
p = int(input('1º nº: '))
s = int(input('2º nº: '))
t = int(input('3º nº: '))
i = True
if p == s == t:
    print('Os 3 numeros são iguais.')
    i = False
elif p > s > t or p == s > t:
    ma = p
    me = t
elif s > t > p or s == t > p:
    ma = s
    me = p
elif t > p > s or t == p > s:
    ma = t
    me = s
elif s > p > t or s == p > t:
    ma = s
    me = t
elif p > t > s or p == t > s:
    ma = p
    me = s
elif t > s > p or t == s > p:
    ma = t
    me = p
if i:
    print('O maior numero é {} e o menor é {}'.format(ma, me))
'''

# exercicio 34
'''
sal = float(input('Qual o salário do funcionário? '))
print('Calculando aumento...')
a = 0.15
if sal > 1250:
    a = 0.1
print('O valor do aumento deve ser de R${:.2f}, totalizando um salário de R${:.2f}'.format(sal * a, sal * (1 + a)))
'''

# exercicio 35
'''
a = float(input('Informe o comprimento da reta a: '))
b = float(input('Informe o compromento da reta b: '))
c = float(input('Informe o comprimento da reta c: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Estas retas podem formar um triangulo')
else:
    print('Estas retas NAO podem formar um triangulo')    
'''

# exercicio 36

imo = float(input('Qual o valor do imovel? '))
sal = float(input('Qual o seu salário? '))
par = int(input('em quantas parcelas'))

imop = imo / par

if imop > (sal * 0.3):
    print()

