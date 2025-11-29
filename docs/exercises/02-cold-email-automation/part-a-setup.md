---
layout: default
title: "Part A: Environment Setup"
parent: "Exercise 2: AI Cold Email Automation"
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

## Prerequisites Checklist

Before starting this exercise, ensure you've completed these from the [Common Prerequisites](../../common-prerequisites/):

### Required Setup

- **n8n Platform** - [Setup guide](../../common-prerequisites/n8n-setup)
- **Gmail & Google Sheets** - [Connect via n8n](../../common-prerequisites/google-setup)
- **Perplexity API** - [Setup guide](../../common-prerequisites/ai-services#perplexity-api-web-research)
- **Google Gemini API** - [Setup guide](../../common-prerequisites/ai-services#google-gemini-free-tier)

{: .important }
> **Haven't completed prerequisites?** Follow the links above to set up each service before continuing.

**Time for this setup**: 5-10 minutes

---

## Create Tracking Spreadsheet

The only exercise-specific setup is creating a Google Sheet to log outreach activity and results.

### Step 1: Create New Spreadsheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Click **"+ Blank"** to create a new spreadsheet
3. Rename it: **"Cold Email Tracking"**

### Step 2: Add Column Headers

In row 1, add these column headers (copy and paste into cells A1-L1):

```
timestamp | prospect_name | prospect_email | company | research_summary | email_subject | email_hook | email_body | email_cta | sent_status | workflow_id | notes
```

{: .tip }
> **Quick Setup**: Select cell A1, paste the entire line above, and the headers will spread across columns A-L automatically.

### Step 3: Get Your Spreadsheet ID

1. Look at your spreadsheet URL in the browser:

   ```
   https://docs.google.com/spreadsheets/d/[SPREADSHEET_ID]/edit
   ```

2. Copy the **SPREADSHEET_ID** portion (the long string between `/d/` and `/edit`)

3. Save this ID somewhere - you'll need it when building the workflow in Part B

{: .note }
> **Example ID**: `1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms`

### Step 4: Verify Access

Make sure the Google account used for your Google Sheets OAuth credential in n8n has access to this spreadsheet.

{: .highlight }
> **Setup Complete!** Your tracking spreadsheet is ready to log all cold email activity.

---

## Ready to Build

You now have:

- ✅ All common prerequisites configured
- ✅ Tracking spreadsheet created with proper headers
- ✅ Spreadsheet ID ready for the workflow

[Continue to Part B: Build the Workflow →](./part-b-workflow){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
