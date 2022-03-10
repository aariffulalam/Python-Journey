#increasing ordered tables

a =int(input('enter your number'))
b=1
while b>=1 and b<=a:
	i=1
	while i<=10:
		print(b,'*',i,'=',b*i)
		i=i+1
	print()
	b=b+1