# Класс Animal (Животное)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.health = "healthy"  # Все животные изначально здоровы

    def __repr__(self):
        return f"{self.name} ({self.species}, {self.health})"

# Базовый класс Employee (Сотрудник)
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __repr__(self):
        return f"{self.name} ({self.position})"

# Класс ZooKeeper (Смотритель зоопарка)
class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")
        print(f"{animal.name} поел и теперь счастлив!")

# Класс Veterinarian (Ветеринар)
class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        if animal.health == "sick":
            animal.health = "healthy"
            print(f"{self.name} лечит {animal.name}. Теперь {animal.name} здоров!")
        else:
            print(f"{animal.name} уже здоров, лечение не требуется.")

# Класс Zoo (Зоопарк) - использует композицию
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []  # Список для животных
        self.employees = []  # Список для сотрудников

    # Метод для добавления животного
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} был добавлен в зоопарк {self.zoo_name}.")

    # Метод для добавления сотрудника
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} был нанят на работу в зоопарк {self.zoo_name}.")

    # Метод для отображения всех животных
    def display_animals(self):
        if not self.animals:
            print(f"В зоопарке {self.zoo_name} пока нет животных.")
        else:
            print(f"Животные в зоопарке {self.zoo_name}:")
            for animal in self.animals:
                print(animal)

    # Метод для отображения всех сотрудников
    def display_employees(self):
        if not self.employees:
            print(f"В зоопарке {self.zoo_name} пока нет сотрудников.")
        else:
            print(f"Сотрудники зоопарка {self.zoo_name}:")
            for employee in self.employees:
                print(employee)

# Пример использования композиции и полиморфизма

# Создаем зоопарк
my_zoo = Zoo("Central Zoo")

# Создаем животных
elephant = Animal("Dumbo", "Elephant")
lion = Animal("Simba", "Lion")

# Создаем сотрудников
zookeeper = ZooKeeper("Alice")
veterinarian = Veterinarian("Dr. Bob")

# Добавляем животных в зоопарк
my_zoo.add_animal(elephant)
my_zoo.add_animal(lion)

# Добавляем сотрудников в зоопарк
my_zoo.add_employee(zookeeper)
my_zoo.add_employee(veterinarian)

# Симулируем действия сотрудников
zookeeper.feed_animal(elephant)  # Alice кормит Dumbo
lion.health = "sick"  # Задаем статус "больной" для льва
veterinarian.heal_animal(lion)  # Dr. Bob лечит Симбу

# Отображаем всех животных и сотрудников
my_zoo.display_animals()
my_zoo.display_employees()
