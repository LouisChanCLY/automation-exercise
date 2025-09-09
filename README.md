# AI Automation Mastery - Training Exercises

A comprehensive collection of hands-on automation exercises designed to help students gain practical experience with AI and automation tools, improving their future employability.

## 🎯 Mission

To provide detailed, Coursera-quality hands-on exercises that enable students without technical backgrounds to become proficient in AI automation, ultimately enhancing their career prospects in an AI-driven economy.

## 📚 Course Structure

The course consists of 30+ progressive exercises covering:

- **Foundation (Exercises 1-10)**: Core automation concepts with n8n, APIs, and basic AI
- **AI Integration (Exercises 11-20)**: Advanced LLM usage, prompt engineering, and intelligent workflows  
- **Advanced Workflows (Exercises 21-30)**: Complex multi-step automations solving real business problems

## 🌐 Live Course Website

Visit the course at: [https://louischancly.github.io/automation-exercises/](https://louischancly.github.io/automation-exercises/)

## 🛠️ Development Setup

### Prerequisites

- Ruby 3.2+
- Bundler gem
- Git

### Local Development

1. Clone the repository:

    ```bash
    git clone https://github.com/louischancly/automation-exercises.git
    cd automation-exercises
    ```

2. Install dependencies:

    ```bash
    cd docs
    bundle install
    ```

3. Run Jekyll locally:

    ```bash
    bundle exec jekyll serve
    ```

4. Open browser to: `http://localhost:4000/automation-exercises/`

## 📁 Repository Structure

```raw
automation-exercises/
├── .github/
│   └── workflows/
│       ├── deploy.yml         # Main deployment workflow
│       └── pr-preview.yml     # PR preview builds
├── docs/                      # GitHub Pages content
│   ├── _config.yml           # Jekyll configuration
│   ├── Gemfile              # Ruby dependencies
│   ├── index.md             # Landing page
│   ├── assets/              # Global assets
│   ├── exercises/           # All course exercises
│   │   ├── 01-email-classification/
│   │   │   ├── index.md    # Exercise content
│   │   │   ├── images/     # Screenshots
│   │   │   └── resources/  # Downloads
│   │   └── ...
│   ├── guides/              # Supporting documentation
│   └── _data/              # Exercise metadata
├── exercises/               # Development versions
└── README.md               # This file
```

## ✍️ Contributing

### Adding a New Exercise

1. Create exercise folder: `docs/exercises/XX-exercise-name/`
2. Add `index.md` with YAML frontmatter:

    ```yaml
    ---
    layout: exercise
    title: "Exercise XX: Title"
    description: Brief description
    category: foundation|ai-integration|advanced|industry
    difficulty: beginner|intermediate|advanced
    time: 45-120 minutes
    tools: [tool1, tool2]
    ---
    ```

3. Add images to `docs/exercises/XX-exercise-name/images/`
4. Update `docs/_data/exercises.yml` with metadata
5. Create PR for review

### Content Guidelines

- **Detailed Instructions**: Every step should be explicit - assume no prior knowledge
- **Visual Aids**: Include screenshots for every significant UI interaction
- **Real-World Context**: Explain why each technique matters in actual job scenarios
- **Troubleshooting**: Anticipate common errors and provide solutions
- **Progressive Difficulty**: Each exercise builds on previous knowledge

## 🚀 Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch:

1. Push changes to `main`
2. GitHub Actions builds the Jekyll site
3. Deploys to GitHub Pages
4. Available at: `https://louischancly.github.io/automation-exercises/`

### Manual Deployment

To trigger a manual deployment:

1. Go to Actions tab
2. Select "Deploy Jekyll to GitHub Pages"
3. Click "Run workflow"

## 📊 GitHub Actions Workflows

### Main Deployment (`deploy.yml`)

- Triggers on push to `main` branch
- Builds Jekyll site with Ruby 3.2
- Deploys to GitHub Pages
- Uses latest GitHub Actions (v4/v5)

### PR Preview (`pr-preview.yml`)

- Builds PR changes for review
- Posts build status as PR comment
- Helps reviewers verify changes

## 🏷️ Versioning

- Main branch: Production-ready content
- Feature branches: For new exercises
- Releases: Tagged for course milestones

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- Built for students seeking practical AI automation skills
- Inspired by Coursera's hands-on learning approach
- Powered by Jekyll and GitHub Pages

## 📧 Contact

For questions or suggestions, please open an issue or contact the maintainers.

---

**Ready to start learning?** Visit [Exercise 1: Email Classification](https://louischancly.github.io/automation-exercises/exercises/01-email-classification/) to begin your automation journey!
