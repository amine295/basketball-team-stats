# Name: Amine Hafid
# Date: 12-10-2025
# Runs the basketball team statistics program

from team import Team, PlayerNotFoundError
from player import Player

# Creates a team and handles input
def build_team(team):
    print("Enter information for 5 players:\n")

    for i in range(5):
        print("Player", i + 1)
        name = input("Name: ")
        points = int(input("Points: "))
        rebounds = int(input("Rebounds: "))
        assists = int(input("Assists: "))
        steals = int(input("Steals: "))
        blocks = int(input("Blocks: "))
        print()

        new_player = Player(name, points, rebounds, assists, steals, blocks)
        team.add_player(new_player)

# Main program loop
def main():
    team = Team()

    # Load team from CSV file
    team.load_from_csv("team_data.csv")

    print("Basketball Stats Manager")
    print("1. Build Team")
    print("2. Search for Player")
    print("3. Show Team Averages")
    print("4. Save and Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "1":
            build_team(team)

        elif choice == "2":
            name = input("Enter player name to search: ")
            try:
                player = team.find_player(name)
                player.display_stats()
            except PlayerNotFoundError as error:
                print(error)

        elif choice == "3":
            averages = team.calculate_averages()
            if averages is None:
                print("No players on the team yet.")
            else:
                avg_points, avg_rebounds, avg_assists, avg_steals, avg_blocks = averages
                print("Team Averages:")
                print("Points:", avg_points)
                print("Rebounds:", avg_rebounds)
                print("Assists:", avg_assists)
                print("Steals:", avg_steals)
                print("Blocks:", avg_blocks)

        elif choice == "4":
            team.write_to_csv("team_data.csv")
            print("Team saved to team_data.csv.")
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

# Executes program
if __name__ == "__main__":
    main()