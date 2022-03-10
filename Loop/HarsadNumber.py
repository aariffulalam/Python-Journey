x=int(input('enter your number'))
a=x
sum=0
while x>0:
	digit=x%10
	sum=sum+digit
	x=x//10
print(sum)

if a%sum==0:
	print('Harshard number')
else:
	print('not Harshad number')