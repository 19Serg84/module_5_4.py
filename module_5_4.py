class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super(House, cls).__new__(cls)

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

del h1  