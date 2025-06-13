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
so_ex3_m3 = "Solução Exercício 3 método 3"
so_ex3_m4 = "Solução Exercício 3 método 4"