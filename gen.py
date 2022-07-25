import hashlib
import random


def generate_password(length):
    chars = list('+-/*!&$#?=w@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    random.shuffle(chars)
    pasw = ''.join([random.choice(chars) for x in range(length)])
    return pasw


def hash_func(data):
    hash_object = hashlib.sha1(data.encode()).hexdigest()
    return hash_object


print(hash_func(generate_password(5)))
