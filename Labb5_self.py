#from hashfil import Hashtabell
#import hashtest
from hashtest_self import *
from molgrafik import Ruta, Molgrafik
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


def graphics():
	mg = Molgrafik() 
	atomlista = skapaAtomlista()
	hashtabell = lagraHashtabell(atomlista)
	state = 1 
	while state:
		atomNamn = input("Atombeteckning: ")

		try:
			atom = hashtabell.get(atomNamn)
			#print(atom[atomNamn])
			print(atom.vikt)
			r = Ruta(atom.namn, atom.vikt)
			mg.show(r)

		except KeyError:
			print(atomNamn, "finns inte.")
	        
if __name__ == "__main__":
    graphics()
    #main()