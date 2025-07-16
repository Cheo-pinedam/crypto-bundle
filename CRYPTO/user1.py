# The following program creates an account to store user1's crypto wallet
# Store Information
print("---------------------------------")
print("User Login")
print("---------------------------------")

user1_info = []
user1_file = open("user1.txt", "r")
for i in user1_file:
    data = i.replace("\n", "")
    user1_info.append(data)

user1_public_key = int(user1_info[3])
user1_private_key = int(user1_info[4])
user1_money = int(user1_info[5])

# User login
user1_name = input("Name: ")
user1_username = input("Username: ")
user1_password = input("Password: ")

if user1_name == user1_info[0] and user1_username == user1_info[1] and user1_password == user1_info[2]:
    print("\n" + "--------------")
    print(user1_name + "'s Account")
    print("--------------")

    print("Account Balance: " + str(user1_money) + " coins")
    print("Public Key: " + str(user1_public_key))
    print("\n" + "----------------------------------------------------------------------------------------------------")
else:
    print("\n" + "Invalid Username/Password, try again!")
    quit()
