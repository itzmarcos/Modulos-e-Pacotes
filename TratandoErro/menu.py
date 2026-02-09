# MENU
from mods import mod
from arquivo import arquivos
from time import sleep

arq = 'cadastro.txt'

if not arquivos.arquivoExiste(arq):
    arquivos.criarArquivo(arq)

while True:
    resp = mod.menu(['Ver pessoas cadastrada', 'Cadastrar nova pessoas', 'Sair do Sistima'])
    if resp == 1:
        mod.cabeçalho('OPÇÃO 1')
        arquivos.lerArquivo(arq)
    elif resp == 2:
        mod.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        arquivos.cadastrar(arq, nome, idade)
    elif resp == 3:
        mod.cabeçalho('Saindo do sistema.. até logo!')
        break
    else:
        print('ERROR')
    sleep(1)