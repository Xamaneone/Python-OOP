from project.supply.supply import Supply


class FoodSupply(Supply):
    default_needs_increase = 20

    def __init__(self):
        super().__init__(self.default_needs_increase)
