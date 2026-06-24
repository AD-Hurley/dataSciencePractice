class animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

class dog(animal):
    def __init__(self):
        super().__init__("Dog House")

fido = dog()
fido.print_habitat()
