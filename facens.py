"""
# exercicio 1
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))

if a > b:
	print(f'O maior numero é o {a} primeiro.')
elif a == b:
	print('Os dois numeros são iguais.')
else:
	print(f'O maior numero é o {b} segundo.')



# exercicio 2
senha = 'luiz'
while True:
	if input('Adivinhe a senha: ') == senha:
		print('Acertou! \o/')
		break
	print('Errou tente novamente. =/')


senha = 'luiz'
tent = ''
while tent != senha:
	tent = input('Adivinhe a senha: ')
print('Acertou! \o/')

"""
"""	
#exerc 1
a = int(input('Primeiro numero: '))	
b = int(input('Segundo numero: '))
print(a + b)

#exerc 2
m = int(input('Digite o comprimento em metros: '))
print(f'{m * 1000} milimetros')

#exerc 3
d = int(input('Dias: '))
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))
tot = s + (m * 60) + (h * 3600) + (d * 86400)
print(f'Total de {tot} segundos.')

#exerc 4
sal = float(input('Salarário: '))
aum = float(input('Aumento em %:'))
vaum = sal * (aum / 100)
nsal = sal + vaum
print(f'Valor do aumento R${vaum:.2f}')
print(f'Valor do novo salário R${nsal:.2f}')

#exerc 5
prod = float(input('Valor do produto: '))
desc = float(input('Valor do desconto (%): '))
vdesc = prod * (desc/100)
print(f'Valor do desconto R${vdesc:.2f}')
print(f'Valor do produto com o desconto R${(prod - vdesc):.2f}')


#exerc 6
s = float(input('Distancia da viagem (km): ')) * 1000
v = float(input('Velocidade média da viagem (km/h): ')) * 0.277778
t = (s/v)/3600
print(f'O tempo de viagem será de {t:.1f} horas') 


#exerc 7
c = float(input('Temperatura em ºC: '))
f = (9 * (c / 5) + 32)
print(f'Temperatura em ºF: {f:.2f}')
"""


#exercicio lista
"""
v = []
for i in range(5):
	v.append(int(input('Digite um numero: ')))
print(v) 
v2 = []
[v2.append(int(input('digite: '))) for i in range(5)]
print(v2)


v = [5, 3, 7, 8, 10, 12]

print(max(v))

maxv = 0
for i in v:
	if maxv < i:
		maxv = i
print(maxv)
	
print(v[:4])
print(v[4:])


print(v)
for i in range(4):
	print(v[i])
print('-' * 20)
for i in range(4, 6):
	print(v[i])

 """
# m = [[0,0,0],[0,0,0],[0,0,0]]

# inp = input('O que deseja inserir? ')
# lin = int(input('Em qual linha? '))
# col = int(input('Em qual coluna? '))
# m[lin][col] = inp

# [print(l) for l in m


# v = []
# [[v.append(0) for l in range(3)] for c in range(5)]
# [print(l) for l in v]
# def parimpar(numero):
# 	if numero % 2:
# 		return 'Impar'
# 	else:
# 		return 'Par'
	

# print(parimpar(int(input('Numero: '))))


# def fatorial(n):
# 	fat = n
# 	while n > 1:
# 		fat *= (n - 1)
# 		n -= 1
# 	return fat



# def f(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n * f(n-1)

# print(f(4))

def imprimiMenu():
	print(""" Selecione a opção:
 1 - Mostrar as cadeiras
 2 - Contar lugares disponíveis
 3 - Comprar cadeira
 4 - Cancelar compra
 5 - Terminar operação
		""")


def imprimiMatriz():
	[print(l) for l in lugares]


def contador(imprimir=False):
	cont = 0
	for lin in range(4):
		for col in range(5):
			if lugares[lin][col] != 0:
				cont += 1
	if imprimir:			
		print(f'Lugares disponiveis: {20 - cont}')
	return 20 - cont


def cancelarCompra():
	if contador() == 20:
		print('Nenhum ascento comprado')
		return (-1)
	asc = int(input('Quantos ascentos irá cancelar? '))
	for i in range(asc):
		while asc > 0:
			f_sel = int(input('Fileira desejada: '))
			c_sel = int(input('Cadeira desejada: '))
			if lugares[f_sel][c_sel] != 0:
				lugares[f_sel][c_sel] = 0
				asc -= 1
			else:
				print('Cadeira já esta vaga, delecione outra cadeira.')



def ocuparCadeiras():
	asc = int(input('Quantos ascentos irá comprar? '))
	for i in range(asc):
		while asc > 0:
			f_sel = int(input('Fileira desejada: '))
			c_sel = int(input('Cadeira desejada: '))
			if lugares[f_sel][c_sel] == 0:
				lugares[f_sel][c_sel] = 1
				asc -= 1
			else:
				print('Cadeira já ocupada, delecione outra cadeira.')


lugares = []
cadeiras = []
sair = False
arquivo = open('nota.txt', 'w')

arquivo.write('Preço do ingresso = 12 reais')

for i in range(5):
	cadeiras.append(0)
for i in range (4):
	lugares.append(cadeiras.copy())

while sair == False:
	imprimiMenu()
	entrada = int(input())
	print('-=' * 30)
	if entrada == 1:
		imprimiMatriz()
		print('-=' * 30)		
	elif entrada == 2:
		contador(True)
		print('-=' * 30)
	elif entrada == 3:
		ocuparCadeiras()
		print('-=' * 30)
	elif (entrada == 4):
		if cancelarCompra() == -1:
			continue
		print('-=' * 30)
	elif entrada == 5:
		sair = True
	else:
		print('Opção invalida')
		print('-=' * 30)
