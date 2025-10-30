so_ex1_m1 = "data/imagens/img-un1-so1-m1.png"

so_ex1_m2 = """
Para Resolver siga os seguintes passsos:\n
X = 0.6666\n
No gráfico da Imagem podemos ver que o valor X está entre os números 0 e 1, ou seja \n
0 < 0.666 < 1, pois bem, há dois valores numéricos entre 0 e 1, um menor que o outro, portando,\n
visualmente podemos notar pela imagem que o primeiro valor está mais próximo de zero, e,\n
visualmente também podemos verficar tambem que o segundo número está mais próximo de 1,\n
Na opção de comparar valores e variáveis da memória da calculadora com a função VERIFY\n
há duas opções lógicas de saída TRUE quando é Verdadeiro e FALSE quando o resultado é Falso.
Aqui nesta solução por conta das 9 variáveis, temos o seguinte fato técnico: \n
A letra ALPHA('X') não pode ser usada para armazenar na memória desta calculadora, portanto\n
resta as outras 8 letras disponíveis disponíveis para cálculo nesta calculadora.\n
Portanto, o primeiro valor será E que\n
empiricamente adicionammos um valor E na memória sendo aproximadamente igual 0.4\n
(0.4) depois pressione [SHIFT], [RCL] depois pressione [E]\n
que armazena 0.4 na variável de memória E\n
Mesmo sabendo que o segundo valor é muito maior que o primeiro valor\n
Sabemos visualmente pela imagem do enunciado que (0.4) é maior que Zero, aqui\n
o 'E' da memória da calculadora. Agora, estipulamos o valor F sendo igual a 0.41\n
Digitamos (0.41) depois pressione [SHIFT], [RCL] depois pressione [F]\n
e o segundo valor que está mais próximo de 1 será F usamos a função VERIFY da calculadora para comparar\n
logicamente se E é maior que zero com os seguintes comandos etapas\n
[MODE][5] VERIF seguido de [ALPHA][E] então pressione [SHIFT][2] e [SHIFT][3]\n
Que se insere o simbolo de maior em seguida adicionamos [0] e [=] que retorna TRUE.\n
Ou seja, é Verdade que (0.4), aqui o E é maior que 0, apenas como forma de comparação\n
queremos que a calculadora mostre que (0.4) é menor que 1, então fazemos os passos\n
[0.4] depois pressione [Shift], [RCL] depois pressione [E]\n
[MODE][5] VERIF seguido de [ALPHA][E] então pressione [SHIFT][2] e [SHIFT][4]\n
Que se insere o simbolo de menor em seguida adicionamos [1] e [=] que retorna TRUE.\n
semelhante ao anterior que também retorna TRUE.\n
Agora comparamos com verify se F é maior que E, que retorna TRUE.\n
como F também é maior que zero e menor do que 1 e, na calculadora também mostrou com a comparação\n
que F é maior  que E. Logo podemos afirmar que a variável F é o número dado no enunciado da questão. ou seja:\n
F = 0.66666... resposta: letra C.\n
"""

so_ex1_m3 = """
'''
Para Resolver siga os seguintes passos:
No Editor de Código de sua Preferência digite
o seguinte código: 
'''
n = 0.6666 # adicionado a variável n
v1 = 0 # 1º mais próximo de n
v2 = 1 # 2º mais próximo de n
'''
existe um segundo valor no gráfico
da imagem, que está também entre 0 e 1
'''
n2 = 0.4 # estipulamos este n2 sendo 0.4
print('n está no intervalo [0 : 1]?', n > 0 and n < 1) #agora comparamos

print('n2 está em [0 : 1], portanto: ', n2 > 0 and n2 < 1) #se n2 também está no intervalo
'''
Já sabemos e confirmamos que os dois valores
n e n2 são maiores que 0 e menores que 1
ou seja, estes dois números estão no intervalo
em que estamos visualizando, agora precisamos
saber se o número dado é menor que o número
que estamos imaginando, se n > n2?
'''
print('n2 está no intervalo [0 : 1]?', n > n2) #se n é maior que n2
'''
Que retornou True 'Verdadeiro', ou seja o n 
que foi dado no enunciado é maior que o outro 
número que pela imagem imaginamos ser n2.
'''
print('n = ', n, 'Resposta: letra "C"')
'''
então o n é 0.6666.
e a resposta está na letra 'C' da questão 1
'''
'''
e salve com a extensão .py
em seguida no seu sistema Operacional carregue
o arquivo que você editou em um interpretador de Python
'''
"""

so_ex1_m4 = """
Para Resolver siga os seguintes passsos:\n
Na interface do Software Matemático Geogebra versão Classic 5.2\n
Adicione os pontos visualmente com as ferramentas de criação do software\n
e compare e intuitivamente verifique a localização do número dado\n
no plano cartesiano e eixo horizontal conforme ilustra a figura do enunciado.\n
Faça o seguinte: Acessando a função a função Segmento e visualmente clicando\n
no ponto 0 em seguida clicando no ponto C teremos o comprimento\n
n = 0.66666 que arredondado para cima n = 0.67 ou tambem,\n
Acessando o campo de entrada e digitando o seguinte comando Distância((0.0), C)\n
também teremos o valor de n2 = 0.67.\n
Opcionalmente você pode acessar o arquivo diretamente no Software Geogebra.\n
"""

so_ex2_m1 = "data/imagens/img-un1-so2-m1.png"

so_ex2_m2 = """
Para Resolver siga os seguintes passos:\n
para saber o que cada aluno recebeu de troco devemos\n
fazer alguns cálculos que são o que se segue:\n
para fins didáticos vamos usar variável na calculadora HP 300s+\n
Para armazernar valores na memória de sua calculadora\n
digite o número na calculadora, e em seguida,\n
quando o número estiver visivel na tela \n
pressione o botão [Shift] seguido de [RCL] assim:\n
Assim digite o seguinte número: 2749.60 \n 
em seguida pressione [Shift][RCL] em seguida escolha uma letra ALPHA\n
pressionando o respectivo botão da letra assim: [A],\n
que na tela haverá uma saída informando\n
a direção do número para a variável de letra em que você informou,\n
em seguida pressione igual que o número será\n
armazenado na variável de memória de letra correspondente, aqui A.\n
A = 2749.60\n
D = 754.15 + 285.35 + 880.50\n
que resoultou: D = R$ 1920\n
em seguida pressione o botão [=] que você verá\n
na tela de sua calculadora o seguinte valor: 1920\n 
Sabemos pelo enunciado da questão que os alunos arrecadaram\n
o valor de 2749.60 que agora podemos encontrar a diferença\n
do valor com que os alunos pagaram a assim:\n
A - D ou seja: 2749.60 - 1920 que resultou no seguinte valor\n
uma fração com o valor 4148/5 e, pressionando o botão [S D]\n
temos o seguinte valor para o total geral de troco:\n
R$ 829.6 que é o total da sobra das despesas, ou seja, restou o troco\n
que cada aluno vai receber, e dividindo este valor \n
pelo número de alunos temos:\n
 829.6/40 = 4148/5/40 \n
 = 1037/50 \n 
 que pressionando [S D] de novo temos o seguinte valor:\n
 R$ 20.74 que é o troco que cada aluno dessa turma deve receber.
"""

so_ex2_m3 = """
'''
Vamos criar três variáveis
'''
despesas = 0.0
arrecadado = 0.0
trocoTotal = 0.0
'''
sabemos que todos alunos arrecadaram
o valor 2749.60 que excede ao total de 
despesas da turma, então atribuimos:
'''
arrecadado= 2749.60
'''
Sabemos também os valores das despesas
então atribuimos:
'''
despesas = 754.15 + 285.35 + 880.5
'''
Estes números já estão em variáveis do
algoritmo e podemos saber seus valores:
'''
print("arrecadado = ", arrecadado)
print("despesas = ", despesas)
'''
Agora podemos verificar quanto é o troco
que faltar distribuir entre os alunos
'''
trocoTotal = arrecadado - despesas
'''
Que podemos saber quanto será:
'''
print("Troco total = ", trocoTotal)
'''
E agora dividindo este valor pela quantidade
de alunos podemos saber quanto cada aluno
vai receber de troco:
'''
print('Troco cada Aluno = ', trocoTotal/40)
'''
Ou seja a resposta correta é: Letra "D"
'''
"""

so_ex2_m4 = """
para resolver este exercício,  primeiro façamos o seguinte:\n

• criamos a variável arrecadado no campo de entrada\n
adicionando o seguinte comando: arrecadado = 2749.6\n
em seguida pressionamos a tecla ENTER.\n\n

Que cria na janela de álgebra a variável de \n
objeto controle deslizante que não precisamos\n
exibi-lo, consideramos aqui apenas seu valor que\n
está lá na Janela de Álgebra em formato de fração.\n\n

Façamos comandos semelhante ao passo dado\n
da criação da primeira variável "arrecadado", mas,\n
agora, para as demais variáveis que queremos\
conforme os valores informados no enunciado: \n
conjuntoMusical, enfeitesIgreja, salaDeBaile, atribuindo o respectivo\n
valor para cada variável.\n\n

• Lembre conforme consultando a cada variável\n
com suas propriedades você verá que é possível fazer\n
operações matemáticas e lógicas com as variáveis, além também\n
de executar funções matemáticas presente nos módulos\n
do software geogebra. Conferindo as operações e\n
analisando as operações de cálculo você verá que\n
a resposta para esta questão é v = 20.74.
Ou seja: respsosta é letra "D"\n
"""

so_ex3_m1 = "data/imagens/img-un1-so3-m1.png"

so_ex3_m2 = """
Sabemos que a letra C é uma fração que consiste no resto\n
da soma das demais frações, e, ao somar a fração A + B + C\n
corresponde a unidade, ou seja A + B + C = 1 que no todo trata-se\n
dos 120 apartamentos, então vamos para a calculadora:
com sua calculadora ligada pressione [1] e depois [÷] e então [4]\n
logo depois pressione [Shift] e então [RCL]\n
seguido de [A] que sua calculadora vai mostrar uma seta apontando\n
a fração 1/4 para a variável A, então pressione [=] igual\n
agora vamos armazenar a segunda fração:
[1] depois pressionamos [÷] e depois  [3] que vai exibir a fração\n
na tela da calculadora em seguida com o valor 1/3 na tela pressione\n
[Shift] e [RCL] seguida da variável ALPHA [B] então [=]\n
que vai armazenar a variável B também na memória da calculadora\n
agora sabemos que os 120 apartamentos corresponde na unidade,\n
ou seja as fração A + B + C = 1, o total de apartamentos\n
Pois bem, para sabermos o valor que corresponde à fração C\n
fazemos a diferença: C = 1 - A - B, então com esta fórmula \n
podemos encontrar o valor de C com a calculadora \n
a expressão de comandos na calculadora fica da seguinte forma\n
[1] depois [-] seguido de [ALPHA] e [A] e continua [-] e [ALPHA] [B]\n
depois pressione igual que você verá o resultado dessa soma de frações:\n
pressionando [=] resultará e aparecerá na tela 5/12\n
se você seguiu todos os passos de forma coreta.\n
Teremos, portanto como resposta letra "C".
"""

so_ex3_m3 = """
'''
Queremos encontrar a fração que corresponde a C.
No enunciado temos três frações A = 1/4, B=1/3
e C que não sabemos o valor ainda. Portanto, 
adicionando as variáveis de valores de ponto
flutuante que corresponde às frações teremos.
'''
a = 1/4
b = 1/3
print("A = ", a)
print("B = ", b)
'''
que vai retornar os valores aproximados em 
ponto flutuante correspondente a cada fração
que já atribuimos.
Agora já podemos calcular o valor de C
'''
print("C = ", 1 - a - b)
'''
Se a linha abaixo retornar True, então nosso
cálculo está correto.
'''
print(1 - a - b == 5/12)
'''
Que mesmo sendo um número com casas decimais
podemos comparar estes valores e verificar que 
o C que encontramos é o que equivale à fração 5/12. 
Portanto a resposta é letra "C"
'''
"""

so_ex3_m4 = """
Para resolver este exercício vamos criar três variáveis a, b e c.\n
No campo de entrada digita a = 1/4\n
depois digite b= 1/3\n
Sabemos que a soma a + b + c = 1 que corresponde ao\n
total de 120 apartamentos, portanto podemos continuar e\n
Agora digite no campo de entrada c = 1 - a- b que você\n
poderá notar que estes nomes de variáveis aparecerão\n
com uma coloração diferente e visivel no painel da Janela de Álgebra\n
pois já estão na memória deste atual software matemática.\n\n
Portanto a resposta é letra C: 5/12
"""

so_ex4_m1 = "data/imagens/img-un1-so4-m1.png"

so_ex4_m2 = """
Para resolver este exercício de forma explicativa\n
Imagine um número q = a/b com a e b inteiros e b diferente de zero\n
você poderá procurar digitando uma grande variedade\n
de números em sua calculadora para encontrar porém não\n
vai conseguir um número q deste formato que seja igual ao número\n
informado no inunciado, pelo fato de que este número dado\n
é um número irracional, ou seja não existe esta fração\n
dadas as condições que temos que seja igual a raiz quadrada de 30.\n
ou seja a resposta é "D" irracional.\n
"""

so_ex4_m3 = """
'''
Queremos encontrar um número n tal que
n seja igual a raiz quadrada de 30, e para isso
podemos usar o operador ** para expoente que
iremos encontrar a raiz quadra de 30 sendo
o valor que queremos encontrar. Porém teremos
duas opções, achar um inteiro ou encontrar um
número de ponto flutuante, aqui se o número for
de ponto flutuante e tiver infintas casas decimais
que não é dízima periódica: não há um padrão de
repetições númericas teremos um número irracional.
então façamos o seguinte no editor de códigos
'''

n = 30 ** (0.5) # Raiz quadrada de 30
print(n)

'''
Que exibiu um número que tem infinitas casas decimais\n
e também não é dízima periódica. E para confirmarmos\n
Que este número é irracional podemos digitar type(n)\n
que confirmemos que se trata de um número irracional\n
por não ser inteiro, logo "float" que aqui estabelecemos\n
 sendo um número irracional.\n
'''
print(n, type(n))
'''
n não é integer, mas float, tem ponto decimal, com infinitas\n
casas decimais, mas não é dízima periódica.\n
portanto isso explica n ser irracional.\n
Resposta letra "D" irracional.
'''
"""
so_ex4_m4 = """
Pelo enunciado o número n é raiz quadrada de 30\n
O número n não é inteiro, pois há infinitas casas decimais\n
e, também não há um número q = n tal que\n
q = a/b tal a e b seja inteiro com b diferente de zero que\n
seja igual a raiz quadrada de 30, não é racional e\n
também não é dizima periódica, ou seja n é irracional.\n
Podemos também comparar no campo de entrada se n é inteiro.\n
com a função ÉInteiro(x) que retorna false, o número\n
não é inteiro, não é racional é irracional letra "D".
"""
so_ex5_m1 = "data/imagens/img-un1-so5-m1.png"

so_ex5_m2 = """
Para resolver este exercício com auxílio da calculadora\n
Científica, você pode adicionar a expressão toda na calculadora\n
que ela fará a simplificação desses radicais e retornar\n
o valor 8. Uma dica use o botão de raiz quadrada e separe\n
cada parte interna com radical com [(] e [)], abrindo e\n 
fechando parênteses, fazendo corretamente a expressão\n
matemática na calculadora você terá como resultado o número 8.\n
Ou seja, resposta letra "b" 8.
"""

so_ex5_m3 = """
'''
Podemos fazer o cálculo imediatamente no terminal de programação,\n 
com linhas de código, então faça o seguinte. digite a seguinte\n
fórmula matemática para o script encontrar a solução.\n
'''
n = (62 + (1 + (9)**0.5)**0.5)**0.5
print(n)
'''
Que exibe, 8.0, ou seja n = 8.\n
Resposta letra 'b' 8.
'''
"""

so_ex5_m4 = """
Podemos fazer o cálculo imediatamente no campo de Entrada, \n
como comando matemático, então faça o seguinte: Digite a seguinte\n
fórmula matemática na área de entrada de fórmulas para encontrar a solução.\n

n = (62 + (1 + (9)**0.5)**0.5)**0.5

Que exibe, n = 8 na Janela de Álgebra, ou seja n = 8.\n
Resposta letra 'b' 8.
"""

so_ex6_m1 = "data/imagens/img-un1-so6-m1.png"

so_ex6_m2 = """
Solução do Exercício 6 com a calcudora científica HP 300s+:\n
Primeiro examinando o gráfico da imagem no enunciado temos \n
a posição dos números na reta numérica. Ou seja para solucionarmos\n
este exercício basta verificarmos se os números dados da alternativa\n
de resposta estão na posição correta do gráfico, como segue:\n
olhando inicialmente achamos que a solução correta é letra a, mas\n
vamos analisar também as outras alternativas e comparar.\n
Sabemos pelo gráfico, que A está entre -2 e -1 ou seja: -2 < A < -1 e\n
assim, sabemos também que A é negativo. B está entre 0 e 1 positivo: \n
e C está entre 1 e 2. Que assim podemos verificar que C não é pi.\n
Para sabermos o valor de pi, sendo pi o símbolo π, podemos com a calculadora\n
no modo 1: COMP digitar [SHIFT] [x10^x] [=] que como saída podemos \n
verificar 3.1415 o valor numérico desta letra dada na alternativa d. \n
Na letra "b" temos A = -15/10 = -1.5 B= -0.6 e C = √2, sabemos também \n
o valor de √2 que no modo 1: COMP da calculadora resulta em aproximadamente 1.4142\n
ou seja, já sabemos que esta alternativa está eliminada, pelo fato de que\n
o número B deve ser positivo. E, a letra c também é eliminada\n
pelo fato de que o número A deve ser negativo, e, da mesma forma,\n
a alternativa d também é eliminada pelo fato de que o número A deve ser negativo\n
e recorrendo ao modo 1: COMP da calculadora ao acionarmos a letra pi \n
retorna um número maior que 2 que extrapola e é maior que os números dados do gráfico.\n
Portanto, como resposta, resta confirmarmos que a solução é a alternativa "a".\n
"""

so_ex6_m3 = """
from math import pi
'''
Olhando inicialmente o gráfico da imagem
dada no enunciado podemos imaginar que a
resposta correta seja letra "a", mas vamos
analisar as outras alternativas.
'''
A1 = -1.5 # variável do número 'A' da alternativa a
B1 = 6/10 # variável do número 'B' da alternativa a
C1 = 2**0.5 # variável do número 'C' da alternativa a

print("A1 = ", A1)
print("B1 = ", B1)
print("C1 = ", C1)
print("______________________________________________________")

A2 = -15/10 # variável do número 'A' da alternativa b
B2 = -0.6 # variável do número 'B' da alternativa b
C2 = 2**0.5 # variável do número 'C' da alternativa b

print("A2 = ", A2)
print("B2 = ", B2)
print("C2 = ", C2)
print("______________________________________________________")

A3 = 1.5 # variável do número 'A' da alternativa c
B3 = 0.6 # variável do número 'B' da alternativa c
C3 = 1.5 # variável do número 'C' da alternativa c

print("A3 = ", A3)
print("B3 = ", B3)
print("C3 = ", C3)
print("______________________________________________________")

A4 = 1.5 # variável do número 'A' da alternativa d
B4 = 2**0.5 # variável do número 'B' da alternativa d
C4 = pi # variável do número 'C' da alternativa d

print("A4 = ", A4)
print("B4 = ", B4)
print("C4 = ", C4)
print("______________________________________________________")

'''
Com o seguinte comando podemos verificar
que a alternativa "b" está incorreta, pelo
fato de que o B2 é menor que 0
'''
print("B2 > 0 ? ", B2 > 0)
'''
Que resultou em False, ou seja:
esta alternativa b está incorreta.
Com o seguinte comando podemos verificar
que c alternativa "b" está incorreta, pelo
fato de que o B2 é menor que 0
'''
print("A3 < 0 ? ", A3 < 0)
'''
Que resultou em False, ou seja:
esta alternativa b está incorreta
Com o seguinte comando podemos verificar
que c alternativa "b" está incorreta, pelo
fato de que o B2 é menor que 0
'''
print("2 = pi ? ", 2 == C4)
'''
Que resultou em False, ou seja:
esta alternativa b está incorreta.
Ou seja, resultou como correta apenas a opção "a".
Esta é a resposta da questão: letra "a"
'''
"""

so_ex6_m4 = """
Podemos fazer o seguinte para solução desta questão:
Vamos criar doze números um para cada valor dado nas alternativaszn
para A, B, C e, D, respectivamente, que ficará assim:\n
A1 = -1.5; B1 = 6/10; C1 = 2**0.5, faça de forma análoga para com\n
os demais valores informado no enunciado. que na interface gráfica\n
do software geogebra essas variáveis que inicializadas no campo de entrada\n
serão listadas no canto esquerdo da tela da Janela de Álgebra\n
vamos comparar cada valor informado com uma expressão lógica que\n
verifica estes números para nós com apenas um comando para cada alternativa:\n
(An >= (-2) && An <=(-1)) && (Bn >= (0) && Bn <=(1)) and ((Cn >= (1) and Cn <=(2)))\n
Assim: digitando o comando acima atribuido a uma variavel da questão a, qa = formula\n
para a alternativa a substituimos o n pelo número dado de cada alternativa\n
e faça as demais alternativas b, c e d com os valores da respectiva alternativa.\n
Analisando assim podemos verificar que a opção que exibir verdade para toda \n
a expressão lógica será a correta\n
que podemos verficar que apenas a alternativa a é correta.\n
solução letra "a".
"""

so_ex7_m1 = "data/imagens/img-un1-so7-m1.png"
so_ex7_m2 = """
A solução desta questão na calculadora HP 300s+ consiste\n
nas seguintes em digitar no modo de operação 1: COMP a expressão\n
dada no enunciado conforme se faz um cálculo manual, mas agora \n
usando as funções de sua calculadora, lembre se de substituir\n
a letra x da fórmula pelo valor 2/5 e siguir fazendo o cálculo normalmente\n
com as demais funções de expoente, soma e divisão, que ao pressionar\n
a tecla [=] você terá o valor de resposta: 9/25, ou seja, a resposta
correta é letra 'b' 9/25.
"""
so_ex7_m3 = """
'''
Temos uma expressão matemática para
resolver neste exercício. O interpretador
desta linguagem de programação faz
cálculos matemáticos com rapidez e precisão.
então vamos criar uma função matemática
e passar para ela o valor dado no enunciado.
'''

def exercicio7(x):
    
    print("x = ", x, " f(x) = ", x**2 + 1/5)

'''
Na linha abaixo chamamos o método e passamos
um argumento com o valor de x.
'''
exercicio7(2/5)

'''
que retorna um número de ponto flutuante
que tem como resposta 0.36, o mesmo valor da fração 9/25,
ou seja, resposta: letra "b"
'''
"""    
    
so_ex7_m4 = """
Para resolvermos esta questão vamos fazer o seguinte,\n
primeiro no campo de Entrada digitamos o seguinte comando n = 2/5\n
Em seguida digitamos a expressão atribuida ao valor q7:\n
assim: q7 = n**2 + 1/5 que como resposta na Janela de Álgebra\n
teremos o valor q7 = 9/25, portanto, resposta: letra 'b'.
"""

so_ex8_m1 = "data/imagens/img-un1-so8-m1.png" 
so_ex8_m2 = """
Seria interessante se nesta calculadora houvesse também uma função\n
de expandir polinômio e fatorar expressões matemáticas.
"""
so_ex8_m3 = """

'''
Podemos testar uma função matemática
se assume o mesmo valor da expressão dada,
se ocorrer de os valores serem iguais
podemos afirmar que a função pode ser a mesma,
porém, fatorada.
'''
def verificarFuncao():
    x = 5 #considere este número apenas para teste.
    formula = "4*x**2 + 16*x + 16"
    qfa = "(x + 4)**2"
    qfb = "(2*x + 2)**2"
    qfc = "(x + 4) * (x - 4)"
    qfd = "4*((x + 2)**2)"

    if eval(formula) ==  eval(qfa):
        print("funcao a: sim, pode ser esta função")
    else:
        print("funcao a: não, função icorreta")

    if eval(formula) ==  eval(qfb):
        print("funcao b: sim, pode ser esta função")
    else:
        print("funcao b: não, função icorreta")

    if eval(formula) ==  eval(qfc):
        print("funcao c: sim, pode ser esta função")
    else:
        print("funcao c: não, função icorreta")

    print(eval(formula)) # veja que esta formula funciona
    print(eval(qfd)) # esta formula e a do enunciado são iguais
    
    if eval(formula) ==  eval(qfd):
        print("funcao d: sim, pode ser esta função")
    else:
        print("funcao d: não, função icorreta")
    '''
    Veja que construimos uma função matemática
    que está totalmente dinâmica assumindo o valor de x
    resposta letra "d"
    '''
        
verificarFuncao()
"""
so_ex8_m4 = """
Para resolver esta questão com o software Geogebra \n
vamos fazer o seguinte, crie uma função de nome fa com o \n
seguinte valor no campo de entrada "fa = (x + 4)^2 \n
Note que o geogebra plotou o desenho do gráfico da quadrática fa\n
agora vamos para a segunda fórmula no campo de entrada "fb = (2*x + 2)^2" \n
De fórmula análoga digite as seguintes outras fórmulas dadas na questão\n
"fc = (x + 4)*(x - 4)"\n
"fd = 4*(x + 2)^2"\n
agora, por fim digite a função f que é a fórmula que queremos comparar,\n
se o gráfico for o mesmo e a expressão matemática também ser a mesma\n
então esta função é a mesma do enunciado, porém no modo fatorada.\n
a função f dada no enunciado é f = 4*x^2 + 16*x + 16, você pode ocultar\n
uma dessas duas, a fd ou a f junto com as demais que você verá que as \n
funções fd e f são a mesma e na janela de visualização tem o gráfico sobreposto\n
Opcionalmente você pode digitar no campo de entrada o seguinte comando \n
fd == f [ENTER] que retorna "true", sendo assim, verificamos que \n
a função da alternativa "d" é a mesma do enunciado.\n
e assim vemos que a letra "d" é a alternativa correta.

"""

so_ex9_m1 = "data/imagens/img-un1-so9-m1.png" 
so_ex9_m2 = """
Trata-se de uma expressão algébrica, que com a calculadora não há \n
uma forma de somar esta expressão por comandos próprios, portanto. \n
as demais soluções respondem a esta questão.

"""
so_ex9_m3 = """

'''
Podemos testar uma função matemática
se assume o mesmo valor da expressão dada,
se ocorrer de os valores serem iguais
podemos afirmar que a função pode ser a mesma,
que equivale ao perímetro do quadrilátero.
'''
qfa = "6*x - 4"
qfb = "4*x - 6"
qfc = "-4*x**2 + x - 3"
qfd = "x + 4"

def verificarFuncao(expressao):
    x = 5 #considere este número apenas para teste.
    ladoA = "2*x + 1"
    ladoB = "x - 3"
    ladoC = "2*x + 1"
    ladoD = "x - 3"
    perimetro = eval(ladoA) + eval(ladoB)+ eval(ladoC)+ eval(ladoD)

    print(perimetro)
    print(eval(expressao))
    
    if perimetro ==  eval(expressao):
        print("Sucesso, A expressão {} está correta.".format(expressao))
    else:
        print("Falha, a expressão {} não está correta.".format(expressao))
    '''
    Veja que construimos uma função matemática
    que está totalmente dinâmica assumindo o valor de x
    resposta letra "a"
    '''
        
verificarFuncao(qfa)

"""
so_ex9_m4 = """
A solução para este exercício consiste em desenhar um polígono\n
com os pontos definidos dinâmicamente com a ferramenta controle deslizante\n
Adicione um controle deslizante de nome vx com incremento de 0.1 e \n
limites de 0 a 20, e adicione os vértices do quadrilátero que assume\n
o valor vx para o lugar do tamanho dos lados, que são definidos os Pontos\n
que contém a componentes definidas pelo controle deslizante dada a fórmula matemática\n
em seguida desenhe o quadrilátero clicando no botão polígono\n
em seguida selecione cada Ponto para definir o lado na ordem correta\n
Você pode opcionalmente também calcular o perímetro do quadrilátero\n
de várias formas para comparar a resposta da questão:\n
ao digitar a fórmula Perímetro( <Polígono> ) em que o Texto <Polígono>\n
você pode medir o perímetro do polígono e comparar se a soma dos lados\n
é exatamente este mesmo valor em que se obteve com a função do Geogebra.\n
assume o nome do quadrilátero exibido na Janela de Álgebra.\n
Lembrando que para o cálculo correto de cada  lado do polígono \n
deve calcular a fórmula com a função abs() de valor absoluto para cada lado.
que assim, você poderá chegar na resposta correta: letra "a".
"""

so_ex10_m1 = "data/imagens/img-un1-so10-m1.png"
so_ex10_m2 = """
Vamos encontrar as raízes desta equação por Soma e Produto na Calculadora\n
para isso vamos usar as variáveis de memória E, F, C e D para as raízes.\n
E é a menor raiz e F é a maior raiz, C é o valor da soma das raízes\n
que resulta nos coeficientes C = -b/a e D é o valor do produto das duas raízes\n
agora estabelecemos C = -13/1 e D = 40/1
e agora 
Pela regra de soma e produto encontramos dois pares de números que satisfaz\n
a regra à saber (5, 8) e (-5 e -8), mas devemos nos atentarmos para o sinal\n
destes números, porque a soma dois dois resulta em 13 e -13, mas, ainda pela regra\n
sabemos queo valor C é negativo, então nos resta a segunda opção em que as raízes\n
são iguais a (-5, e -8) e agora comparando para termos certeza de que encontramos \n
as reais raizes da equação fazemos a seguinte operação:
substituímos na expressão a primeira raiz que encontramos:\n
(-5)² + 13*(-5) + 40 e continuando\n
25 -65 + 40 =  65 -65 = 0, está correto, e agora com a segunda raiz\n
(-8)² + 13*(-8) + 40 e continuando \n
64 - 104 + 40 = 104 - 104, está correto, e,\n
portanto: -5 e -8 são raizes da quadrática dada.\n
e, para verificar a questão do enunciado temos:\n
-5 (a maior) - (-8) (a menor) subtraindo a menor raiz da maior:\n
-5 -(-8) = -5 + 8 = 3\n
resposta: letra "a".

"""
so_ex10_m3 = """
'''
#Encontrar as Raízes por Soma e Produto com Script
class ExDez():
   num = 10
   den = 0
   cont = 0
   expr = "x**2 + 13*x + 40" 
   def posNums(self, n, d):
      '''
      Este método é para encontrar números racionais\n
      do tipo n/d, no intervalo de -10 a 10, \n
      para compararmos na fórmula se este\n
      número é raiz da quadrática.
      '''
      if n >= -10 and n <= 10:
         if self.den >= (-10) and self.den < 10:
            self.den += 1
         else:
            self.num -= 1
            self.den = 0 
            n = self.num
      else:
         self.num += 1
         self.den += 1
         n = self.num
      self.cont += 1
      #print("num = ", self.num, "den = ", self.den)    
      if  self.den > 0 or  self.den < 0:
          x = self.num/self.den
          #print(eval(self.expr))
          if eval(self.expr) == 0:
             print(x)
             '''
             Que na linha acima resultou em três números com os\n
             números -5, -8 -5, o menos cinco se repetiu, e vamos\n
             utilizar os outros dois números, o -5 e -8 \n
             dado o enunciado, vamos subtrair a menor raiz\n
             da maior raiz assim: -5 -(-8) =  3,\n
             resposta letra "a"
             '''
      else:
          pass
      if self.num >= (-10) and self.num <= 10:         
         self.posNums(n, d)
         
if __name__ == "__main__":
   ExDez().posNums(1, -10)

'''
"""

so_ex10_m4 = """
Solução com Software Geogebra\n
Ao adicionar a fórmula da quadrática na Janela de àlgebra\n
podemos ver o gráfico da função matemática "f" na\n
Janela de visualização.\n
Então adicionamos o segundo comando: Raiz(f)\n
que o software geogebra cria dois Pontos A e B\n
sendo A(-5, 0) e B(-8,0), ou seja as ráizes são -5 e -8\n
e, subtraindo o menor número do maior temos:\n
-5 - (-8) = 3, ou seja, a resposta é letra(a)\n
"""

