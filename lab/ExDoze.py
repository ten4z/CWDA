

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
