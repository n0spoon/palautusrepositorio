from kirjanpito import Kirjanpito as accounting


class Pankki:
    def __init__(self, kirjanpito=accounting):
        self._kirjanpito = kirjanpito

    def __init__(self):
        self._kirjanpito = Kirjanpito.get_instance()

    def tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        self._kirjanpito.lisaa_tapahtuma(
            f"tilisiirto: tililtä {tililta} tilille {tilille} viite {viitenumero} summa {summa}e"
        )

        # täällä olisi koodi joka ottaa yhteyden pankin verkkorajapintaan
        return True
