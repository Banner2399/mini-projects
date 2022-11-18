import string
import random

length = int(input("Enter password length: "))

characterList = ""


while(True):
	
		characterList = string.punctuation + string.digits + string.ascii_letters
    
		break

password = []

for i in range(length):

	randomchar = random.choice(characterList)
	

	password.append(randomchar)

print("The random password is " + "".join(password))
