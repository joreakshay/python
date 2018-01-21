#!/usr/bin/python
no1=input("enter no1:")
no2=input("enter no2:")
no3=input("enter no3:")
if no1 < no2 and no1 < no3:
   print("Min=",no1)
elif no2<no1 and no2<no3:
   print("Min=",no2)
else:
   print("Min=",no3)

