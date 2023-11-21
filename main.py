from src.Engine.Engine import Engine



if __name__ == '__main__':
    print("Starting ...")
    players = [
        {
            "name": "Kilian"
        },
        {
            "name": "Autre"
        }
    ]
    engine =Engine(players_config=players)
    engine.game()