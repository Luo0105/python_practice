class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def introduce(self):
        return f"Hi, I'm {self.name}, and I'm a {self.__class__.__name__}."


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball!"


class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"

    def climb(self):
        return f"{self.name} climbs up the tree gracefully."


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says Tweet!"

    def fly(self):
        return f"{self.name} spreads wings and flies into the sky!"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, name):
        for i, animal in enumerate(self.animals):
            if animal.name == name:
                removed = self.animals.pop(i)
                print(f"Removed {removed.name} the {removed.__class__.__name__} from the zoo.")
                return
        print(f"No animal named {name} found in the zoo.")

    def make_all_sounds(self):
        for animal in self.animals:
            print(animal.make_sound())

    def list_animals(self):
        if not self.animals:
            print("The zoo has no animals.")
            return
        print("Animals in the zoo:")
        for animal in self.animals:
            print(f"- {animal.name} ({animal.__class__.__name__})")

zoo = Zoo()

zoo.add_animal(Dog("Fido"))
zoo.add_animal(Cat("Whiskers"))
zoo.add_animal(Bird("Tweety"))

zoo.list_animals()
print()

zoo.make_all_sounds()
print()

# 调用各自的特殊方法
print(zoo.animals[0].fetch())     # Fido (Dog)
print(zoo.animals[1].climb())     # Whiskers (Cat)
print(zoo.animals[2].fly())       # Tweety (Bird)
print()

# Introduce all
for animal in zoo.animals:
    print(animal.introduce())
print()

# 移除一个动物
zoo.remove_animal("Whiskers")
zoo.list_animals()

