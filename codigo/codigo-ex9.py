
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

