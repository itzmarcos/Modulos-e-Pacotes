def lin(t=42):
    return '-' * t

def cabeçalho(msg):
    print(lin())
    print(msg.center(42))
    print(lin())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(lin())
    opc = leiaInt('Sua Opção: ')
    return opc

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERROR')
        except(KeyboardInterrupt):
            print('ERROR')
            return 0
        else:
            return n