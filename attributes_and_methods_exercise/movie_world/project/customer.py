class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        rented_dvds = list(d.name for d in self.rented_dvds)
        if not rented_dvds:
            rented_dvds = ''
        else:
            rented_dvds = f"{', '.join(rented_dvds)}"
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({rented_dvds})"
