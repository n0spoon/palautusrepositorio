class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = 0

class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        try:
            arvo = int(self.lue_syote())
        except Exception:
            pass
        self.sovelluslogiikka.tulos += arvo

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        try:
            arvo = int(self.lue_syote())
        except Exception:
            pass
        self.sovelluslogiikka.tulos -= arvo

class Nollaus:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.tulos = 0

class Kumoa:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
    
    def suorita(self):
        pass