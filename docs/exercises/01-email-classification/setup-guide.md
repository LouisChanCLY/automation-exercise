---
layout: exercise
title: "Gmail API & OAuth2 Setup Guide"
description: Complete setup instructions with screenshots
parent: /exercises/01-email-classification/
---

This guide provides detailed, screenshot-based instructions for setting up Gmail API access for the email
classification exercise.

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] Gmail account with 2-factor authentication enabled
- [ ] Access to Google Cloud Console
- [ ] n8n account (free tier is sufficient)
- [ ] OpenRouter account for AI processing
- [ ] 30-45 minutes for complete setup

## Part 1: Google Cloud Console Setup

### Step 1: Access Google Cloud Console

1. Open your browser and navigate to [console.cloud.google.com](https://console.cloud.google.com)
2. Sign in with your Google account
3. If this is your first time, accept the terms of service

### Step 2: Create a New Project

1. **Click the project dropdown** at the top of the page (it may show "Select a project" or an existing project name)
2. **Click "NEW PROJECT"** in the modal that appears
3. **Configure your project:**
   - Project name: `n8n-email-automation`
   - Location: Leave as default (No organization)
   - Click **CREATE**
4. **Wait for project creation** (10-30 seconds)
   - You'll see a notification when complete
   - The new project should auto-select

> 💡 **Tip**: If the project doesn't auto-select, use the dropdown to manually select it

### Step 3: Enable Gmail API

1. **Use the search bar** at the top of the console
2. **Type "Gmail API"** and press Enter
3. **Click on "Gmail API"** from the search results
4. **Click the blue "ENABLE" button**
5. **Wait for activation** (typically 10-30 seconds)
   - You'll see "API enabled" when complete

> ✅ **Checkpoint**: The Gmail API page should show management options and usage metrics (all at 0)

## Part 2: OAuth2 Credentials Creation

### Step 4: Navigate to Credentials

1. **In the left sidebar**, click on "Credentials"
   - If you don't see it, click the hamburger menu (☰) first
2. You should see an empty credentials page with a **"+ CREATE CREDENTIALS"** button at the top

### Step 5: Prepare n8n for OAuth Connection

**Important**: Complete this step before creating Google credentials

1. **Open n8n** in a new browser tab
2. **Navigate to your workflow** (or create a new one)
3. **Access Credentials section:**
   - Look for "Credentials" in the left sidebar
   - Or click the user menu → Settings → Credentials
4. **Click "Add Credential"**
5. **Search for "Gmail"** and select **"Gmail OAuth2 API"**
6. **Critical**: Copy the **OAuth Redirect URL** shown
   - It looks like: `https://your-instance.n8n.cloud/rest/oauth2-credential/callback`
   - Keep this window open - you'll need this URL in the next step

### Step 6: Create OAuth Client ID

Back in Google Cloud Console:

1. **Click "+ CREATE CREDENTIALS"** button
2. **Select "OAuth client ID"** from the dropdown
3. **Configure the OAuth consent screen** (if prompted):
   - User Type: External
   - App name: `n8n Email Automation`
   - User support email: Your email
   - Developer contact: Your email
   - Click "SAVE AND CONTINUE"
   - Scopes: Click "ADD OR REMOVE SCOPES"
   - Search and select: `https://www.googleapis.com/auth/gmail.modify`
   - Click "UPDATE" then "SAVE AND CONTINUE"
   - Test users: Add your Gmail address
   - Click "SAVE AND CONTINUE"

### Step 7: Configure OAuth Client

1. **Application type**: Select **"Web application"**
2. **Name**: `n8n Gmail Integration`
3. **Authorized JavaScript origins**: Leave empty
4. **Authorized redirect URIs**:
   - Click **"+ ADD URI"**
   - Paste the OAuth Redirect URL from n8n (Step 5)
   - Ensure it's exactly as copied (including https://)
5. **Click "CREATE"**

### Step 8: Save Your Credentials

A popup will appear with your credentials:

1. **Copy the Client ID**
   - Format: `xxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com`
2. **Copy the Client Secret**
   - Format: `GOCSPX-xxxxxxxxxxxxxxxxxxxxxxxxx`
3. **Click "OK"** to close the popup

> ⚠️ **Critical**: Save these credentials immediately! The Client Secret cannot be viewed again.

## Part 3: Connect n8n to Gmail

### Step 9: Configure n8n Credentials

Back in the n8n credentials window:

1. **Paste your Client ID** in the "Client ID" field
2. **Paste your Client Secret** in the "Client Secret" field
3. **Click "Sign in with Google"** button

### Step 10: Authorize Gmail Access

A Google authorization window will open:

1. **Choose your Gmail account**
2. **Handle the security warning**:
   - You'll see: "Google hasn't verified this app"
   - Click **"Advanced"** (bottom left)
   - Click **"Go to n8n Email Automation (unsafe)"**
   - This is expected for personal projects
3. **Review permissions**:
   - The app will request to "Read, compose, send, and permanently delete all your email from Gmail"
   - This is necessary for the automation to work
4. **Click "Continue"** or **"Allow"**

### Step 11: Verify Connection

1. **You'll be redirected back to n8n**
2. **Look for confirmation**:
   - "Account connected" message
   - Green checkmark or success indicator
3. **Name your credential**: `Gmail - Main Account`
4. **Click "Save"** to store the credential

> ✅ **Success**: Your Gmail OAuth2 connection is now established!

## Part 4: OpenRouter Setup

### Step 12: Create OpenRouter Account

1. **Navigate to** [openrouter.ai](https://openrouter.ai)
2. **Sign up** using Google or GitHub
3. **Verify your email** if required

### Step 13: Generate API Key

1. **Click on "Keys"** in the left sidebar
2. **Click "Create Key"**
3. **Configure the key**:
   - Name: `n8n-email-classifier`
   - Credits: Start with $5 free credits
4. **Click "Create"**
5. **Copy the API key immediately**
   - Format: `sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Step 14: Add OpenRouter to n8n

1. **In n8n, go to Credentials**
2. **Add Credential** → Search "OpenRouter"
3. **Paste your API key**
4. **Name**: `OpenRouter - AI Processing`
5. **Save** the credential

## Common Issues and Solutions

### Issue 1: "Google hasn't verified this app"

**Solution**: This is normal for personal projects. Click "Advanced" → "Go to [app name] (unsafe)"

### Issue 2: OAuth Redirect URI Mismatch

**Symptoms**: Error message about redirect_uri_mismatch

**Solution**:

1. Ensure the URI in Google Cloud Console exactly matches n8n's OAuth Redirect URL
2. Check for trailing slashes or https vs http
3. Wait 5 minutes for Google to propagate changes

### Issue 3: Insufficient Permissions

**Symptoms**: Gmail operations fail with permission errors

**Solution**:

1. Return to Google Cloud Console → OAuth consent screen
2. Add scope: `https://www.googleapis.com/auth/gmail.modify`
3. Re-authenticate in n8n

### Issue 4: API Not Enabled

**Symptoms**: "Gmail API has not been used in project"

**Solution**:

1. Go to Google Cloud Console → APIs & Services → Library
2. Search for "Gmail API"
3. Click "ENABLE"
4. Wait 1-2 minutes before retrying

### Issue 5: Rate Limiting

**Symptoms**: "Quota exceeded" errors

**Solution**:

1. Gmail API free tier: 250 quota units per user per second
2. Each email read = 5 units, each label = 5 units
3. Solution: Add delays between operations or upgrade quota

## Testing Your Setup

### Quick Test Checklist

1. **In n8n workflow canvas**:
   - Add a Gmail Trigger node
   - Select your saved Gmail credential
   - Click "Listen for Event"
   - Send yourself a test email
   - Verify it appears in n8n within 60 seconds

2. **Test OpenRouter**:
   - Add a Basic LLM Chain node
   - Connect to OpenRouter credential
   - Use model: `google/gemma-2-27b-it:free`
   - Test with simple prompt

## Security Best Practices

1. **Never share your credentials**:
   - Client Secret is sensitive
   - API keys grant full access
   - Use environment variables in production

2. **Limit OAuth scopes**:
   - Only request necessary permissions
   - Review granted permissions regularly

3. **Monitor usage**:
   - Check Google Cloud Console for unusual activity
   - Set up billing alerts even on free tier

4. **Rotate credentials regularly**:
   - Regenerate API keys every 90 days
   - Update OAuth clients if compromised

## Next Steps

With credentials configured, you're ready to:

1. Build the email classification workflow
2. Test with real emails
3. Implement routing logic
4. Add logging and monitoring

Return to the [main exercise](/exercises/01-email-classification/) to continue building your automation.

## Need Help?

- **n8n Community**: [community.n8n.io](https://community.n8n.io)
- **Gmail API Docs**: [developers.google.com/gmail/api](https://developers.google.com/gmail/api)
- **OpenRouter Support**: [openrouter.ai/docs](https://openrouter.ai/docs)
