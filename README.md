# API Platform Documentation

This is the WSO2 API Platform documentation repository. This repository is open and we welcome your contributions!

To see the API Platform documentation site, go to [https://wso2.com/api-platform/docs/](https://wso2.com/api-platform/docs/)

## Local Development Setup

This documentation site is built using [MkDocs](https://www.mkdocs.org/) with the Material theme. Follow these steps to set up and run the documentation locally.

### Prerequisites

- **Python 3.12** (required)
- **Node.js** (for spell checking and link validation tools)
- **Git** (for version control)

### Setup Instructions

#### Option 1: Automated Setup (Recommended)

Run the setup script for automatic environment configuration:

```bash
./setup-dev.sh
```

This script will:
- Check for Python 3.12+ 
- Create a virtual environment
- Install all Python dependencies
- Install Node.js validation tools (if Node.js is available)
- Provide next steps

#### Option 2: Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wso2/docs-bijira.git
   cd docs-bijira
   ```

2. **Create and activate a Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   cd en
   pip install -r requirements.txt
   ```

4. **Install Node.js tools for spell checking and link validation (optional):**
   ```bash
   npm install -g markdown-spellcheck markdown-link-check
   ```

### Running the Documentation Locally

#### Quick Start (Documentation Only)
To start the development server with live reload:

```bash
cd en
python -m mkdocs serve
```

The documentation will be available at: [http://localhost:8000/bijira/docs/](http://localhost:8000/bijira/docs/)

#### Custom Port
If port 8000 is already in use, specify a different port:

```bash
python -m mkdocs serve --dev-addr localhost:8001
```

#### Full Validation (with spell check and link validation)
If you have the Node.js tools installed, you can run the complete validation script:

```bash
./serve.sh
```

This script will:
- Run spell checking on all markdown files
- Validate all links in the documentation
- Build the static site
- List the generated files

### Building for Production

To build the static site for deployment:

```bash
cd en
python -m mkdocs build
```

The built site will be generated in the `site/` directory.

### Project Structure

```
docs-bijira/
├── en/                          # English documentation
│   ├── docs/                    # Documentation source files
│   ├── theme/                   # Custom theme files
│   ├── mkdocs.yml               # MkDocs configuration
│   ├── requirements.txt         # Python dependencies
│   └── serve.sh                 # Validation and build script
├── devportal-theming/           # Theming assets
└── README.md                    # This file
```

### Making Changes

1. Edit markdown files in the `en/docs/` directory
2. The development server will automatically reload changes
3. Preview your changes at the local development URL
4. Test links and spelling using the validation tools
5. Submit a pull request with your changes

### Adding a Version Selector to a Section

Some top-level nav sections (e.g. **API Gateway**, **AI Gateway**) show a
**version dropdown** in the left panel. Selecting a version swaps the subtopic
list *and* the docs shown for that section. To add versioning to a new top-level
section, follow the steps below.

The mechanism lives in three theme files you normally do **not** need to touch —
`en/theme/material/partials/nav-item.html` (renders the selector + one hidden
group per version), `en/docs/assets/js/theme.js` (switches groups, remembers the
choice, keeps the user on the equivalent page), and
`en/theme/material/assets/css/partials/_version-select.css` (styling). A doc
writer only edits `en/mkdocs.yml` and the content folders.

> **Only top-level tabs can be versioned.** The selector is applied at nav
> `level == 1`. A section nested under another tab is rendered normally even if
> its title matches.

#### 1. Lay out one folder per version

Put each version's pages under a `<version>` sub-folder inside the section's
docs folder. The path segment right after the section slug **must** be the
version string, because both the server-side and client-side logic detect the
active version by matching `"<slug>/<version>/"` in the page URL.

```
en/docs/api-gateway/
├── 1.1.0/
│   ├── overview.md          # first page = the version's "home"/fallback
│   └── ...
└── 1.0.0/
    ├── overview.md
    └── ...
```

To seed a new version, copy the current folder (e.g. `cp -r 1.1.0 1.2.0`) and
edit from there. Keep the **same tail paths** across versions (e.g.
`policies/overview.md` in both) — the switcher lands the user on the equivalent
page when the tail matches, and falls back to that version's first page
(overview) when it does not.

#### 2. Register the section under `extra.versioned_sections`

In `en/mkdocs.yml`, add a block keyed by the **exact nav title**:

```yaml
extra:
  versioned_sections:
    API Gateway:            # must match the nav title exactly
      slug: api-gateway     # path segment before the version (the docs folder)
      default: "1.1.0"      # version shown when the URL has no version segment
      versions:             # dropdown order = list order (newest first)
        - "1.1.0"
        - "1.0.0"
```

#### 3. Structure the nav with one group per version

In the `nav:` tree, the versioned section's immediate children must be the
version strings, each holding that version's subtopics. The child title has to
match a value in `versions:` above.

```yaml
nav:
  - API Gateway:
    - "1.1.0":
        - Overview: api-gateway/1.1.0/overview.md
        - Policies:
            - Overview: api-gateway/1.1.0/policies/overview.md
    - "1.0.0":
        - Overview: api-gateway/1.0.0/overview.md
        - Policies:
            - Overview: api-gateway/1.0.0/policies/overview.md
```

#### 4. (Recommended) Make it a top-level expanded section

To get the vertical line + divider styling other top-level tabs use, add the
title to `extra.expanded_navs` (and optionally `extra.nav_icons`):

```yaml
extra:
  expanded_navs:
    - title: API Gateway
      options:
        - verticle-line
        - divider
```

#### 5. (Recommended) Redirect the un-versioned URLs

So old links (and the bare `<slug>/overview.md`) resolve into the default
version, add one entry per page to the `redirects` plugin's `redirect_maps`:

```yaml
plugins:
  - redirects:
      redirect_maps:
        api-gateway/overview.md: api-gateway/1.1.0/overview.md
        api-gateway/policies/overview.md: api-gateway/1.1.0/policies/overview.md
```

#### 6. Verify

```bash
cd en && python -m mkdocs build      # expect 0 warnings
```

Then `python -m mkdocs serve` and confirm: the section shows a version dropdown;
switching versions swaps the subtopic list; you stay on the equivalent page when
it exists (otherwise land on the version overview); and the choice persists as
you navigate (stored in `localStorage` under `docVersion:<slug>`). Search
results are automatically scoped to the active version and show a breadcrumb.

#### Prompt for an AI coding agent

If you use an AI coding assistant (Claude Code, Cursor, etc.), fill in the four
placeholders and paste the prompt below. It captures every rule above so the
agent can do the change end-to-end.

````text
You are working in the WSO2 API Platform docs repo (MkDocs Material, root `en/`).
Add a left-nav VERSION SELECTOR to an existing top-level nav section, using the
existing versioned-section mechanism. DO NOT modify the theme files that power it
(`en/theme/material/partials/nav-item.html`, `en/docs/assets/js/theme.js`,
`en/theme/material/assets/css/partials/_version-select.css`) — they are generic
and already handle rendering, switching, persistence, and version-scoped search.

Inputs:
- SECTION TITLE : <exact nav title, e.g. "API Gateway">
- SLUG          : <docs folder / URL segment, e.g. "api-gateway">
- VERSIONS      : <newest-first list, e.g. "1.1.0", "1.0.0">
- DEFAULT       : <version shown when URL has no version segment, e.g. "1.1.0">

Do the following, all within `en/`:

1. CONTENT: Ensure each version's pages live under `docs/<SLUG>/<VERSION>/...`.
   The path segment immediately after <SLUG> MUST equal the version string.
   To seed a new version, copy the existing version folder and keep the SAME
   tail paths across versions so equivalent-page switching works. Every version
   folder must contain an `overview.md` (used as the fallback page).

2. mkdocs.yml — register under `extra.versioned_sections`, keyed by the EXACT
   SECTION TITLE:
     <SECTION TITLE>:
       slug: <SLUG>
       default: "<DEFAULT>"
       versions:
         - "<each VERSION, newest first>"

3. mkdocs.yml — restructure this section's `nav:` subtree so its immediate
   children are the version strings (each child title must match a VERSIONS
   entry), each holding that version's subtopics pointing at
   `<SLUG>/<VERSION>/...` paths. Only top-level (level 1) tabs can be versioned.

4. mkdocs.yml — if not already present, add the title to `extra.expanded_navs`
   with options `verticle-line` and `divider` for top-level styling (and to
   `extra.nav_icons` if the section should have an icon).

5. mkdocs.yml — in the `redirects` plugin `redirect_maps`, add one entry per
   page mapping the old/un-versioned path to the DEFAULT version, e.g.
   `<SLUG>/overview.md: <SLUG>/<DEFAULT>/overview.md`. Generate these
   mechanically from the moved file list.

6. Fix any internal cross-links whose relative depth changed due to the moves.

7. VERIFY: run `cd en && python -m mkdocs build` and ensure ZERO warnings.
   Confirm built pages exist under `site/<SLUG>/<VERSION>/...` and that
   `data-md-versioned-section="<SLUG>"` appears in the generated nav HTML.
   Do not commit; leave changes in the working tree and report what changed.
````

### Troubleshooting

**Virtual environment activation issues:**
- On macOS/Linux: `source venv/bin/activate`
- On Windows: `venv\Scripts\activate`

**Port conflicts:**
Use a different port with `--dev-addr localhost:XXXX`

**Missing Node.js tools:**
The spell checking and link validation are optional. You can still build and serve the documentation without them.

**Python version issues:**
This project requires Python 3.12. Check your version with `python3 --version`
