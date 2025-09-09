# Documentation Structure

This `docs/` folder contains all content for the GitHub Pages site.

## Folder Structure

```
docs/
├── _config.yml              # Jekyll configuration
├── index.md                 # Landing page
├── assets/                  # Global assets
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Global images (logo, etc.)
├── exercises/              # All course exercises
│   ├── index.md           # Exercise listing page
│   ├── 01-email-classification/
│   │   ├── index.md       # Exercise content
│   │   ├── images/        # Exercise-specific images
│   │   ├── resources/     # Downloadable files
│   │   └── solutions/     # Answer keys
│   └── 02-xxx/           # More exercises...
├── guides/                # Supporting documentation
│   ├── setup.md          # Environment setup
│   ├── troubleshooting.md # Common issues
│   └── faq.md            # Frequently asked questions
├── _includes/            # Reusable components
│   ├── header.html       # Site header
│   ├── footer.html       # Site footer
│   └── exercise-nav.html # Exercise navigation
├── _layouts/             # Page templates
│   ├── default.html      # Base layout
│   ├── exercise.html     # Exercise layout
│   └── home.html         # Homepage layout
└── _data/               # Data files
    ├── exercises.yml     # Exercise metadata
    └── navigation.yml    # Site navigation

```

## Adding New Exercises

1. Create folder: `exercises/XX-exercise-name/`
2. Add `index.md` with exercise content
3. Add images to `exercises/XX-exercise-name/images/`
4. Add downloadable resources to `exercises/XX-exercise-name/resources/`
5. Update `_data/exercises.yml` with metadata

## Image Guidelines

- **Global images** (logo, icons): `/assets/images/`
- **Exercise images**: `/exercises/XX-name/images/`
- **Format**: PNG for screenshots, SVG for diagrams
- **Naming**: `step-01-description.png`, `architecture-diagram.svg`
- **Size**: Max 1200px width, optimised for web

## Markdown Files

- All exercise content uses Markdown with YAML frontmatter
- Support for Mermaid diagrams
- Code syntax highlighting
- Tables and formatted content

## Local Development

```bash
# Install Jekyll
gem install bundler jekyll

# Install dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# View at http://localhost:4000
```