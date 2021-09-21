class Item:
	def __init__(
		self,
		type,
		range=-1,
		loc='ground',
		color=-1,
		targets=None,
		desc=''
	):
		self.type = type
		self.range = range
		self.location = loc
		self.color = color
		self.targets = targets
		self.description = desc

		self.item_name = ''
		self.target_name = ''

	def find(self):
		res = FindType(self.type, self.range, self.location, self.color)
		if res:
			self.item_name = Name('found')
		return res

	def find_target(self):
		if not self.targets:
			return True
		res = next((t.find() for t in self.targets), False)
		if res:
			self.target_name = Name('found')
		return res

	def msg_usage(self):
		msg = '# {}'.format(self.item_name)
		if self.targets:
			msg += ' -> {}'.format(self.target_name)
		HeadMsg(msg, 'self', 45)

	def msg_no_target(self):
		HeadMsg('# {} -> ?'.format(self.item_name), 'self', 45)

	def use(self):
		item_res = self.find() # found updated

		if not item_res:
			return False

		UseObject('found')

		target_res = self.find_target() # found updated

		if not target_res:
			self.msg_no_target()
			return False

		if self.targets:
			WaitForTarget(1000)
			Target('found', True, True)

		self.msg_usage()
		return True

items = [
	Item(0x124d, desc='umbra, iron maiden'),
	Item(0x99b, range=2, desc='shadowguard a bottle of Liquor'),
	Item(0x9d0, loc='backpack', desc='shadowguard apple'),
	Item(0xd01, range=2, desc='shadowguard cypress tree'),
	Item(0x4686, loc='backpack', color=2075, targets=[Item(0x19ab)], desc='shadowguard dirty'),
	Item(0x4686, loc='backpack', color=0, targets=[Item(0x1512), Item(0x151a)], desc='shadowguard pure'),
	Item(0x1e85, loc='backpack', desc='shadowguard a dragon wing'),
]

def main():
	result = False
	for item in items:
		if item.use():
			result = True
			break

	if not result:
		HeadMsg('No Interaction', 'self', 45)

main()
