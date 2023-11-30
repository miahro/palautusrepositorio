class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.edelliset_tilat = []

    def miinus(self, operandi):
        self.tallenna_tila()
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self.tallenna_tila()
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self.tallenna_tila()
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def tallenna_tila(self):
        self.edelliset_tilat.append(self._arvo)

    def palauta_edellinen(self):
        edellinen = self.edelliset_tilat.pop()
        self.aseta_arvo(edellinen)
