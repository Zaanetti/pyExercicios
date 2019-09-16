import pyperclip as clipb


def verQuery(query):
    if type(query) == str:
        q = query.strip().upper()
        if 'SELECT' == q[:6]:
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
            clipb.copy(q.strip())


def repQuery(query):
    if type(query) == str:
        q = query.strip().upper()
        q = q.replace(' FROM', '\nFROM')
        q = q.replace(' SET', '\nSET')
        q = q.replace(' JOIN', '\nJOIN')
        q = q.replace(' INNER JOIN', '\nINNER JOIN')
        q = q.replace(' LEFT JOIN', '\nLEFT JOIN')
        q = q.replace(' WHERE', '\nWHERE')
        q = q.replace(' AND', '\nAND')
        q = q.replace(' GROUP BY', '\nGROUP BY')
        q = q.replace(' ORDER BY', '\nORDER BY')

        clipb.copy(q)


def repQuery2(query):
    if type(query) == str:
        q = query.strip().upper()
        sql = ('SELECT', 'UPDATE', 'INSERT INTO', 'DELETE', 'FROM', 'SET', 'JOIN', 'INNER JOIN', 'LEFT JOIN', 'WHERE', 'AND', 'OR', 'GROUP BY', 'ORDER BY', 'SUM')
        for sql in sql:
            q = q.replace(f' {sql}', f'\n{sql}')
        clipb.copy(q)


# verQuery(clipb.paste())
# repQuery(clipb.paste())
repQuery2(clipb.paste())


