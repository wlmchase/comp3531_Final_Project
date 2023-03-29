import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

"""
COMP3531 - Simulation & Modelling
Final Project - Monopoly

Andrew Mackenzie
Wallace Mackenzie Chase
"""

 # init a board
def createBoard():
    go = Tile(0, "GO", 0, 0)
    mediterranean_ave = Tile(1, "Mediterranean Ave", 60, 2)
    chest_1 = Tile(2, "Chance", 0, 0)
    baltic_ave = Tile(3, "Baltic Ave", 0, 4)

    income_tax = Tile(4, "Income Tax", 200, 0)

    reading_railroad = Tile(5, "Reading Railroad", 200, 25)

    oriental_ave = Tile(6, "Oriental Ave", 100, 6)
    chance_tile_1 = Tile(7, "Chance", 0, 0)
    vermont_ave = Tile(8, "Vermont Ave", 100, 6)
    conn_ave = Tile(9, "Connecticut Ave", 120, 8)

    jail = Tile(10, "Jail", 0, 0)

    st_charles_pl = Tile(11, "St. Charles Place", 140, 10)
    electric = Tile(12, "Electric",150, 0)
    states_ave = Tile(13, "States Ave", 140, 10)
    virginia_ave = Tile(14, "Virginia Ave", 160, 12)

    penn_railroad = Tile(15, "Pennsylvania Railroad", 200, 25)

    st_james_pl = Tile(16, "St. James Place", 180, 14)
    chest_2 = Tile(17, "Chest", 0, 0)
    tenn_ave = Tile(18, "Tennessee Ave", 180, 14)
    ny_ave = Tile(19, "New York Ave", 200, 16)

    free_parking = Tile(20, "Free Parking", 0, 0)

    ken_ave = Tile(21, "Kentucky Ave", 220, 18)
    chance_tile_2 = Tile(22, "Chance", 0, 0)
    indi_ave = Tile(23, "Indiana Ave", 220, 18)
    illi_ave = Tile(24, "Illinois Ave", 240, 20)

    bo_railroad = Tile(25, "B & O Railroad", 200, 25)

    atla_ave = Tile(26, "Atlantic Ave", 260, 22)
    vent_ave = Tile(27, "Ventnor Ave", 260, 22)
    water_works = Tile(28, "Water Works", 150, 0)
    marv_grdn = Tile(29, "Marvin Garden", 280, 24)

    goto_jail = Tile(30, "Go To Jail", 0, 0)

    pac_ave = Tile(31, "Pacific Ave", 300, 26)
    ncar_ave = Tile(32, "North Carolina Avenue", 300, 26)
    chest_3 = Tile(33, "Chance", 0, 0)
    penn_ave = Tile(34, "Pennsylvania Ave", 320, 28)

    short_line_railroad = Tile(35, "Short Line Railroad", 200, 25)

    chance_3 = Tile(36, "Chance", 0, 0)
    park_pl = Tile(37, "Park Place", 350, 35)
    lux_tax = Tile(38, "Luxury Tax", 0, 0)
    boardwalk = Tile(39, "Boardwalk", 400, 50)

    return [go, mediterranean_ave, baltic_ave, income_tax, reading_railroad, oriental_ave, chance_tile_1,
            vermont_ave, conn_ave, jail, st_charles_pl, electric, states_ave, virginia_ave, penn_railroad,
            st_james_pl, chest_1, tenn_ave, ny_ave, free_parking, ken_ave, chance_tile_2, indi_ave, illi_ave,
            bo_railroad, atla_ave, vent_ave, water_works, marv_grdn, goto_jail, pac_ave, ncar_ave, chest_2,
            penn_ave, short_line_railroad, chance_3, park_pl, lux_tax, boardwalk]



class Game:
    # init a game
    def __init__(self, number_of_players):
        self.turnCount = 0
        self.playerList = []
        self.currentPlayer = None
        self.board = createBoard()
        self.winner = None
        self.trip_around_board = 0

        for i in range(number_of_players):
            player = Player()
            self.playerList.append(player)            
    
    def enoughFunds(player, tile):
        if (player.money >= tile.cost):
            return True
        else:
            return False

    def chooseToBuy():
        decisionToBuy = np.random.random()
        if decisionToBuy > 0.30:
            return True
        else:
            return False

    def buyProperty(player, property):
        propertyCost = property.cost
        player.money -= propertyCost
        player.properties.append(property)

    def auctionOff(self, player, property):
        propertyCost = property.cost
        otherPlayers = []
        for i in range(len(self.playerList)):
            if self.playerList[i] != player:
                if self.playerList[i].money >= propertyCost:
                    otherPlayers.append(self.playerList[i])

        buyer = random.choice(otherPlayers)
        self.buyProperty(buyer, property)

    def handlePropertyTile(self, newTile):
        # TODO Fix
        if (newTile.bought):
            if (self.currentPlayer.money < self.board[self.currentPlayer.place].rent):
                    self.currentPlayer.lost = True
            else:
                if (self.enoughFunds(self.currentPlayer, newTile)):
                    if self.chooseToBuy():
                        self.buyProperty(self.currentPlayer, newTile)
                    else:
                        if (houseRules):
                            return
                        else:
                            self.auctionOff(self.currentPlayer, newTile)
                        
    def handleRailroad():
        
    def handleUtility():
    
    def handleTax():
        
    def handleParking():
    
    def handleGO():
        
    
    def handleNewTileType(self, newTile):
        if newTile.type == "property":
            self.handlePropertyTile(newTile)
        elif newTile.type == "railroad":
            self.handleRailroad()
        elif newTile.type == "go to jail":
            self.handleGoToJail()
        elif newTile.type == "chance" or newTile.type == "chest":
            # do nothing
            return
        elif newTile.type == "utility":
            self.handleUtility()
        elif newTile.type == "tax":
            self.handleTax()
        elif newTile.type == "parking":
            if (houseRules):
                handleParking()
            else:
                # do nothing
                return
        else:
            self.handleGO()
    
    # play the game
    def play(self):
        self.currentPlayer = self.players[0]
        index = 0
        while (game.winner == None):
            
            
            move = rollTwoDice()
            # check if past go
            self.currentPlayer.place = (self.currentPlayer.place + move) % 40

            newTile = self.board[self.currentPlayer.place]
            
            self.handleNewTileType(self, newTile)
            
            if index == self.number_of_players:
                index = -1
            index += 1
            self.currentPlayer = self.players[index]

        return self.turnCount, self.trip_around_board, self.winner

class Player:
    def __init__(self):
        self.money = 1500
        self.properties = []
        self.place = 0
        self.lost = False

class Tile:
    def __init__(self, place, name, cost, rent):
        self.place = place
        self.name = name
        self.cost = cost
        self.rent = rent
        self.bought = False
        self.owner = None

# roll a 6 sided die
def rollDice():
    return np.random.randint(1,7)

# roll two 6-sided die  and return whether or not they were doubles, and the total
def rollTwoDice():
    doubles = False
    roll1 = rollDice()
    roll2 = rollDice()
    if roll1 == roll2:
        doubles = True
    return doubles, (roll1 + roll2)



###  Main loop  ###
N = 500
number_of_players = 4
houseRules = False
game_type_1_stats = []
for i in range(N):
    game = Game(num_players)