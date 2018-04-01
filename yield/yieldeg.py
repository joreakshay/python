def squqre(n):
	for i in range(1,n) :
		yield i*i
x=squqre(5)
for i in x:
	print i
#print next(x)
#print next(x)
