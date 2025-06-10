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