import random
import string


def generate_bvn():
    lenght = 11
    digits1 = string.digits
    digits2 = string.digits
    all = digits1 + digits2
    temp = random.sample(all, lenght)
    bvn = "".join(temp)
    print("YOUR NEW BVN ==> ",bvn)