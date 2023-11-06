import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    finplayers = [p for p in players if p.nationality == "FIN"]
    finplayers_sorted = sorted(
        finplayers, key=lambda p: p.points, reverse=True)
    for player in finplayers_sorted:
        print(player)


if __name__ == "__main__":
    main()
