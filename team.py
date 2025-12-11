# Name: Amine Hafid
# Date: 12-10-2025
# Stores the Team class and custom exception

from player import Player

# Custom exception for when a player is not found
class PlayerNotFoundError(Exception):
    pass

class Team:
    # Constructor: creates an empty roster list
    def __init__(self):
        self.roster = []

    # Add a player object to the team
    def add_player(self, player):
        self.roster.append(player)

    # Search for a player by name (raises custom exception)
    def find_player(self, name):
        for p in self.roster:
            if p.get_name().lower() == name.lower():
                return p
        raise PlayerNotFoundError("Error: Player '" + name + "' was not found on the team.")

    # Calculate and return average stats
    def calculate_averages(self):
        if len(self.roster) == 0:
            return None

        total_points = 0
        total_rebounds = 0
        total_assists = 0
        total_steals = 0
        total_blocks = 0

        for p in self.roster:
            total_points += p.get_points()
            total_rebounds += p.get_rebounds()
            total_assists += p.get_assists()
            total_steals += p.get_steals()
            total_blocks += p.get_blocks()

        avg_points = total_points / len(self.roster)
        avg_rebounds = total_rebounds / len(self.roster)
        avg_assists = total_assists / len(self.roster)
        avg_steals = total_steals / len(self.roster)
        avg_blocks = total_blocks / len(self.roster)

        return avg_points, avg_rebounds, avg_assists, avg_steals, avg_blocks

    # Write team roster to a CSV file
    def write_to_csv(self, filename):
        file = open(filename, "w")
        for p in self.roster:
            line = (
                p.get_name() + "," +
                str(p.get_points()) + "," +
                str(p.get_rebounds()) + "," +
                str(p.get_assists()) + "," +
                str(p.get_steals()) + "," +
                str(p.get_blocks()) + "\n"
            )
            file.write(line)
        file.close()

    # Read team roster from CSV file
    def load_from_csv(self, filename):
        try:
            file = open(filename, "r")
            for line in file:
                data = line.strip().split(",")
                name = data[0]
                points = int(data[1])
                rebounds = int(data[2])
                assists = int(data[3])
                steals = int(data[4])
                blocks = int(data[5])

                new_player = Player(name, points, rebounds, assists, steals, blocks)
                self.add_player(new_player)

            file.close()

        except FileNotFoundError:
            print("CSV file not found. A new one will be created when the team is saved.")