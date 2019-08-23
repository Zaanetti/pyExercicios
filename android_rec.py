import os
import tempfile
from subprocess import Popen, call
import getpass
import stat


def instalações():
    if input('Instalar android-tools e usbutils(S/N): ').upper() == 'S':
        os.system('sudo apt-get update')
        os.system('sudo apt install android-tools-adb android-tools-fastboot')
        os.system('sudo apt install usbutils')

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


# os.mkdir('/etc/udev/rules.d/teste')
# call(['chmod', '0444', '/home/usuario/Documentos/meus/pyExercicios/android_rec.py'])
# os.chmod('/home/usuario/Documentos/meus/pyExercicios/android_rec.py', stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH | stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)

os.system('clear')

ini = os.getcwd()

if os.path.exists('/etc/udev/rules.d/99-android-debug.rules'):
    if input('Deseja aparagar o 99-android-debug.rules.rules?(s/n)').upper == 'S':
       reset = True


instalações()
lusb1 = con_output('lsusb')

print('Habilite a depuração de USB e conecte o cabo USB a um android')
input()

lusb2 = con_output('lsusb')

susb1 = set(lusb1)
susb2 = set(lusb2)

device = str(susb2.difference(susb1))[2:-2].strip().lstrip()  # gera um set de elementos só tem no set2
print(device)
det = devd(device)
print(det)
if type(det) == dict:
    # cmd = f"sudo ls -l /dev/bus/usb/{det['bus']}/{det['device']}"
    # per = con_output(cmd, tipo='str') deu merda ainda não descobri o pq
    # if 'crw-rw-r--' in per:
    rules = f'SUBSYSTEM=="usb", ATTR{{idVendor}}=="{det["idfab"]}", ATTR{{idProduct}}=="{det["iddev"]}", GROUP="androiddev", MODE="0664"'
    os.system('sudo groupadd androiddev')
    os.system(f'sudo usermod -aG androiddev {getpass.getuser()}')
    os.chdir('/etc/udev/rules.d')
    if reset:
        os.system('sudo rm -rf 99-android-debug.rules')
        os.system('sudo touch 99-android-debug.rules')
    with open('99-android-debug.rules', 'a') as arq:
        arq.write(rules)

input('FIM')
os.system(f'exec su -l ${getpass.getuser()}')
