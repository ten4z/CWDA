'''
Para Resolver siga os seguintes passos:
No Editor de Código de sua Preferência digite
o seguinte código: 
'''
n = 0.66666 # adicionado a variável n
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
o arquivo que você editou em um interpretado de Python
'''