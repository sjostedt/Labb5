########################################
##### Hashing dictionary
class Hashtabell:
	def __init__(self, antalElement):
		self.hashonary = {}
		dict()
	def put(self, namn, node):
		if not namn in self.hashonary:
			self.hashonary[namn] = node

	def get(self, namn):
		return self.hashonary[namn]