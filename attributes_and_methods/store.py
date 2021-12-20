class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @staticmethod
    def can_add_item(items, capacity):
        total_items_count = sum(value for value in items.values())
        return total_items_count <= capacity

    @staticmethod
    def can_remove_item(items, item_name, amount):
        return item_name in items \
               and amount <= items[item_name]

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def add_item(self, item):
        if not self.can_add_item(self.items, self.capacity):
            return "not enough capacity in the store"

        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1
        return f"{item} added to the store"

    def remove_item(self, item, amount):
        if not self.can_remove_item(self.items, item, amount):
            return f"Cannot remove {amount} {item}"

        self.items[item] -= amount
        return f"{amount} {item} removed from the store"





first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))

import unittest


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.store = Store("First Store", "Best Type", 5)

    def test_from_size_should_create_class(self):
        store = Store.from_size("Test", "Test Type", 20)
        self.assertEqual(store.name, "Test")
        self.assertEqual(store.type, "Test Type")
        self.assertEqual(store.capacity, 10)
        self.assertEqual(store.items, {})

    def test_add_item_success(self):
        result = self.store.add_item("tomato")
        self.assertEqual(self.store.items["tomato"], 1)
        self.assertEqual(result, "tomato added to the store")

    def test_remove_item_success(self):
        self.store.add_item("tomato")
        result = self.store.remove_item("tomato", 1)
        self.assertEqual(result, "1 tomato removed from the store")

    def test_remove_item_success(self):
        self.store.add_item("tomato")
        result = self.store.remove_item("tomato", 1)
        self.assertEqual(result, "1 tomato removed from the store")

    def test_remove_item_unsuccessful(self):
        self.store.add_item("tomato")
        result = self.store.remove_item("tomato", 2)
        self.assertEqual(result, "Cannot remove 2 tomato")

    def test_repr(self):
        self.assertEqual(repr(self.store), "First Store of type Best Type with capacity 5")


if __name__ == "__main__":
    unittest.main()