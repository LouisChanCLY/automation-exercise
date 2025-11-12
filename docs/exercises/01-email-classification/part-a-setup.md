---
layout: default
title: "Part A: Environment Setup"
parent: "Exercise 1: Email Classification"
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
- ✅ **Gmail API** - OAuth2 credentials configured
- ✅ **OpenRouter** - API key added to n8n
- ✅ **Google Cloud Project** - Gmail API enabled

{: .important }
> **Missing any?** Complete the [Common Prerequisites](../../common-prerequisites/) before continuing.

**Time for this setup**: 2-5 minutes

---

## Create Gmail Labels

The only exercise-specific setup is creating labels in your Gmail account for the classification system.

### Step 1: Access Gmail Settings

1. Open [Gmail](https://mail.google.com) in your browser
2. Click the gear icon (⚙️) in the top-right
3. Select **"See all settings"**
4. Navigate to the **"Labels"** tab

### Step 2: Create Classification Labels

Click **"Create new label"** and add these four labels:

1. `URGENT-SUPPORT`
2. `HIGH-PRIORITY`
3. `ANGRY-CUSTOMER`
4. `STANDARD-PROCESSING`

{: .note }
> **Label names matter**: Use these exact names. The workflow will apply them based on AI classification.

### Step 3: Verify Labels

Go back to your Gmail inbox and confirm all four labels appear in your left sidebar under "Labels".

{: .highlight }
> **Setup Complete!** Your Gmail is ready for automated classification.

---

## Ready to Build

You now have:

- ✅ All common prerequisites configured
- ✅ Gmail labels created for classification

[Continue to Part B: Build the Workflow →](./part-b-workflow){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
