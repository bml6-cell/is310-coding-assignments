import csv
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()
Fields = ["Game", "Release year", "Revenue"]
table = Table(title = "Highest grossing games of all time")
for field in Fields:
    table.add_column(field)
table.add_row("Grand Theft Auto V", "2013", "$6 billion")
table.add_row("Call of Duty: Modern Warfare 2", "2009", "$1.3 billion")
table.add_row("Call of Duty: Black Ops", "2010", "$1.2 billion")
console.print(table)

print("\nPlease enter your preferred game to create your own list")

game = []
release_year = []
revenue = []

game_list = game  # Added: keep the list before input overwrites game

while True:
    game = input("Enter a game: ")
    year = input("Enter the release year for the game: ")
    rev = input("Enter the revenue for the game: ")
    print(f"You entered: {game}, {year}, {rev}")
    game_name = game  # Added: save the entered name
    game = game_list  # Added: restore the list
    answer = input("is this entry correct? (yes/no): ").strip().lower()
    if answer == "yes":
        game.append(game)
        game[-1] = game_name  # Added: store the name in the new entry
        release_year.append(year)
        revenue.append(rev)
        if input("Add another game? (yes/no): ").strip().lower() == "yes":  # Added
            continue  # Added
        break
    else:
        print("Please re-enter the information.")



user_table = Table(title = "User's preferred games")
user_table.add_column("Game")
user_table.add_column("Release year")
user_table.add_column("Revenue")
for i in range(len(game)):
    user_table.add_row(game[i], release_year[i], revenue[i])
console.print(user_table)


output_path = Path(__file__).resolve().parent / "User's preferred games.csv"
with output_path.open('w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Game", "Release year", "Revenue"])
    for i in range(len(game)):
        writer.writerow([game[i], release_year[i], revenue[i]])

print(f"Data saved to: {output_path}")
