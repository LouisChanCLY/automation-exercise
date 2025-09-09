---
layout: default
title: Visual Guide
parent: Email Classification
grand_parent: Exercises
nav_order: 3
---

This guide shows the exact screens you'll see during the Gmail OAuth2 setup process.

## n8n Credential Setup

### Creating Gmail OAuth2 Credential in n8n

**What you'll see**: The n8n credential creation screen showing:

- Gmail OAuth2 API option in the credentials list
- OAuth Redirect URL that you need to copy
- Fields for Client ID and Client Secret
- "Sign in with Google" button

**Key elements to notice**:

- The OAuth Redirect URL (you'll need this for Google Cloud Console)
- The credential type should be "Gmail OAuth2 API"
- Both Client ID and Secret fields must be filled before connecting

## Google Cloud Console Setup

### Step 1: API Library - Gmail API

**Navigation path**: APIs & Services → Library → Search "Gmail API"

**What you'll see**:

- Gmail API card with the Gmail logo
- "Google Enterprise API" tag underneath
- Blue "ENABLE" button
- Description: "View and manage Gmail mailbox data"

**Action**: Click the blue "ENABLE" button

### Step 2: Creating OAuth2 Credentials

**Navigation path**: APIs & Services → Credentials → Create Credentials

**Dropdown menu options**:

- API key
- **OAuth client ID** (select this)
- Service account

**What to select**: OAuth client ID

### Step 3: OAuth Client Configuration

**Application Type Selection Screen**:

- **Web application** (correct choice)
- Android
- Chrome extension
- iOS
- TVs and Limited Input devices
- Desktop app
- Universal Windows Platform (UWP)

**Configuration fields**:

- Name: "n8n Gmail Integration"
- Authorized JavaScript origins: (leave empty)
- Authorized redirect URIs: (paste the n8n OAuth URL here)

### Step 4: Google Authorization Screen

**When you click "Sign in with Google" in n8n**:

**First screen**: Account selection

- Choose your Gmail account
- May show multiple accounts if you're signed into several

**Security warning screen**:

- Title: "Google hasn't verified this app"
- Warning message about unverified app
- **Click "Advanced"** (small text, bottom left)
- **Then click "Go to n8n-email-automation (unsafe)"**

**Permissions screen**:

- Shows app name: "n8n Email Automation"
- Lists requested permissions:
  - Read, compose, send and permanently delete all your email from Gmail
- **Click "Continue"** or **"Allow"**

## Verification Steps

### Successful Connection in n8n

**What success looks like**:

- Green checkmark or "Connected" status
- Your Gmail account email displayed
- Credential saved successfully message
- Ability to test the connection

### Testing the Connection

**In n8n workflow**:

1. Add Gmail Trigger node
2. Select your saved credential
3. "Listen for Event" button becomes active
4. Send test email
5. Email appears in n8n within 60 seconds

## Common Error Screens

### Redirect URI Mismatch Error

**Error message**: "Error 400: redirect_uri_mismatch"

**What it means**: The OAuth Redirect URL in Google doesn't match n8n's

**Fix**:

1. Copy the exact URL from n8n (including https://)
2. Update in Google Cloud Console
3. Wait 5 minutes for propagation

### Insufficient Scopes Error

**Error message**: "Insufficient Permission"

**What it means**: Gmail API scopes not properly configured

**Fix**:

1. Return to OAuth consent screen
2. Add scope: `https://www.googleapis.com/auth/gmail.modify`
3. Re-authenticate

## Tips for Following Along

1. **Keep both windows open**: Have n8n and Google Cloud Console in separate tabs
2. **Copy carefully**: OAuth URLs must match exactly (no extra spaces or characters)
3. **Wait for propagation**: Google changes can take 1-5 minutes to take effect
4. **Use the same browser**: Complete the entire flow in one browser session
5. **Check your spam**: Verification emails might go to spam

## Reference Locations

The actual screenshot files are stored in:

- `/docs/exercises/01-email-classification/images/setup/`

Files include:

- `Screenshot 2025-09-09 at 08.51.14.png` - Gmail API enable screen
- `Screenshot 2025-09-09 at 08.51.32.png` - n8n credential type selection
- `Screenshot 2025-09-09 at 08.51.45.png` - Gmail OAuth2 API selection
- `Screenshot 2025-09-09 at 08.52.00.png` - Create credentials dropdown
- `Screenshot 2025-09-09 at 08.52.14.png` - Application type selection

These screenshots correspond to the exact steps described in the setup guide.
