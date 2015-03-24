from time import *
from hash_self import Hashtabell 

class Song:

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title 

    def __str__(self):
        return "{" + self.namn + " " +  str(self.vikt) + "}"

def lasfil(filnamn):
    minlista = Hashtabell(8000000)
    with open(filnamn) as fil:
        for rad in fil:
            data = rad.split("<SEP>")
            artist = data[2].strip()
            song = data[3].strip()
            newsong = Song(artist, song)
            minlista.put(artist, newsong) #= song
    return minlista

def hitta(artist, songtable):
    start = time()
    print(songtable[artist])
    stop = time()
    tidhash = stop - start
    return tidhash

songtable = lasfil("unique_tracks.txt")
artist = "Elude"
tidhash = hitta(artist, songtable)
print(tidhash)
