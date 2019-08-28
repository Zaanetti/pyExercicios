import os
import tempfile
from subprocess import Popen
import getpass
import signal


class rules:

    existe = False
    conteudo = ''

    def check(self):
        if os.path.exists('/etc/udev/rules.d/99-android-debug.rules'):
            self.existe = True
            dir_ant = os.getcwd()
            os.chdir('/etc/udev/rules.d')
            with open('99-android-debug.rules', 'r') as arq:
                self.conteudo = arq.read()
            os.chdir(dir_ant)

    def delete(self):
        dir_ant = os.getcwd()
        os.chdir('/etc/udev/rules.d')
        os.system('sudo rm -rf 99-android-debug.rules')
        os.chdir(dir_ant)
        self.existe = False
        self.conteudo = ''

    def insert(self, ndevice):
        os.system('sudo groupadd androiddev')
        os.system(f'sudo usermod -aG androiddev {getpass.getuser()}')
        dir_ant = os.getcwd()
        os.chdir('/etc/udev/rules.d')
        with open('99-android-debug.rules', 'a') as arq:
            arq.write(ndevice)
        os.chdir(dir_ant)




def instalações():
    if input('Instalar android-tools e usbutils(S/N): ').upper() == 'S':
        os.system('sudo apt-get update')
        os.system('sudo apt install android-tools-adb android-tools-fastboot')
        os.system('sudo apt install usbutils')

        print('=-=-=-=-=-=-= ATUALIZAÇÕES CONCLUÍDAS =-=-=-=-=-=-=')
        input()
        os.system('clear')

        # os.system('sudo apt install yum')  # sudo apt install yum
        # os.system('sudo yum repolist all')  # sudo yum repolist all
        # os.system('sudo yum install android-tools')  # sudo yum install android-tools
        # os.system('sudo yum install usbutils')  # sudo yum install usbutils


def con_output(cmd, tipo='t'):
    with tempfile.TemporaryFile() as tempf:
        proc = Popen([cmd], stdout=tempf)
        proc.wait()
        tempf.seek(0)
        if tipo == 't':
            output = str(tempf.read())[2:-3]
            return tuple(output.split('\\n'))
        if tipo == 'str':
            return str(tempf.read())[2:-3]


def devd(device):
    if 'Bus' in device:
        ldev = device.split(' ')
        det = {'bus': ldev[ldev.index('Bus') + 1],
               'device': ldev[ldev.index('Device') + 1],
               'idfab': ldev[ldev.index('ID') + 1][:4],
               'iddev': ldev[ldev.index('ID') + 1][-4:]
               }
        return det
    else:
        print('Nenhum dispositivo encontrado')
        return None


def printpassos(passo):
    if passo == 'ab':
        print('==' * 50)
        print("""
    Com o ADB devidamente configurado e comunicando com o Android, vamos para os proximos passos.

            a)Faça o download do arquivo .zip da build e o renomeie para ota.zip

            b)Certificando-se que o android esteja conectado ao PC, o modo Desenvolvedor e a
              depuração USB estão ativados, no PC coloque o arquivo ota.zip onde esta salvo
              o android_rec.py
              """)
        print('==' * 50)

    elif passo == 'de':
        print('==' * 50)
        print("""
            d)Com o android reiniciado e na tela de fastboot com os botões de volume va até
              a opção recovery mode e selecione a mesma com o botão de Liga/desliga (ou com 
              o botão de ascender a tela, isso depende de cada android).

            e)Dentro do recovery mode selecione a opção “Aply update from ADB” 
              (O dispositivo entrará com uma mensagem dizendo que esta
              aguardando o arquivo ota).
              """)
        print('==' * 50)
    elif passo == 'g':
        print('==' * 50)
        print("""
            g)Após a finalização da instalação, ligue o android normalmente e indo nas 
              configurações, va na opção Restaurar padrão de fábrica, assim fará com 
              que ele resete o aparelho e ativando a nova build.
              """)
        print('==' * 50)

# Inicio do processo
os.system('clear')


if os.path.exists(f'{os.getcwd()}/etapa.txt'):
    with open('etapa.txt', 'r') as arq:
        etapa = arq.read()
else:
    with open('etapa.txt', 'w') as arq:
        etapa = '1'
        arq.write(etapa)


if etapa == '1':
    instalações()

    crules = rules()
    crules.check()

    if crules.existe:
        if input('Deseja apagar o 99-android-debug.rules(s/n):').upper() == 'S':
            crules.delete()

    print('Caso o aparelho esteja conectado ao computador desconecte ele')
    input()

    lusb1 = con_output('lsusb')

    print('Habilite a depuração de USB e conecte o cabo USB a um android')
    input()

    lusb2 = con_output('lsusb')

    susb1 = set(lusb1)
    susb2 = set(lusb2)

    device = str(susb2.difference(susb1))[2:-2].strip().lstrip()  # gera um set de elementos só tem no set2

    if len(device) > 50:
        print(device)

    det = devd(device)

    if type(det) == dict:
        # cmd = f"sudo ls -l /dev/bus/usb/{det['bus']}/{det['device']}"
        # per = con_output(cmd, tipo='str')  # deu merda ainda não descobri o pq
        # if 'crw-rw-r--' in per:
        nrules = f'SUBSYSTEM=="usb", ATTR{{idVendor}}=="{det["idfab"]}", ATTR{{idProduct}}=="{det["iddev"]}", GROUP="androiddev", MODE="0664"\n'
        if crules.existe and (nrules in crules.conteudo):
                print('Dispositivo ja registrado')
        else:
            crules.insert(nrules)
        input('1ª PARTE DO PROCESSO FINALIZADO.\nCaso o terminal não feche automaticamente, feche e execute novamente '
          'o mesmo arquivo(android_rec.py)')
        with open('etapa.txt', 'w') as arq:
            arq.write('2')
        os.kill(os.getppid(), signal.SIGHUP)
    else:
        input()


else:
    print('INICIO DA 2ª PARTE')

    os.system('sudo udevadm control --reload')
    os.system('sudo systemctl restart systemd-udevd.service')


    print('Desconecte e conecte o dispositivo android\n')

    print('Neste momento o dispositivo android deve mostrar na tela uma mensagem para você verificar a RSA Key do PC.'
          ' Para confirmar esta Key, verifique o retorno abaixo\n')

    os.system("sudo cut -d' ' -f1 ~/.android/adbkey.pub | base64 -d | md5sum")

    input('\nSe o retorno bater com a informação na tela do android, basta dar OK na mensagem.\n')

    os.system('sudo adb devices')

    print('')
    printpassos('ab')

    input("""
Ao dar ENTER o dispositivo será reiniciado via comando, para entrar na tela de fastboot. 
PROSSEGUIR COM O PROCESSO?
""")

    os.system('sudo adb reboot recovery')

    printpassos('de')

    input("""
Ao dar ENTER o será dado o comando para o dispositivo executar o ota.zip. 
PROSSEGUIR COM O PROCESSO?
    """)

    os.system('sudo adb sideload ota.zip')

    printpassos('g')

    print('FIM')

    os.system('sudo rm -rf etapa.txt')

