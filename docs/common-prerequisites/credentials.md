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

Add your API keys and OAuth credentials into n8n so your workflows can connect to external services.

**Prerequisites**: Complete [Google Setup](./google-setup) and [AI Services Setup](./ai-services) first.

---

## Access Credentials in n8n

1. Open your n8n instance
2. Click **Credentials** in the left sidebar
3. You'll see the credentials manager

{: .note }
> **First Time?** The credentials list will be empty - that's normal!

---

## Add Google OAuth2 (Gmail & Sheets)

**What you need**: Client ID and Client Secret from [Google Setup](./google-setup)

1. Click **"Add Credential"**
2. Search for "Google OAuth2 API"
3. Enter your credentials:
   - **Client ID**: From Google Cloud Console
   - **Client Secret**: From Google Cloud Console
4. Click **"Sign in with Google"**
5. Authorise the requested permissions
6. Name it: `Google - All Services`
7. Click **"Save"**

{: .highlight }
> **One Credential**: This single OAuth connection works for Gmail, Sheets, and Drive.

**Test**: Click the credential → Click **"Test"** → Should return your Google account info

---

## Add OpenRouter API

**What you need**: API key from [AI Services Setup](./ai-services#openrouter-multiple-ai-models)

1. Click **"Add Credential"**
2. Search for "OpenRouter"
3. Enter your OpenRouter API key
4. Name it: `OpenRouter - AI Models`
5. Click **"Create"**
6. Test the connection

---

## Add Google Gemini

**What you need**: API key from [AI Services Setup](./ai-services#google-gemini-free-tier)

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

## Add Perplexity API

**What you need**: API key from [AI Services Setup](./ai-services#perplexity-api-web-research)

1. Click **"Add Credential"**
2. Search for "Perplexity"
3. Enter your Perplexity API key
4. Name it: `Perplexity - Research`
5. Click **"Create"**
6. Test the connection

---

## Naming Best Practices

Use descriptive names:

- ✅ `Google - All Services`
- ✅ `OpenRouter - AI Models`
- ✅ `Gemini - Free AI`
- ❌ `Credential 1`
- ❌ `Test`

---

## Quick Reference

All credentials you need for the exercises:

| Service | Credential Type in n8n | Suggested Name |
|---------|------------------------|----------------|
| Gmail & Sheets | Google OAuth2 API | `Google - All Services` |
| OpenRouter | OpenRouter API | `OpenRouter - AI Models` |
| Gemini | Google Gemini (PaLM) API | `Gemini - Free AI` |
| Perplexity | Perplexity API | `Perplexity - Research` |

---

## Troubleshooting

**Google OAuth "Access blocked"**: Add your email to test users in Google Cloud Console OAuth consent screen

**"Invalid redirect"**: Check redirect URI in Google Console matches your n8n instance URL exactly

**API key "Invalid" or "Unauthorised"**: Check for extra spaces when pasting, regenerate key if needed

**"Rate limited"**: Check usage quotas in the service dashboard

---

## What You've Accomplished

✅ All credentials connected to n8n
✅ All connections tested successfully
✅ Ready to build workflows
