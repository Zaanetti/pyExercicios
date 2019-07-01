from time import sleep

# Ttask = int(input('Informe o Ttask desejado: '))
# Umax = int(input('Informe o Umax desejado: '))
tic = int(5)
loutput = ()

# path = '/home/luiz/Documentos/meus/pyExercicios/input2.txt'  # lendo o arquivo linux
path = 'C:/Users/Zanetti/Documents/Python/pyExercicios/input2.txt'  # lendo o arquivo windows
linput = open(path).read().split()  # transformando em uma lista

# if (str(input('Mostrar tamanho do input? ')).upper()) == 'S':
#    print(len(linput))

# for t in linput:
#    sleep(0.5)
#    print(f'Valor: {t}')

# dserv['user'][0] += 2
dgServ = {}
Uws = 3
for s in range(1, 3):
    dserv = {'tic': 0, 'user': [s, 2, 2, 2]}
    dgServ[f'Server{s}'] = dserv.copy()
    
    print(1 in dgServ[f'Server{s}']['user'])  # localizando algo dentro de uma lista de dentro de um dicionário dentro de outro dicionário
    dgServ[f'Server{s}']['user'].append(999)  # adiciona algo na lista de dentro de um dicionário dentro de outro dicionário
    dgServ[f'Server{s}']['user'].pop()  # retira algo da lista de dentro de um dicionário dentro de outro dicionário
    print(dgServ)
    dgServ[f'Server{s}']['user'].remove(999)
    print(dgServ)
# print(user)


# print(len(lteste[1]))  # ve o tamanho de um dicionário dentro da lista
# print(len(lteste[0]['user']))  # ve o tamanho de uma lista dentro de um dicionário que esta dentro de uma outra lista

# print(dgServ['lista']['tic'])  # mostra o valor de uma key de um dicionário dentro de outro dicionário

