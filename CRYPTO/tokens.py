# The following program generates unique non-fungible tokens
import string
import random


def nft_token():
    token = ""
    letters = string.ascii_lowercase
    numbers = string.digits
    for i in range(30):
        token += ''.join(random.choice(letters + numbers))
    return token


#print(nft_token())