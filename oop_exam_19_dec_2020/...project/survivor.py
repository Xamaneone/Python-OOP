class Survivor:
    default_health = 100
    default_needs = 100

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.health = self.default_health
        self.needs = self.default_needs

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self.__age = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        if value > 100:
            self.__health = 100
        else:
            self.__health = value

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        if value > 100:
            self.__needs = 100
        else:
            self.__needs = value

    @property
    def needs_sustenance(self):
        if self.needs < 100:
            return True
        return False

    @property
    def needs_healing(self):
        if self.health < 100:
            return True
        return False
