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

## Overview

In this section, we'll set up all the accounts and credentials needed for our email classification system. This takes about 15 minutes and only needs to be done once.

---

## Step 1: n8n Account Setup

### Create Your n8n Workspace

1. Navigate to [n8n.io](https://n8n.partnerlinks.io/gsl7xpbjua51)
2. Click "Get started for free"

   ![n8n Homepage](./images/setup/01-n8n-homepage.png)

3. Create account with email verification

   ![n8n Signup Form](./images/setup/02-n8n-signup-form.png)

4. Choose workspace name (e.g., "ai-automation-course")
5. Select the "Starter" plan for this exercise

{: .highlight }
> **Checkpoint**: You should see the n8n workflow canvas

---

## Step 2: OpenRouter API Setup

### Get Your AI Access Token

1. Open new tab: [openrouter.ai](https://openrouter.ai)

   ![OpenRouter Homepage](./images/setup/03-openrouter-homepage.png)

2. Sign up using Google/GitHub authentication
3. Navigate to "API Keys" in dashboard
4. Click "Create New Key"

   ![OpenRouter API Keys](./images/setup/04-openrouter-api-keys.png)

5. Name it "n8n-email-classifier"
6. Copy and save the API key securely

{: .warning }
> **Important**: This key is shown only once. Save it in a password manager.

---

## Step 3: Gmail API Configuration

### Enable Gmail Access for Automation

1. In n8n, click "Credentials" → "New"
2. Search and select "Gmail OAuth2 API"

   ![Gmail OAuth Setup](./images/setup/05-gmail-oauth-setup.png)

3. Click "Sign in with Google"
4. Select your Gmail account

   ![Google Account Selection](./images/setup/06-google-account-select.png)

5. Review permissions (read, modify, labels)

   ![Gmail Permissions](./images/setup/07-gmail-permissions.png)

6. Click "Allow" to grant access

   ![Gmail Allow Access](./images/setup/08-gmail-allow.png)

{: .note }
> **Why these permissions?** We need to read emails, apply labels, and mark as read.

---

## Step 4: Connect n8n with Gmail

### Complete the OAuth Flow

1. You'll be redirected back to n8n
2. Name the credential "Gmail - Personal"

   ![n8n Gmail Connected](./images/setup/09-n8n-gmail-connected.png)

3. Click "Save" to store the credential
4. Test connection with "Test credential"

   ![Test Gmail Connection](./images/setup/10-test-gmail-connection.png)

{: .highlight }
> **Success!** You should see "Connection successful"

---

## Step 5: OpenRouter Credential Setup

### Add AI Model Access

1. In n8n, go to "Credentials" → "New"
2. Search for "OpenRouter"
3. Select "OpenRouter API"

   ![OpenRouter Credential](./images/setup/11-openrouter-credential.png)

4. Paste your API key from Step 2
5. Name it "OpenRouter - Free Tier"
6. Click "Save"

   ![OpenRouter Save](./images/setup/12-openrouter-save.png)

7. Test the connection

   ![Test OpenRouter](./images/setup/13-test-openrouter.png)

{: .highlight }
> **Checkpoint**: Both Gmail and OpenRouter show "Connected"

---

## Troubleshooting

### Common Issues and Solutions

#### Gmail Connection Fails

- **Issue**: "Access blocked" error
- **Solution**: Enable "Less secure app access" in Google Account settings
- **Alternative**: Use App Password if 2FA is enabled

#### OpenRouter API Key Invalid

- **Issue**: "Invalid API key" error
- **Solution**: Regenerate key in OpenRouter dashboard
- **Check**: No extra spaces when pasting

#### n8n Canvas Not Loading

- **Issue**: Blank screen after login
- **Solution**: Clear browser cache and cookies
- **Try**: Different browser or incognito mode

---

## Next Steps

Environment setup complete! You now have:

- ✅ n8n workspace created
- ✅ OpenRouter API configured
- ✅ Gmail OAuth connected
- ✅ All credentials tested

Continue to [Part B: Workflow Construction →](./part-b-workflow)
