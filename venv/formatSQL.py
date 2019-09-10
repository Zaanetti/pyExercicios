import pyperclip as clipb


def verQuery(query):
    if type(query) == str:
        q = query.strip().upper()
        if 'SELECT ' == q[:6]:
            if ' FROM ' in q:
                q = q[:q.find('FROM')] + '\n' + q[q.find('FROM'):]
            else:
                print('SELECT sem FROM')
                return False
        elif 'UPDATE' == q[:6]:
            if ' SET ' in q:
                q = q[:q.find('SET')] + '\n' + q[q.find('SET'):]
            else:
                print('UPDATE sem SET')
                return False
        elif 'INSERT' == q[:6]:
            if '(' in q and 'VALUES' in q:
                q = q[:q.find('(')] + '\n' + q[q.find('('):]
                q = q[:q.find('VALUES')] + '\n' + q[q.find('VALEUS'):]
            else:
                print('INSERT incompleto')
                return False
        else:
            print('Comando SQL não reconhecido')
            return False

        if ' WHERE ' in q:
            q = q[:q.find('WHERE')] + '\n' + q[q.find('WHERE'):]
            while ' AND' in q:
                q = q[:q.find(' AND')] + '\nAND ' + q[q.find(' AND') + 5:]



clip = clipb.paste()

if verQuery(clip):
    comando = clipb.paste()
