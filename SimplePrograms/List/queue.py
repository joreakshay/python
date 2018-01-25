def isEmpty(l1):
   return len(l1)==0
def isFull(l1):
   return len(l1)==100
def Enqueue(l1,data):
   if not isFull(l1) :
      l1.append(data)
   else:
      print( "queue full")
def Dequeue(l1):
   if not isEmpty(l1):
      return l1.pop(0)
   else:
      print (" queue empty")
def menu():
   print(" 1.Enqueue data \n 2.Dequeue data\n 3. exit")      
   return input("Enter choice :")
def main():
   l1=[1,2]  
   while True:
      ch=menu()
      if ch ==1:
         data=input("enter data")
         Enqueue(l1,data)
      elif ch ==2:
         print (Dequeue(l1))
      elif ch==3:
         break
   
if __name__=="__main__":
   main()
