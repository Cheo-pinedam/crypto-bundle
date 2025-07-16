# The following program checks if a number is prime and generates prime pairs for the RSA algorithm.
p_nums = []
q_nums = []


def isprime(n: int):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    k = 5
    while k ** 2 <= n:
        if n % k == 0 or n % (k + 2) == 0:
            return False
        k += 6
    return True


# print(isprime(3))


# Find all prime numbers in the given range
primes_num = []
for i in range(128, 512):
    if isprime(i):
        primes_num.append(i)
#print(primes_num)

# Find primes that work well together for use in RSA
for i in primes_num:
    for x in range(1, 5):
        check = i * x + 1
        if primes_num.count(check) == 1:
            #print("For: " + str(i) + " q: " + str(check))
            p_nums.append(i)
            q_nums.append(check)

length = 0
if len(p_nums) == len(q_nums):
    length = len(p_nums)