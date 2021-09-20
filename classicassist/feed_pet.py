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
]
item_meats = [
	0x9c9, # ham
]

# check pet
if not FindAlias('pet') or not FindObject('pet'):
	PromptAlias('pet')

pet_current = GetAlias('pet')
pet_graphic = Graphic(pet_current)

def findOneByTypes(types):
	for type in types:
		if FindType(type, -1, 'backpack'):
			return True
	return False

def main():
	current_foods = []

	if pet_graphic in pet_meat:
		current_foods = item_meats
	elif pet_graphic in pet_vegetables:
		current_foods = item_vegetables

	if not findOneByTypes(current_foods):
		HeadMsg("no foods")
		return

	Feed(pet_current, Graphic('found'), 1)

main()
