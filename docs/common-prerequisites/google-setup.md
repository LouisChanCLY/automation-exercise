---
layout: default
title: Google Services Setup
parent: Common Prerequisites
nav_order: 1
---

# Google Services Setup via n8n

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Connect Gmail and Google Sheets to n8n using OAuth2 authentication. n8n handles the credential management - you just need to authenticate your Google account.

**Time Required**: 5 minutes

**What You're Connecting**:

- Gmail (for sending/reading emails)
- Google Sheets (for data logging)

---

## Step 1: Connect Gmail in n8n

### Add Gmail Credential

1. In your n8n workflow, add a **Gmail** node
2. Click on **Credential to connect with**
3. Click **"Create New Credential"**
4. Select **"Gmail OAuth2 API"**

### Authenticate with Google

1. Click **"Sign in with Google"** or **"Connect my account"**
2. Choose your Google account
3. Review permissions:
   - Read, compose, and send emails
   - Manage labels
4. Click **"Allow"**

{: .highlight }
> **Success**: You'll see "Connected" status in n8n

{: .note }
> **First-time setup**: Google may show a warning that the app isn't verified. Click "Advanced" → "Go to n8n (unsafe)" → "Allow". This is normal for OAuth apps in development mode.

---

## Step 2: Connect Google Sheets in n8n

### Add Sheets Credential

1. In your n8n workflow, add a **Google Sheets** node
2. Click on **Credential to connect with**
3. Click **"Create New Credential"**
4. Select **"Google Sheets OAuth2 API"**

### Authenticate with Google

1. Click **"Sign in with Google"** or **"Connect my account"**
2. Choose your Google account (same as Gmail)
3. Review permissions:
   - See, edit, create, and delete spreadsheets
4. Click **"Allow"**

{: .highlight }
> **Success**: You'll see "Connected" status in n8n

---

## Troubleshooting

### "This app isn't verified" Warning

When connecting for the first time, Google may show a security warning:

1. Click **"Advanced"** at the bottom left
2. Click **"Go to n8n (unsafe)"**
3. Review permissions and click **"Allow"**

{: .important }
> **This is expected**: Apps in development mode show this warning. Your credentials are safe - n8n uses industry-standard OAuth2.

### "Access blocked" Error

If you see "Access blocked: n8n has not completed the Google verification process":

**Solution**: Use a different Google account that isn't managed by a Workspace admin, or contact your workspace administrator to allow n8n.

### Connection Expires

OAuth tokens may expire. If you see authentication errors:

1. Go to **Credentials** in n8n
2. Find your Gmail/Sheets credential
3. Click **"Reconnect"**
4. Re-authenticate with Google

---

## What You've Accomplished

✅ Connected Gmail to n8n via OAuth2
✅ Connected Google Sheets to n8n via OAuth2
✅ Ready to use Gmail and Sheets nodes in any workflow
