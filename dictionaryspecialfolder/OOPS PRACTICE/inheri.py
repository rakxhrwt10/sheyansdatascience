class Father:
    def skills(self):
        print("Coding")


class Mother:
    def skills(self):
        print("Cooking")


class Child(Father, Mother):
    def show(self):
        Father.skills(self)
        Mother.skills(self)


c = Child()
c.show()