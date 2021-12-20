from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    init_comfort = 5
    init_price = 10
    def __init__(self):
        super().__init__(self.init_comfort, self.init_price)