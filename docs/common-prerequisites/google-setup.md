---
layout: default
title: Google & OAuth Setup
parent: Common Prerequisites
nav_order: 1
---

# Google Cloud & OAuth Setup

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Set up Google Cloud Console for OAuth authentication with Gmail, Sheets, and Drive APIs. This single setup works across all exercises.

**Time Required**: 10 minutes

---

## Step 1: Create Google Cloud Project

### New Project Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" dropdown → "New Project"
3. Project details:
   - **Name**: `n8n-automation`
   - **Organisation**: Leave as is
   - **Location**: Leave as is
4. Click "Create"
5. Wait for project creation (takes ~30 seconds)

{: .highlight }
> **Success**: You'll see a notification when the project is ready.

---

## Step 2: Enable Required APIs

### Activate Google Services

In your project, navigate to **APIs & Services** → **Library**

#### Gmail API

1. Search for "Gmail API"
2. Click on it
3. Click "Enable"
4. Wait for activation

#### Google Sheets API

1. Return to Library
2. Search for "Google Sheets API"
3. Click "Enable"

#### Google Drive API

1. Return to Library
2. Search for "Google Drive API"
3. Click "Enable"

{: .note }
> **Why Three APIs?** Gmail for email, Sheets for data, Drive for Sheets file access permissions.

---

## Step 3: Configure OAuth Consent Screen

### Set Up App Information

1. Go to **APIs & Services** → **OAuth consent screen**
2. Choose "External" (unless you have Google Workspace)
3. Click "Create"

### App Configuration

Fill in required fields:

- **App name**: `n8n Automation`
- **User support email**: Your email
- **Developer contact**: Your email
- Skip logo and other optional fields

Click "Save and Continue"

### Add Scopes

1. Click "Add or Remove Scopes"
2. Search and select these permissions:
   - `https://www.googleapis.com/auth/gmail.modify`
   - `https://www.googleapis.com/auth/gmail.labels`
   - `https://www.googleapis.com/auth/spreadsheets`
   - `https://www.googleapis.com/auth/drive.file`
3. Click "Update"
4. Click "Save and Continue"

### Add Test Users

1. Click "Add Users"
2. Add your Gmail address
3. Add any team members' emails
4. Click "Save and Continue"

{: .important }
> **Test Users**: Only emails added here can use the app while in testing mode.

---

## Step 4: Create OAuth Credentials

### Generate Client ID & Secret

1. Go to **APIs & Services** → **Credentials**
2. Click **"+ Create Credentials"** → **"OAuth client ID"**
3. Configure:
   - **Application type**: Web application
   - **Name**: `n8n OAuth Client`

### Add Redirect URIs

Add these authorised redirect URIs:

```
http://localhost:5678/rest/oauth2-credential/callback
https://app.n8n.cloud/rest/oauth2-credential/callback
```

If using self-hosted n8n, also add:

```
https://[your-domain]/rest/oauth2-credential/callback
```

Click "Create"

### Save Your Credentials

{: .warning }
> **Important**: Save these immediately - you'll need them in n8n setup.

- Copy **Client ID**
- Copy **Client Secret**
- Store securely (password manager recommended)

---

## What You've Accomplished

✅ Created Google Cloud Project
✅ Enabled Gmail, Sheets, and Drive APIs
✅ Configured OAuth consent screen
✅ Generated OAuth credentials
✅ Added test users
