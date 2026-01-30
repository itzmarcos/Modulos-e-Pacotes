import moeda
#ex107,108

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
# print(f'Aumentando 10%, temos {moeda.aumento(p, 10)}')
# print(f'Reduzindo 15%, temos {moeda.diminuir(p, 15)}')