def isEmpty(l1):
   return len(l1)==0
def isFull(l1):
   return len(l1)==100
def push(l1,data):
   if not isFull(l1) :
      l1.append(data)
   else:
      print( "stack full")
def popx(l1):
   if not isEmpty(l1):
      return l1.pop()
   else:
      print (" stack empty")
def menu():
   print(" 1.push data \n 2.pop data\n 3. exit")      
   return input("Enter choice :")
def main(): 
   l1=[1,2]  
   while True :
       ch=menu()
       if ch == 1:
          data=input("enter data")
          push(l1,data)
       elif ch ==2:
          print (popx(l1))
       elif ch==3:
          break
    
if __name__=="__main__":
   main()
