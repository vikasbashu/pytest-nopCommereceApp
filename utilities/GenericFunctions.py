import string, random


def random_generator(size, chars = string.ascii_lowercase + string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))


def get_test_email():
    return random_generator(12) + '@gmail.com'


def get_test_password(chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation):
    return ''.join(random.choice(chars) for x in range(10))


def get_test_username():
    return random_generator(7) + ' ' + random_generator(8)

