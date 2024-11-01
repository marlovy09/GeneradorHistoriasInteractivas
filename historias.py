import random


characters = ["El fantasma encantado", "El enano sabio", "El lobo feroz"]
actions = ["lucha contra", "descubre", "explora"]
places = ["la mansion embrujada", "el bosque oscuro", "los portales a otras dimenciones"]


def add_elements():
    new_character = input("Agrega un nuevo personaje: ")
    new_action = input("Agrega una nueva acción: ")
    new_place = input("Agrega un nuevo lugar: ")

    
    if new_character:
        characters.append(new_character)
    if new_action:
        actions.append(new_action)
    if new_place:
        places.append(new_place)


def generate_story():
    character = random.choice(characters)
    action = random.choice(actions)
    place = random.choice(places)
    return f"{character} {action} en {place}."


add_elements()


print("\n========= [HISTORIA GENERADA] =========")
print(generate_story())
print("========================================")
