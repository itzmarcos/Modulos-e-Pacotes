# MENU
from mods import mod
from time import sleep

while True:
    resp = mod.menu(['Cadastrar Pessoas', 'Ver lista de pessoas', 'Sair do Sistima'])
    if resp == 1:
        mod.cabeçalho('OPÇÃO 1')
    elif resp == 2:
        mod.cabeçalho('OPÇÃO 2')
    elif resp == 3:
        mod.cabeçalho('Saindo do sistema.. até logo!')
        break
    else:
        print('ERROR')
    sleep(1)