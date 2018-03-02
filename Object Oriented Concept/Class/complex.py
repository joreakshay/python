class Complex :
 def __init__(self,real=0,imgn=0):
  self.real=real
  self.imgn=imgn
 def __del__(self):
  del(self)
 def addComplex(self,c2):
  c3=Complex()
  c3.real=self.real+c2.real
  c3.imgn=self.imgn+c2.imgn
  return c3
 def subtractComplex(self,c2):
  c3=Complex()
  c3.real=self.real-c2.real
  c3.imgn=self.imgn-c2.imgn
  return c3
def main():
 c1=Complex(10,20)
 c2=Complex(4,5)
 c3=c1.addComplex(c2)
 print("{} {}".format(c3.real,c3.imgn))
 