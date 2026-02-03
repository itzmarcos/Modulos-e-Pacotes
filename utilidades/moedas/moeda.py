def metade(p=0, f=False):
    r = p / 2
    return r if f is False else moeda(r)


def dobro(p=0, f=False):
    r = p * 2
    return r if not f else moeda(r)
    

def aumento(p=0, t=0, f=False):
    r = p + (p * t / 100)
    return r if f is False else moeda(r)

    
def diminuir(p=0, t=0, f=False):
    r = p - (p * t / 100)
    return r if f is False else moeda(r)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p=0, t=0, d=0):
    print('-=' * 15)
    print('RESUMO DO VALOR'.center(30))
    print('=-' * 15)
    print(f'Preço analisado: {moeda(p)}')
    print(f'Dobro do preço:  {dobro(p, True)}')
    print(f'Metade do preço: {metade(p, True)}')
    print(f'80% de aumento:  {aumento(p, t,True)}')
    print(f'35% de redução:  {diminuir(p, d, True)}')
    print('-' * 30)