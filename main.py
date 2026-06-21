from commands import (commands, say_animals)
from animal_manager import animal_exists

def handler(text: str):
    if not text.strip():
        return ""
    parts = text.split(maxsplit=1)
    first_word = parts[0].lower()
    if first_word in commands:
        return commands[first_word]()
    elif animal_exists(first_word):
        message = parts[1] if len(parts) > 1 else ""
        return say_animals(first_word, message)
    else:
        return "Unknown command or animal."


def main():
    while True:
        inp = input("> ")
        print(handler(inp))

if __name__ == "__main__":
    main()