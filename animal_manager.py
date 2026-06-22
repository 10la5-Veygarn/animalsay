from config import ANIMAL_DIR


def load_animals():
    animals = {}
    for file in ANIMAL_DIR.glob("*.txt"):
        animals[file.stem.lower()] = file.read_text(encoding="utf-8")
    return animals


def list_animals(randomtxt):
    output = []
    for i, animal in enumerate(animals, start=1):
        output.append(f"{i}. {animal}")
    return "\n".join(output)


def get_animals(name):
    return animals[name]
    

def animal_exists(name):
    return name in animals.keys()


def get_animals_names():
    animal_names = animals.keys()
    return animal_names

animals = load_animals()