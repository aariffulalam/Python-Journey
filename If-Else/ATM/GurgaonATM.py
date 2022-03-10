print('   <---Welcome to "ggn ATM"--->   ')
card=input('enter your ggn card   --->   ')
if card =='ggn card':
	languege=input('enter your languge - hindi, english   --->   ')
	if languege=='hindi' or languege=='english':
		transection=input('enter your transection - enquary, deposite, withdrawal   --->   ')
		if transection=='enquary':
				password=int(input('inter your 4 digit password   --->   '))
				if (password>999 and password<10000):
					print('S.A',16000)
					print('Thank you for using "ggn ATM"')
				else:
					print('invalide password')
					print('Thank you for using "ggn ATM"')
		elif transection=='deposite':
			password=int(input('inter your 4 digit password   --->   '))
			if (password>999 and password<10000):
					amount=int(input('enter your amount   --->   '))
					if amount>0:
						print('diposite done',(16000+amount))
						print('Thank you for using "ggn ATM"')
					else:
						print('"please use ATM properly"     S.A--->  ',16000)
						print('Thank you for using "ggn ATM"')
			else:
				print('wrong password')
				print('Thank you for using "ggn ATM"')
		elif transection=='withdrawal':
			withdrawal=int(input('withdrawal amount   --->   '))
			if withdrawal<=16000:
				password=int(input('inter your 4 digit password'))
				if (password>999 and password<10000):
					print(withdrawal)
					print('Thank you for using "ggn ATM"')
				else:
					print('wrong password')
					print('Thank you for using "ggn ATM"')
			else:
				print('you do not have this amount')
				print('Thank you for using "ggn ATM"')
		else:
			print('ATM pin change not avalible here')
			print('Thank you for using "ggn ATM"')
	else:
		print('this languege not avalible in this atm')
		print('Thank you for using "ggn ATM"')
else:
	print('only accept ggn ATM cards')	