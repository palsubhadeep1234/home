# Subhadeep Pal — academic website

A Jekyll website for research in multiscale mechanics, polymer materials, and scientific AI. Published at https://palsubhadeep1234.github.io/home/.

## Local development

Use a recent Ruby supported by the Gemfile and Bundler version in Gemfile.lock.

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Open `http://127.0.0.1:4000/home/`. Keep `baseurl: /home` for the existing GitHub Pages project site.

## Content

- `_pages/about.md`: homepage and news.
- `_pages/research_projects.md`: current research and established foundations.
- `_pages/future_research.md`: proposed thrusts, outcomes, and links to their research foundations.
- `_pages/projects_*.md`: research detail pages with links to connected future thrusts; existing project URLs are preserved.
- `_data/publications.json`: shared source for the publication list, selected homepage papers, and PDF CV bibliography.
- `_pages/teaching.html`: teaching and mentoring.
- `_pages/cv.md`: HTML CV; `files/Subhadeep_CV.pdf`: public CV download.
- `_pages/contact.md`: contact details and professional profiles.
- `_layouts/faculty.html` and `assets/css/faculty.css`: shared layout, navigation, metadata, responsive and print styles.

Update publication statuses using the corresponding publisher/preprint record. Keep proposed research distinct from completed results. News dates should match documented events.

## Validation

```sh
bundle exec jekyll build
python3 scripts/check_site.py _site
```

The audit checks local links and fragments, image alt attributes, page headings, and inherited template text. Browser review should include the homepage, research figures, publications, navigation, and CV download at desktop and narrow widths.

To regenerate the public CV, install ReportLab in your Python environment and run:

```sh
python3 scripts/build_public_cv.py
```

Inspect all PDF pages after regenerating. This public CV intentionally omits the application CV's private phone number, referee contacts, and individual mentee names. The original application documents are not stored in this repository.

## Provenance and publishing

The October 2026 revision draws on the owner's supplied research statement and faculty-application CV. Figure assets in `images/research/` are extracted from the research statement; future-work captions identify proposed workflows. The proposal's institution-specific fit section is not published.

This remains a GitHub Pages/Jekyll site. A local build does not update the live website; publish through the repository's configured Pages source after reviewing the branch.

The repository originated from AcademicPages / Minimal Mistakes; retained theme components remain subject to the repository license.
