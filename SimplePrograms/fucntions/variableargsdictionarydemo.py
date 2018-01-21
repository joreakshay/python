def VariableArgsDictionaryDemo(a,b,c,*args,**kwargs):
   print(a,b,c)
   print(type(args))
   for x in args:
      print(x)
   for key in kwargs:
      print(key,kwargs[key]
def main():
   VariableArgsDictionaryDemo(1,2,3,7,8,9,10,name="akshay",last="Jore")
if __name__ == "__main__":
   main()