# The following program creates a blockchain.
from SHA256 import *
from data import *
from genesis_block import *

old_hash = ""


def createBlockchain():
    message = ""
    block_data = []
    blockchain = []
    block = {}
    count = 0

    for transactions in stored_data[1:]:
        for i in transactions:
            message += i + " - "
        transactions = message[:-3]
        block_data.append(transactions)
        message = ""

    blockchain.append(genesis_block)
    hash_print = genesis_block['New Hash']

    for i in block_data:
        count += 1

        block['Block'] = str(count)
        block['Previous Hash'] = hash_print

        padded_msg = pad_message(i + " - " + hash_print)
        hashed_msg = SHA256(padded_msg)
        hash_print = hex(hashed_msg)[2:]

        block['Transaction'] = i
        block['New Hash'] = hash_print
        block['Timestamp'] = timestamp

        blockchain.append(block | block)

    print("-----------------------------------------------------------------------------------------------------------")
    print("Block Chain" + "\n")

    for i in blockchain:
        for key, j in i.items():
            print(key, ':', j)
        print("\n")

    last_block = blockchain[-1]
    old_hash = last_block['New Hash']

    return blockchain


createBlockchain()