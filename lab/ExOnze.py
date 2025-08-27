

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
