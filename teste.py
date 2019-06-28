from time import sleep

#Ttask = int(input('Informe o Ttask desejado: '))
#Umax = int(input('Informe o Umax desejado: '))
tic = int(5)
loutput = ()

path = '/home/luiz/Documentos/meus/pyExercicios/input2.txt'  # lendo o arquivo
linput = open(path).read().split() # transformando em uma lista

#if (str(input('Mostrar tamanho do input? ')).upper()) == 'S':
#    print(len(linput))

#for t in linput:
#    sleep(0.5)
#    print(f'Valor: {t}')




dserv = {'tic': 0, 'user': 5, 'user': 5}
lteste = [dserv.copy()]
dserv['user'] += 2
print(lteste)
deserg = {'lista': dserv}
lteste.append(dserv.copy())
print(lteste)

print(len(lteste[1])) # ve o tamanho de um dicionário dentro da lista

print(deserg)