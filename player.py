class Player:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        
        
    def andarCima(self, mapa):
        if mapa.estrutura[self.y-1][self.x] == '██':
            mapa.estrutura[self.y][self.x] == '()'
            return mapa
                
        else:
            mapa.estrutura[self.y][self.x] = '  '
            self.y-=1
            mapa.estrutura[self.y][self.x] = '()'
            return mapa
        
        
              
    def andarBaixo(self, mapa):
        if mapa.estrutura[self.y+1][self.x] == '██':
            mapa.estrutura[self.y][self.x] == '()'
            return mapa
                  
        else:
            mapa.estrutura[self.y][self.x] = '  '
            self.y +=1
            mapa.estrutura[self.y][self.x] = '()'
            return mapa
            
    def andarDireita(self, mapa):
        if mapa.estrutura[self.y][self.x+1] == '██':
            mapa.estrutura[self.y][self.x] == '()'
            return mapa
                  
        else:
            mapa.estrutura[self.y][self.x] = '  '
            self.x += 1
            mapa.estrutura[self.y][self.x] = '()'
            return mapa
            
    def andarEsquerda(self, mapa):
        if mapa.estrutura[self.y][self.x-1] == '██':
            mapa.estrutura[self.y][self.x] == '()'
            return mapa
                  
        else:
            mapa.estrutura[self.y][self.x] = '  '
            self.x -=1
            mapa.estrutura[self.y][self.x] = '()'
            return mapa