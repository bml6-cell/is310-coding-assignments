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
python -m pip install -r python-libraries/requirements.txt
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

The program then displays a table of the confirmed entries and saves them to `User's preferred games.csv` in the `python-libraries` folder, and prints its full path.

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

AI also helped troubleshoot code, repair the Git repository, and create the HTML interface and this comparison. See the AI log for details.

## Run the HTML Interface

Open `python-libraries/index.html` in a web browser (double-click it in Finder). No installation or server is needed.

Enter a game, four-digit release year, and revenue. Select **Review entry**, then **Confirm and add** or **Edit entry**. Repeat for at least two games. Select **Download CSV** to save the confirmed records. The browser chooses the download location. Refreshing or closing the page clears entries, so download first.

## Interface Comparison

The CLI guides users through one question at a time and saves a CSV automatically after they finish. It requires Python, Rich, and a terminal. The HTML version shows all fields together and keeps the collection visible, making it easier to review several entries. It requires a manual download and does not preserve entries after a refresh.

Both versions collect game names, release years, and revenue and ask for confirmation. The HTML version adds required-field checks and a four-digit year check. Its revenue hint asks users to include currency, period, and whether a figure is estimated. The CLI accepts free-form text with fewer checks. Neither interface verifies revenue accuracy, and figures with different time periods or scopes should not be compared directly.

AI generated the HTML, CSS, and JavaScript, including review and edit controls, validation, and CSV export. The existing game fields were retained from the CLI. AI also drafted these instructions and tested the workflow. No rejected HTML proposals or user-authored revisions are recorded at this point.

For a casual user collecting video game information, the browser interface is likely the better fit because it needs no Python setup and displays the collection while entries are added. The CLI fits users already comfortable working in a terminal. This comparison describes the interfaces; it does not claim that classmates have tested them.
