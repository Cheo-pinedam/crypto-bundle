# The following program updates the crypto funds in the users accounts.
def updateUser1(amount):
    file = open('user1.txt', "r")
    user_info = []
    for i in file:
        data = i.replace("\n", "")
        user_info.append(data)

    user_info[5] = amount

    with open('user1.txt', 'w') as file:
        file.write(user_info[0] + "\n")
        file.write(user_info[1] + "\n")
        file.write(user_info[2] + "\n")
        file.write(str(user_info[3]) + "\n")
        file.write(str(user_info[4]) + "\n")
        file.write(str(user_info[5]) + "\n")


def updateUser2(amount):
    file = open('user2.txt', "r")
    user_info = []
    for i in file:
        data = i.replace("\n", "")
        user_info.append(data)

    user_info[5] = amount

    with open('user2.txt', 'w') as file:
        file.write(user_info[0] + "\n")
        file.write(user_info[1] + "\n")
        file.write(user_info[2] + "\n")
        file.write(str(user_info[3]) + "\n")
        file.write(str(user_info[4]) + "\n")
        file.write(str(user_info[5]) + "\n")

updateUser1(180)

updateUser2(350)