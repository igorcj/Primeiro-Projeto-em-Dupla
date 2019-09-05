import random as rm
import numpy as np

class populacao:

    def __init__(self,n):
        self.tamanho = int(n)
        self.individuos = self.pessoas(self.tamanho)

    def pessoas(self, n):
        pop = np.chararray((int(n),14), itemsize=15)
        for i in range(int(n)):

            #Escolha do atributo 1 (região):
            comparador = rm.random()
            if (comparador <= (np.random.normal(30, 10.7)/477)):
                pop[i,0] = 'Norte'
            elif (comparador <= (np.random.normal(115, 8.4)/477)):
                pop[i,0] = 'Nordeste'
            elif (comparador <= (np.random.normal(360, 6)/477)):
                pop[i,0] = 'Sudeste'
            elif (comparador <= (np.random.normal(434, 8.9)/477)):
                pop[i,0] = 'Sul'
            else:
                pop[i,0] = 'Centro-Oeste'

            #Escolha do atributo 2 (sexo):
            pop[i,1] = 'Homem' if(rm.random() <= (np.random.normal(269, 5.1)/477)) else 'Mulher'

            #Escolha do atributo 3(Cor):
            pop[i, 2] = 'Branca' if(rm.random() <= (np.random.normal(272, 5.2)/477)) else 'Preta ou Parda'

            #Escolha do atributo 4(Situação de Ocupação):
            pop[i, 3] = 'Ocupado' if(rm.random() <= (np.random.normal(362, 4.4)/477)) else 'Nao Ocupado'

            #Escolha do atributo 5(Rendimento Mensal Domiciliar):
            comparador = rm.random()
            if (comparador <= (np.random.normal(11, 24.4)/477)):
                pop[i,4] = '0 a 1'
            elif (comparador <= (np.random.normal(42, 13.4)/477)):
                pop[i,4] = '1 a 2'
            elif (comparador <= (np.random.normal(93, 11.4)/477)):
                pop[i,4] = '2 a 3'
            elif (comparador <= (np.random.normal(209, 7.7)/477)):
                pop[i,4] = '3 a 5'
            elif (comparador <= (np.random.normal(375, 7.1)/477)):
                pop[i,4] = '5 a 10'
            elif (comparador <= (np.random.normal(435, 11)/477)):
                pop[i,4] = '10 a 20'
            elif (comparador <= (np.random.normal(450, 23)/477)):
                pop[i,4] = '20 ou mais'
            else:
                pop[i,4] = 'Sem Declaracao'

            #Escolha do atributo 6(Rendimento Domiciliar Per Capita):
            comparador = rm.random()
            if (comparador <= (np.random.normal(21, 24.4)/477)):
                pop[i,5] = '0 a 1/2'
            elif (comparador <= (np.random.normal(109, 13.4)/477)):
                pop[i,5] = '1/2 a 1'
            elif (comparador <= (np.random.normal(280, 11.4)/477)):
                pop[i,5] = '1 a 2'
            elif (comparador <= (np.random.normal(369, 7.7)/477)):
                pop[i,5] = '2 a 3'
            elif (comparador <= (np.random.normal(424, 7.1)/477)):
                pop[i,5] = '3 a 5'
            elif (comparador <= (np.random.normal(449, 11)/477)):
                pop[i,5] = '5 ou mais'
            else:
                pop[i,5] = 'Sem Declaracao'

            #Escolha do atributo 7(Rede de Ensino):
            pop[i,6] = 'Publica' if(rm.random() <= (np.random.normal(105, 9.1)/477)) else 'Particular'

            #Escolha dos atributos 8(Modalidade) e 9(Turno):
            comparador = rm.random()
            if (comparador <= (np.random.normal(392, 4.3)/477)):
                pop[i, 7] = 'Presencial'
                if (comparador <= (np.random.normal(48, 11.7)/392)):
                    pop[i, 8] = 'Manha'
                elif (comparador <= (np.random.normal(68, 17.5)/392)):
                    pop[i, 8] = 'Tarde'
                elif (comparador <= (np.random.normal(370, 5)/392)):
                    pop[i, 8] = 'Noite'
                else:
                    pop[i, 8] = 'Dois Parciais'
            else:
                pop[i,7] = 'A Distancia'
                pop[i,8] = 'Nao se Aplica'

            #Escolha do atributo 10(Dificuldade Financeira):
            pop[i,9] = 'Sim' if(rm.random() <= (np.random.normal(27, 15.7)/477)) else 'Nao'

            #Escolha do atributo 11(Dificuldade de acesso ao local do curso):
            pop[i, 10] = 'Sim' if (rm.random() <= (np.random.normal(25, 17) / 477)) else 'Nao'

            #Escolha do atributo 12(Dificuldade de cumprir o horário do curso):
            pop[i, 11] = 'Sim' if (rm.random() <= (np.random.normal(24, 16.5) / 477)) else 'Nao'

            #Escolha do atributo 13(Falta de tempo para estudar):
            pop[i, 12] = 'Sim' if (rm.random() <= (np.random.normal(15, 21.6) / 477)) else 'Nao'

            #Escolha do atributo 14(Outra dificuldade):
            pop[i, 13] = 'Sim' if (rm.random() <= (np.random.normal(6, 33.5) / 477)) else 'Nao'

        return pop

    def amostra(self, tamanho_amostra):

        if tamanho_amostra > self.tamanho:
            raise ValueError('"Tamanho da amostra" out of bounds.')
        elif tamanho_amostra < 1:
            raise ValueError('"Tamanho da amostra" out of bounds.')
        else:
            indices = rm.sample(range(self.tamanho), tamanho_amostra)
            amostra = [self.individuos[x,:] for x in indices]
        return amostra