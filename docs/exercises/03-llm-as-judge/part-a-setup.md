---
layout: default
title: "Part A: Setup"
parent: "Exercise 3: LLM as a Judge"
grand_parent: Exercises
nav_order: 2
---

# Part A: Environment Setup

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Prerequisites Checklist

Before starting this exercise, ensure you've completed the [Common Prerequisites](../../common-prerequisites/):

- ✅ **n8n** - Platform setup complete
- ✅ **Google Gemini** - API key added to n8n

{: .important }
> **Missing Gemini?** Follow the [Google Gemini setup guide](../../common-prerequisites/ai-services#google-gemini-free-tier) to get your free API key.

**Time for this setup**: 2 minutes (just verify Gemini credential)

---

## Verify Gemini Access

This exercise only requires Google Gemini for both the generator and judge AI models.

### Quick Verification

1. Open your n8n instance
2. Go to **Credentials** menu
3. Confirm you have a "Google PaLM API" or "Gemini API" credential
4. The credential should show as valid/connected

{: .highlight }
> **Already set up?** Great! You're ready to build.

---

## No Additional Setup Required

Unlike other exercises, this one doesn't need:

- ❌ Gmail setup
- ❌ Google Sheets
- ❌ Additional API keys
- ❌ External services

Just Gemini and you're good to go!

---

## Ready to Build

You now have:

- ✅ n8n platform access
- ✅ Google Gemini API configured

[Continue to Part B: Build the Workflow →](./part-b-workflow){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
