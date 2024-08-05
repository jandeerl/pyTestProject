class Member:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def printName(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")

    def print_character_length(self):
        print(len(self.name) + len(self.surname))


bob = Member("Bobby", "DD")
bob.printName()
bob.print_character_length()