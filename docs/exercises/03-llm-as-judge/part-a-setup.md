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

Before starting this exercise, ensure you've completed these from the [Common Prerequisites](../../common-prerequisites/):

### Required Setup

- **n8n Platform** - [Setup guide](../../common-prerequisites/n8n-setup)
- **Google Gemini API** - [Setup guide](../../common-prerequisites/ai-services#google-gemini-free-tier)

{: .important }
> **Haven't completed prerequisites?** Follow the links above to set up each service before continuing.

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
> **Credential verified?** You're ready to build!

---

## Ready to Build

You now have:

- ✅ n8n platform access
- ✅ Google Gemini API configured

[Continue to Part B: Build the Workflow →](./part-b-workflow){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
