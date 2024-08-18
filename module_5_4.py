 # module_5_4.py Домашняя работа по уроку "Различие атрибутов класса и экземпляра."

class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __del__(self):
        print(f'{self.name} снесён но останется в истории.')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
h4 = House('ЖК Этажи', 25)
print(House.houses_history)
h5 = House('ЖК Ильинка', 16)
print(House.houses_history)

