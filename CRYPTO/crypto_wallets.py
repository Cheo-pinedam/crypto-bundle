# The following program creates crypto wallets.
import random
from RSA import *
from primes import *

# Number of accounts
get_users = input("Enter the number of users: ")
users = int(get_users)

# Create a wallet
for i in range(users):
    # Public/Private Key
    get_key = random.randrange(len(primes_num))
    public_key = primes_num[get_key]
    private_key = find_private_key(public_key, carmichael)

    # Validate the Key
    validate_public_key(public_key, carmichael)

    print("--------------------------------------------------------------------------------------------------------")
    name = input("Enter your name: ")
    username = input("Create a username: ")
    password = input("Create a password: ")
    money = input("Account Balance: ")

    print("\n" + "----------------")
    print("Your Keys")
    print("----------------")

    if public_key == private_key:
        print("Sign Up Unsuccessful! Try Again!")
        quit()
    else:
        print("Public Key: " + str(public_key))
        print("Private Key: " + str(private_key) + "\n")

        with open('user' + str(i + 1) + '.txt', 'w') as file:
            file.write(name + "\n")
            file.write(username + "\n")
            file.write(password + "\n")
            file.write(str(public_key) + "\n")
            file.write(str(private_key) + "\n")
            file.write(str(money) + "\n")
