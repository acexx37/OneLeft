from core.game.GameEngine import GameEngine
from Player import Player
from players.EasyPlayer import Player as EasyPlayer
# from players.HardPlayer import Player as HardPlayer
# from players.MediumPlayer import Player as MediumPlayer

players = [Player(), EasyPlayer()]

game_engine = GameEngine(players, 10)
game_engine.start()
