def main():
  string1=input("enter 1st string:")
  string2=input("enter 2nd string:")
  tempstr=string1+string1
  count1=tempstr.count(string2)
  if count1==1:
     print("strings are right rotated")
  else :
     print("strings are not right rotated")
if __name__=="__main__":
   main()