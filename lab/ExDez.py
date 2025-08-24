

class ExDez():
   num = 10
   den = 0
   cont = 0
   expr = "x**2 + 13*x + 40"
   
   def posNums(self, n, d):
      if n >= -10 and n <= 10:
         if self.den >= -10 and self.den <= 10:
            self.den += 1
         else:
            self.num -= 1
            self.den = 0 
            n = self.num
      else:
         self.num += 1
         self.den += 1
         n = self.num
         
      print("num = ", self.num, "den = ", self.den)
      
      x = self.num / self.den
      print(str(self.num) + "/" + str(self.den) + " = " + str(x))
      print("resultado:")
      print(eval(self.expr))
      self.cont += 1

      if self.num >= (-10) and self.num <= 10:
         try:
            self.posNums(n, d)
         except:
            print("Impossível dividir por zero.")
            
      
if __name__ == "__main__":
   ExDez().posNums(1, -10)
