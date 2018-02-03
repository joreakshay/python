#def isunique(l1):
def fromkeys(l1,l2):
   l3={}
   y=0
   if type(l2)==list or type(l2)==tuple:
      for x in l1:
         if y< len(l2):
            l3[x]=l2[y]
         else:
            l3[x]=None
         y+=1
   else:
     l3=dict.fromkeys(l1,l2)
   return l3
def inter(l1,l2):
   return[x for x in l1 if x in l2]
#def multtable(l1,l2):
   #return [ for x in range(len(l1,l2+1)) [x*i for i in range(1,11)]] 
#def multof5(l1):
   #return [ x for x in range(len(l1))
   # if (l1.count(l1[x])==1 or l1.remove(l1[x])==None)]
def main():
   l1={1:2,2:3,3:4}
   l2=[1,4]
   print(fromkeys(l1,[]))
if __name__=="__main__":
   main()