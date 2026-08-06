import secrets
import string

class password_gen:
    def __init__(self):
        s1 = list(string.ascii_lowercase)
        s2 = list(string.ascii_uppercase)
        s3 = list(string.digits)
        s4 = [secrets.choice("#_!") for k in range(round(30 * 0.20))]

        secrets.SystemRandom().shuffle(s1)
        secrets.SystemRandom().shuffle(s2)
        secrets.SystemRandom().shuffle(s3)
        secrets.SystemRandom().shuffle(s4)

        length = secrets.randbelow(16) + 16

        p1 = round(length * (30/100))
        p2 = round(length * (20/100))

        result = []

        for x in range(p1):
            result.append(s1[x])
            result.append(s2[x])

        for x in range(p2):
            result.append(s3[x])
            result.append(s4[x])

        secrets.SystemRandom().shuffle(result)

        self.password = "".join(result)
        print(f"Password generated")


