---
layout: default
title: Common Prerequisites
nav_order: 2
---

# Common Prerequisites & Service Setup

{: .fs-9 }

One-time setup guide for all services used across automation exercises.
{: .fs-6 .fw-300 }

---

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

This guide covers the initial setup for all services you'll use throughout the automation exercises. Complete these once, and you're ready for all exercises.

### Services We'll Configure

| Service | Purpose | Exercises Used |
|---------|---------|----------------|
| **Google Cloud Console** | OAuth authentication hub | All exercises |
| **Gmail API** | Email automation | Exercise 1, 2, 7+ |
| **Google Sheets API** | Data storage & logging | Exercise 1, 2, 3+ |
| **Google Gemini** | Free AI model | Exercise 2, 4+ |
| **OpenRouter** | Access to multiple AI models | Exercise 1, 3+ |
| **Perplexity API** | Real-time web research | Exercise 2, 5+ |
| **n8n** | Workflow automation platform | All exercises |

{: .important }
> **Complete This First**: Set up these prerequisites before starting any exercise. Once configured, you won't need to repeat these steps.

---

## Google Cloud Console Setup

### Why OAuth Over App Passwords

{: .highlight }
> **OAuth is the Professional Choice**: While app passwords seem simpler, OAuth provides better security, granular permissions, and works across all Google services with one setup.

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" dropdown → "New Project"
3. Project details:
   - **Name**: `n8n-automation`
   - **Organisation**: Leave as is
   - **Location**: Leave as is
4. Click "Create"
5. Wait for project creation (takes ~30 seconds)

### Step 2: Enable Required APIs

Enable all APIs you'll need across exercises:

1. In your project, navigate to **APIs & Services** → **Library**

2. **Enable Gmail API**:
   - Search for "Gmail API"
   - Click on it
   - Click "Enable"
   - Wait for activation

3. **Enable Google Sheets API**:
   - Return to Library
   - Search for "Google Sheets API"
   - Click "Enable"

4. **Enable Google Drive API** (for Sheets access):
   - Return to Library
   - Search for "Google Drive API"
   - Click "Enable"

{: .note }
> **Why Three APIs?** Gmail for email, Sheets for data, Drive for Sheets file access permissions.

### Step 3: Configure OAuth Consent Screen

1. Go to **APIs & Services** → **OAuth consent screen**
2. Choose "External" (unless you have Google Workspace)
3. Click "Create"
4. Fill in required fields:
   - **App name**: `n8n Automation`
   - **User support email**: Your email
   - **Developer contact**: Your email
   - Skip logo and other optional fields
5. Click "Save and Continue"

6. **Scopes** - Add these permissions:
   - Click "Add or Remove Scopes"
   - Search and select:
     - `https://www.googleapis.com/auth/gmail.modify`
     - `https://www.googleapis.com/auth/gmail.labels`
     - `https://www.googleapis.com/auth/spreadsheets`
     - `https://www.googleapis.com/auth/drive.file`
   - Click "Update"
   - Click "Save and Continue"

7. **Test users**:
   - Click "Add Users"
   - Add your Gmail address
   - Add any team members' emails
   - Click "Save and Continue"

### Step 4: Create OAuth Credentials

1. Go to **APIs & Services** → **Credentials**
2. Click **"+ Create Credentials"** → **"OAuth client ID"**
3. Configure:
   - **Application type**: Web application
   - **Name**: `n8n OAuth Client`
   - **Authorised redirect URIs**: Add:

     ```
     http://localhost:5678/rest/oauth2-credential/callback
     https://app.n8n.cloud/rest/oauth2-credential/callback
     ```

   - If using self-hosted n8n, add your instance URL
4. Click "Create"
5. **Save your credentials**:
   - Copy **Client ID**
   - Copy **Client Secret**
   - Store securely (you'll need these in n8n)

{: .warning }
> **Security Note**: Never share or commit OAuth credentials to version control.

---

## AI Model Access

### Google Gemini (Free Tier)

Google's Gemini offers generous free quotas perfect for learning.

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key"
4. Select your `n8n-automation` project
5. Click "Generate API Key"
6. Copy and save securely

{: .highlight }
> **Free Limits**: 60 requests/minute, 1 million tokens/month - plenty for all exercises!

### OpenRouter Setup

Access multiple AI models with one API.

1. Visit [OpenRouter](https://openrouter.ai/)
2. Click "Sign Up" → Use Google/GitHub
3. Navigate to [API Keys](https://openrouter.ai/keys)
4. Click "Create Key"
5. Name it: `n8n-exercises`
6. Copy and save securely

{: .note }
> **Free Credits**: OpenRouter provides $1 free credit. Exercise 1 uses ~$0.001 per email with Gemma.

#### Recommended Models for Exercises

| Model | Cost | Best For | Speed |
|-------|------|----------|-------|
| **google/gemma-3-27b-it:free** | Free | Classification, simple tasks | Fast |
| **meta-llama/llama-3.2-3b-instruct:free** | Free | Quick responses | Very Fast |
| **google/gemini-flash-1.5** | $0.075/1M tokens | Complex reasoning | Fast |
| **anthropic/claude-3-haiku** | $0.25/1M tokens | Quality + Speed | Fast |

### Perplexity API

For real-time web research capabilities.

1. Go to [Perplexity AI](https://www.perplexity.ai/)
2. Navigate to [API Settings](https://www.perplexity.ai/settings/api)
3. Sign up for API access
4. Generate API key:
   - Click "Generate New Key"
   - Name: `n8n-research`
   - Copy and save

{: .highlight }
> **Monthly Credits**: $5 free monthly (~1000 searches) - resets each month!

---

## n8n Platform Setup

### Option 1: Cloud (Recommended for Beginners)

1. Go to [n8n.cloud](https://n8n.cloud)
2. Sign up for free account
3. Verify email
4. Your instance URL will be: `https://[your-name].app.n8n.cloud`

### Option 2: Self-Hosted

```bash
# Using Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n

# Using npm
npm install n8n -g
n8n start
```

### Adding Credentials to n8n

Once in n8n, add all your credentials:

1. Go to **Credentials** (left sidebar)
2. Click **"Add Credential"**

#### Google OAuth2 (Gmail & Sheets)

1. Search "Google OAuth2 API"
2. Enter:
   - **Client ID**: From Google Cloud Console
   - **Client Secret**: From Google Cloud Console
3. Click "Sign in with Google"
4. Authorise permissions
5. Name: `Google - All Services`
6. Save

#### OpenRouter

1. Search "OpenRouter"
2. Enter API Key
3. Name: `OpenRouter - AI Models`
4. Save

#### Google Gemini

1. Search "Google PaLM" (covers Gemini)
2. Enter:
   - **API Key**: Your Gemini key
   - **Host**: `generativelanguage.googleapis.com`
3. Name: `Gemini - Free AI`
4. Save

#### Perplexity

1. Search "Perplexity"
2. Enter API Key
3. Name: `Perplexity - Research`
4. Save

---

## Verify Your Setup

### Quick Checklist

- [ ] Google Cloud Project created
- [ ] Gmail API enabled
- [ ] Google Sheets API enabled
- [ ] Google Drive API enabled
- [ ] OAuth consent screen configured
- [ ] OAuth credentials created and saved
- [ ] Google Gemini API key obtained
- [ ] OpenRouter account and API key
- [ ] Perplexity API key (if doing Exercise 2+)
- [ ] n8n instance running
- [ ] All credentials added to n8n

### Test Your Configuration

1. In n8n, create a test workflow
2. Add a Gmail node
3. Select your Google OAuth credential
4. Click "Execute Node"
5. If it lists your emails, you're ready!

{: .highlight }
> **Success!** You've completed all prerequisites. These credentials will work across all exercises.

---

## Security Best Practices

### Credential Management

1. **Never share API keys** in screenshots or support requests
2. **Use environment variables** for production
3. **Rotate keys regularly** (every 90 days)
4. **Set usage alerts** in Google Cloud Console
5. **Enable 2FA** on all accounts

### API Quotas & Limits

| Service | Free Tier Limits | Reset Period |
|---------|-----------------|--------------|
| Gmail API | 250 quota units/second | Per second |
| Sheets API | 100 requests/100 seconds | Rolling |
| Gemini | 60 requests/minute | Per minute |
| OpenRouter | $1 credit | One-time |
| Perplexity | $5/month credit | Monthly |

---

## Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| "Access blocked" in OAuth | Check consent screen test users |
| "Quota exceeded" | Wait for reset or upgrade plan |
| "Invalid credentials" | Regenerate and update in n8n |
| "Scope not authorised" | Add scope in consent screen |
| "Redirect URI mismatch" | Add n8n URL to OAuth credentials |

### Getting Help

- **n8n Community**: [community.n8n.io](https://community.n8n.io)
- **Google Cloud Support**: [cloud.google.com/support](https://cloud.google.com/support)
- **Exercise Support**: Create issue in course repository

---

## Next Steps

With prerequisites complete, you're ready to begin any exercise:

- [Exercise 1: Email Classification](./exercises/01-email-classification/) - Start here
- [Exercise 2: Cold Email Automation](./exercises/02-cold-email-automation/) - AI research & personalisation
- [View All Exercises](./exercises/) - Browse the complete curriculum

{: .highlight }
> **Pro Tip**: Bookmark this page - you'll reference these credentials in every exercise!
