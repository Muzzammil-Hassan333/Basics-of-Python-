class person:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


person1=person(10,20)
person1.x=12
print(person1.x)

