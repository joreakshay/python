def ToUpper():
	while True:
		input_string=yield
		yield(input_string.upper())
def Wrapper(func):
	def foo(*args):
		z=func()
		next(z)
		return z
	return foo
@Wrapper
def ToLower():
	while True:
		input_string=yield
		yield(input_string.lower())
toUpper=Wrapper(ToUpper)
z=toUpper()
#next(z)
print(z.send("Hello"))
#	next(z)
#print(z.send("aaaaa"))
z=ToLower()
#next(z)
print(z.send("WWWWWW"))
#next(z)
#print(z.send("qqqqq"))

