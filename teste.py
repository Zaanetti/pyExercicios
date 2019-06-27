from time import sleep

#Ttask = int(input('Informe o Ttask desejado: '))
#Umax = int(input('Informe o Umax desejado: '))
tic = int(5)
loutput = ()

path = '/home/luiz/Documentos/meus/pyExercicios/input2.txt'  # lendo o arquivo
linput = open(path).read().split() # transformando em uma lista

#if (str(input('Mostrar tamanho do input? ')).upper()) == 'S':
#    print(len(linput))

for t in linput:
    sleep(0.5)
    print(f'Valor: {t}')


