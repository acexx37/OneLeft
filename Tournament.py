from core.game.GamePlayer import GamePlayer
from core.game.GameEngine import GameEngine


class Tournament:


    #this is a private method that will get the loser of two players from
    #the game simulation and return that loser
    def getLoser(self, playerOne: GamePlayer, playerTwo: GamePlayer):
        GamePlayer loser = null #get the loser from the game simulation
        return loser

    #gets all the players from the game simulation so we can begin bracketing them
    def getPlayers(self):
        game_players = GameEngine.__get_game_players()
        return game_players
    
    #code for running the tournament
    def run(self):
        game_players = self.getPlayers()
        playerCount = game_players.length
        #if there are an odd number of players pad the bracket with a null
        #essentially adding a bye for someone
        if (playerCount % 2)== 1:
            game_players.add(null)
        
        loserBracket = []
        
        #first round, move half the players into a seperate bracket, creating a loser
        #bracket
        index = 0
        while index < len(game_players):
            GamePlayer loser = self.getLoser(game_players[index], game_players[index +1])
            game_players.remove(loser)
            loserBracket.__add__(loser)
            index = index + 2
            
        #while there are still rounds left to be played (more than 1 player left in
        #each bracket) loop through both brackets, if a player loses in the winning
        #bracket move them to the losing bracket, if a player loses in the loser bracket
        #remove them from the losing bracket, and they are removed from the tournament
        roundsStillLeft = True
        while roundsStillLeft
            innerIndex = 0
            while innerIndex < len(game_players)
                GamePlayer loser =  self.getLoser(game_players[innerIndex], game_players[innerIndex +1])
                game_players.remove(loser)
                loserBracket.__add__(loser)
                innerIndex = innderIndex + 2
                
            idx = 0
            while idx < len(loserBracket)
                GamePlayer loser =  self.getLoser(loserBracket[idx], loserBracket[idx +1]
                loserBracket.remove(loser)
            
            #there are no more players left to play eachother
            if len(loserBracket) == 1 and len(game_players) == 1
                roundsStillLeft = False
        
        #ToDo
        #will have to check for top 5 players, top 4 can be easy, something like
        #if winnberbracket.length == 2, then do the last match winner, is 1, loser is 
        #2 likewise for loser bracket and 3rd/4th.  5th will be more difficult, 
        #must do something like save both top 4s, remove the actual top 4 and have the 
        #next top 4 compete back for 5th place.
        
        return #returns something, maybe a list of users //top5


