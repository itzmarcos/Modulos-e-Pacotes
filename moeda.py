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

