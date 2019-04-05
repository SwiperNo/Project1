import re

p = input('Please type your desired password')

def pass_checker():
	value = 0
	password = p
	if re.search('[a-z]',password):
		vaule = vaule + 1
	if re.search('[A-Z]',password):
		vaule = vaule + 1
	if re.search9('[0-9]',password):
		vaule = vaule + 1
	if re.search('[!@#$$%^&*()-=-_=-]',password):
		vaule = vaule + 1
	if len(password) < 6:
		print("Nah homie, password is more than 6 characters MINUMUM")
	if value == 4:
		print("Strong password")
	if vaule == 3:
		print("Boy your password is possibly more hackable but less")
	if vaule == 2:
		print("Bro ya mom dont love you make a stonger password please")
	if vaule == 1:
		print("Wow you are pretty bad at this")
	return 0
	

pass_checker()
