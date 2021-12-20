class countdown_iterator:
    def __init__(self, start):
        self.current_num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < 0:
            raise StopIteration
        temp = self.current_num
        self.current_num -= 1
        return temp


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")