import time
import os
import random

class Mapa:
      def gerarEstrutura(self):
            mapa = [['  ' for x in range(self.largura)] for x in range(self.altura)]
                     
            for i in range(self.altura):
                  for j in range(self.largura):
                        if i == 0 or i == self.altura - 1 or j == 0 or j == self.largura - 1:
                              mapa[i][j] = '██'

                        elif random.random() < self.fator:  
                              mapa[i][j] = '██'
            return mapa

      def __init__(self, altura, largura, fator):
            self.altura =  altura
            self.largura = largura
            self.fator = fator
            self.estrutura = self.gerarEstrutura()

      def printMap(self):
            os.system('cls')
            for i in self.estrutura:
                  for j in i:
                        print(j, end='')
                  print("")
            time.sleep(0.15)
            
