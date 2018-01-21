
def turnoffbits(num,pos,noofbits):
   if pos<noofbits:
      return 0
   x=(1<<noofbits)-1
   x=x<<(pos-noofbits)
   return num&(~x)
   
def IsMultipleof8(num):
   return num & mult-1 ==0
  
def countBit(num):
   no=1
   cnt=0
   while(num <no):
      if num & no !=0:
         cnt +=1
      no =no<<1
   return cnt
   
def offrhightmostbit(num):
   no=1
   
   while(num >=no):
      if num & no !=0:
         break
      no =no<<1
   return num&(~no)

   from sys import getsizeof
def CountOnBits(num):
	x=1
	count=0
	while(abs(num)>=x):
		if num<0:
			if (num & x ==0):
				count+=1
		else:			
			if (num & x !=0):
				count+=1
		x=x<<1
	if num<0:
		count=((getsizeof(num)*8)-count)
	
	return count
	
def IsMultOf32(num):
	return num&32==0

def turnoffbits(num,pos,noofbits):
   if pos<=noofbits:
      return -1
   x=(1<<noofbits)-1
   x=x<<(pos-noofbits)
   return num&(~x)

def turnonbits(num,pos,noofbits):
   if pos<=noofbits:
      return -1
   x=(1<<noofbits)-1
   x=x<<(pos-noofbits)
   return num|(x)
   
def togglebits(num,pos,noofbits):
   if pos<=noofbits:
      return -1
   x=(1<<noofbits)-1
   x=x<<(pos-noofbits)
   return num^(x)

def swapbits(num1,num2,pos,noofbits):
   if pos<=noofbits:
      return -1
   x=(1<<noofbits)-1
   y=(1<<noofbits)-1
   x=x<<(pos-noofbits)
   y=y<<(pos-noofbits)
   num1=num1&(~x)
   num2=num2&(~y)
   x=num1&x
   y=num2&y
   num1=num1|y
   num2=num2|x
   print("after swap bits{},{}".format(num1,num2))

def main():

   num1 = eval(input("enter no1="))
   num2 = eval(input("enter no2="))
   pos = eval(input("enter pos="))
   noofbits= eval(input("enter no of bits="))
   #print("num of bit is",turnoffbits(num,pos,noofbits))
   #print("num of bit is",turnonbits(num,pos,noofbits))
   #print("num of bit is",togglebits(num,pos,noofbits))
   swapbits(num1,num2,pos,noofbits)
if __name__=="__main__":
   main()