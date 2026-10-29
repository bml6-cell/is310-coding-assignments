# AI Chat Log

**Date:** October 29, 2026
**Tool:** Claude (Anthropic)
**Project:** IS310 Minecraft mob scraper (Python, `requests` + `BeautifulSoup`)

## Summary

I used Claude to debug and improve a script that scrapes mob info from the Minecraft Wiki and saves it to a CSV.

- **Only Cow was scraped:** The history-parsing code was outside the `for` loop, so it only ran for the last mob. Indenting it inside the loop fixed it.
- **Mob description and type:** Claude showed how to pull the intro paragraph from each page and detect passive/neutral/hostile with plain string checks (no extra library).
- **Variable name conflict:** `description` was used for two different things. Renaming one to `cell` fixed it.
- **Missing pieces:** Claude pointed out the script needed CSV output, error handling, and checks for missing mobs.
- **Cleaner output:** Claude suggested shortening the "About" text, printing an aligned table in the terminal, and reordering CSV columns.

## Takeaway

Code that should run once per item must be indented inside the loop. Selectors should be checked against the live page, since Claude did not run the scraper on the wiki.
