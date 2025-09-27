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

## Overview

This setup phase takes about 20 minutes and prepares all the tools needed for AI-powered cold email automation.

### What We'll Set Up

1. **Perplexity API** - For real-time web research
2. **Google Gemini** - For AI agents (free tier)
3. **Gmail OAuth** - For sending emails
4. **Google Sheets** - For logging and analytics
5. **n8n Workspace** - If not already configured

---

## Step 1: Perplexity API Setup

### Create Your Research Account

Perplexity provides real-time web search capabilities that our AI agent will use to research prospects.

1. Go to [Perplexity AI](https://www.perplexity.ai/)
2. Click "Try Pro" or "API" in the navigation
3. Navigate to [Perplexity API Settings](https://www.perplexity.ai/settings/api)
4. Sign up for an API account (free tier available)

### Generate API Key

1. In your Perplexity dashboard, go to "API Keys"
2. Click "Generate New Key"
3. Name it: "n8n-cold-email"
4. Copy and save the API key securely

{: .warning }
> **Important**: Perplexity offers $5 free credits monthly. This covers ~1000 research queries.

### Understanding Perplexity Models

- **Sonar**: Fast, efficient model for basic research (we'll use this)
- **Sonar Pro**: Advanced reasoning for complex queries
- **Online Models**: Include real-time web search results

---

## Step 2: Google Gemini Setup

### Access Gemini API

We'll use Google's Gemini for our AI agents as it offers a generous free tier.

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key"
4. Select or create a Google Cloud project
5. Click "Generate API Key"
6. Copy and save the key

{: .highlight }
> **Free Tier**: Gemini offers 60 requests per minute free - perfect for development!

---

## Step 3: Gmail Configuration

### Enable Gmail API

If you completed Exercise 1, skip to "Create App Password". Otherwise:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project: "n8n-automations"
3. Enable Gmail API:
   - Navigate to "APIs & Services" → "Library"
   - Search for "Gmail API"
   - Click "Enable"

### Create App Password (Recommended)

For simpler setup, use an App Password:

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable 2-factor authentication if not already enabled
3. Search for "App passwords"
4. Create new app password:
   - App: Mail
   - Device: n8n
5. Copy the 16-character password

{: .note }
> **OAuth vs App Password**: App passwords are simpler for testing. Use OAuth for production.

---

## Step 4: Google Sheets Preparation

### Create Your Tracking Spreadsheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet: "Cold Email Tracking"
3. In row 1, add these column headers:

   ```
   timestamp | prospect_name | prospect_email | company |
   research_summary | email_subject | email_hook | email_body |
   email_cta | sent_status | workflow_id | notes
   ```

4. Note your spreadsheet ID from the URL:

   ```
   https://docs.google.com/spreadsheets/d/[SPREADSHEET_ID]/edit
   ```

### Enable Sheets API

1. Return to Google Cloud Console
2. Enable "Google Sheets API" (same process as Gmail)
3. Your existing credentials will work for both

---

## Step 5: n8n Workspace

### Access Your Workspace

**If you completed Exercise 1:**

- Log into your existing n8n account
- Your Gmail and Sheets credentials are already configured

**If you're starting fresh:**

1. Go to [n8n.cloud](https://n8n.cloud)
2. Sign up for free account
3. Verify your email
4. Log into your workspace

### Add Credentials in n8n

Navigate to "Credentials" → "Add Credential" for each:

#### Perplexity Credential

1. Search for "Perplexity"
2. Select "Perplexity API"
3. Paste your API key
4. Name: "Perplexity - Research"
5. Click "Create"

#### Google Gemini Credential

1. Search for "Google Palm" (includes Gemini)
2. Select "Google PaLM API"
3. Enter:
   - **API Key**: Your Gemini key
   - **Host**: `generativelanguage.googleapis.com`
4. Name: "Gemini - AI Agents"
5. Click "Create"

#### Gmail Credential (App Password Method)

1. Search for "Gmail"
2. Select "Gmail OAuth2 API"
3. For App Password:
   - Toggle to "Service Account or App Password"
   - **Email**: Your Gmail address
   - **Password**: Your 16-character app password
4. Name: "Gmail - Outreach"
5. Test and save

#### Google Sheets Credential

1. Search for "Google Sheets"
2. Select "Google Sheets OAuth2 API"
3. Follow OAuth flow (similar to Gmail)
4. Name: "Sheets - Tracking"
5. Test and save

---

## Step 6: Verify Setup

### Credentials Checklist

Confirm all credentials show "Connected":

- [ ] Perplexity API
- [ ] Google Gemini
- [ ] Gmail (OAuth or App Password)
- [ ] Google Sheets
- [ ] Spreadsheet created with headers

### Test Connections

1. In n8n, create a new workflow
2. Add a node for each service
3. Select your credentials
4. Run "Test" on each node

{: .highlight }
> **All Green?** You're ready to build the automation!

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Perplexity "Invalid API Key" | Check for spaces, regenerate if needed |
| Gemini "Quota Exceeded" | Wait 1 minute, you hit rate limit |
| Gmail "Authentication Failed" | Ensure 2FA is on, recreate app password |
| Sheets "File Not Found" | Check spreadsheet ID, ensure it's shared |

### Getting Help

- **Perplexity Docs**: [docs.perplexity.ai](https://docs.perplexity.ai)
- **Gemini Reference**: [ai.google.dev](https://ai.google.dev)
- **n8n Community**: [community.n8n.io](https://community.n8n.io)

---

## Next Steps

Setup complete! You now have:

- ✅ AI research capabilities via Perplexity
- ✅ Powerful language model via Gemini
- ✅ Email sending via Gmail
- ✅ Data logging via Google Sheets
- ✅ All credentials configured in n8n

[Continue to Part B: Build the Workflow →](./part-b-workflow){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
