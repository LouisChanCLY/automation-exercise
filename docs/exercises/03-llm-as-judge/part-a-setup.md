---
layout: default
title: "Part A: Setup"
parent: "Exercise 3: LLM as a Judge"
grand_parent: Exercises
nav_order: 2
---

# Part A: Environment Setup

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

In this section, you'll prepare your environment for the LLM as a Judge workflow. This includes verifying your API credentials and creating a Google Sheet to track content generation iterations.

**Time Required**: 15 minutes

---

## Step 1: Verify Prerequisites

### Required Credentials

Before starting, ensure you have these credentials already configured in n8n:

| Service | Credential Type | Setup Guide |
|---------|----------------|-------------|
| **OpenRouter** | API Key | [AI Services Setup](../../common-prerequisites/ai-services) |
| **Google Sheets** | OAuth2 | [Google Setup](../../common-prerequisites/google-setup) |

### Check Your Credentials in n8n

1. Open your n8n instance
2. Click **Settings** (gear icon, bottom-left)
3. Select **Credentials**
4. Verify you see:
   - **OpenRouter API** credential
   - **Google Sheets OAuth2** credential

{: .important }
> **Don't have these?** Complete the [Common Prerequisites](../../common-prerequisites/) first. These are required for this exercise.

---

## Step 2: Create Google Sheet for Logging

### Why We Need This Sheet

This spreadsheet will track:
- All content generation attempts
- Quality scores from each iteration
- Feedback provided by the judge
- Final approved content
- Success/failure status
- Timestamp and iteration count

### Create the Sheet

1. **Open Google Sheets**
   - Go to [sheets.google.com](https://sheets.google.com)
   - Click "Blank" to create new spreadsheet

2. **Name Your Sheet**
   - Click "Untitled spreadsheet" at the top
   - Rename to: `LLM Judge Quality Log`

3. **Create Column Headers**

   In **Row 1**, enter these column headers:

   | A | B | C | D | E | F | G | H | I | J |
   |---|---|---|---|---|---|---|---|---|---|
   | timestamp | topic | target_audience | iteration_count | final_score | passed | final_content | all_scores | all_feedback | total_iterations |

4. **Format Headers**
   - Select Row 1
   - Make it **bold** (Ctrl/Cmd + B)
   - Set background color to light gray (optional)
   - Click **View** → **Freeze** → **1 row** (keeps headers visible when scrolling)

5. **Set Column Widths**
   - Column A (timestamp): 180px
   - Column B (topic): 200px
   - Column C (target_audience): 150px
   - Column D (iteration_count): 120px
   - Column E (final_score): 100px
   - Column F (passed): 80px
   - Column G (final_content): 400px
   - Column H (all_scores): 150px
   - Column I (all_feedback): 300px
   - Column J (total_iterations): 120px

6. **Save the Sheet ID**

   Copy the Spreadsheet ID from the URL:
   ```
   https://docs.google.com/spreadsheets/d/[SPREADSHEET_ID]/edit
   ```

   **Example**:
   ```
   https://docs.google.com/spreadsheets/d/1a2B3c4D5e6F7g8H9i0J1k2L3m4N5o6P/edit
   ```

   The ID is: `1a2B3c4D5e6F7g8H9i0J1k2L3m4N5o6P`

   {: .highlight }
   > **Save this ID**: You'll need it when building the workflow in Part B.

---

## Step 3: Understand the Data Schema

### What Gets Logged

Each successful or failed generation run creates one row with:

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| **timestamp** | DateTime | When the workflow completed | `2025-01-15T10:30:45Z` |
| **topic** | String | Content topic provided as input | `"Write a blog post about remote work productivity"` |
| **target_audience** | String | Intended audience | `"Remote workers, 25-45 years old"` |
| **iteration_count** | Number | How many times content was regenerated | `3` |
| **final_score** | Number | Quality score of final content (0-100) | `85` |
| **passed** | Boolean | Whether quality threshold was met | `TRUE` |
| **final_content** | Text | The approved or best-attempt content | `"Remote work has transformed..."` |
| **all_scores** | Array | Scores from each iteration | `[65, 78, 85]` |
| **all_feedback** | Array | Feedback from each iteration | `["Add examples", "Improve conclusion", "Good!"]` |
| **total_iterations** | Number | Total attempts made (same as iteration_count) | `3` |

### Example Row

After a successful run:

```
timestamp: 2025-01-15T14:22:10Z
topic: Product description for wireless headphones
target_audience: Remote workers, 25-45
iteration_count: 2
final_score: 88
passed: TRUE
final_content: "Experience studio-quality sound while working from anywhere..."
all_scores: [72, 88]
all_feedback: ["Add battery life details", "Perfect!"]
total_iterations: 2
```

---

## Step 4: Understanding the Quality Criteria

### Default Evaluation Framework

The judge LLM will evaluate generated content using these criteria:

#### 1. Accuracy (25% weight)
- Content is factually correct
- No hallucinated information
- Claims are verifiable
- Data is realistic

#### 2. Clarity (25% weight)
- Easy to understand
- Well-structured sentences
- Logical flow
- Appropriate vocabulary for audience

#### 3. Completeness (20% weight)
- Covers all required points
- Includes necessary details
- Addresses the full topic
- No missing critical information

#### 4. Tone (15% weight)
- Matches target audience
- Appropriate formality level
- Consistent voice
- Brand-aligned (if specified)

#### 5. Creativity (15% weight)
- Engaging and interesting
- Original angles
- Vivid examples
- Memorable phrasing

### Scoring System

- **Each criterion**: Scored 0-100
- **Overall score**: Weighted average
- **Pass threshold**: 80 or higher
- **Maximum iterations**: 5 attempts

### Customization (Optional)

You can modify these criteria in Part B when building the judge prompt. Common variations:

**For Technical Documentation**:
- Replace "Creativity" with "Technical Accuracy"
- Increase "Clarity" weight to 30%
- Add "Code Examples" criterion

**For Marketing Copy**:
- Increase "Creativity" to 25%
- Add "Call-to-Action Strength" criterion
- Add "Emotional Appeal" metric

**For Customer Service**:
- Add "Empathy" criterion (20%)
- Increase "Tone" to 25%
- Add "Solution Provided" check

---

## Step 5: Plan Your First Test Case

### Choose a Content Type

For your first test, pick something simple but meaningful:

**Recommended Options**:

1. **Product Description**
   - Topic: "Noise-cancelling headphones"
   - Audience: "Remote workers"
   - Length: 150-200 words

2. **Email Subject Lines**
   - Topic: "Promoting a productivity webinar"
   - Audience: "Busy professionals"
   - Length: 5-10 words

3. **Blog Post Introduction**
   - Topic: "Benefits of automation"
   - Audience: "Small business owners"
   - Length: 100-150 words

4. **Social Media Post**
   - Topic: "Company culture highlight"
   - Audience: "Job seekers, 22-35"
   - Length: 280 characters (Twitter/X)

{: .highlight }
> **Start Simple**: Pick option #1 or #2 for your first run. You can test others after mastering the basics.

### Define Your Success Criteria

Write down what "good" looks like for your chosen content:

**Example for Product Description**:
- ✅ Mentions 3+ key features
- ✅ Includes emotional benefit ("focus better", "enjoy music")
- ✅ Professional but friendly tone
- ✅ Ends with subtle call-to-action
- ✅ 150-200 words

---

## Step 6: Optional - Install Workflow Template

### Quick Start Option

If you want to see the finished workflow before building:

1. Download the template: [llm-judge-workflow.json](./downloads/llm-judge-workflow.json)
2. In n8n, click **Workflows** → **Import from File**
3. Select the downloaded JSON file
4. **Important**: Replace placeholder credential IDs and Sheet ID before activating

### Or Build From Scratch (Recommended)

Part B will guide you through building each node step-by-step. This approach helps you understand the logic and customize for your needs.

---

## Step 7: Setup Checklist

Before moving to Part B, verify:

- ✅ n8n is open and accessible
- ✅ OpenRouter credential exists in n8n
- ✅ Google Sheets OAuth2 credential exists in n8n
- ✅ Google Sheet created with proper column headers
- ✅ Spreadsheet ID saved for reference
- ✅ Test content topic chosen
- ✅ Success criteria defined

---

## Troubleshooting

### "I don't have OpenRouter credentials"

**Solution**: Follow the [AI Services Setup](../../common-prerequisites/ai-services#openrouter-setup) guide to create account and get API key.

### "Google Sheets OAuth not working"

**Solution**:
1. Ensure you completed [Google Cloud Setup](../../common-prerequisites/google-setup)
2. Check Google Sheets API is enabled in Cloud Console
3. Re-authenticate the credential in n8n

### "Can I use a different LLM provider?"

**Yes!** You can substitute:
- **Anthropic Claude** - Direct API or via OpenRouter
- **OpenAI GPT-4** - Direct API
- **Google Gemini** - Via Google AI Studio
- **Local models** - Ollama with supported models

You'll need to adjust node configurations in Part B accordingly.

### "Can I use a different logging destination?"

**Yes!** Instead of Google Sheets, you can use:
- **Airtable** - Similar spreadsheet interface
- **PostgreSQL** - For production systems
- **MongoDB** - For JSON-native storage
- **Webhook** - Send to any API endpoint
- **Local File** - CSV or JSON file

Part B shows Google Sheets, but the logic transfers to other destinations.

---

## What You've Accomplished

✅ Verified all required credentials
✅ Created structured logging sheet
✅ Understood quality evaluation framework
✅ Planned first test content
✅ Ready to build the workflow

---

## Next Steps

Now that your environment is ready, let's build the workflow!

[Continue to Part B: Build Workflow →](./part-b-workflow){: .btn .btn-primary }
