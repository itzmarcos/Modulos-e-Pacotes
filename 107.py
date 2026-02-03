from utilidades.moedas import moeda
from utilidades.dados import dados

p = dados.validador('Digite o preço: R$')
moeda.resumo(p, 80, 35)