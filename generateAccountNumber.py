import random
import string


def generate_Account_Number():
    lenght = 11
    digits1 = string.digits
    digits2 = string.digits
    all = digits1 + digits2
    temp = random.sample(all, lenght)
    accountNumber = "".join(temp)
    print("HERE'S YOUR NEW ACCOUNT NUMBER ==> ",accountNumber)