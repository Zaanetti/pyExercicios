import pyperclip as clipb

larg = []

if type(clipb.paste()) == str and ('SELECT',):
    comando = clipb.paste()
else:
    print('Não corresponde a um comando')





