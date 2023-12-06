from tuomari import Tuomari
from kivisaksetpaperi import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self):
        super().__init__()

    def _toisen_siirto(self):
        return input("Toisen pelajan siirto: ")
