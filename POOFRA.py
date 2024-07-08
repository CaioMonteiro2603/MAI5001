def _init_(self, num,den):
       assert type(num) == int and type(den) == int,'Erro: não é inteiro'
       self.num=num
       self.den=den
       self.simplificar()

def _add_(self,outro):
       somaDen=self.den*outro.den
       somaNum=outro.den*self.num + self.den*outro.num
       if(somaNum%somaDen==0):
           somaNum=somaNum/somaDen
           somaDen=1
       return Fracao(somaNum,somaDen)

def _eq_(self,outro):
       if(self.num/self.den==outro.num/outro.den):
           return True
       return False

def mdc(self):
       num=int(self.num)
       den=int(self.den)
       resto = num % den
       while(resto):
           num=den
           den=resto
           resto=num%den
       return den

def simplificar(self):
       divisor= self.mdc()
       self.num=int(self.num/divisor)
       self.den=int(self.den/divisor)


def _str_(self):
       return str(self.num)+'/'+str(self.den)

f1=Fracao(3,4)
print(f1)
f2=Fracao(4,8)
print(f2)
# # print(f1,f2)
# # f3=f1+f2
# # print(f3)
# # print(f1==f2)
# # f3.simplificar()
# # print(f3)

f1.num=8
f1.simplificar()
print(f1)
f2.den=7
print(f2)
f3=f1._add_(f2) #f3 = f1 + f2
print(f3._str_())
print(f1._eq_(f2))
f3.simplificar()
print(f3._str_())