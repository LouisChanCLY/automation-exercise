---
layout: default
title: "Part A: Setup"
parent: "Exercise 4: Connecting Workflows"
grand_parent: Exercises
nav_order: 2
nav_exclude: true
---

# Part A: Setup & Prerequisites

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Prerequisites Checklist

This exercise builds on previous exercises. Before starting, ensure you've completed these from the [Common Prerequisites](../../common-prerequisites/):

### Required Setup

- **n8n Platform** - [Setup guide](../../common-prerequisites/n8n-setup)
- **Google Cloud Project** - [Setup guide](../../common-prerequisites/google-setup)
- **Gmail API (OAuth2)** - [Setup guide](../../common-prerequisites/credentials#google-oauth2-gmail--sheets)
- **Google Gemini API** - [Setup guide](../../common-prerequisites/ai-services#google-gemini-free-tier)
- **Gmail labels** - Created in Exercise 1 (or [create them now](../01-email-classification/part-a-setup#create-gmail-labels))

{: .important }
> **Haven't completed prerequisites?** Follow the links above to set up each service before continuing.

**Time for this setup**: 2 minutes (just verify existing credentials)

---

## Verify Prerequisites

This exercise has **no unique setup** - it reuses everything from previous exercises.

### Quick Verification

1. Open your n8n instance
2. Go to **Credentials** menu
3. Confirm you have:
   - Gmail OAuth2 credential (for fetching/sending emails)
   - Google Gemini credential (for AI classification and generation)

{: .highlight }
> **Credentials verified?** You're ready to build three interconnected workflows!

---

## Ready to Build

You now have:

- ✅ Gmail API access for email operations
- ✅ Google Gemini for AI capabilities
- ✅ Understanding from previous exercises

[Continue to Part B: Build the Workflows →](./part-b-workflow){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
