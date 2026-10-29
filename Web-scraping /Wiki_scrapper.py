import csv
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


URL = "https://minecraft.wiki/w/Mob"

HEADERS = {
    "User-Agent": (
        "is310-course-scraper/1.0 "
        "(student project; bml6@illinois.edu)"
    )
}

WANTED_MOBS = [
    "Cow", "Axolotl", "Creeper", "Warden", "Enderman",
    "Piglin", "Spider", "Slime", "Ghast", "Shulker", "Phantom"
]


def get_page(url):
    time.sleep(2)

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
    except requests.RequestException as error:
        print(f"Could not request {url}: {error}")
        return None

    print(f"Status {response.status_code}: {url}")

    if response.status_code != 200:
        return None

    if (
        "Just a moment..." in response.text
        or "Enable JavaScript and cookies" in response.text
    ):
        print("The site is blocking this request.")
        return None

    return BeautifulSoup(response.text, "html.parser")


def get_mob_links(soup):
    mob_pages = {}

    for behavior in ["Passive", "Neutral", "Hostile"]:
        heading = soup.find(id=f"{behavior}_mobs")

        if heading is None:
            continue

        for element in heading.find_all_next():
            if element.name in ["h2", "h3"]:
                break

            if element.name != "a":
                continue

            href = element.get("href")

            if not href:
                continue

            full_url = urljoin(URL, href)

            for mob in WANTED_MOBS:
                if full_url == f"https://minecraft.wiki/w/{mob}":
                    mob_pages[mob] = {
                        "url": full_url,
                        "behavior": behavior
                    }

    return mob_pages


def get_description(soup):
    content = soup.select_one("#mw-content-text .mw-parser-output")

    if content:
        for paragraph in content.find_all("p", recursive=False):
            text = paragraph.get_text(" ", strip=True)

            if text:
                # Keep the description on one line.
                return " ".join(text.split())

    return "MissingDescription"


def get_added_version(soup, mob):
    java_history = soup.find(id="Java_Edition")

    if java_history is None:
        return "MissingVersion"

    history_table = java_history.find_next(
        "table",
        attrs={"data-description": "History"}
    )

    if history_table is None:
        return "MissingVersion"

    current_version = None

    for row in history_table.find_all("tr"):
        version_cell = row.find("th", class_="nowrap")

        # Remember versions whose cells span multiple rows.
        if version_cell:
            version_link = version_cell.find("a")

            if version_link:
                current_version = version_link.get(
                    "title",
                    version_link.get_text(strip=True)
                )

        description = row.find("td")

        if description:
            text = description.get_text(" ", strip=True)

            if text.lower().startswith(f"added {mob.lower()}"):
                return current_version or "MissingVersion"

    return "MissingVersion"


def main():
    main_page = get_page(URL)

    if main_page is None:
        print("Could not retrieve the main Mob page.")
        return

    mob_pages = get_mob_links(main_page)
    rows = []

    for mob in WANTED_MOBS:
        if mob not in mob_pages:
            print(f"Could not find a link for {mob}.")
            continue

        details = mob_pages[mob]
        mob_soup = get_page(details["url"])

        if mob_soup is None:
            continue

        about = get_description(mob_soup)
        added_version = get_added_version(mob_soup, mob)

        rows.append([
            mob,
            details["behavior"],
            added_version,
            about,
            details["url"]
        ])

        print(f"{mob}: {details['behavior']} — {added_version}")

    if not rows:
        print("No mob data collected. CSV was not written.")
        return

    # Save in the same folder as this Python script.
    output_path = Path(__file__).parent / "minecraft_mobs.csv"

    with output_path.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        writer.writerow([
            "mob",
            "behavior",
            "first_added_java",
            "about",
            "source_url"
        ])

        writer.writerows(rows)

    print(f"\nSaved {len(rows)} mobs to:")
    print(output_path.resolve())


if __name__ == "__main__":
    main()