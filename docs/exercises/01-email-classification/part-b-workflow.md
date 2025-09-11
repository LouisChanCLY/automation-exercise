---
layout: default
title: "Part B: Workflow Construction"
parent: "Exercise 1: Email Classification"
grand_parent: Exercises
nav_order: 3
---

# Part B: Workflow Construction

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Now we'll build the actual automation workflow. This section takes about 20 minutes and involves creating nodes, connecting them, and configuring the AI classification logic.

---

## Step 5: Create a New Workflow

### Set Up Your Canvas

1. Click "Add workflow" in your workspace
2. Name it: "Email Classification & Routing"
3. Click "Create"

   ![n8n Workspace](./images/workflow/01-n8n-workspace.png)

{: .note }
> **Canvas navigation**: Click and drag to move around, scroll to zoom, right-click for options

---

## Step 6: Gmail Trigger Setup

### Configure Email Detection

1. Click the plus button in the top right corner
2. Search for "Gmail" in the node panel
3. Select "On message received" trigger

   ![Add Gmail Trigger](./images/workflow/02-add-gmail-trigger.png)

4. Configure trigger settings:
   - **Credential**: Select the credential we created earlier
   - **Poll Time**: Every Minute
   - **Event**: "Message Received"
   - **Simplify Output**: Toggle OFF

   ![Gmail Trigger Configuration](./images/workflow/03-gmail-trigger-config.png)

5. Test the trigger:
   - Click "Fetch Test Event"
   - Click "Listen for Event"
   - Send a test email to yourself
   - Wait for it to appear in n8n

{: .highlight }
> **Success**: You should see your test email data in the output panel

---

## Step 7: Email Data Preparation

### Extract and Clean Email Content

1. Add "Code" node after Gmail Trigger (click the + on the connection)
2. Name it: "Prepare Email for AI"
3. Configure:
   - **Mode**: "Run Once for Each Item"
   - **Language**: "Javascript"

   ![Add Code Node](./images/workflow/04-add-ai-node.png)

4. Add this code:

```javascript
// Extract and clean email data
const emailData = {
  sender: $input.item.json.from.value[0].address,
  senderName: $input.item.json.from.value[0].name || 'Unknown',
  subject: $input.item.json.subject,
  body: $input.item.json.text || $input.item.json.snippet,
  receivedDate: $input.item.json.date,
  messageId: $input.item.json.id,
  threadId: $input.item.json.threadId
};

// Clean body text (remove signatures, quotes)
emailData.cleanBody = emailData.body
  .split(/\r?\n-- \r?\n/)[0]  // Remove signature
  .split(/On .+ wrote:/)[0]    // Remove quoted text
  .trim();

// Truncate for API limits (first 1000 chars)
emailData.truncatedBody = emailData.cleanBody.substring(0, 1000);

return {
  json: emailData
};
```

{: .note }
> **Why clean the data?** AI models work better with clean, focused text without signatures or quoted content.

---

## Step 8: AI Classification Node

### Configure the AI Model

1. Add "Basic LLM Chain" node (under AI nodes)
2. Configure initial settings:
   - **Source for Prompt**: "Define below"
   - **Require Specific Output Format**: Toggle ON

3. Close the node temporarily

### Add Chat Model

1. Click the "+" under Chat Model
2. Select "OpenRouter Chat Model"
3. Configure:
   - **Credential**: Choose the OpenRouter credential
   - **Model**: Select "google/gemma-2-9b-it:free"

   ![OpenRouter Configuration](./images/workflow/05-openrouter-config.png)

### Add Output Parser

1. Click the "+" under Output Parser
2. Select "Structured Output Parser"
3. Add this JSON schema:

```json
{
  "priority": "",
  "sentiment": "",
  "department": "",
  "actionRequired": false,
  "confidence": 0.0,
  "reasoning": "Brief explanation"
}
```

### Configure the Prompt

Return to the Basic LLM Chain node and add this prompt:

   ![AI Prompt Setup](./images/workflow/06-ai-prompt-setup.png)

```
Analyze this email and classify it. Return ONLY valid JSON.

Email from: {{$json.senderName}} <{{$json.sender}}>
Subject: {{$json.subject}}
Body: {{$json.truncatedBody}}

Classify as:

1. Priority: "urgent" | "high" | "medium" | "low"
2. Sentiment: "positive" | "neutral" | "negative" | "angry"
3. Department: "sales" | "support" | "technical" | "hr" | "finance" | "other"
4. Action Required: true | false
5. Confidence Score: 0.0-1.0
```

---

## Step 9: Parse AI Response

### Structure the Classification Data

1. Add "Edit Fields" node after Basic LLM Chain
2. Name it: "Parse Classification"

   ![JSON Parser Node](./images/workflow/07-json-parser-node.png)

3. Configure:
   - **Operation**: "Set Fields"
   - **Mode**: "Manual Mapping"

4. Add these field mappings:

**From AI Classification:**

- priority → `={{ $json.priority }}`
- sentiment → `={{ $json.sentiment }}`
- department → `={{ $json.department }}`
- actionRequired → `={{ $json.actionRequired }}` (Type: Boolean)
- confidence → `={{ $json.confidence }}` (Type: Number)
- reasoning → `={{ $json.reasoning }}`

**From Email Data:**

- emailId → `={{ $('Prepare Email for AI').item.json.messageId }}`
- subject → `={{ $('Prepare Email for AI').item.json.subject }}`
- sender → `={{ $('Prepare Email for AI').item.json.sender }}`
- senderName → `={{ $('Prepare Email for AI').item.json.senderName }}`

---

## Step 10: Routing with Switch Node

### Create Decision Tree

1. Add "Switch" node after Parse Classification
2. Name it: "Route by Priority & Sentiment"
3. Configure:
   - **Mode**: "Rules"
   - **Fallback Output**: "Extra Output"

4. Add routing rules:

**Output 1 - Urgent:**

- Condition: `{{ $json.priority }}` equals "urgent"
- Rename Output: "Urgent"

**Output 2 - High Priority:**

- Condition: `{{ $json.priority }}` equals "high"
- Rename Output: "High Priority"

**Output 3 - Angry Customer:**

- Condition: `{{ $json.sentiment }}` equals "angry"
- Rename Output: "Angry Customers"

**Output 4 - Low Priority:**

- Condition: `{{ $json.priority }}` equals "low"
- Rename Output: "Low Priority"

---

## Step 11: Gmail Label Application

### Apply Smart Labels

First, create labels in Gmail:

1. Open Gmail in browser
2. Settings → Labels → Create new labels:
   - URGENT-SUPPORT
   - HIGH-PRIORITY
   - ANGRY-CUSTOMER
   - LOW-PRIORITY
   - STANDARD-PROCESSING

   ![Gmail Label Action](./images/workflow/08-gmail-label-action.png)

Then for each Switch output, add a Gmail node:

**For Urgent Output:**

- Operation: "Label Add"
- Message ID: `{{ $json.emailId }}`
- Labels: Select "URGENT-SUPPORT"

Repeat for other priority levels with appropriate labels.

---

## Step 12: Logging to Google Sheets

### Create Analytics Dashboard

1. Add "Google Sheets" node at the end
2. Connect Google account when prompted
3. Configure:

   ![Google Sheets Node](./images/workflow/09-google-sheets-node.png)

   - **Operation**: "Append"
   - **Document**: Create "Email Classification Log"
   - **Sheet**: "Sheet1"

4. Map data fields:

```json
{
  "Timestamp": "={{new Date().toISOString()}}",
  "Sender": "={{$json.sender}}",
  "Subject": "={{$json.subject}}",
  "Priority": "={{$json.priority}}",
  "Sentiment": "={{$json.sentiment}}",
  "Department": "={{$json.department}}",
  "Action Required": "={{$json.actionRequired}}",
  "Confidence": "={{$json.confidence}}",
  "Reasoning": "={{$json.reasoning}}"
}
```

---

## Workflow Complete

Your complete workflow should look like this:

![Workflow Complete](./images/workflow/10-workflow-complete.png)

### Key Connections

- Gmail Trigger → Prepare Email for AI
- Prepare Email for AI → Basic LLM Chain
- Basic LLM Chain → Parse Classification
- Parse Classification → Switch
- Switch outputs → Individual Gmail nodes
- All paths → Google Sheets logging

---

## Next Steps

Workflow construction complete! You now have:

- ✅ Email trigger configured
- ✅ AI classification implemented
- ✅ Smart routing logic
- ✅ Automated labeling
- ✅ Analytics logging

Continue to [Part C: Testing & Activation →](./part-c-testing)
