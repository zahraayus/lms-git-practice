class Student:
    def __init__(self, name, nim):
        self.name = name
        self.nim = nim

    def display_info(self):
        print(f"Name: {self.name}, NIM: {self.nim}")