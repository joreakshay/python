def VariableNoOfArgs(*args):
   print(type(args))
   for x in args:
      print(x)

def main():
   VariableNoOfArgs(1,2,3,4,5)
   VariableNoOfArgs(1,2,3,4,5,"abc","xyz")
   
if __name__=="__main__":
   main()
