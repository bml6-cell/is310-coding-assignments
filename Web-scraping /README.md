# Community Wiki Web Scraping

## Wiki and Research Question

I chose [Minecraft Wiki](https://minecraft.wiki/), a community-maintained wiki about Minecraft.

My research question is: **Which selected mobs are passive, neutral, or hostile, and when were they first added to Java Edition?**

I chose this topic because I enjoy Minecraft. This data could help researchers explore how the game’s creatures and their behaviors have developed over time.

## Scraping Method

I used Python with `requests` and `BeautifulSoup`. My scraper starts at the [Mob page](https://minecraft.wiki/w/Mob) and follows links to individual mob pages.

For each mob, I collected:

- Name
- Behavior classification
- First Java Edition version
- Introductory description
- Source URL

The scraper identifies itself through a User-Agent, waits two seconds between requests, and checks response codes before parsing pages. The collected data is saved in `minecraft_mobs.csv`.

## Robots.txt and Website Policies

I checked [Minecraft Wiki’s robots.txt](https://minecraft.wiki/robots.txt) before scraping. It does not disallow the regular mob articles or the main Mob page I used, but it restricts areas such as API endpoints, special pages, and search-related URLs.

The [Weird Gloop Terms of Use](https://weirdgloop.org/terms/) separately restrict automated access without prior consent and require compliance with content licenses. The robots.txt rules alone do not establish permission.

## Results

My scraper collected data for seven mobs: Cow, Axolotl, Creeper, Warden, Enderman, Shulker, and Phantom. The dataset includes their behavior classifications, introductory descriptions, first Java Edition versions, and source URLs.

## Reflection

Behavior categories simplify actions that can depend on specific conditions. The first version listed may also be a snapshot or experimental version rather than a full release.

Missing values could result from differences in page formatting rather than missing information. Since I selected only seven mobs, the results cannot represent all Minecraft mobs or establish which mobs are most popular or difficult.

## Files

- `wiki_scraping.py`: Python script used to scrape the wiki.
- `minecraft_mobs.csv`: CSV file containing the collected mob data.

## How to Run

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

Run the script:

```bash
python wiki_scraping.py
```

The CSV saves in the same directory as the script. Each run replaces the previous CSV.
