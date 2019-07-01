from time import sleep

Ttask = int(input('Informe o Ttask desejado: '))
Umax = int(input('Informe o Umax desejado: '))

Tu = int()  # Total users
Uws = int()  # Users without server
ul = int()  # Users left
sc = int()  # Servers created
st = int()  # Servers Terminated
dgServ = {'nserv': 0}  # Dicionário geral de todos os Servers usados no processo - 'nserv'= numero de servidores criados

# path = '/home/luiz/Documentos/meus/pyExercicios/input2.txt'  # lendo o arquivo linux
path = 'C:/Users/Zanetti/Documents/Python/pyExercicios/input1.txt'  # lendo o arquivo windows
linput = open(path).read().split()  # transformando em uma lista

for i in range(0, len(linput) + Ttask - 1):
    if i < len(linput):
        Uws = int(linput[i])   # Informa o numero de usuários sem servidor que foram inputados neste tic
    else:
        Uws = 0
    if i == 0 and Uws > 0:  # Condição de tratamento e criação de servidores para o primeiro input quando Tu = 0
        Tu += Uws
        serv = {'Tic': 0, 'Users': []}  # Cria o dicionário de um novo servidor
        dgServ['nserv'] += 1
        sc += 1
        while Uws != 0:
            serv['Users'].append(Ttask)
            Uws -= 1
            if len(serv['Users']) == Umax:
                dgServ[f"Server{dgServ['nserv']}"] = serv.copy()
                serv = {'Tic': 0, 'Users': []}
                dgServ['nserv'] += 1
                sc += 1
        dgServ[f"Server{dgServ['nserv']}"] = serv.copy()
    elif Uws > 0:
        Tu += Uws
        while Uws > 0:
            for k, v in dgServ.items():
                if k != 'nserv' and len(v['Users']) < Umax and Uws > 0:
                    while Uws > 0 and len(v['Users']) < Umax:
                        v['Users'].append(Ttask)
                        Uws -= 1
            if Uws > 0:
                serv = {'Tic': 0, 'Users': []}  # Cria o dicionário de um novo servidor
                dgServ['nserv'] += 1
                dgServ[f"Server{dgServ['nserv']}"] = serv.copy()

    # incrementar os tics
    for k, v in dgServ.items():
        if k != 'nserv':
            if len(v['Users']) > 0:
                v['Tic'] += 1
            # subtrair os Ttasks
            for s in range(0, len(v['Users'])):
                v['Users'][s] -= 1

    # retirar os Users com Ttask = 0
    for k, v in dgServ.items():
        if k != 'nserv':
            while 0 in v['Users']:
                v['Users'].remove(0)
                Tu -= 1
                ul += 1
                if len(v['Users']) == 0:
                    st += 1

    # print('Retirado Users com task = 0')
    # for k, v in dgServ.items():
    #     if k != 'nserv':
    #         print(f'{k}: {v}')
    # print(f'USUARIOS TOTAL: {Tu}')
    # print('-=' * 30)

    print(f"{'clock':^7}|{'input':^7}|{'Output':^8}|{'Tip':^7}")
    if i < len(linput):
        print(f'{i + 1:^7}|{linput[i]:^7}|{Tu:^8}|{" ":^7}')
    else:
        print(f'{i + 1:^7}|{" ":^7}|{Tu:^8}|{" ":^7}')
    ul = 0
    sc = 0
    st = 0

