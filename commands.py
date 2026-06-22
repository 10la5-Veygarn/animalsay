import sys
from renderer import speech_bubble
from animal_manager import (get_animals, list_animals, get_animals_names)

def say_animals(animal, message):
    if not message:
        return get_animals(animal) + "\n" + "Valid Usage: <command> | <animal> <message>"
    return speech_bubble(message) + "\n" + get_animals(animal)


def help_animals():
    output = []
    for i, command in enumerate(commands, start=1):
        output.append(f"{i}. {command}")
    return "Avaliable commands:\n" + "\n".join(output)


def stats_animals():
    return "In progress, please visit later!"


commands = {
    "list": list_animals,
    "stats": stats_animals,
    "help": help_animals,
    }