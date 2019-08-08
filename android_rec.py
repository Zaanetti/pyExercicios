import os
import tempfile
from subprocess import Popen


def instalações():
    if input('Instalar android-tools e usbutils(S/N): ').upper() == 'S':
        os.system('sudo yum install android-tools')  # sudo yum install android-tools
        os.system('sudo yum install usbutils')  # sudo yum install usbutils

def con_output(cmd):
    with tempfile.TemporaryFile() as tempf:
        proc = Popen([cmd], stdout=tempf)
        proc.wait()
        tempf.seek(0)
        output = str(tempf.read())[2:-3]
    return output.split('\\n')


instalações()
lusb1 = con_output('lsusb')

print('Habilite a depuração de USB e conecte o cabo USB a um android')
input()

lusb2 = con_output('lsusb')

susb1 = set(lusb1)
susb2 = set(lusb2)

device = str(lusb2.difference(susb1))[2:-2].strip().lstrip()

input()

# device_usb = set(lusb2).dif(set(lusb1))  # gera um set de elementos só tem no set2

# print(device_usb)
# identificar quem é o aparelho no meio do retorno tratado

# ls -l /dev/bus



