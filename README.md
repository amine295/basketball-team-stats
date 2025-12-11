# Basketball Team Stats Manager

## Project Description
This Python program allows users to manage and analyze a basketball team's statistics using object-oriented programming (OOP). Users can build a 5-player team, view individual player statistics, calculate team averages, and save/load team data from a CSV file.  

The project demonstrates key OOP concepts, file handling, and exception management while producing a practical tool for managing basketball team data.

---

## Features
- Build a 5-player basketball team
- Store and update each player's stats: points, rebounds, assists, steals, and blocks
- Search for a player by name and display full statistics
- Calculate and display team average statistics
- Save/load team data from a CSV file
- Handle errors gracefully if a player is not found
- Organized across multiple Python modules (`player.py`, `team.py`, `main.py`)

---

## File Descriptions

### `player.py`
- Represents an individual player and stores all stats.
- Key components:
  - `__init__`: Initializes a player's name and stats
  - Getters and setters: Access and update stats safely
  - `display_stats()`: Print player's stats in readable format
  - `__str__`: Returns a concise string representation of the player

### `team.py`
- Manages the team roster and team-level operations.
- Key components:
  - `__init__`: Initializes an empty roster
  - `add_player(player)`: Adds a player to the roster
  - `find_player(name)`: Searches for a player; raises an error if not found
  - `calculate_averages()`: Computes average points, rebounds, assists, steals, and blocks
  - `write_to_csv(filename)`: Saves roster to CSV file
  - `load_from_csv(filename)`: Loads roster from CSV; handles missing files

### `main.py`
- Program entry point and user interface.
- Key components:
  - Creates a `Team` object and loads CSV data
  - Displays a menu:
    1. Build Team
    2. Search Player
    3. Team Averages
    4. Save + Exit
  - Loops until the user chooses to exit
  - Calls appropriate methods from `Team` and `Player` classes

---

## Program Flow

