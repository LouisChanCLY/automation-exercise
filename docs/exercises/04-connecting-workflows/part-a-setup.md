---
layout: default
title: "Part A: Setup"
parent: "Exercise 4: Connecting Workflows"
grand_parent: Exercises
nav_order: 2
---

# Part A: Setup & Prerequisites

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Prerequisites Checklist

This exercise builds on previous exercises. Before starting, ensure you've completed:

### From Exercise 1

- ✅ **Gmail API** - OAuth2 credentials configured
- ✅ **Gmail labels** - Created for classification

### From Exercise 3

- ✅ **Google Gemini** - API key configured for AI models

{: .important }
> **Haven't done Exercise 1 or 3?** You can still do this exercise, but you'll need to complete the [Common Prerequisites](../../common-prerequisites/) first and set up Gmail + Gemini.

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
> **All set?** You're ready to build three interconnected workflows!

---

## No Additional Setup Required

This exercise focuses on **workflow orchestration patterns** - how to connect multiple workflows together. You don't need:

- ❌ New API keys
- ❌ New credentials
- ❌ External services
- ❌ Additional setup steps

Everything you need was already configured in previous exercises.

---

## Ready to Build

You now have:

- ✅ Gmail API access for email operations
- ✅ Google Gemini for AI capabilities
- ✅ Understanding from previous exercises

[Continue to Part B: Build the Workflows →](./part-b-workflow){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
