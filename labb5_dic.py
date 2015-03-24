#from hashfil import Hashtabell
#import hashtest
from hashtest import *
def main():
	state = 1
	atomlista = skapaAtomlista()
	hashtabell = lagraHashtabell(atomlista)

	while state:
		atomNamn = input("Atombeteckning: ")

		try:
			atom = hashtabell.get(atomNamn)
			#print(atom[atomNamn])
			print(atom.vikt)

		except KeyError:
			print(atomNamn, "finns inte.")
	        
if __name__ == "__main__":
    main()