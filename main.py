import keyboard
import random
from player import *
from mapas import *

altura = random.randint(15,30)
largura = random.randint(20,80)
fator_preenchimento_aleatorio = random.randint(0, 30)/100

mapa_Atual = Mapa(altura, largura, fator_preenchimento_aleatorio)

x = random.randint(1,len(mapa_Atual.estrutura[0])-2)
y = random.randint(1,len(mapa_Atual.estrutura)-2)

player = Player(x,y)

mapa_Atual.estrutura[player.y][player.x] = '()'

mapa_Atual.printMap()
    
while keyboard.is_pressed('esc') == False:
           
      if keyboard.is_pressed('w'):
            player.andarCima(mapa_Atual).printMap()
           
      if keyboard.is_pressed('s'):  
            player.andarBaixo(mapa_Atual).printMap()
                            
      if keyboard.is_pressed('a'):
            player.andarEsquerda(mapa_Atual).printMap()
                          
      if keyboard.is_pressed('d'):
            player.andarDireita(mapa_Atual).printMap()