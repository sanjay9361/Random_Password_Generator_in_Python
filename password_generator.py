import random

print("Welcome to Random Password Generator!")

randomchars="ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678910@!#$%^&"
nbrofpwds=int(input("Please enter the number of password to be generated:"))
pwdlen=int(input("Please enter the length of Random Password needed:"))

print("Here are your  random Password:")

for x in range(nbrofpwds):
    pwd=""
    for chars in range(pwdlen):
        pwd=pwd+random.choice(randomchars)
    print(pwd)
    
