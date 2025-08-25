

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
