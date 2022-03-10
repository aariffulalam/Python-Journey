x=int(input('enter your number '))
for i in range(2,x,1):
	
	if x%i==0:
		print(x,'not prime no')
		break
	else:
		print(x,'prime no')
		break