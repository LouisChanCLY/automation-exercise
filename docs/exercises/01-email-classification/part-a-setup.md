---
layout: default
title: "Part A: Environment Setup"
parent: "Exercise 1: Email Classification"
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

This section covers the specific setup needed for the email classification exercise.

{: .important }
> **Prerequisites First**: If you haven't completed the [Common Prerequisites](/common-prerequisites), do that first. It covers Google Cloud Console, OAuth setup, and API keys you'll need across all exercises.

---

## What You'll Need

From the Common Prerequisites, ensure you have:

- ✅ Google Cloud Project with Gmail API enabled
- ✅ OAuth credentials configured
- ✅ OpenRouter API key
- ✅ n8n instance running

If any are missing, complete the [Common Prerequisites](/common-prerequisites) first.

---

## Step 1: Verify n8n Setup

### Access Your Workspace

If you completed the Common Prerequisites:

1. Log into your n8n instance
2. You should see the workflow canvas

If you haven't set up n8n yet:

1. Follow the [n8n Platform Setup](/common-prerequisites#n8n-platform-setup) guide
2. Return here once complete

{: .highlight }
> **Checkpoint**: You should see the n8n workflow canvas

---

## Step 2: Add OpenRouter to n8n

### Configure AI Model Access

From the Common Prerequisites, you should have your OpenRouter API key.

1. In n8n, go to **Credentials** → **Add Credential**
2. Search for "OpenRouter"
3. Enter:
   - **API Key**: Your OpenRouter key from prerequisites
   - **Name**: `OpenRouter - Email Classification`
4. Click "Create"

{: .note }
> **No API Key?** Complete [OpenRouter Setup](/common-prerequisites#openrouter-setup) first.

---

## Step 3: Connect Gmail to n8n

### Use Your Google OAuth Credentials

From the Common Prerequisites, you should have:

- Google Cloud Project with Gmail API enabled
- OAuth Client ID and Secret

1. In n8n, go to **Credentials** → **Add Credential**
2. Search and select "Gmail OAuth2 API"
3. Enter your credentials:
   - **Client ID**: From Google Cloud Console
   - **Client Secret**: From Google Cloud Console
4. Click "Sign in with Google"
5. Authorise the permissions:
   - Read and modify emails
   - Manage labels
   - Mark emails as read
6. Name it: `Gmail - Email Classification`
7. Click "Save"

{: .note }
> **Missing OAuth Credentials?** Complete [Google Cloud Console Setup](/common-prerequisites#google-cloud-console-setup) first.

{: .highlight }
> **Success**: You should see "Connection Established" in n8n.

---

## Step 4: Create Gmail Labels

### Prepare Your Inbox

For the classification system to work, create these labels in Gmail:

1. Open [Gmail](https://mail.google.com) in your browser
2. Click the gear icon → "See all settings"
3. Go to "Labels" tab
4. Create these labels by clicking "Create new label":
   - `URGENT-SUPPORT`
   - `HIGH-PRIORITY`
   - `ANGRY-CUSTOMER`
   - `STANDARD-PROCESSING`

{: .note }
> **Why Labels?** The workflow will automatically apply these based on AI classification.

---

## Troubleshooting

### Common Issues and Solutions

| Problem | Solution |
|---------|----------|
| "Access blocked" in Gmail OAuth | Add your email to test users in Google Cloud Console |
| "Scope not authorised" | Add Gmail scopes in OAuth consent screen |
| "Invalid API key" for OpenRouter | Check for extra spaces, regenerate if needed |
| "Redirect URI mismatch" | Ensure n8n URL matches exactly in Google Cloud |

{: .tip }
> **Need Help?** Check the [Common Prerequisites Troubleshooting](/common-prerequisites#troubleshooting) for detailed solutions.

---

## Next Steps

Setup complete! You now have:

- ✅ n8n workspace accessible
- ✅ Gmail OAuth connected via Google Cloud Console
- ✅ OpenRouter API configured
- ✅ Gmail labels created
- ✅ All credentials tested and working

{: .highlight }
> **Ready to Build!** You've completed all setup. The OAuth approach you've learned will work for any Google service.

Continue to [Part B: Build & Test →](./part-b-workflow)
