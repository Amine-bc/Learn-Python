
"""
So here I will be discovering oop using Python:
1. First you need to know that they are instance attributes which you find in the constructor __init__ function.
2. And class attributes which are outside the constructor
"""
class myclass:

    def __init__(self,attribute1):
        self.fattr = attribute1

object = myclass("This is the first attribute")
print(object.fattr)


class member:

    def __init__(self,firstname,lastname):
        self.fname = firstname
        self.lname = lastname
    def fullname(self):
        return f'{self.fname} {self.lname}'
    def wlcm(self):
        return f'Welcome {self.fullname()}'

user1 = member("Ahmed","Bouchoucha")
print(user1.fullname())
print(user1.wlcm())