import random
import string

class passwordGen:
    def __init__(self):
        s1 = list(string.ascii_lowercase)
        s2 = list(string.ascii_uppercase)
        s3 = list(string.digits)
        s4 = random.choices("#_!", k = round(30 * 0.20))

        random.shuffle(s1)
        random.shuffle(s2)
        random.shuffle(s3)
        random.shuffle(s4)

        length = random.randint(15,30)

        p1 = round(length * (30/100))
        p2 = round(length * (20/100))

        result = []

        for x in range(p1):
            result.append(s1[x])
            result.append(s2[x])

        for x in range(p2):
            result.append(s3[x])
            result.append(s4[x])

        random.shuffle(result)

        self.password = "".join(result)
        print(f"Password generated")


