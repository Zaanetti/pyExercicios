import os
import tempfile
from subprocess import Popen, call
import getpass
import stat


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
        with open('99-android-debug.rules', 'a') as arq:
            arq.write(ndevice)





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


os.system('clear')
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
# print(det)
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
else:
    input()


os.system('exit')

