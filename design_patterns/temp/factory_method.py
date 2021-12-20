import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



    
class JsonParser:
    def parse(self, obj):
        return json.dumps(obj)



class CsvParser:
    def parse(self, obj):
        header = obj.__dict__.keys()
        result = []
        result.append(','.join(obj.__dict__.keys()))
        result.append(','.join(obj.__dict__.values()))
        return '\n'.join(result)


class StringParser:
    def parse(self, obj):
        return str(obj)

def parse_string(obj):
    return str(obj)


def get_parser(format):
    if format == 'json':
        return JsonParser().parse(pesho)
    elif format == 'csv':
        return CsvParser().parse(pesho)
    else:
        return StringParser()

pesho = Person('Pesho', 11)

format = input()


parser = get_parser(format)
result = parser.parse(pesho)


print(result)