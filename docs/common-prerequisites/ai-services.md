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

Google's Gemini offers generous free quotas perfect for AI agents and complex tasks.

### Generate API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key"
4. Select your `n8n-automation` project (from Google setup)
5. Click "Generate API Key"
6. Copy and save securely

{: .highlight }
> **Free Limits**: 60 requests/minute, 1 million tokens/month - plenty for all exercises!

### When to Use Gemini

- AI Agents (Exercise 2+)
- Complex reasoning tasks
- Multi-step workflows
- When you need consistent, free performance

---

## Perplexity API (Web Research)

### What is Perplexity?

Real-time web search capabilities for your AI agents. Essential for research tasks.

### Get Your API Key

1. Go to [Perplexity AI](https://www.perplexity.ai/)
2. Navigate to [API Settings](https://www.perplexity.ai/settings/api)
3. Sign up for API access
4. Generate API key:
   - Click "Generate New Key"
   - Name: `n8n-research`
   - Copy and save

{: .highlight }
> **Monthly Credits**: $5 free monthly (~1000 searches) - resets each month!

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
| AI agents | Google Gemini | Free tier, powerful |
| Web research | Perplexity | Real-time data |
| Complex reasoning | Gemini or Claude | Better understanding |
| Quick tests | Free models | No cost |

---

## What You've Accomplished

✅ OpenRouter API key obtained
✅ Google Gemini API configured
✅ Perplexity API ready
✅ Understand which service for which task
✅ Keys stored securely

---

## Next Steps

Set up the n8n platform to use these APIs.

[Continue to n8n Setup →](./n8n-setup){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
