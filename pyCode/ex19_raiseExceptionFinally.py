class AdultException(Exception):
    def __init__(self, age):
        self.age = age
    def handle(self):
        print(f"{self.age} is not old enough")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_age(self):
        if self.age <= 18:
            try:
                raise AdultException(self.age)
            except AdultException as e:
                e.handle()
                return "a minor"
        else:
            return self.age

def display_person(person):
    adultAge = person.get_age()
    print(f"{person.name} is {adultAge}")

timmy = Person("Timmy", 15)
display_person(timmy)