import pyperclip as clipb


def verQuery(query):
    if type(query) == str:
        q = query.strip().upper()
        if 'SELECT ' == q[:6]:
            if ' FROM ' in q:
                q = q[:q.find('FROM')] + '\n' + q[q.find('FROM'):]
            else:
                return print('SELECT sem FROM')
        elif 'UPDATE' == q[:6]:
            if ' SET ' in q:
                q = q[:q.find('SET')] + '\n' + q[q.find('SET'):]
            else:
                return print('UPDATE sem SET')
        elif 'INSERT' == q[:6]:
            if '(' in q and 'VALUES' in q:
                q = q[:q.find('(')] + '\n' + q[q.find('('):]
                q = q[:q.find('VALUES')] + '\n' + q[q.find('VALEUS'):]
            else:
                return print('INSERT incompleto')
        elif 'DELETE' == q[:6]:
            pass


clip = clipb.paste()

if verQuery(clip):
    comando = clipb.paste()
else:
    print('Não corresponde a um comando')
