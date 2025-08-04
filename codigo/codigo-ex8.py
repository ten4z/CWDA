
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

