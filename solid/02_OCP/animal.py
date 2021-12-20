from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_sound(self):
        pass


class SoundMakingAnimal(Animal, ABC):
    @abstractmethod
    def get_sound(self):
        pass


class Cat(SoundMakingAnimal):
    sound = 'meow'

    def get_sound(self):
        return self.sound


class Dog(SoundMakingAnimal):
    sound = 'woof-woof'

    def get_sound(self):
        return self.sound


class Dragon(SoundMakingAnimal):
    sound = 'rawr'

    def get_sound(self):
        return self.sound


class Donkey(SoundMakingAnimal):
    sound = 'I am a talking donkey'

    def get_sound(self):
        return self.sound


class Mole(Animal):
    sound = "Silence"

    def get_sound(self):
        raise TypeError("Moles cannot make sound")


def animal_sound(animals: list[SoundMakingAnimal]):
    for animal in animals:
        print(animal.get_sound())


def animal_eat(animals: list[Animal]):
    for animal in animals:
        print(animal.eat())


animals = [Cat(), Dog(), Dragon(), Donkey()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
