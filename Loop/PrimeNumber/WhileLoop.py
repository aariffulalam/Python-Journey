#Prime number
x=int(input('enter your number       --->  '))
i=2
c=0
while i<x:
	if x%i==0:
		c=c+1
	i=i+1
if c==0:
	print('prinme number      --->   ',x)
else:
	print('not prime number     --->   ',x)
	