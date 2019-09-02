from populacao import populacao
from individuo import individuo
from numpy import unique

pop = populacao(1000)

print(pop.tamanho)

amostra = pop.amostra(100)

sexos = []
for i in pop.individuos:
    sexos.append(individuo(i).sexo)

valores = unique(sexos)

print(valores[0], sexos.count(valores[0])/len(sexos), 269/477)
print(valores[1], sexos.count(valores[1])/len(sexos), 1 - 269/477)

