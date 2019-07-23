# code-test, Autor: Luiz Henrique Zanetti
import sys

# Declaração de variáveis usadas no processo
Tu = 0                                      # Total users
Uws = 0                                     # Users without server
ul = 0                                      # Users left
sc = 0                                      # Servers created
sr = 0                                      # Servers reactivated
st = 0                                      # Servers Terminated
swu = 0                                     # Servers without server
tt = 0                                      # Total ticks
ups = '0'                                   # Users per server
tip = ''                                    # Texto de informação sobre alterações feitas no tick corrente
dgServ = {'nserv': 0}                       # Dicionário de todos os Servers usados no processo  'nserv'= numero de servidores

path = '/home/luiz/Documentos/meus/pyExercicios/input1.txt'  # lendo o arquivo no linux
# path = 'C:/Users/Zanetti/Documents/Python/pyExercicios/input1.txt'  # lendo o arquivo no windows
linput = open(path).read().split()          # transformando o input.txt em uma lista

Ttask = int(input('Informe o Ttask desejado: '))
Umax = int(input('Informe o Umax desejado: '))

print('', file=open('output.txt', 'w'))
file = open('output.txt', 'w')              # Definindo o nome do arquivo de output
sys.stdout = file                           # Definindo o arquivo padrão para escrita

# Escrita do cabeçalho do output
print(f'Maximo de usuários (Umax) = {Umax}')
print(f'Numero de tasks por usuário (Ttask) = {Ttask}')
print('-=' * 40)
print(f"\n{'tick':^7}|{'input':^7}|{'Output':^14}|{'Tip':^25}")
print('--' * 40)
# Inicio do processoa principal
for i in range(0, len(linput) + Ttask - 1):
    if i < len(linput):
        Uws = int(linput[i])                # Informa o numero de usuários sem servidor que foram inputados neste tic
    else:
        Uws = 0                             # Caso a lista de input acabe, mas ainda possua users em algum server

    if i == 0 and Uws > 0:                  # Criação de servidores para o primeiro input quando Tu = 0
        Tu += Uws                           # Soma os novos users ao total
        serv = {'tick': 0, 'Users': []}     # Cria o dicionário de um novo servidor
        dgServ['nserv'] += 1                # Contabiliza o novo servidor
        sc += 1
        while Uws != 0:
            serv['Users'].append(Ttask)     # Adiciona um user ao servidor atual
            Uws -= 1
            if len(serv['Users']) == Umax:  # Se o limite de users é alcançado no servidor é criado um novo
                dgServ[f"Server{dgServ['nserv']}"] = serv.copy()
                serv = {'tick': 0, 'Users': []}
                dgServ['nserv'] += 1
                sc += 1                     # Contabiliza um servidor criado neste tick
        dgServ[f"Server{dgServ['nserv']}"] = serv.copy()  # Adicionando servidor ao dicionário geral dos servidores
    elif Uws > 0:                           # Tratativa para o 2º tick em diante
        Tu += Uws
        while Uws > 0:
            for k, v in dgServ.items():     # Verificação de servidores existentes para realocar os novos users
                if k != 'nserv' and len(v['Users']) < Umax and Uws > 0:
                    while Uws > 0 and len(v['Users']) < Umax:
                        if v['tick'] != 0 and len(v['Users']) == 0:
                            sr += 1         # Contabilização de um servidor reativado neste tick
                        v['Users'].append(Ttask)  # Adiciona um user ao servidor atual
                        Uws -= 1
            if Uws > 0:                     # Caso o servidor atual atinja o limite de users é criado um novo servidor
                serv = {'tick': 0, 'Users': []}
                dgServ['nserv'] += 1
                dgServ[f"Server{dgServ['nserv']}"] = serv.copy()
                sc += 1

    for k, v in dgServ.items():             # Processo de incrementação de ticks, subtração de tasks e varredura de users com task = 0
        if k != 'nserv':
            if len(v['Users']) > 0:         # Incrementação dos ticks nos servidores com users
                v['tick'] += 1
                tt += 1

            for s in range(0, len(v['Users'])):  # Subtraído 1 tick de cada task dos usuários do servidor atual
                v['Users'][s] -= 1

            while 0 in v['Users']:          # Varredura e contabilização de users com task = 0 neste tick
                v['Users'].remove(0)
                Tu -= 1
                ul += 1
                if len(v['Users']) == 0:    # Contabilização de servidores desativados neste tick
                    st += 1
    # Montagem da resolução de acontecimentos do tick atual
    for k, v in dgServ.items():
        if k != 'nserv':
            if len(v['Users']) != 0:        # Contabilização de users por servidor ativo
                if ups == '0':
                    ups = len(v['Users'])
                else:
                    ups = f'{ups},{len(v["Users"])}'
            else:                           # Contabilização de servidores sem users
                swu += 1


    tip = f" {dgServ['nserv'] - swu} server(s) for {Tu} user(s)"  # Montagem do resumo
    if sr:
        tip = tip + f" ({sr} server(s) reactivated)"
    if sc:
        tip = tip + f" ({sc} server(s) created)"
    if st:
        tip = tip + f" ({st} server(s) terminated)"

    if i < len(linput):
        print(f'{i + 1:^7}|{linput[i]:^7}|{ups:^14}|{tip:^7}')
    else:
        print(f'{i + 1:^7}|{" ":^7}|{ups:^14}|{tip:^7}')

    ul = sc = st = swu = sr = 0
    ups = '0'
# Fim do processo principal

# Detalhamento do processo por completo
print('--' * 40)
print(f'{"Total cost":^15}|{str(tt) + "$":^14}|')
print('--' * 40)
print('\nRESUMO DO PROCESSO\n')
print('--' * 40)
for k, v in dgServ.items():
    if k == 'nserv':
        print(f'Numero de servidores criados: {v}')
        print('--' * 40)
        print('Detalhamento de custos por server:')
    else:
        print(f'• {k} ({v["tick"]} ticks x 1$) = {v["tick"]}$ ')
file.close()


