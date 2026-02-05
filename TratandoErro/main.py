def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número válido')
        if ok:
            break
    return valor

def leiaFlot(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return float(valor)
        else:
            print('ERRO: POR FAVOR, DIGITE UM NÚMERO REAL VALIDO')
#     while True:
#         valor = input(msg)
#         if valor.isnumeric():
#             return int(valor)
#         else:
#             print('ERRO: POR FAVOR, DIGITE UM NÚMERO INTEIRO VÁLIDO')

# def leiaFlot(msg):
#     while True:
#         valor = input(msg)
#         if valor.isnumeric():
#             return float(valor)
#         else:
#             print('ERRO: POR FAVOR, DIGITE UM NÚMERO REAL VALIDO')

i = leiaInt('Digite um INTEIRO: ')
r = leiaFlot('Digite um numero REAL: ')
print (f'O valor inteiro digitado foi {i} e o real foi {r}')