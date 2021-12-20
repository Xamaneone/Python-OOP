class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.animals = []
        self.workers = []
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget

    def is_capacity_animals(self):
        return len(self.animals) < self.__animal_capacity

    def is_capacity_workers(self):
        return len(self.workers) < self.__workers_capacity

    def add_animal(self, animal, price):
        if self.__budget >= price and self.is_capacity_animals():
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.Type} added to the zoo"
        elif self.__budget < price and self.is_capacity_animals():
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__budget >= worker.salary and self.is_capacity_workers():
            self.workers.append(worker)
            return f"{worker.name} the {worker.Type} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        budget_needed = sum([worker.salary for worker in self.workers])
        if self.__budget >= budget_needed:
            self.__budget -= budget_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        budget_needed = sum([animal.get_needs() for animal in self.animals])
        if self.__budget >= budget_needed:
            self.__budget -= budget_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.Type == "Lion":
                lions.append(animal)
            elif animal.Type == "Tiger":
                tigers.append(animal)
            elif animal.Type == "Cheetah":
                cheetahs.append(animal)
        if lions:
            result += f"\n----- {len(lions)} Lions:"
            for lion in lions:
                result += f"\n{lion}"
        if tigers:
            result += f"\n----- {len(tigers)} Tigers:"
            for tiger in tigers:
                result += f"\n{tiger}"
        if cheetahs:
            result += f"\n----- {len(cheetahs)} Cheetahs:"
            for cheetah in cheetahs:
                result += f"\n{cheetah}"
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.Type == "Keeper":
                keepers.append(worker)
            elif worker.Type == "Caretaker":
                caretakers.append(worker)
            elif worker.Type == "Vet":
                vets.append(worker)
        if keepers:
            result += f"\n----- {len(keepers)} Keepers:"
            for keeper in keepers:
                result += f"\n{keeper}"
        if caretakers:
            result += f"\n----- {len(caretakers)} Caretakers:"
            for caretaker in caretakers:
                result += f"\n{caretaker}"
        if vets:
            result += f"\n----- {len(vets)} Vets:"
            for vet in vets:
                result += f"\n{vet}"
        return result

