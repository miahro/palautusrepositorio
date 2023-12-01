KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = max(0, kapasiteetti)
        self.kasvatuskoko = max(0, kasvatuskoko)
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.ljono = self._luo_lista(
                    self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.ljono)
            return True

        return False

    def poista(self, n):
        if n not in self.ljono:
            return False

        ind = self.ljono.index(n)
        self.ljono[ind] = 0

        for j in range(ind, self.alkioiden_lkm-1):
            self.ljono[j] = self.ljono[j+1]
        self.alkioiden_lkm -= 1

        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [self.ljono[i] for i in range(self.alkioiden_lkm)]

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()

        for item in a.ljono:
            yhdiste_joukko.lisaa(item)
        for item in b.ljono:
            yhdiste_joukko.lisaa(item)

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()
        for item in a.ljono:
            if b.kuuluu(item):
                leikkaus_joukko.lisaa(item)
        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()

        for item in a.ljono:
            if not b.kuuluu(item):
                erotus_joukko.lisaa(item)

        return erotus_joukko

    def __str__(self):
        items = [str(self.ljono[i]) for i in range(self.alkioiden_lkm)]
        return "{" + ", ".join(items) + "}" if items else "{}"
