---
layout: default
title: Connect Credentials
parent: Common Prerequisites
nav_order: 4
---

# Connect Credentials to n8n

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Connect all your API keys and OAuth credentials to n8n. This is where everything comes together.

**Time Required**: 10 minutes

---

## Access Credentials Section

### Navigate to Credentials

1. Open your n8n instance
2. Click **Credentials** in the left sidebar
3. You'll see the credentials manager

{: .note }
> **First Time?** The credentials list will be empty - that's normal!

---

## Google OAuth2 (Gmail & Sheets)

### One Credential for All Google Services

This single OAuth connection works for Gmail, Sheets, and Drive.

#### Add Google OAuth2

1. Click **"Add Credential"**
2. Search for "Google OAuth2 API"
3. Enter your credentials:
   - **Client ID**: From Google Cloud Console
   - **Client Secret**: From Google Cloud Console
4. Click **"Sign in with Google"**
5. Authorise permissions:
   - Read and modify emails
   - Manage labels
   - Access spreadsheets
   - Manage files
6. Name it: `Google - All Services`
7. Click **"Save"**

{: .highlight }
> **Success**: Should show "Connection Established"

### Testing Google Connection

1. Click the credential
2. Click **"Test"**
3. Should return your Google account info

---

## OpenRouter API

### Connect AI Models

1. Click **"Add Credential"**
2. Search for "OpenRouter"
3. Enter:
   - **API Key**: Your OpenRouter key
4. Name it: `OpenRouter - AI Models`
5. Click **"Create"**
6. Test the connection

{: .note }
> **Model Selection**: You'll choose specific models when building workflows

---

## Google Gemini

### Add Gemini for AI Agents

1. Click **"Add Credential"**
2. Search for "Google Gemini (PaLM)" or just "Gemini"
3. Enter:
   - **API Key**: Your Gemini key
   - **Host**: `generativelanguage.googleapis.com`
4. Name it: `Gemini - Free AI`
5. Click **"Create"**
6. Test the connection

{: .important }
> **Host Required**: Don't forget to set the host URL!

---

## Perplexity API

### For Web Research

1. Click **"Add Credential"**
2. Search for "Perplexity"
3. Enter:
   - **API Key**: Your Perplexity key
4. Name it: `Perplexity - Research`
5. Click **"Create"**
6. Test the connection

---

## Credential Management

### Best Practices

#### Naming Convention

Use descriptive names:

- ✅ `Google - All Services`
- ✅ `OpenRouter - Production`
- ✅ `Gemini - Development`
- ❌ `Credential 1`
- ❌ `Test`

#### Organisation Tips

- Group by service type
- Add environment tags (dev/prod)
- Include purpose in name
- Document special configurations

### Security

#### Access Control

- Only share credentials within workflows
- Don't expose in screenshots
- Rotate keys regularly
- Use separate keys for dev/prod

#### Credential Sharing

In n8n cloud:

1. Go to credential settings
2. Click "Share"
3. Add team members
4. Set permission level

---

## Quick Reference

### All Required Credentials

| Service | Credential Type | Name in n8n |
|---------|----------------|-------------|
| Gmail | Google OAuth2 API | `Google - All Services` |
| Sheets | Google OAuth2 API | Same as Gmail |
| OpenRouter | OpenRouter API | `OpenRouter - AI Models` |
| Gemini | Google Gemini (PaLM) API | `Gemini - Free AI` |
| Perplexity | Perplexity API | `Perplexity - Research` |

---

## Common Issues

### Google OAuth Problems

| Issue | Solution |
|-------|----------|
| "Access blocked" | Add email to test users in Google Console |
| "Invalid redirect" | Check redirect URI matches exactly |
| "Scope error" | Re-add scopes in consent screen |

### API Key Issues

| Issue | Solution |
|-------|----------|
| "Invalid API key" | Check for extra spaces |
| "Unauthorised" | Regenerate key |
| "Rate limited" | Check quotas |

---

## What You've Accomplished

✅ Google OAuth connected (Gmail + Sheets)
✅ OpenRouter API configured
✅ Gemini API ready
✅ Perplexity API connected
✅ All credentials tested

---

## Next Steps

Verify everything is working correctly.

[Continue to Verification →](./verification){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
