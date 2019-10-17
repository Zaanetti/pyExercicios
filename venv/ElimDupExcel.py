import pandas as pd

def cnpj_format_cell(cell):
    if type(cell) == str:
        ncell = cell.replace('.', '')
        ncell = ncell.replace('/', '')
        ncell = ncell.replace('-', '')
        return ncell
    return cell

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 3)

df = pd.read_excel(r'CLIENTES - TARGET.xlsx', error_bad_lines=False, converters = {
    'CNPJ': cnpj_format_cell
})


# print(df[~df.duplicated(subset=['CNPJ'])])


df[~df.duplicated(subset=['CNPJ'])].to_excel('Cliente MINNAS (clean).xlsx', index=False)
