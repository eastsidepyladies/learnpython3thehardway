import ex40_mystuff

ex40_mystuff.apple()

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
                            "I wish I had a girl, if I did, I would call her"])

# list-o-strings
miner =  Song(['Face worker, a serpentine miner',
                        'A roof falls, an underliner',
                        'Of leaf structure, the egg timer'])


# test is a dict (only the key is used)
test = Song(ex40_mystuff.testing)
# testy is a list
testy = Song(ex40_mystuff.testingy)

wish.sing_me_a_song()
miner.sing_me_a_song()
test.sing_me_a_song()
testy.sing_me_a_song()
