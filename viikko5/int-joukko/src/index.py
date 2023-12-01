import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)
    joukko.lisaa(7)
    joukko.lisaa(4)

    # print(joukko)
    # print(joukko.to_int_list())
    # joukko.poista(2)
    print(joukko)
    # joukko.poista(2)
    # print(joukko)

    joukko2 = IntJoukko()
    joukko2.lisaa(2)
    joukko2.lisaa(8)
    print(joukko2)

    res = IntJoukko.erotus(joukko, joukko2)
    print(res)


if __name__ == "__main__":
    main()
