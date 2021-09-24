# pet eats vegetable
pet_vegetables = [
    0x115, # cu sidhe
    0x7a, # unicorn
]
pet_meat = [
    0x317, # beetle
    0xa9, # fire beetle
    0x509, # najasaurus
]
item_vegetables = [
    0x9d0, # apple
    0x9d2, # peach
    0x9d1, # grape
    0x994, # pear
]
item_meats = [
    0x9c9, # ham
]

def adjust_pet():
    if not FindAlias('pet') or not FindObject('pet'):
        PromptAlias('pet')
    return GetAlias('pet')

def find_one_by_types(types):
    for type in types:
        if FindType(type, -1, 'backpack'):
            return True
    return False

def feed_pet(pet_serial):
    current_foods = []
    pet_graphic = Graphic(pet_serial)

    if pet_graphic in pet_meat:
        current_foods = item_meats
    elif pet_graphic in pet_vegetables:
        current_foods = item_vegetables

    if not find_one_by_types(current_foods):
        HeadMsg("no foods")
        return False

    Feed(pet_serial, Graphic('found'), 1)

    return True

def main():
    pet_serial = adjust_pet()
    feed_pet(pet_serial)

main()
