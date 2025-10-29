
class Exercicio14():
    '''
    Inicializando as medidas dos lados
    '''
    x2 = 50
    y2 = 150
    rz = 2/5
    def encontrarLados(self):
        '''
        rz = 0.4 é a medida da razão de semelhança 2/5
        '''
        x = self.x2 * self.rz
        y = self.y2 * self.rz
        '''
        E portanto temos os valores dos lados do segundo
        retângulo menor que vale x, e y respectivamente:
        '''        
        print('Os lados medem x = ', x, 'm e y = ', y , 'm')
        '''
        Como você pode ver na saída acima temos que
        x = 20m e y = 60m
        E portanto a resposta correta é a alternativa 'b'.
        '''

Exercicio14().encontrarLados()
        
    
        
