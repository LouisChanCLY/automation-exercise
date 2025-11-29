---
layout: default
title: AI Services Setup
parent: Common Prerequisites
nav_order: 2
---

# AI Services Setup

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Get API keys for AI models and research tools. All services offer free tiers perfect for learning.

**Time Required**: 10 minutes

---

## OpenRouter (Multiple AI Models)

### What is OpenRouter?

Access multiple AI models with one API key. Perfect for comparing different models.

### Get Your API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Click "Sign Up" → Use Google/GitHub
3. Navigate to [API Keys](https://openrouter.ai/keys)
4. Click "Create Key"
5. Name it: `n8n-exercises`
6. Copy and save securely

{: .highlight }
> **Free Credits**: OpenRouter provides $1 free credit. Exercises use minimal credits (~$0.001 per operation).

### Recommended Models

| Model | Cost | Best For | Speed |
|-------|------|----------|-------|
| **google/gemma-3-27b-it:free** | Free | Classification, simple tasks | Fast |
| **meta-llama/llama-3.2-3b-instruct:free** | Free | Quick responses | Very Fast |
| **google/gemini-flash-1.5** | $0.075/1M tokens | Complex reasoning | Fast |
| **anthropic/claude-3-haiku** | $0.25/1M tokens | Quality + Speed | Fast |

---

## Google Gemini (Free Tier)

### Why Gemini?

Google's Gemini offers generous free quotas perfect for AI agents, complex reasoning tasks, and iterative workflows.

### Part 1: Get Your Gemini API Key from Google AI Studio

#### 1.1 Visit Google AI Studio

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
1. Sign in with your Google account

![Google AI Studio API Keys Page](./images/13-google-ai-studio-empty.png)

#### 1.2 Accept Terms of Service

1. On your first visit, you'll see a "Welcome to AI Studio" screen
1. Read the Gemini API Additional Terms of Service
1. Check the agreement checkbox
1. Optionally, check the second box to receive updates
1. Click **"Continue"**

![AI Studio Terms](./images/14-ai-studio-terms.png)

#### 1.3 Create API Key

1. Click **"Create API key"** in the top-right corner
1. You'll see a "Create a new key" modal
1. Choose **"Default Gemini Project"** (or create a new project)

![Create New Key Modal](./images/17-create-new-key-modal.png)

#### 1.4 Copy Your API Key

1. Your API key will appear in the list (starts with `AIza...`)
1. Click the **three-dot menu** (⋮) next to your key
1. Select **"Copy API key"**

![API Key Created](./images/15-api-key-created.png)

![Copy API Key](./images/16-copy-api-key.png)

1. Save the key securely in your password manager

{: .warning }
> **Important**: Store your API key immediately. While you can copy it again later, keeping it secure is critical.

### Part 2: Add Gemini Credential to n8n

#### 2.1 Search for Gemini Credential

1. In n8n, click the **+ button** and select **Credential**
1. Search for **"Gemini"**
1. Select **"Google Gemini(PaLM) Api"**

![Gemini Search in n8n](./images/11-gemini-search-credential.png)

#### 2.2 Configure Credential

1. The **Host** field should already be filled with:

   ```
   https://generativelanguage.googleapis.com
   ```

1. Paste your API key into the **API Key** field
1. Click **"Save"**

![Gemini API Key Field](./images/12-gemini-api-key-field.png)

{: .highlight }
> **Success**: Your Gemini credential is now ready to use in any workflow!

### Free Tier Limits

{: .highlight }
> **Generous Free Quota**:
>
> - 60 requests/minute
> - 1 million tokens/month
> - 1,500 requests/day
>
> More than enough for all exercises!

### When to Use Gemini

- AI Agents with complex reasoning
- Iterative workflows with feedback loops
- Multi-step content generation
- LLM as a Judge patterns
- When you need consistent, free performance

### Gemini vs OpenRouter

| Feature | Google Gemini | OpenRouter |
|---------|--------------|------------|
| **Free Tier** | 1M tokens/month | $1 credit (~100K tokens) |
| **Setup** | Direct API key | Account + payment method |
| **Best For** | Learning, prototyping, AI agents | Production, model comparison |
| **Quota Reset** | Monthly | One-time credit |

---

## Perplexity API (Web Research)

### What is Perplexity?

Real-time web search capabilities for your AI agents. Essential for research tasks.

### Student Access (Recommended)

{: .highlight }
> **Students Get 12 Months Free!** Students worldwide can get Perplexity Pro for free for 12 months (worth $240), which includes API credits, unlimited searches, and access to the Comet browser.

**To claim your free student access:**

1. Visit [Perplexity Student Program](https://www.perplexity.ai/grow/comet/students)
2. Click to verify your student status
3. Verify using one of these methods:
   - **Student email** (`.edu` or university email address)
   - **Student ID card** or documentation upload
   - Verification is handled through SheerID
4. Get instant access to 12 months of Perplexity Pro
5. Bonus: Skip the waitlist for Comet browser

**What's Included for Students:**

- **12 months of Perplexity Pro** ($240 value)
- Unlimited Quick Searches
- 600+ Pro Searches per day
- Access to advanced AI models (GPT-4, Claude, etc.)
- **$5/month in API credits** (automatically included)
- File upload and analysis
- Access to Comet browser (AI-powered browser built for students)

**Eligibility:**

- Available to students globally (US, UK, and international)
- Must verify student status through student email or documentation
- UK students and international students can verify with university email or ID

### Get Your API Key

1. Go to [Perplexity AI](https://www.perplexity.ai/)
2. Navigate to [API Settings](https://www.perplexity.ai/settings/api)
3. Sign up for API access (use your student account if eligible)
4. Generate API key:
   - Click "Generate New Key"
   - Name: `n8n-research`
   - Copy and save

{: .highlight }
> **Monthly Credits**: $5 free monthly (~1000 searches) - resets each month! Students get this automatically with Pro access.

### Available Models

| Model | Use Case | Speed |
|-------|----------|-------|
| **Sonar** | Basic research, fact-finding | Fast |
| **Sonar Pro** | Complex queries, reasoning | Medium |
| **Online Models** | Real-time web data | Fast |

---

## API Key Security

### Best Practices

1. **Never share API keys** in screenshots or support requests
2. **Store securely** in password manager
3. **Don't commit to git** - use .env files
4. **Rotate regularly** - every 90 days
5. **Monitor usage** - set up alerts

### Quick Security Check

- [ ] Keys stored in password manager
- [ ] No keys in code repositories
- [ ] Usage alerts configured
- [ ] Test/production keys separated

---

## Service Comparison

### Which Service for What?

| Need | Use This Service | Why |
|------|------------------|-----|
| Email classification | OpenRouter (Gemma) | Free, fast, simple |
| Content generation | OpenRouter or Gemini | Flexible options |
| AI agents | Google Gemini | Free tier, powerful, consistent |
| Web research | Perplexity | Real-time data access |
| Complex reasoning | Gemini or Claude | Better understanding |
| Iterative workflows | Google Gemini | Good for feedback loops |
| Quick tests | Free models | No cost, fast iteration |

---

## What You've Accomplished

✅ OpenRouter API key obtained
✅ Google Gemini API configured
✅ Perplexity API ready
✅ Understand which service for which task
✅ Keys stored securely
