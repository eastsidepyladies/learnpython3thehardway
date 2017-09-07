import ex40_mystuff

class Song(object):

    #  __init__ is the constructor for a class
    def __init__(self, lyrics):

        # sooo... "self" makes clear you are referring to the instance of the object itself
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # here we make clear we want to treat each line in the object, not possible if we directly refer to the object's attribute (I think?)
        for line in self.lyrics:
            print(line)

# list-o-strings
wish = Song(["I wish I was a little bit taller",
                            "I wish I was a baller",
                            "I wish I had a squirrel, trained good, I would call her"])

# list-o-strings
miner =  Song(['Face worker, a serpentine miner',
                        'A roof falls, an underliner',
                        'Of leaf structure, the egg timer'])

# lyrics are in a variable contained in imported module
up = Song(ex40_mystuff.creek)

wish.sing_me_a_song()
miner.sing_me_a_song()
up.sing_me_a_song()
