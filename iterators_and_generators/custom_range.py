class custom_range():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = start


    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration

        value = self.value
        self.value += 1
        return value

    class iterator:
        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.value = self.custom_range_obj.start

        def __next__(self):
            if self.value > self.custom_range_obj.start:
                return self.value




one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)