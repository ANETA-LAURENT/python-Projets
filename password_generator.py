####password generator####

import random as r
import string as s


all = s.ascii_lowercase + s.ascii_uppercase + s.digits + s.punctuation
print("hello, Welcome to Password generator!")
while True:

    question = int(input("Enter the length of password, min 8 and max 32 characters: "))

    if question < 8:
        print("It's too short- try again")
        continue
    elif question > 32:
        print("It's too long- try again")
        continue
    else:

        password = r.choices(all, k=int(question))
        final = "".join(password)
        if any([x.isdigit() for x in password]):
            print(final)
        """  else:
            print("we bugged, try again")
            continue"""
        break
