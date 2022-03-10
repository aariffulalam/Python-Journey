card=input('enter your ggn card')
if card =='ggn card':
	languege=input('enter your languge - hindi, english')
	if languege=='hindi' or languege=='english':
		transection=input('enter your transection - enquary, deposite, withdrawal')
		if transection=='enquary':
			print('S.A',16000)
		elif transection=='deposite':
			amount=int(input('enter your amount'))
			if amount>0:
				print('diposite done',(16000+amount))
			else:
				print('S.A',16000)
		elif transection=='withdrawal':
			withdrawal=int(input('withdrawal amount'))
			if withdrawal<=16000:
				password=int(input('inter your 4 digit password'))
				if (password>999 and password<10000):
					print(withdrawal)
				else:
					print('wrong password')
			else:
				print('you do not have this amount')
		else:
			print('ATM pin change not avalible here')
	else:
		print('this languege not avalible in this atm')
else:
	print('only accept ggn ATM cards')
	