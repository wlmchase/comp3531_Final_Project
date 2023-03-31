import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

"""
COMP3531 - Simulation & Modelling
Final Project - Monopoly

Wallace Mackenzie Chase
Andrew Mackenzie
"""


# initiates a board by setting up an array of all the tiles objects
# one tile object for each tile on the board
def createBoard():
    go = Tile(0, "GO", 0, 0, "go")
    mediterranean_ave = Tile(1, "Mediterranean Ave", 60, 2, "property")
    chest_1 = Tile(2, "Chance", 0, 0, "chest")
    baltic_ave = Tile(3, "Baltic Ave", 0, 4, "property")

    income_tax = Tile(4, "Income Tax", 0, 200, "tax")

    reading_railroad = Tile(5, "Reading Railroad", 200, 25, "railroad")

    oriental_ave = Tile(6, "Oriental Ave", 100, 6, "property")
    chance_tile_1 = Tile(7, "Chance", 0, 0, "chance")
    vermont_ave = Tile(8, "Vermont Ave", 100, 6, "property")
    conn_ave = Tile(9, "Connecticut Ave", 120, 8, "property")

    jail = Tile(10, "Jail", 0, 0, "jail")

    st_charles_pl = Tile(11, "St. Charles Place", 140, 10, "property")
    electric = Tile(12, "Electric",150, 0, "utility")
    states_ave = Tile(13, "States Ave", 140, 10, "property")
    virginia_ave = Tile(14, "Virginia Ave", 160, 12, "property")

    penn_railroad = Tile(15, "Pennsylvania Railroad", 200, 25, "railroad")

    st_james_pl = Tile(16, "St. James Place", 180, 14, "property")
    chest_2 = Tile(17, "Chest", 0, 0, "chest")
    tenn_ave = Tile(18, "Tennessee Ave", 180, 14, "property")
    ny_ave = Tile(19, "New York Ave", 200, 16, "property")

    free_parking = Tile(20, "Free Parking", 0, 0, "free parking")

    ken_ave = Tile(21, "Kentucky Ave", 220, 18, "property")
    chance_tile_2 = Tile(22, "Chance", 0, 0, "chance")
    indi_ave = Tile(23, "Indiana Ave", 220, 18, "property")
    illi_ave = Tile(24, "Illinois Ave", 240, 20, "property")

    bo_railroad = Tile(25, "B & O Railroad", 200, 25, "railroad")

    atla_ave = Tile(26, "Atlantic Ave", 260, 22, "property")
    vent_ave = Tile(27, "Ventnor Ave", 260, 22, "property")
    water_works = Tile(28, "Water Works", 150, 0, "utility")
    marv_grdn = Tile(29, "Marvin Garden", 280, 24, "property")

    goto_jail = Tile(30, "Go To Jail", 0, 0, "property")

    pac_ave = Tile(31, "Pacific Ave", 300, 26, "property")
    ncar_ave = Tile(32, "North Carolina Avenue", 300, 26, "property")
    chest_3 = Tile(33, "Chance", 0, 0, "chance")
    penn_ave = Tile(34, "Pennsylvania Ave", 320, 28, "property")

    short_line_railroad = Tile(35, "Short Line Railroad", 200, 25, "railroad")

    chance_3 = Tile(36, "Chance", 0, 0, "chance")
    park_pl = Tile(37, "Park Place", 350, 35, "property")
    lux_tax = Tile(38, "Luxury Tax", 0, 75, "tax")
    boardwalk = Tile(39, "Boardwalk", 400, 50, "property")

    return [go, mediterranean_ave, chest_1, baltic_ave, income_tax, reading_railroad, oriental_ave, chance_tile_1,
            vermont_ave, conn_ave, jail, st_charles_pl, electric, states_ave, virginia_ave, penn_railroad,
            st_james_pl, chest_2, tenn_ave, ny_ave, free_parking, ken_ave, chance_tile_2, indi_ave, illi_ave,
            bo_railroad, atla_ave, vent_ave, water_works, marv_grdn, goto_jail, pac_ave, ncar_ave, chest_3,
            penn_ave, short_line_railroad, chance_3, park_pl, lux_tax, boardwalk]


class Game:

    # initiates the game by setting up the board and players
    # initializes the instance variables for the game object
    def __init__(self, player_count):
        self.turn_count = 0
        self.players = []
        self.player_count = player_count
        self.current_player = None
        self.board = createBoard()
        self.winner = None
        self.trip_around_board = 0
        self.all_properties_bought = False
        self.allPropBoughtTurnCount = -1

        # pythonic way of creating a list of player objects
        [self.players.append(Player()) for _ in range(player_count)]

    def enough_funds(self, player, tile):
        return player.money >= tile.cost

    def choose_to_buy(self):
        # player has a randomized 70% chance
        # of buying the property
        decision_to_buy = np.random.random()
        return decision_to_buy > 0.30

    def buy_property(self, player, property):
        # deduct the cost of the property from the player's money
        # then add the property to the player's list of properties
        player.money -= property.cost
        player.properties.append(property)

    def auction_off(self, property):
        # create a list of players excluding the current player
        possible_buyers = self.players.copy()
        possible_buyers.remove(self.current_player)

        # if property cost is more than each player's money
        # remove them from the list of possible buyers
        for player in possible_buyers:
            if not self.enough_funds(player, property):
                possible_buyers.remove(player)

    def potentialBuy(self, property):
        if (self.currentPlayer.money < self.board[self.currentPlayer.place].rent):
                    self.currentPlayer.lost = True
        else:
            if (self.enoughFunds(self.currentPlayer, property)):
                if self.chooseToBuy():
                    self.buyProperty(self.currentPlayer, property)
                else:
                    if (houseRules):
                        return
                    else:
                        self.auctionOff(self.currentPlayer, property)
        
    def payRent(self, property, player):
        propertyOwner = property.owner
        propertyRent = property.rent
        player.money -= propertyRent
        propertyOwner += propertyRent
        
    def handlePropertyTile(self, property):
        if (not property.bought):
            self.potentialBuy(property)
        else:
            self.payRent(property, self.currentPlayer)
                        
    def handleRailroad(self, railroad):
        if (not railroad.bought):
            self.potentialBuy(railroad)
        else:
            self.payRent(railroad, self.currentPlayer)
            
    def handleGoToJail(self):
        self.currentPlayer.place = 10
        self.currentPlayer.inJail = True
            
    def handleUtility(self, utility):
        if (not utility.bought):
            self.potentialBuy(utility)
        else:
            self.payRent(utility, self.currentPlayer)
    
    def handleTax(self, tax):
        self.currentPlayer.money -= tax.rent
        
    def handleParking(self):
        if houseRules:
            self.currentPlayer.money += 500
        else:
            return
    
    def handleGO(self):
        self.currentPlayer.money += 200  
    
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
                self.handleParking()
            else:
                self.current_player.money -= newTile.rent
                newTile.owner.money += newTile.rent

        # if the tile the player lands on is not bought
        # and the player has enough money to buy it
        # and they would like to buy it
        # then the player buys the property
        elif not newTile.bought and self.enough_funds(self.current_player, newTile) and self.choose_to_buy():
            self.buy_property(self.current_player, newTile)

        # if the tile the player lands on is not bought
        # and the player either can't afford the property
        # or they don't want to buy it
        # and the house rules are disabled
        # then the property is auctioned off
        elif not newTile.bought and not houseRules:
            self.auction_off(newTile)

        # if the tile the player lands on is not bought
        # and the player can't/won't buy the property
        # and the house rules are enabled
        # then nothing happens
        else:
            return

    def handle_railroad(self):
        pass

    def handle_utility(self):
        pass

    def handle_go_to_jail(self):
        pass

    def handle_taxes(self):
        pass

    def handle_parking(self):
        # give the player 500 bucks
        self.current_player.money += 500

    def handle_GO(self):
        # TODO: increment trips around board ... somehow
        #  must only do for the first player to do so
        #  going to need some logic for whether or not
        #  a player is the first to go around the board
        #  something, something, then do self.trip_around_board += 1

        # also give the player 200 bucks
        self.current_player.money += 200

    def handle_tile(self, new_tile):
        if new_tile.type == "property":
            self.handle_property_tile(new_tile)
            return
        elif new_tile.type == "railroad":
            self.handle_railroad()
            return
        elif new_tile.type == "go to jail":
            self.handle_go_to_jail()
            return
        elif new_tile.type == "utility":
            self.handle_utility()
            return
        elif new_tile.type == "tax":
            self.handle_taxes()
            return
        elif new_tile.type == "parking" and houseRules:
            # only handle parking if house rules are enabled
            self.handle_parking()
            return
        elif new_tile.type == "chance" or new_tile.type == "chest":
            return  # do nothing
        else:
            return  # do nothing

    # play the game
    # TODO: handle doubles
    def play(self):
        self.currentPlayer = self.players[0]
        index = 0
        while (game.winner == None):
            
            double, move = roll_two_dice()
            
            if not self.currentPlayer.lost:
                
                if self.currentPlayer.inJail:
                    if double:
                        self.currentPlayer.inJail = False
                else:
                    if double:
                        self.currentPlayer.doublesCount += 1
                        if self.currentPlayer.doublesCount == 3:
                            self.handGoToJail(self.currentPlayer)
                    
                # check if past go
                currentPlace = self.currentPlayer.place
                self.currentPlayer.place = (self.currentPlayer.place + move) % 40
                if currentPlace > self.currentPlayer.place:
                    self.handleGO()

                newTile = self.board[self.currentPlayer.place]
            
                self.handleNewTileType(self, newTile)
            
            if index == self.number_of_players:
                index = -1
            index += 1
            self.currentPlayer = self.players[index]


class Player:
    def __init__(self):
        self.money = 1500
        self.properties = []
        self.place = 0
        self.doublesCount = 0
        self.inJail = False
        self.lost = False


class Tile:
    def __init__(self, tile_index, name, cost, rent):
        self.tile_index = tile_index
        self.name = name
        self.cost = cost
        self.rent = rent
        self.bought = False
        self.owner = None


# roll a 6 sided die
def roll_die():
    return np.random.randint(1, 7)


# roll two die, check if doubles, sum total
def roll_two_dice():
    roll1 = roll_die()
    roll2 = roll_die()
    return (roll1 == roll2), (roll1 + roll2)


###  Main loop  ###
N = 500
number_of_players = 4
houseRules = False
game_turnCount_data = []
game_tripCount_data = []
game_winner_data = []
for i in range(N):
    game = Game(number_of_players)
    turnCount, trip_around_board, winner = game.play()
    game_turnCount_data.append(turnCount)
    game_tripCount_data.append(trip_around_board)
    game_winner_data.append(winner)