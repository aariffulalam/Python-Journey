#Prime number
x=int(input('enter your number       --->  '))
c=0
for i in range(2,x,1):
	if x%i==0:
		c=c+1
if c==0:
	print('-prinme number      --->   ',x)
else:
	print('-not prime number     --->   ',x)