# The following program mints a nft for a digital asset.
import time
import webbrowser
from datetime import datetime
from user1 import *
from update_accounts import *
from tokens import *

minting_fees = 10
current_owner = user1_info[0]
timestamp = datetime.now().strftime("%B %d, %Y %H:%M:%S")


def mintNFT():
    time.sleep(3)
    print("Create Your NFT")
    print("----------------------------------------------------------------------------------------------------")

    digital_asset = input("Digital Asset: ")
    asset_name = input("Asset Name (one word): ")
    description = input("Description: ")
    selling_price = input("Price: ")
    confirm = input("Would you like to create your NFT? (y/n): ")

    if user1_money >= minting_fees and confirm == "y":
        updateUser1(user1_money - minting_fees)

        with open(asset_name + '-NFT.txt', 'w') as file:
            file.write(current_owner + "\n")
            file.write(digital_asset + "\n")
            file.write(asset_name + "\n")
            file.write(description + "\n")
            file.write(selling_price + "\n")
            file.write(nft_token())

        webbrowser.open(digital_asset)

        print("\n" + "------------------------------------")
        print("New NFT Minted!" + "\n" + timestamp)
        print("------------------------------------")

    elif confirm == "n":
        print("Failed to create NFT!")

    else:
        print("Insufficient Funds!")


mintNFT()