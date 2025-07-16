# The following program creates the genesis bloc of a blockchain
from SHA256 import *
from data import *
from datetime import *

genesis_block = {}
hashed_msg = 0
timestamp = datetime.now().strftime("%B %d, %Y %H:%M:%S")


def create_block():
    message = ""
    block_data = []
    previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"

    for i in stored_data[0]:
        message += i + ""
    transactions = message[:-3]
    block_data.append(transactions)

    # Genesis block setup
    for i in block_data:
        genesis_block['Block'] = str(0)
        genesis_block['Previous hash'] = previous_hash

        padded_msg = pad_message(i)
        hashed_msg = SHA256(padded_msg)
        hash_print = hex(hashed_msg)[2:]

        genesis_block['Transaction'] = i
        genesis_block['New Hash'] = hash_print
        genesis_block['Timestamp'] = timestamp

    for key, j in genesis_block.items():
        print(key, ':', j)
    return genesis_block


create_block()
