
def leiaInt(msg):            
    while True:
        try:
            valor = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: POR FAVOR, DIGITE UM NÚMERO INTEIRO VÁLIDO')
            continue
        except(KeyboardInterrupt):
            print('Usuário preferiu não digita esse número.')
            return 0
        else:
            return valor
def leiaFloat(msg):
     while True:
        try:
            valor = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO: POR FAVOR, DIGITE UM NÚMERO REAL VÁLIDO')
            continue
        except(KeyboardInterrupt):
            print('O usuário prefiriu não digita esse número.')
        else:
            return valor


i = leiaInt('Digite um INTEIRO: ')
f = leiaFloat('Digite um numero REAL: ')
print (f'O valor inteiro digitado foi {i} e o real foi {f} ...')