from tekoaly import Tekoaly
from kivisaksetpaperi import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
