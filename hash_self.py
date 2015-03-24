############################
#### Hashning egen metod

class Hashtabell:
	def __init__(self, antalElement):
		self.hashlist = []
		self.N = 1023
		for i in range(self.N):
			self.hashlist.append(None)

	def put(self, name, node):
		key = self.keyGenerator(name)
		#print ("putkey: ",key)
		if self.hashlist[key] == None:
			self.hashlist[key] = node
			return

		else:
		#linjär probning
			i = True
			while i:
				key = key+1
				#print("krock")
				if self.hashlist[key] == None:
					self.hashlist[key] = node
					i = False
			return
		#else:
		#	print("key is broken")

	def get(self, name):
		 
		key = self.keyGenerator(name)
		#print("getkey: ", key)
		
		if None == self.hashlist[key]:
			raise KeyError
			#return KeyError

		if name == self.hashlist[key].namn:
			return self.hashlist[key]

		#probning med steg
		elif self.hashlist[key].namn != name:
			i = True
			while i:
				key = key+1
				if None == self.hashlist[key]:
					raise KeyError
				if name == self.hashlist[key].namn:
					return self.hashlist[key]
		else:
			print("superknas")

	def keyGenerator(self,name):
	#genererar hashnyklar med avseende på namn.
		#key = ord(name)%17
		key = 0
		for tkn in name:
			key = (key*77+ord(tkn))%self.N
		#print(key)
		return key
