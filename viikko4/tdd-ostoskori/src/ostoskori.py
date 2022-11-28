from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoskori = []

    def tavaroita_korissa(self):
        tavaroiden_maara = 0
        for tuote in self._ostoskori:
            tavaroiden_maara += tuote.lukumaara()
        return tavaroiden_maara

    def hinta(self):
        hintojen_summa = 0
        for tuote in self._ostoskori:
            hintojen_summa += tuote.hinta()
        return hintojen_summa

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        for tuote in self._ostoskori:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                tuote.muuta_lukumaaraa(1)
                return
        self._ostoskori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        ostos = Ostos(poistettava)
        for tuote in self._ostoskori:
            if tuote.tuotteen_nimi() == ostos.tuotteen_nimi():
                tuote.muuta_lukumaaraa(-1)
                if tuote.lukumaara() == 0:
                    self._ostoskori.remove(tuote)

    def tyhjenna(self):
        self._ostoskori.clear()

    def ostokset(self):
        return self._ostoskori
