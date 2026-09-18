# NFL QB Maze — Brayden

## What this maze is about

Match NFL quarterbacks to their teams. This easy maze takes about 3–5 minutes.
Every clue includes the answer and the commands for the next step.

NFL fandom connects players, teams, and cities. Rosters turn those connections
into data. This maze uses team memberships checked on September 17, 2026.

## Start here

1. Unzip `nfl-qb-maze.zip`. This creates the `nfl-qb-maze` folder.
   If you already have that extracted folder, use it directly.
2. Open that folder in VS Code with **File → Open Folder**.
3. Choose **Terminal → New Terminal**.
4. On Windows PowerShell only, run `.\hide-dotfiles.ps1` first so the
   hidden clue is hidden on Windows too. If script execution is blocked,
   ask your instructor for help. Mac/Linux users skip this step.
5. Type these commands, one line at a time:

```sh
cd entrance
cat start.txt
```

Follow each clue until the terminal says **MAZE SOLVED**.
You do not need to edit or delete anything, install software, or know NFL trivia.

## Commands you need

| Task | Mac/Linux | Windows PowerShell |
|---|---|---|
| Show your location | `pwd` | `Get-Location` |
| Show files and folders | `ls` | `Get-ChildItem` |
| Show hidden files | `ls -la` | `Get-ChildItem -Force` |
| Enter a folder | `cd chiefs` | `cd chiefs` |
| Go up one folder | `cd ..` | `cd ..` |
| Read a clue | `cat clue.txt` | `Get-Content clue.txt` |

In PowerShell, `cat` is also a shortcut for `Get-Content`, so the clues work as written.
`../bills` means go up one folder, then into the `bills` folder.

## Sources

- [Patrick Mahomes — Kansas City Chiefs](https://www.chiefs.com/team/players-roster/patrick-mahomes/)
- [Buffalo Bills roster — Josh Allen](https://www.buffalobills.com/team/players-roster/)
- [Joe Burrow — Cincinnati Bengals](https://www.bengals.com/team/players-roster/joe-burrow/)
- [Assignment instructions](https://cultureasdata-uiuc.github.io/is310-fall-2026/materials/introducing-defining-cad/06-intro-file-formats.html#homework-lost-found-in-the-cultural-command-line)

## Files to share

Place this `command-line-maze` folder in your `is310-coding-assignments` repository.
Keep `README.md` and `ai-chat-log.md` next to `nfl-qb-maze.zip` so people can read
them before unzipping. The ZIP does not contain the README. The extracted
`nfl-qb-maze` folder is also provided for easy local use.
