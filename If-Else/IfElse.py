# Greater then of not
a =88
b =99
if (a>b):
	print('a is greater')
elif(a<b):
	print( 'b is greater')
else:
	print('a and b are same')
 
 
 
#take one veriable which is divisible by 5 and 15.
varx = int(input('hello'))
if (varx % 5 and varx % 15) == 0:
	print('divisibla')
else:
	print('not divisible')
 
 
 
#1- 5 saal ki umar ke baad school ja sakte ho.
# 2-18 saal ki umar ke baad vote de sakte ho.
#3- 21 saal ki umar ke baad car drive kar sakte ho.
#4- 24 saal ki umar ke baad shaadi kar sakte ho.
#5- 25 saal ke baad legally drink kar sakte ho.
# i want in print all eligiblities
age = int(input('put your age'))
if age >= 25:
	print('1. eligible for drink alcohol, 2. eligible for marrige, 3. eligible for driving licence, 4. acceptable for vote, 5. eligible for school addimition')
elif age >= 24:
	print('1. eligible for marrige, 2. eligible for driving licence, 3. acceptable for vote, 4. eligible for school addmition')
elif age >= 21:
	print('1. eligible for driving licence, 2. acceptable for vote, 3. eligible for school addmition')
elif age>=18:
	print('1. acceptable for vote, 2. eligible for school addimition')
elif age>=5:
	print('eligible for school addimition')
else:
	print('ghar bethkar dudh piyo')
 
 
 #a shop will give discount of 10% if the cost of parchesed quantity is more than 1000. ask user for quantity suppose, one unit will cost 100. judge and print total cost for user.
quantity = int(input('x'))
if quantity * 100 >= 1000:
	print ('cost is',((quantity*100)-(0.1*quantity*100)))
else:
	print ('cost is', (quantity*100))