# The following program transfers crypto funds between accounts.
import time
from RSA import *
from blockchain import *
from update_accounts import *


def transfer(user1_name, user1_money, user2_name, user2_money, private_key, public_key, amount_due):
    print("\n" + "-----------------------------------------------------------------------------------------------------")
    print(user1_name + "'s Current Balance: " + str(user1_money) + " coins")
    print(user2_name + "'s Current Balance: " + str(user2_money) + " coins" + "\n")

    user2_money -= amount_due

    if user2_money < 0:
        transaction = user2_name + " sends " + str(amount_due) + " coins to " + user1_name
        print(transaction + "\n")

        signature = write_signature(transaction, private_key, modulus)
        validate_transaction = str(amount_due)
        check_signature(validate_transaction, signature, public_key, modulus)

    elif amount_due == 0:
        print("No transaction was made.")

    else:
        transaction = user2_name + " sends " + str(amount_due) + " coins to " + user1_name
        print(transaction + "\n")

        signature = write_signature(transaction, private_key, modulus)
        validate_transaction = user2_name + " sends " + str(amount_due) + " coins to " + user1_name
        check_signature(validate_transaction, signature, public_key, modulus)

        user1_money = user1_money + amount_due
        updateUser1(user1_money)
        updateUser2(user2_money)

        print(user1_name + " New Balance: " + str(user1_money) + " coins")
        print(user2_name + " New Balance: " + str(user2_money) + " coins" + "\n")

        new_block = [validate_transaction]
        stored_data.append(new_block)
        time.sleep(10)

    createBlockchain()
