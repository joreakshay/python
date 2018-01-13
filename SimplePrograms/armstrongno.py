def IsArmstrong(num):
   num2=0
   tempnum=num
   while(tempnum>0):
      rem=tempnum % 10
      rem=rem*rem*rem
      num2=num2+rem
      tempnum=int(tempnum/10)
   if num==num2:
      return True
   else:
      return False
def main():
   num=eval(input("enter num="))
   if IsArmstrong(num):
      print("armstrong")
   else:
      print("not")

if __name__ == "__main__":
   main()