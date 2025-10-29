
class LosangosEx13():
    '''
    Criamos a lista do dicionário com os ângulos e medida dos lados:
    '''
    dados =  [{"l1": [120, 2]}, {"l2": [150, 2]}, {"l3": [60, 3]}, {"l4": [90, 3]}]
    '''
    Criamos o método para calcular o ângulo e verficiar a alternativa correta
    chamando o método verificar proporsão:
    '''
    def preeencherLosango(self):
        ax1 = self.dados[0]["l1"][0]
        ay1 = self.dados[1]["l2"][0]
        az1 = self.dados[2]["l3"][0]
        aw1 = self.dados[3]["l4"][0]
        '''
        Para saber a medida do ângulo do outro lado:
        '''
        ax2 = 180 - ax1
        ay2 = 180 - ay1
        az2 = 180 - az1
        aw2 = 180 - aw1          
        '''
        Passamos como parâmetro cada ângulo para identificarmos a
        alternativa correta.
        '''
        if self.verificarProporsao(ax1, ax2, ay1, ay2):
            print("A alternativa 'a' está correta")
            
        if self.verificarProporsao(ay1, ay2, az1, az2):
            print("A alternativa 'b' está correta")
            
        if self.verificarProporsao(ay1, ay2, aw1, aw2):
            print("A alternativa 'c' está correta")
            
        if self.verificarProporsao(ax1, ax2, az1, az2):
            print("A alternativa 'd' está correta")
        
    def verificarProporsao(self, a1, a2, x1, x2):
        '''
        Se estiver correto os calculos abaixo teremos como
        verdadeiro a alternativa correta.
        '''
        if (a1 + a2 + x1 + x2 == 360):
            if (a1 == x1 and a2 == x2) or ((a1 == x2 and a2 == x1)):
                return True

LosangosEx13().preeencherLosango()





