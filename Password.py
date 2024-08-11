import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','+','(',')']
print("Welcome to Password Generator!")
n_letters = int(input("How many letters you want in your password?:\n"))
n_symbols = int(input("How many symbols you want in your password?:\n"))
n_numbers = int(input("How many numbers you want in your password?:\n"))
password_list = []
for i in range(1,n_letters+1):
    password_list += random.choice(letters)
for i in range(1,n_numbers+1):
    password_list += random.choice(numbers)
for i in range(1,n_symbols+1):
    password_list += random.choice(symbols)
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)