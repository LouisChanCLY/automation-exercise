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

### Generate API Key

1. **Go to Google AI Studio**
   - Visit [ai.google.dev](https://ai.google.dev/)
   - Click **Get API key** in the top-right corner

2. **Sign In**
   - Use your Google account
   - If prompted, accept terms of service

3. **Create API Key**
   - Click **Create API key**
   - Option 1: Select existing Google Cloud project (recommended if you completed Google setup)
   - Option 2: Click **Create API key in new project** (simpler, but creates separate project)

4. **Copy and Save**
   - Your API key will start with `AIza...`
   - Copy the key immediately (you won't be able to view it again)
   - Store securely in your password manager

5. **Optional: Test Your Key**
   ```bash
   curl -H 'Content-Type: application/json' \
        -d '{"contents":[{"parts":[{"text":"Hello!"}]}]}' \
        -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=YOUR_API_KEY'
   ```

{: .highlight }
> **Free Limits**: 60 requests/minute, 1 million tokens/month, 1,500 requests/day - plenty for all exercises!

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

---

## Next Steps

Set up the n8n platform to use these APIs.

[Continue to n8n Setup →](./n8n-setup){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
