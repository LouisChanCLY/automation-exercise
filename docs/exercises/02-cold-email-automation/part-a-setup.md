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

This section covers the specific setup needed for the cold email automation exercise.

{: .important }
> **Prerequisites First**: If you haven't completed the [Common Prerequisites](../../common-prerequisites/), do that first. It covers Google Cloud Console, OAuth setup, and core services you'll need.

### Additional Services for This Exercise

Beyond the common prerequisites, you'll need:

1. **Perplexity API** - For real-time web research
2. **Google Gemini** - For AI agents (free tier)

---

## Step 1: Verify Prerequisites

### Check Your Setup

From the Common Prerequisites, ensure you have:

- ✅ Google Cloud Project with Gmail & Sheets APIs enabled
- ✅ OAuth credentials configured
- ✅ n8n instance running
- ✅ Gmail connected to n8n
- ✅ Google Sheets connected to n8n

If any are missing, complete the [Common Prerequisites](../../common-prerequisites/) first.

---

## Step 2: Perplexity API Setup

### Get Your Research API Key

If you haven't already set up Perplexity:

1. Follow the [Perplexity API guide](../../common-prerequisites/ai-services#perplexity-api-web-research)
2. Return here with your API key

If you have your Perplexity API key:

1. In n8n, go to **Credentials** → **Add Credential**
2. Search for "Perplexity"
3. Enter:
   - **API Key**: Your Perplexity key
   - **Name**: `Perplexity - Cold Email Research`
4. Click "Create"

{: .note }
> **Model Selection**: We'll use "sonar" for fast, efficient research

---

## Step 3: Google Gemini Setup

### Configure AI Agent Model

If you haven't set up Gemini:

1. Follow the [Google Gemini guide](../../common-prerequisites/ai-services#google-gemini-free-tier)
2. Return here with your API key

If you have your Gemini API key:

1. In n8n, go to **Credentials** → **Add Credential**
2. Search for "Google Gemini (PaLM)" or just "Gemini"
3. Enter:
   - **API Key**: Your Gemini key
   - **Host**: `generativelanguage.googleapis.com`
   - **Name**: `Gemini - AI Agents`
4. Click "Create"

{: .highlight }
> **Why Gemini?**: Free tier with 60 req/min - perfect for AI agents!

---

## Step 4: Verify Gmail & Sheets Access

### Confirm Google Services

From the Common Prerequisites, you should already have:

- Gmail OAuth connected to n8n
- Google Sheets OAuth connected to n8n

If not configured:

1. Complete [Google Cloud Console Setup](../../common-prerequisites/google-setup)
2. Add Gmail OAuth credential to n8n
3. Add Google Sheets OAuth credential to n8n

{: .important }
> **OAuth is Best Practice**: We use OAuth for professional, secure access to Google services. App passwords are deprecated and less secure.

---

## Step 5: Create Tracking Spreadsheet

### Set Up Your Analytics

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

{: .note }
> **Sheets API**: Already enabled if you completed Common Prerequisites

---

## Summary: Required Credentials

### Verify All Services

In your n8n instance, confirm these credentials are configured:

| Service | Credential Name | Setup Guide |
|---------|----------------|-------------|
| **Gmail** | `Google - All Services` | [Common Prerequisites](../../common-prerequisites/credentials#google-oauth2-gmail--sheets) |
| **Google Sheets** | `Google - All Services` | Same OAuth credential as Gmail |
| **Perplexity** | `Perplexity - Cold Email Research` | Step 2 above |
| **Google Gemini** | `Gemini - AI Agents` | Step 3 above |

{: .note }
> **Single OAuth**: One Google OAuth credential works for both Gmail and Sheets - that's the power of OAuth!

---

## Step 6: Final Verification

### Credentials Checklist

Confirm all credentials show "Connected":

- [ ] Perplexity API
- [ ] Google Gemini
- [ ] Gmail (OAuth via Google Cloud Console)
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
| Gmail "Scope not authorised" | Add Gmail scopes in OAuth consent screen |
| Sheets "File Not Found" | Check spreadsheet ID, ensure it's shared |
| "Redirect URI mismatch" | Update redirect URI in Google Cloud Console |

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
