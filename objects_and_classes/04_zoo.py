class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    species, name = input().split()
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))


============================================================================



class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''

        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"

        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"

        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f" Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name,)

info = input()

print(zoo.get_info(info))


==========================================================================================



class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.animals = {
            "mammal": [],
            "fish": [],
            "bird": []
        }

    def add_animal(self, species, name):
        self.animals[species].append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        animal_list = self.animals.get(species, [])
        animal_str = ", ".join(animal_list)
        species_str = species.capitalize() + "s" if species != "fish" else "Fishes"
        total_str = f" Total animals: {Zoo.__animals}"
        return f"{species_str} in {self.name}: {animal_str}\n{total_str}"


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for _ in range(count):
    species, name = input().split()
    zoo.add_animal(species, name)

info = input()

print(zoo.get_info(info))
