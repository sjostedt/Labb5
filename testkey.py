# test av nyckelhenererningsfunktion

def keyGenerator(name):
	#genererar hashnyklar med avseende på namn.
		#key = ord(name)%17
		#key = ord(name[0])//(len(name))
		#if len(name) == 2:
			#key = (ord(name[0])+2*ord(name[1]))
		key = 0
		for tkn in name:
			key = (key*77+ord(tkn))%1000
		#print(key)
		return key

keyGenerator("Ag")
keyGenerator("H")
keyGenerator("I")
keyGenerator("Pu")

testlista = ["A","B","C","D","Öh","Au","ö","öö","ÖÖ"]
for i in range(len(testlista)):
	keyGenerator(testlista[i])