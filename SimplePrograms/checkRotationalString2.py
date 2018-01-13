def rrotation(str1,str2):
   if len(str1) != len(str2):
      print("length not same")
   else:
      if str2 in (str1+str1):
         print("strings are rrotate")
      else:
         print("strings are not rrotate")
def main():
   str1=input("str1:")
   str2=input("str2:")
   rrotation(str1,str2)
if __name__=="__main__":
   main()
