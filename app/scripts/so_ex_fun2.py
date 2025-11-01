so_ex11_m1 = "data/imagens/img-un1-so11-m1.png"
so_ex11_m2 = """
Podemos com papel e caneta expandir o polinômio \n 
Que corresponde a àrea total do terreno\n
que corresponde à seguinte função f(x) = x² + 6x -16\n
então vamos substiuir os números localizados nas alternativas dadas\n
no enunciada desta questão para ver se x é raiz da quadrática\n
digitando para a letra a) 1m [1][x²][+][6][*][1][-][16]\n
em seguida pressione [=] que o resultado será -9, \n
ou seja: [1] não é raiz.
digitando para a letra b) 2m [2][x²][+][6][*][2][-][16]\n
em seguida pressione [=] que o resultado será 0, \n
encontramos [2] que é raiz, vamos agora verificar os outros\n
números também dados no enunciado da questão\n
digitando para a letra c) 5m [5][x²][+][6][*][5][-][16]\n
em seguida pressione [=] que o resultado será 39, \n
5m não é x e também não é raiz da expressão matemática.\n
e, por fim, vamos comparar a letra d) 8m:
[8][x²][+][6][*][8][-][16] em seguida [=]\n
que resulta em 96m que não é x.
Ou seja a resposta para o enúnciado é x = 2m letra "b".
"""
so_ex11_m3 = """
class ExOnze():
   expr = "x**2 + 6*x -16" #expressão da área total
   lista  = [1, 2, 5, 8] #lista com a resposta
   def verificar(self):
      for x in self.lista:
         if eval(self.expr) == 0: #compara a fórmula
            print(str(x) + " é raiz")
         else:
            print(str(x) + " não é raiz")

ExOnze().verificar()
'''
Que como saída também mostrou no terminal a seguinte linha\n
"2 é raiz" ou seja: x = 2m letra "b"
'''
"""

so_ex11_m4 = """
Queremos saber a expressão matemática para\n
encontrar o valor de x, portanto sabemos que com a área\n
do terreno junto com a área, podemos encontrar a fórmula\n
que estamos buscando. portanto, vamos calcular área total do terreno\n
Queremos encontrar a área total do terreno,\n
para isso, façamos o cálculo da área informada no enunciado.\n
no Campo de Entrada digite:\n
(5+2x)*(7+2x)=99. que temos a fórmula fatorada,\n
para exibir o polinômio completo clique com o\n
botão direito em cima da formula gerada\n
e clique no item de menu flutuante \n
Equação ax² + bxy + cy² + dx + ey = f\n
que temos como fórmula a nova função f\n 
que é f(x) = x² + 6x -16\n
Agora, podemos criar uma função g(x) quadrática\n
para a expressão que encontramos para área\n
e fazendo raízes(g), temos como \n
resposta (2, 0) e (-8, 0) o x deve ser positivo,\n
e portanto x = 2 e como resposta temos letra(b)\n"""

so_ex12_m1 = "data/imagens/img-un1-so12-m1.png"
so_ex12_m2 = """
Podemos resolver este exercício de matemática utilizando Soma e Produto\n
Ao modelar os dados podemos estabelecer a fórmula da quadrática\n
E também consiste nas seguintes regras: o perímetro: 2l1 + 2l2 = 20m\n
ou seja simplificando: \n
I) l1+ l2 = 10m e a área do retângulo:\n
II) l1 * l2 = 24m² que resulta na regra de Soma e Produto da quadrática\n
ou Seja x1 + x2 = 10 e x1 * x2 = 24, e com a calculadora\n
podemos comparar qual das alternativas satisfaz regra de soma e produto:\n
letra a) 2 e 12 na calculadora: [2][+][12][=] \n
resulta em 14 resultado que por (I) está incorreto\n
letra b) 3 e 8 na calculadora [3][+][8][=] resulta em 11 por (I) está incorreta\n
letra c) [3][*][7][=] resulta em 21 por (II) está incorreta\n
letra d) [4][+][6][=] resulta em 10 que satisfaz,\n
e comparando (II) temos [4][*][6][=] 24 que satisfaz também\n
ou seja a alternativa "d" está correta.

"""
so_ex12_m3 = """
class ExDoze():
   expr1 = "x + y" #expressão da área total
   expr2 = "x * y"
   lista  = [(2, 12), (3,8), (3,7), (4,6)] #lista com a resposta
   def verificar(self):
      for ls in self.lista:
         x = ls[0]
         y = ls[1]

         if eval(self.expr1)==10 and eval(self.expr2) == 24: #compara a fórmula
            print(str(ls) + " é resposta")
         else:
            print(str(ls) + " não é resposta")
ExDoze().verificar()
'''
Que além das outras saídas também imprime\n
no terminal a seguinte mensagem: (4, 6) é resposta\n
Ou seja resposta letra "d"
'''

"""
so_ex12_m4 = """
Podemos encontrar a fórmula matemática dados as informações
do enunciado. Então temos duas fórmulas: x1 + x2 =10
e x1 * x2 = 24 e isolando o x na primeira fórmula temos
x2 = 10 -x1 e substituindo esta expressão na segunda fórmula temos:
x1 * (10 - x1) = 24, que teremos a segunda fórmula matemática
f(x) = x*(10-x) -24, que é a mesma fórmula de g(x) = -x^2+10x-24, 
o software desenha o gráfico da quadrática
e podemos ver as raízes onde a curva toca o eixo x:
ou também acionando o comando Raízes(f)
Que é criado os pontos A(4,0) e B(6,0)
ou seja resposta: letra "d"
"""
so_ex13_m1 = "data/imagens/img-un1-so13-m1.png"
so_ex13_m2 = """
Para solução usando a calculadora científica vamos\n
partir da ideia que os losangos possuem quatro lados\n
e todos lados congruentes: "angulos iguais ou proporcionais"\n
na mesma direção, então vamos considerar também que a soma\n
dos ângulos internos dos losangos mede 360°, então com\n
a calculadora científica vamos comparar as quatro opções:\n
a) I e II: [120] + [60] [=] [180] dois ângulos opostos medem 120°\n
e os outros dois ângulos opostos medem 60° façamos o seguinte cálculo:\n
 [120] [+] [60] [+] [120] [+] [60] [=] [360] e assim I e II\n
está incorreto, porquê o segundo ângulo dado mede 150° e o terceiro\n
ângulo só poderia valer [30°]
b) II e III: o primeiro ângulo mede 150° e o segundo ângulo deverá\n
medir 30° porque [150] [+] [30] [+] [150] [+] [30] [=] [360], então\n
esta alternativa está incorreta porque na terceira imagem podemos ver\n
que o ângulo dado mede 60° e assim, o outro lado deveria medir 120°\n
que esta figura é incongruente com a do segundo losango.\n
c) II e IV: Na figura na imagem IV temos um losango reto: os lados\n
internos medem 90° e na figura II não é um losango reto: os lados \n
são diferentes de 90°, ou seja esta alternativa está incorreta.\n
d) I e III: Esta alternativa está correta, porque os lados são proporcionais\n
e todos os ângulos de mesma direção são congruentes.Ou seja\n
no losango I um ângulo mede 120° e o outro ângulo seguinte deve valer então 60°\n
o que é semelhante ao losango II pois há na imagem o ângulo de 60°\n
e intuitivamente podemos afirmar que o outro ângulo oposto ao dado na\n
figura IV vale 60° restando o ângulo seguinte medindo 120°, que está correto.\n


"""
so_ex13_m3 = """
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
"""
so_ex13_m4 = """
I) Para construirmos um ângulo de 120 graus e alguns\n
pontos previamente definidos, vamos criar um\n
polígono regura de 6 lados.\n
II) Com a ferramenta ângulo clique em três\n
pontos adjacentes para você formar um
ângulo de 120º com o primeiro losango.\n
oculte os demais pontos e o polígono\n
clicando no pequeno circulo preenchido\n
da Janela de Álgebra.\n
III) Com a ferramenta segmento você pode\n
ligar os pontos para desenhar cada lada do primeiro\n
losango, o de 120º\n
IV) Com a ferramenta reta paralela crie retas paralelas\n
aos dois lados que você conseguiu montar com os segmentos\n
cada reta deve passar pelo ponto de extremidade do lado.\n
V) Com a ferramenta ponto, crie um ponto para fixar a localização\n
dos outros lados que restam e clique na intersecção das duas\n
retas que você acabou de desenhar.\n
VI) Para construir um ângulo de 150º, para o próximo\n
polígono do enunciado, você pode usar \n
um polígono regular de 12 lados\n
VII) Para construir um ângulo de 60º você pode usar\n
um polígono regular de 3 lados\n
VIII) Para construir o quarto losango podemos usar um\n
polígono regular de 4lados que obtemos um ângulo de 90º\n\n

Com o suporte da ferramenta ângulo podemos verificar que\n
os quatro ângulos internos dos losangos I e III são iguais\n
(congruentes), e, portanto como resposta temos letra "d"\n
"""



so_ex14_m1 = "data/imagens/img-un1-so14-m1.png"
so_ex14_m2 = """
Há dois dois valores para os lados do retângulo, e, para que\n
os lados sejam semelhantes, é necessário que os valores para\n
dos lados x e y no retângulo menor sejam proporcionais aos lados\n
dos retângulo maior, então usando sua calculadora vamos calcular\n
agora o valor de x [50] [*] [(] [2] [÷] 5 [)] [=] que corresponde \n
à medida do x para o segundo retângulo x = 50 * 0.4 = 20, e agora, \n
para calcular o valor do lado y temos [150] [*] [(] [2] [÷] [5] [)] [=]\n
que resulta em 60, ou seja y = 150 * 0.4 = 300 ÷ 5 = 60, \n
e assim temos x = 20 e y = 60, está correta a alternativa 'b'.
"""
so_ex14_m3 = """
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
"""
so_ex14_m4 = """
No geogebra criemos uma variável númerica sendo\n
x2 = 50 e outra variável y2 = 150, estes são as medidas\n
dos lados do retângulo maior, que agora podemos calcular\n
a variável da razão de semelhança: no campo de Entrada\n
digitamos rz = 2/5, que na Janela de Álgebra fixa o valor\n
de rz sendo igual a 0.4, agora podemos calcular o valor de x e y\n
que são as medidas dos lados de mesmo nome do retângulo menor\n
temos então assim no campo de Entrada.\n
x1 = x2 * rz, que fixa x1 sendo o lado x com o valor 20\n
e em seguida y1 = y2 * rz que resulta em y1 = y = 60\n
e, portanto, temos os valor x = 20 e y = 60 as medidas
dos lados proporcionais ao retângulo maior, ou seja\n
resposta letra 'b)' x e y valem 20 m e 60 m respectivamente.
"""

so_ex15_m1 = "data/imagens/img-un1-so15-m1.png"
so_ex15_m2 = """
Com a calculadora científica podemos aplicar um cálculo\n
de proporção por semelhança de triângulos, temos dois triângulos\n
retângulos que representam a altura e tamanho da sombra do prédio\n
e um segundo triângulo retângulo que corresponde à altura e sombra de \n
um poste, e por tanto os lados de mesmo nome são proporcionais, \n
x / 40 = 2 / 5\n
x = (2 / 5) * 40\n
ou seja, a altura x do prédio está para 40 "sombra do prédio"\n
assim como 2 "a altura do poste" está para 5\n
e resolvendo esta equação acima teremos o valor correspondente de x\n
fazendo este cálculo na calculadora saberemos o valor de x, \n
ou seja [(] [2] [÷] [5] [)] [*] [40] [=]\n
que resulta em x = 16 metros\n
portanto a resposta correta é letra 'd'.\n
"""
so_ex15_m3 = """
class Exercicio15(): 
    def alturaPredio(self):
        "Modelando a equação do enunciado teremos: "
        x = (2/5) * 40
        print("O predio tem ", x, " metros de altura.")
        '''
        Que resulta em x = 16m, ou seja: resposta letra 'd'
        '''
Exercicio15().alturaPredio()
"""
so_ex15_m4 = """
No Geogebra vamos calcular a altura do prédio assim:\n
No campo de Entrada digitamos s1 = 40, que fixa na Janela de Álgebra\n
s1 = 40 para a sombra do prédio, e agora, s2 = 5, para a sombra do poste,\n
x não sabemos mas para x2 sendo a altura do poste digitemos x2 = 2 metros,\n
que fixa também x2 para a altura do poste.\n
agora modelando a equação por semelhança de triângulos, pois\n
temos dois triângulos retângulos e sabemos as medidas dos outros lados\n
restando assim saber o valor da altura x do prédio então sabemos que\n
x será o valor x1 da expressão matemática:\n
x1 = (x2/s2) * s1 ou seja a altura x = (2/5) * 40\n
em seguida pressionamos enter que teremos a altura x1 = x = 16 metros\n
ou seja, a resposta correta é letra 'd'\n
"""
so_ex16_m1 =  "data/imagens/img-un1-so16-m1.png"

so_ex16_m2 = """
Com a calculadora científica podemos modelar o problema\n
e encontrar mas, propomos a mesma solução assim também,\n
Trata-se de um problema algébrico, que com papel e caneta podemos\n
resolver, a rua da frente é comum às três áreas que\n
são três trapézios, para encontrarmos\n
a relação e comprimentos dos lados x, y e z, do enunciado queremos\n
encontrar a medida z que é o lado que faz frente com a Rua das Rosas.\n
o lado y é o lado reto que faz frente com a Rua das Margaridas\n
o lado x é o lado que faz frente com a Rua das Rosas mas é um\n
dos lados do muro do terreno I.\n
Então modelando os dados podemos estabelecer três equações\n
a) X = (4 * Y)/3\n
b) Z = (24 * X) / Y\n
c) Substiruindo a Equação 'a' na Equação 'c'\n
temos: Z = (24 * (4 * Y)/3 ) / Y\n
podemos verificar esta última fórmula que obtemos\n
24 * 4Y / 3 = ZY\n
96Y = 3ZY então divindo ambos os lados por 3Y temos:\n
32 = Z \n
Ou seja, resposta letra 'c'
"""
so_ex16_m3 = """
Para modelar este exercício você pode comparar os três\n
terenos e então você irá encontrar as relações entre os terrenos\n
usando proporções e usando as medidas que estão disponíveis no\n
exercício para poder encontrar as equações e relações possíveis.\n
use a calculadora para simplificar a fração e encontrar a resposta:\n
o lado 'z' de frente à rua das rosas mede 32 metros.
"""
so_ex16_m4 = """
Para resolvermos este problema de geometria\n
podemos aplicar proporções para encontrarmos a\n
medida do lado 'z'\n
vamos encontrar duas equações fracionárias já\n 
que as medidas são proporcionais pois estão\n
na mesma direção: 'a rua' sendo a rua reta até o limite\n
de encontro com as outras ruas, então façamos assim:\n
observando os terrenos i e iii temos\n
1) y/x = 15/20 ou seja o lado y do terreno está \n
para o lado x “frente com a rua das rosas” assim como\n
o que mede 15 metros do terreno iii está para o lado\n
que mede 20 metros: frente para a rua das rosas \n
e isolando, e simplificando a fração temos: x = 4y/3 \n
e semelhantemente podemos continuar com o terren o i e ii:\n
2) y/x = 24/z leia assim: y está para x assim como 24 está para z\n
substituindo a equação 1 em 2 e isolando o z temos:\n
z = 24x/y e continuando:\n
24x/y = 24*(4y/3)/y e resolvendo esta equação matemática\n
teremos que z é igual a 32 \n
"""