class Game:
    def __init__(game, name, home_console, price):
        game.name = name
        game.home_console = home_console
        game.price = price
        #cib(bool), manuals(bool), repo(bool), year(int), last_updated(??), count(int)
    
    def __str__(game):
        return f"{game.name} for {game.home_console} @ (${game.price})"
        
g1 = Game("Mario Party 6","GameCube", 49.99)
print(g1)
