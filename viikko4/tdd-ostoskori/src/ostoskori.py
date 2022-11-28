from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoskori = []

    def tavaroita_korissa(self):
        return len(self._ostoskori)

    def hinta(self):
        hintojen_summa = 0
        for tuote in self._ostoskori:
            hintojen_summa += tuote.hinta()
        return hintojen_summa

    def lisaa_tuote(self, lisattava: Tuote):
        self._ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostoskori
