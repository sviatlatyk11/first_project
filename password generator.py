import random
import string


def password_generator(password_length):
    special_characters = "!()_-.,"
    characters = [string.digits, string.ascii_lowercase, string.ascii_uppercase, special_characters]
    password = ""
    for i in range(len(characters)):
        add = random.choice(characters[i])
        password = password + add
    for i in range(password_length - len(characters)):
        rand_number = random.randint(0, len(characters) - 1)
        add = random.choice(characters[rand_number])
        password = password + add
    lst = [*password]
    random.shuffle(lst)
    password = "".join(lst)
    return password

password = password_generator(9)
print(password)




