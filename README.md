# Basketball Team Stats Manager

## Project Overview
For the ITS 211 Introduction to Programming final project, this program manages and analyzes a basketball team's statistics using object-oriented programming (OOP). Users can build a 5-player roster, including each Player’s points, rebounds, steals, assists, and blocks. Users input information for each Player in a loop until the whole Team is complete. Once the Team is entered, the program allows searching for a player by name to retrieve their complete statistics and calculate the Team’s average statistics for each category.

---

## Purpose
The program demonstrates major concepts learned in the course, including:
- Instance attributes and instance methods
- Magic methods (e.g., `__str__`)
- Getter and setter methods
- Reading from and writing to files
- Handling and raising exceptions
- Organizing code across multiple modules

The program produces a practical tool for managing basketball team data while demonstrating object-oriented programming concepts.

---

## Project Goals
- Allow users to input a complete 5-player basketball team.
- Retrieve a player’s statistics by name.
- Calculate and display team averages for points, rebounds, assists, steals, and blocks.
- Save and load team data to/from a CSV file.
- Demonstrate key OOP concepts including instance methods, magic methods, getters/setters, modular code, file I/O, and exception handling.

---

## Features
- Build and manage a 5-player basketball team roster
- Store and update individual player statistics
- Search for a player and display complete stats
- Calculate team averages
- Save and load team data to/from a CSV file (`team_data.csv`)
- Graceful handling of errors such as searching for a non-existent player
- Code organized across multiple modules: `player.py`, `team.py`, `main.py`
- Demonstrates instance methods, magic methods, getters/setters, file handling, exception handling

---

## File Descriptions

### `player.py`
**Purpose:** Represents an individual player.  

**Functionality:**
- `__init__(self, name, points, rebounds, assists, steals, blocks)`  
  Initializes a Player object with a name and statistics.
- Getter and Setter methods: Access and update stats safely.
- `display_stats(self)`  
  Prints the player's statistics in a readable format.
- `__str__(self)`  
  Returns a concise string representation of the player for printing.

---

### `team.py`
**Purpose:** Manages the team roster and team-level operations.  

**Functionality:**
- `__init__(self)`  
  Initializes an empty roster.
- `add_player(self, player)`  
  Adds a Player object to the roster.
- `find_player(self, name)`  
  Searches for a player by name. Raises `PlayerNotFoundError` if the player is not found.
- `calculate_averages(self)`  
  Computes average points, rebounds, assists, steals, and blocks for the team.
- `write_to_csv(self, filename)`  
  Saves the roster to a CSV file.
- `load_from_csv(self, filename)`  
  Loads the roster from a CSV file. Handles missing file errors gracefully.

---

### `main.py`
**Purpose:** Program entry point and user interface.  

**Functionality:**
- Creates a `Team` object.
- Loads saved team data from `team_data.csv` if available.
- Displays a menu:
  1. Build Team: Input details for 5 players.
  2. Search Player: Search by name and display stats.
  3. Team Averages: Display average statistics.
  4. Save + Exit: Save data to CSV and exit.
- Loops continuously until the user chooses to save and exit.
- Calls methods from `Team` and `Player` as needed.

---

## Program Flow
1. Start the program.
2. Load team data from `team_data.csv` if it exists.
3. Display the menu:
   - Build Team
   - Search Player
   - Team Averages
   - Save + Exit
4. Based on user selection:
   - Build Team: Loop 5 times to create Player objects and add them to the roster.
   - Search Player: Find a player by name, display stats, or raise an error.
   - Team Averages: Calculate and display averages for all statistics.
   - Save + Exit: Write data to CSV and terminate the program.
5. Menu repeats after each action until the user exits.
6. Exceptions are handled with informative error messages to prevent crashes.

---

## Example Usage

**Build Team**
Enter player name: LeBron
Enter points: 25
Enter rebounds: 8
Enter assists: 7
Enter steals: 2
Enter blocks: 1
Player added to team!


**Search Player**


Enter player name to search: LeBron
LeBron Stats:
Points: 25
Rebounds: 8
Assists: 7
Steals: 2
Blocks: 1

If the player is not found:


PlayerNotFoundError: Player 'Jordan' not found in team roster.


**Team Averages**


Team Average Stats:
Points: 20.4
Rebounds: 7.2
Assists: 6.0
Steals: 1.8
Blocks: 0.8


**Save + Exit**


Team data saved to team_data.csv.
Exiting program...
