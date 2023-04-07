import numpy as np
import matplotlib.pyplot as plt
import random

"""
COMP3531 - Simulation & Modelling
Final Project - Monopoly

Wallace Mackenzie Chase
Andrew Mackenzie
"""

# class Player
# has an id (just their index in the list of players), money, list of properties, current tile
# how many doubles they've rolled
# amount of railroads and utlities owned
# whether they're in jail or not, jail time
# and if they lost
class Player:
    def __init__(self, id):
        self.id = id
        self.money = 1500
        self.properties = []
        self.tile_index = 0
        self.doubles_count = 0
        self.railroads_owned = 0
        self.utilities_owned = 0
        self.jailed = False
        self.jail_time = 0
        self.lost = False

# class Tile
# holds the info of a tile on the board
# name, cost, rent, type, and color
# check if bought and who the owner is
class Tile:
    def __init__(self, tile_index, name, cost, rent, type, color):
        self.tile_index = tile_index
        self.name = name
        self.cost = cost
        self.rent = rent
        self.type = type
        self.color = color
        self.bought = False
        self.owner = None

# initiates a board by setting up an array of all the tiles objects
# one tile object for each tile on the board
def createBoard():
    go = Tile(0, "GO", 0, 0, "go", None)

    mediterranean_ave = Tile(1, "Mediterranean Ave", 60, 2, "property", "purple")
    chest_1 = Tile(2, "Chance", 0, 0, "chest", None)
    baltic_ave = Tile(3, "Baltic Ave", 0, 4, "property", "purple")
    income_tax = Tile(4, "Income Tax", 0, 200, "tax", None)

    reading_railroad = Tile(5, "Reading Railroad", 200, 25, "railroad", None)

    oriental_ave = Tile(6, "Oriental Ave", 100, 6, "property", "grey")
    chance_tile_1 = Tile(7, "Chance", 0, 0, "chance", None)
    vermont_ave = Tile(8, "Vermont Ave", 100, 6, "property", "grey")
    conn_ave = Tile(9, "Connecticut Ave", 120, 8, "property", "grey")

    jail = Tile(10, "Jail", 0, 0, "jail", None)

    st_charles_pl = Tile(11, "St. Charles Place", 140, 10, "property", "pink")
    electric = Tile(12, "Electric",150, 0, "utility", None)
    states_ave = Tile(13, "States Ave", 140, 10, "property", "pink")
    virginia_ave = Tile(14, "Virginia Ave", 160, 12, "property", "pink")

    penn_railroad = Tile(15, "Pennsylvania Railroad", 200, 25, "railroad", None)

    st_james_pl = Tile(16, "St. James Place", 180, 14, "property", "orange")
    chest_2 = Tile(17, "Chest", 0, 0, "chest", None)
    tenn_ave = Tile(18, "Tennessee Ave", 180, 14, "property", "orange")
    ny_ave = Tile(19, "New York Ave", 200, 16, "property", "orange")

    free_parking = Tile(20, "Free Parking", 0, 0, "free parking", None)

    ken_ave = Tile(21, "Kentucky Ave", 220, 18, "property", "red")
    chance_tile_2 = Tile(22, "Chance", 0, 0, "chance", None)
    indi_ave = Tile(23, "Indiana Ave", 220, 18, "property", "red")
    illi_ave = Tile(24, "Illinois Ave", 240, 20, "property", "red")

    bo_railroad = Tile(25, "B & O Railroad", 200, 25, "railroad", None)

    atla_ave = Tile(26, "Atlantic Ave", 260, 22, "property", "yellow")
    vent_ave = Tile(27, "Ventnor Ave", 260, 22, "property", "yellow")
    water_works = Tile(28, "Water Works", 150, 0, "utility", None)
    marv_grdn = Tile(29, "Marvin Garden", 280, 24, "property", "yellow")

    goto_jail = Tile(30, "Go To Jail", 0, 0, "go to jail", None)

    pac_ave = Tile(31, "Pacific Ave", 300, 26, "property", "green")
    ncar_ave = Tile(32, "North Carolina Avenue", 300, 26, "property", "green")
    chest_3 = Tile(33, "Chance", 0, 0, "chance", None)
    penn_ave = Tile(34, "Pennsylvania Ave", 320, 28, "property", "green")

    short_line_railroad = Tile(35, "Short Line Railroad", 200, 25, "railroad", None)

    chance_3 = Tile(36, "Chance", 0, 0, "chance", None)
    park_pl = Tile(37, "Park Place", 350, 35, "property", "blue")
    lux_tax = Tile(38, "Luxury Tax", 0, 100, "tax", None)
    boardwalk = Tile(39, "Boardwalk", 400, 50, "property", "blue")

    return [go, mediterranean_ave, chest_1, baltic_ave, income_tax, reading_railroad, oriental_ave, chance_tile_1,
            vermont_ave, conn_ave, jail, st_charles_pl, electric, states_ave, virginia_ave, penn_railroad,
            st_james_pl, chest_2, tenn_ave, ny_ave, free_parking, ken_ave, chance_tile_2, indi_ave, illi_ave,
            bo_railroad, atla_ave, vent_ave, water_works, marv_grdn, goto_jail, pac_ave, ncar_ave, chest_3,
            penn_ave, short_line_railroad, chance_3, park_pl, lux_tax, boardwalk]


# class Game
# simulates a game of monopoly
class Game:

    # initiates the game by setting up the board and players
    # initializes the instance variables for the game object
    def __init__(self, player_count):
        self.turn_count = 0
        self.players = []
        self.player_count = player_count
        self.remaining_players = player_count
        self.current_player = None
        self.current_roll = -1
        self.board = createBoard()
        self.winner = None
        self.trip_around_board = -1
        self.properties_bought_counter = 0
        self.all_properties_bought = False
        self.all_properties_bought_turn_count = -1
        self.inflation = 0

        # pythonic way of creating a list of player objects
        [self.players.append(Player(i)) for i in range(player_count)]

    def enough_funds(self, player, tile):
        return player.money >= tile.cost

    def choose_to_buy(self):
        # player has a randomized 70% chance
        # of buying the property
        decision_to_buy = np.random.random()
        return decision_to_buy > 0.30

    def checkIfAllBought(self):
        if self.properties_bought_counter == 28:
            self.all_properties_bought = True
            self.all_properties_bought_turn_count = self.trip_around_board
        
    def buy_property(self, player, property):
        # deduct the cost of the property from the player's money
        # then add the property to the player's list of properties
        player.money -= property.cost
        player.properties.append(property)
        property.owner = player
        property.bought = True
        self.properties_bought_counter += 1
        self.checkIfAllBought()

        if property.type == "railroad":
            player.railroads_owned += 1
        elif property.type == "utility":
            player.utilities_owned += 1

    def auction_off(self, property):
        # create a list of players excluding the current player
        possible_buyers = self.players.copy()
        possible_buyers.remove(self.current_player)

        # if property cost is more than each player's money
        # remove them from the list of possible buyers
        for player in possible_buyers:
            if not self.enough_funds(player, property):
                possible_buyers.remove(player)

        # if there are no possible buyers, the property is not bought
        if len(possible_buyers) == 0:
            return

        buyer = random.choice(possible_buyers)
        self.buy_property(buyer, property)

    def pay_rent(self, new_tile):
        rent = new_tile.rent + new_tile.rent * self.inflation

        # if the property is a railroad
        # the rent is 25 * 2^(no. of railroads owned by owner - 1)
        # 1 = 25, 2 = 50, 3 = 100, 4 = 200
        if new_tile.type == "railroad":
            rent = 25 * (2 ** (new_tile.owner.railroads_owned - 1))

        # if the property is a utility
        # the rent is 4 * dice roll if the owner owns 1 utility
        # and 10 * dice roll if the owner owns 2 utilities
        # the dice roll being the roll that the player made
        # to get to the new tile (both dice)
        elif new_tile.type == "utility":
            if new_tile.owner.utilities_owned == 1:
                rent = 4 * self.current_roll
            elif new_tile.owner.utilities_owned == 2:
                rent = 10 * self.current_roll

        # check if property owner owns set
        #double rent
        else:
            if self.ownsSet(new_tile):
                rent = 2 * rent

        # if the player doesn't have enough money to pay the rent
        # they lose the game
        if self.current_player.money < rent:
            self.current_player.lost = True
            self.remaining_players -= 1

        # if the player has enough money to pay the rent
        # deduct the rent from the player's money
        # and add the rent to the owner's money
        else:
            self.current_player.money -= rent
            new_tile.owner.money += rent

    # checks if property owner owns the set
    def ownsSet(self, property):
        ownSet = False
        owner = property.owner
        prop_color = property.color
        set_counter = 1
        for i in range(len(owner.properties)):
            if owner.properties[i].color == prop_color:
                set_counter += 1
        
        if prop_color == "blue" or prop_color == "purple":
            if set_counter == 2:
                ownSet = True
        else:
            if set_counter == 3:
                ownSet = True
        
        return ownSet
        
    def potential_buy(self, new_tile):
        # if the player has enough money to buy the property
        # and they would like to buy it
        # then the player buys the property
        if self.enough_funds(self.current_player, new_tile) and self.choose_to_buy():
            self.buy_property(self.current_player, new_tile)

        # if the player either can't afford the property
        # or they don't want to buy it
        # and the house rules are disabled
        # then the property is auctioned off
        elif not houseRules:
            self.auction_off(new_tile)

        # if the player can't/won't buy the property
        # and the house rules are enabled
        # then nothing happens
        else:
            return

    def handle_property_tile(self, new_tile):
        # if the tile the player lands on is already bought
        # check if the player has enough money to pay the rent
        if new_tile.bought:
            self.pay_rent(new_tile)

        # if the tile the player lands on has not been bought
        # run through the logic to try and buy the property
        else:
            self.potential_buy(new_tile)

    def handle_railroad(self, new_tile):
        self.handle_property_tile(new_tile)

    def handle_utility(self, new_tile):
        self.handle_property_tile(new_tile)

    def handle_taxes(self, new_tile):
        # if the player doesn't have enough money to pay the tax
        # then they lose the game
        if not self.enough_funds(self.current_player, new_tile):
            self.current_player.lost = True
            self.remaining_players -= 1

        # otherwise they pay the tax cost listed on the tile
        else:
            self.current_player.money -= new_tile.cost

    def handle_go_to_jail(self):
        self.current_player.jailed = True
        self.current_player.doubles_count = 0
        self.current_player.tile_index = 10

    def handle_parking(self):
        # give the player 500 bucks if house rules are enabled
        if houseRules:
            self.current_player.money += 500

    def handle_GO(self):
        # give the player 200 bucks
        # increment trips around board
        self.current_player.money += 200
        self.trip_around_board += 1

    def handle_tile(self, new_tile):
        if new_tile.type == "property":
            self.handle_property_tile(new_tile)
            return

        elif new_tile.type == "railroad":
            self.handle_railroad(new_tile)
            return

        elif new_tile.type == "go to jail":
            self.handle_go_to_jail()
            return

        elif new_tile.type == "utility":
            self.handle_utility(new_tile)
            return

        elif new_tile.type == "tax":
            self.handle_taxes(new_tile)
            return

        elif new_tile.type == "parking":
            self.handle_parking()
            return

        elif new_tile.type == "chance" or new_tile.type == "chest":
            return  # do nothing

        else:
            return  # do nothing

    # play the game
    def play(self):
        player_index = 0
        while self.winner is None:
            
            # INFLATION
            if self.turn_count % 50 == 0:
                self.inflation += 3
            
            # if the player has lost, skip their turn
            if self.players[player_index].lost:
                player_index = (player_index + 1) % self.player_count
                continue

            self.current_player = self.players[player_index]
            doubles, self.current_roll = roll_two_dice()

            # if the player rolled doubles, increment the doubles counter
            if self.current_player.jailed:
                # Check for doubles
                if doubles:
                    # reset jail time and jailed status
                    self.current_player.jail_time = 0
                    self.current_player.jailed = False
                else:
                    # increment jail time
                    self.current_player.jail_time += 1
                
                # if 3 turns in jail and no doubles
                # pay the $50
                # reset attributes
                if self.current_player.jail_time == 3:
                    self.current_player.money -= 50
                    self.current_player.jail_time = 0
                    self.current_player.jailed = False                    
                    

            # if the player rolled doubles and is not jailed, increment the doubles counter
            elif doubles:
                self.current_player.doubles_count += 1

                # if the player rolled doubles 3 times in a row
                # send them to jail and then skip their turn
                if self.current_player.doubles_count == 3:
                    self.handle_go_to_jail()
                    player_index = (player_index + 1) % self.player_count
                    continue

            # if the player didn't roll doubles, reset the doubles counter
            else:
                self.current_player.doubles_count = 0

            # modulate the player's tile_index by 40 to wrap around the board
            # when the player passes go
            previous_place = self.current_player.tile_index
            self.current_player.tile_index = (self.current_player.tile_index + self.current_roll) % 40

            # if the player passes go, execute the handleGO() function
            # (if the players tile_index is less than the roll, then the player passed go)
            # (because the player must have then spent at least 1 placement increment on the last trip around the board)
            if self.current_player.tile_index < previous_place:
                self.handle_GO()

            # set new_tile to the tile the player landed on and handle the tile
            new_tile = self.board[self.current_player.tile_index]
            self.handle_tile(new_tile)

            # set player_index to the next player
            player_index = (player_index + 1) % self.player_count

            # if there is only one player left, they are the winner
            if self.remaining_players == 1:
                for player in self.players:
                    if not player.lost:
                        self.winner = player
                        break
                    
            self.turn_count += 1
        
        return self.turn_count, self.all_properties_bought_turn_count, self.winner.id

# roll a 6 sided die
def roll_die():
    return np.random.randint(1, 7)


# roll 2 die
# return boolean for doubles and total
def roll_two_dice():
    roll_1 = roll_die()
    roll_2 = roll_die()
    return (roll_1 == roll_2), (roll_1 + roll_2)


###  Main loop  ###
N = 50000
player_count = 4
houseRules = True
turn_data = []
turns_before_all_props_bought = []
winners = []

for i in range(N):
    game = Game(player_count)
    turns, loops, winner = game.play()
    turn_data.append(turns)
    turns_before_all_props_bought.append(loops)
    winners.append(winner)


plt.hist(winners)
plt.xlabel("Winner")
plt.ylabel("won")
if houseRules:
    plt.title("Player win rate with House Rules")
else:
    plt.title("Player win rate without House Rules")
plt.xticks([0, 1, 2, 3], [1, 2, 3, 4])
plt.show()

turn_avg = np.mean(turn_data)
loop_avg = np.mean(turns_before_all_props_bought)
if houseRules:
    print("House rules: " + str("ON"))
else:
    print("House rules: " + str("OFF"))
print(N, "Games", "took on average", turn_avg, "turns and on average ", loop_avg, "loops around the board before all properties bought")
