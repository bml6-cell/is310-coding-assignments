# Video Game Data Entry

This Python command-line program collects video game names, release years, and revenue figures. It displays example games using Rich, lets users enter multiple games, and saves confirmed entries to a CSV file.

## Setup

You need Python 3 and the Rich library.

From your repository’s main folder, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If you already have a course virtual environment, activate that environment instead.

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Run the Program

From the repository’s main folder, run:

```bash
python python-libraries/cli_data_entry.py
```

For each game:

1. Enter its name, release year, and revenue.
2. Review the information.
3. Type `yes` to confirm it or `no` to enter it again.
4. Type `yes` when asked to add another game, or `no` to finish.

The program then displays a table of the confirmed entries and saves them to `User's preferred games.csv` in the folder where you ran the command.

## Data Format

The CSV contains three columns:

| Column | Description | Example |
|---|---|---|
| Game | Video game title | Grand Theft Auto V |
| Release year | Year the game was released | 2013 |
| Revenue | Revenue figure entered by the user | $6 billion |

Revenue figures are stored as entered. The program does not verify their accuracy or standardize currencies and units.

## AI Use

See `ai-chat-log.md` for relevant AI prompts and responses. AI helped draft this README and explain the assignment requirements.