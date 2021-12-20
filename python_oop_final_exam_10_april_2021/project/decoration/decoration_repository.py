from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        result = None
        for decor in self.decorations:
            if decor.__name__ == decoration_type:
                result = decor
                break
        return result


