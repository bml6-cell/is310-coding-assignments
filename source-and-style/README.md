# Assignment 1: Inspecting the Cultural Web

## Iowa State University Football Programs

Website: [Iowa State University Football Programs](https://digitalcollections.lib.iastate.edu/isufootballprograms/)

Inspection date: October 1, 2026

I selected this archive because I am interested in college football. It preserves digitized game programs, making it useful for studying football as part of campus culture. These objects contain more than scores: rosters, advertising, and articles show how games were presented to fans. For example, the Data page lists a program for Iowa State's October 24, 1896 game against Minnesota. [Collection data](https://digitalcollections.lib.iastate.edu/isufootballprograms/data.html)

## What technologies were used?

With AI assistance, I inspected the About and Data pages in a browser and examined the About page's stylesheet and script references. I found evidence of all three main web technologies:

| Technology | Observed file examples | Purpose |
| --- | --- | --- |
| HTML | `about.html`, `data.html`, and `browse.html` | Structures pages, including headings, links, and collection information. |
| CSS | `assets/css/cb.css?v=2026-08-24` and `bootstrap.min.css` | Controls the appearance and layout. The `?v=...` part is a URL parameter; the file still ends in `.css`. |
| JavaScript | `bootstrap.bundle.min.js` and `lazysizes.min.js` | Supports interactive components and efficient image loading. |

The About page loads `cb.css` from the collection's own domain. Its Bootstrap CSS and JavaScript and its lazysizes script are linked from an external `web.core.windows.net` address. This shows that a page can combine resources from several locations. The page also references a Google Fonts stylesheet and a Google tag script whose URL does not end in `.js`. File extensions are useful clues, but they are not the only way to identify a resource's purpose.

The site's [technical credits](https://digitalcollections.lib.iastate.edu/isufootballprograms/about.html) explicitly identify **CollectionBuilder-CSV** and **Jekyll**. Jekyll is a static site generator: it turns source content and templates into web pages. CollectionBuilder's documentation explains that its generated output includes HTML, CSS, and JavaScript. Therefore, a static site can still have browser-based interactive features. [CollectionBuilder documentation](https://collectionbuilder.github.io/about.html)

I also found less familiar formats. The Data page's Download Data menu links to `metadata.csv` and `metadata.json`. CSV stores information in rows and columns, while JSON represents structured data for software. The linked source repository includes `_config.yml`, `README.md`, a `Gemfile`, and an `_sass` folder. YAML (`.yml`) stores configuration, Markdown (`.md`) stores formatted text, and a Gemfile declares Ruby dependencies used in building the site. Sass is used to prepare CSS. These are supporting source formats rather than the HTML pages visitors read. [Source repository](https://github.com/isu-digital/digital-collections-template)

## Who built it, and how many people were involved?

The archive is presented by **Iowa State University Library**, as shown by its branding and its About page. However, the software foundation comes from another institution: the technical credits say that University of Idaho faculty librarians developed CollectionBuilder. This suggests several kinds of work contributed to the result, including preserving the physical programs, digitizing them, describing them, and developing the website. The credits do not give a complete list of the people who performed those tasks. [Archive credits](https://digitalcollections.lib.iastate.edu/isufootballprograms/about.html)

CollectionBuilder's own About page names **Olivia Wikle, Evan Peter Williamson, Devin Becker, and Julia Stone** in its project presentations and workshops, and describes Stone joining its team. This documents at least four people associated with the underlying framework; it does **not** establish that those four built Iowa State's football archive. I could not verify an exact total for this particular website. Giving a precise number would overstate the available evidence. [CollectionBuilder project background](https://collectionbuilder.github.io/about.html)

## GitHub evidence

The Data page's Download Data menu includes a Website Source Code section. Its Source Code link points to [isu-digital/digital-collections-template](https://github.com/isu-digital/digital-collections-template). I would describe this as the repository linked by the archive, while noting that its name identifies a general template rather than a football-only project. The About page also links to the upstream [CollectionBuilder-CSV repository](https://github.com/CollectionBuilder/collectionbuilder-csv).

This archive shows how digitization depends on both cultural and technical work. Scanning programs makes the objects available, while metadata and web technologies help people discover and interpret them.

## AI assistance

I used Codex to help locate the archive, inspect its browser-visible pages and resource references, research its credits, and draft this assessment. The relevant prompt and a summary of the assistance are recorded in [ai-chat-log.md](ai-chat-log.md).
