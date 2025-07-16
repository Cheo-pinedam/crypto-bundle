# The following program transfers NFT ownership.
from datetime import datetime
from update_accounts import *
from tokens import *

timestamp = datetime.now().strftime("%B %d, %Y %H:%M:%S")


def transferOwnership(seller_money, buyer_money, new_owner):
    asset_info = []
    file = open("Piskel-NFT.txt", "r")

    for i in file:
        info = i.replace("\n", "")
        asset_info.append(info)

    price = int(asset_info[4])

    if buyer_money >= price:
        updateUser2(buyer_money - price)
        updateUser1(seller_money + price)

        with open('Piskel-NFT.txt', 'w') as file:
            file.write(new_owner + "\n")
            file.write(asset_info[1] + "\n")
            file.write(asset_info[2] + "\n")
            file.write(asset_info[3] + "\n")
            file.write(nft_token())

        print("\n" + "------------------------------------")
        print("NFT Transferred!" + "\n" + timestamp)
        print("------------------------------------")
    else:
        print("Insufficient Funds!")