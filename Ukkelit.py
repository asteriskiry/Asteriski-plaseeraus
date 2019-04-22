class Henkilo:
    def __init__(self, name, gender, friends, holiton, lihaton):
        self.name = name
        self.gender = gender
        self.friends = friends
        self.holiton = holiton
        self.lihaton = lihaton

Anna = Henkilo("Anna", "woman", [], "holiton", "lihaa")
Sanna = Henkilo("Sanna", "other", [], "holillinen", "lihaa")
Janna = Henkilo("Janna", "woman", [], "holillinen", "lihaa")
Manna = Henkilo("Manna", "woman", [], "holillinen", "kasvis")
Jaakko = Henkilo("Jaakko", "man", [], "holiton", "lihaa")
Kaakko = Henkilo("Kaakko", "man", [], "holiton", "lihaa")
Saakko = Henkilo("Saakko", "other", [], "holillinen", "lihaa")
Laakko = Henkilo("Laakko", "man", [], "holillinen", "kasvis")
Salli = Henkilo("Salli", "woman", [], "holiton", "lihaa")
Lalli = Henkilo("Lalli", "man", [], "holillinen", "piispa")
Malli = Henkilo("Malli", None, [], "holillinen", "lihaa")
Nalli = Henkilo("Nalli", "other", [], "holillinen", "kasvis")

Sanna.friends = [Anna]
Janna.friends = [Manna, Salli]
Jaakko.friends = [Lalli]
Kaakko.friends = [Jaakko, Salli]
Saakko.friends = [Malli, Lalli, Laakko]
Laakko.friends = [Saakko]
Salli.friends = [Kaakko, Janna]
Malli.friends = [Saakko]

testiukkoja = [Sanna, Janna, Manna, Jaakko, Anna, Kaakko, Saakko, Laakko, Salli, Lalli, Malli, Nalli]
def tuolista():
    return testiukkoja