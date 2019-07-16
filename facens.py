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

