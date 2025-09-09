# Image Organization for Exercise 1

This directory contains all images and screenshots for the Email Classification exercise.

## Directory Structure

```text
images/
├── setup/              # Environment setup screenshots
│   ├── n8n-signup.png
│   ├── openrouter-api-key.png
│   ├── google-cloud-console.png
│   └── gmail-oauth.png
├── workflow/           # Workflow building screenshots
│   ├── gmail-trigger-config.png
│   ├── ai-node-setup.png
│   ├── switch-node-routing.png
│   └── complete-workflow.png
├── testing/            # Testing process screenshots
│   ├── test-email-send.png
│   ├── execution-view.png
│   └── debug-panel.png
└── results/           # Results and output screenshots
    ├── gmail-labels-applied.png
    ├── google-sheets-log.png
    └── analytics-dashboard.png
```

## Image Naming Convention

- Use lowercase with hyphens
- Be descriptive but concise
- Include step numbers where applicable (e.g., `step-01-signup.png`)
- Max width: 1200px
- Format: PNG for screenshots, SVG for diagrams

## Adding New Images

1. Take screenshot at appropriate resolution
2. Crop to focus on relevant area
3. Annotate if necessary (arrows, highlights)
4. Save to appropriate subdirectory
5. Reference in markdown as: `![Alt text](./images/category/filename.png)`

## Example Usage in Markdown

```markdown
![n8n signup page](./images/setup/n8n-signup.png)
*Caption: The n8n signup page - choose the free tier*
```
