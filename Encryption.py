#Reverse Cipher 
#Riginal authoer nostarch.com/crackingcodes// (BSD license)

message = input("Enter the text to encrypt. ")
translated = ""


i = len(message) - 1
while i >=0:
	translated = translated + message[i]
	i = i - 1
	
print(translated)

