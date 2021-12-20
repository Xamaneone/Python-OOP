class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = int(health)

    def pokemon_details(self, *args):
        if "name" in args:
            return self.name
        elif "health" in args:
            return self.health
        return f"{self.name} with health {self.health}"
