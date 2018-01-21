#!/usr/bin/python
s1=input("enter s1:")
s2=input("enter s2:")
s3=input("enter s3:")
if (s1 + s2) > s3 and  (s1 + s3) > s2 and (s2 + s3) > s1:
	print("Valid triangle")
else:
	print("Invalid triangle")
