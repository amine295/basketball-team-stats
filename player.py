# Name: Amine Hafid
# Date: 12-10-2025
# Stores the Player class for the basketball stats program

class Player:
    # Constructor that sets all instance attributes
    def __init__(self, name, points, rebounds, assists, steals, blocks):
        self.name = name
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks

    # Getter and setter methods for all attributes
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_points(self):
        return self.points

    def set_points(self, value):
        self.points = value

    def get_rebounds(self):
        return self.rebounds

    def set_rebounds(self, value):
        self.rebounds = value

    def get_assists(self):
        return self.assists

    def set_assists(self, value):
        self.assists = value

    def get_steals(self):
        return self.steals

    def set_steals(self, value):
        self.steals = value

    def get_blocks(self):
        return self.blocks

    def set_blocks(self, value):
        self.blocks = value

    # Displays player stats in a formatted way
    def display_stats(self):
        print("----- Player Stats -----")
        print("Name:", self.name)
        print("Points:", self.points)
        print("Rebounds:", self.rebounds)
        print("Assists:", self.assists)
        print("Steals:", self.steals)
        print("Blocks:", self.blocks)
        print("------------------------")

    # Magic Method: string representation of the Player
    def __str__(self):
        return f"{self.name}: {self.points} pts, {self.rebounds} reb, {self.assists} ast, {self.steals} stl, {self.blocks} blk"
