#!/usr/bin/python
no1=input("enter no1:")
no2=input("enter no2:")
no3=input("enter no3:")
if no1 > no2:
   if no1 > no3:
      print("Max=",no1)
   else:
      print("Max=",no3)
elif no2>no1:
   if no2 > no3:
      print("Max=",no2)
   else:
      print("Max=",no3)

