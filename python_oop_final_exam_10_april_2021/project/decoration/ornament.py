from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    init_comfort = 1
    init_price = 5
    def __init__(self):
        super().__init__(self.init_comfort, self.init_price)


