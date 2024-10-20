class Mammal:
    def walk(self):
        print("walk")


class dog(Mammal):
    def bark(self):
        print("Bark")
class cat(Mammal):
    pass



dog1=dog()
dog1.walk()
    