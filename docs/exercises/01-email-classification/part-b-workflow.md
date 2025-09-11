---
layout: default
title: "Part B: Build & Test"
parent: "Exercise 1: Email Classification"
grand_parent: Exercises
nav_order: 3
---

# Part B: Build & Test

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Now we'll build, test, and activate the automation workflow. This section takes about 25 minutes and covers creating nodes, configuring AI classification, testing, and going live.

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

1. Click the plus button in the top right corner to open the nodes panel

   ![Nodes Panel](./images/workflow/03-nodes-panel.png)

2. Search for "Gmail" in the search box

   ![Gmail Trigger Search](./images/workflow/04-gmail-trigger-search.png)

3. Select "On message received" trigger

   ![Gmail Trigger Selection](./images/workflow/05-gmail-trigger-selection.png)

4. Configure trigger settings:
   - **Credential**: Select the credential we created earlier
   - **Poll Time**: Every Minute
   - **Event**: "Message Received"
   - **Simplify Output**: Toggle OFF

   ![Gmail Trigger Configuration](./images/workflow/06-gmail-trigger-config.png)

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

   ![Basic LLM Chain Node](./images/workflow/08-llm-chain-node.png)

3. This node needs three components: Chat Model, Output Parser, and the Prompt (configured below)

### Add Chat Model

1. Click the "+" under Chat Model to see available language models

   ![Language Models Menu](./images/workflow/09-language-models-menu.png)

2. Select "OpenRouter Chat Model" from the list
3. Configure:
   - **Credential**: Choose the OpenRouter credential
   - **Model**: Select "google/gemma-3-27b-it:free"

   ![OpenRouter Model Selection](./images/workflow/10-openrouter-model-select.png)

### Add Output Parser

1. Click the "+" under Output Parser

   ![Output Parser Selection](./images/workflow/12-output-parser-selection.png)

2. Select "Structured Output Parser"
3. Add this JSON schema in the JSON Example field:

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

Return to the Basic LLM Chain node and enter this prompt in the "Prompt" text field (copy and paste exactly):

```
Analyze this email and classify it. Return ONLY valid JSON.

Email from: {{ $json.senderName }} <{{ $json.sender }}>
Subject: {{ $json.subject }}
Body: {{ $json.truncatedBody }}

Classify as:
1. Priority: "urgent" | "high" | "medium" | "low"
2. Sentiment: "positive" | "neutral" | "negative" | "angry"
3. Department: "sales" | "support" | "technical" | "hr" | "finance" | "other"
4. Action Required: true | false
5. Confidence Score: 0.0-1.0
```

   ![LLM Chain Prompt](./images/workflow/07-llm-chain-prompt.png)

{: .important }
> **Critical**: Copy this prompt exactly as shown above, including the spaces inside `{{ }}`. These field references pull data from the "Prepare Email for AI" node. The prompt should appear in n8n's interface with the variable references highlighted in a different colour.

---

## Step 9: Routing with Switch Node

### Create Decision Tree

1. Add "Switch" node after Basic LLM Chain
2. Name it: "Route by Priority & Sentiment"
3. Configure:
   - **Mode**: "Rules"
   - **Fallback Output**: "Extra Output"

   ![Switch Node Outputs](./images/workflow/16-switch-node-outputs.png)

4. Add routing rules by clicking "+ Add Rule" for each output:

**Output 1 - Urgent:**

- Click "+ Add Rule"
- Left Value: `{{ $json.priority }}`
- Operator: equals
- Right Value: `urgent`
- Toggle "Rename Output" ON
- Output Name: "Urgent"

**Output 2 - High Priority:**

- Click "+ Add Rule"
- Left Value: `{{ $json.priority }}`
- Operator: equals
- Right Value: `high`
- Toggle "Rename Output" ON
- Output Name: "High Priority"

**Output 3 - Angry Customer:**

- Click "+ Add Rule"
- Left Value: `{{ $json.sentiment }}`
- Operator: equals
- Right Value: `angry`
- Toggle "Rename Output" ON
- Output Name: "Angry Customers"

**Output 4 - Low Priority:**

- Click "+ Add Rule"
- Left Value: `{{ $json.priority }}`
- Operator: equals
- Right Value: `low`
- Toggle "Rename Output" ON
- Output Name: "Low Priority"

---

## Step 10: Gmail Label Application

### Apply Smart Labels

**Prerequisites - Create Labels in Gmail:**

1. Open Gmail in your browser
2. Click the gear icon → "See all settings"
3. Go to "Labels" tab
4. Create these labels by clicking "Create new label" for each:
   - URGENT-SUPPORT
   - HIGH-PRIORITY
   - ANGRY-CUSTOMER
   - LOW-PRIORITY
   - STANDARD-PROCESSING

**Configure Gmail Nodes in n8n:**

For each Switch output, add a Gmail node:

**For Urgent Output:**

1. Add "Gmail" node connected to the "Urgent" output
2. Configure:
   - Operation: "Label Add"
   - Message ID: `{{ $('Prepare Email for AI').item.json.messageId }}`
   - Labels: Select "URGENT-SUPPORT" from dropdown

**For High Priority Output:**

1. Add "Gmail" node connected to the "High Priority" output
2. Configure:
   - Operation: "Label Add"
   - Message ID: `{{ $('Prepare Email for AI').item.json.messageId }}`
   - Labels: Select "HIGH-PRIORITY" from dropdown

**For Angry Customers Output:**

1. Add "Gmail" node connected to the "Angry Customers" output
2. Configure:
   - Operation: "Label Add"
   - Message ID: `{{ $('Prepare Email for AI').item.json.messageId }}`
   - Labels: Select "ANGRY-CUSTOMER" from dropdown

**For Low Priority Output:**

1. Add "Gmail" node connected to the "Low Priority" output
2. Configure:
   - Operation: "Label Add"
   - Message ID: `{{ $('Prepare Email for AI').item.json.messageId }}`
   - Labels: Select "LOW-PRIORITY" from dropdown

**For Fallback (Extra) Output:**

1. Add "Gmail" node connected to the "extra" output
2. Configure:
   - Operation: "Label Add"
   - Message ID: `{{ $('Prepare Email for AI').item.json.messageId }}`
   - Labels: Select "STANDARD-PROCESSING" from dropdown

---

## Step 11: Logging to Google Sheets

### Create Analytics Dashboard

1. Add "Google Sheets" node at the end of your workflow
2. When prompted, connect your Google account (similar to Gmail OAuth)
3. Configure the node:
   - **Operation**: "Append"
   - **Document**: Select or create "Email Classification Log"
   - **Sheet**: "Sheet1"
   - **Options**: Toggle "Data Property Name" OFF

4. Map data fields by clicking "Add Field" for each:

- **Timestamp**: `={{ new Date().toISOString() }}`
- **Sender**: `={{ $('Prepare Email for AI').item.json.sender }}`
- **Subject**: `={{ $('Prepare Email for AI').item.json.subject }}`
- **Priority**: `={{ $json.priority }}`
- **Sentiment**: `={{ $json.sentiment }}`
- **Department**: `={{ $json.department }}`
- **Action Required**: `={{ $json.actionRequired }}`
- **Confidence**: `={{ $json.confidence }}`
- **Reasoning**: `={{ $json.reasoning }}`

---

## Step 12: Test Your Workflow

### Complete Workflow Overview

Your complete workflow should look like this:


### Run Test

1. Click "Test Workflow" button in n8n

2. Send test emails covering all scenarios:
   - **Urgent support request**: Subject: "URGENT: Server is down!" Body: "Our production server has been down for 2 hours. Need immediate assistance!"
   - **Sales inquiry**: Subject: "Interested in enterprise pricing" Body: "We're looking to purchase licenses for 500 users. Can you send pricing?"
   - **Technical bug report**: Subject: "Bug found in login process" Body: "Users cannot log in with special characters in passwords."
   - **HR policy question**: Subject: "Question about vacation policy" Body: "How many vacation days do new employees get?"
   - **Angry customer complaint**: Subject: "Terrible service!" Body: "I've been waiting 3 days for a response. This is unacceptable!"

3. Monitor the execution:
   - Watch the workflow execute in real-time
   - Click on each node to see the output data
   - Verify the classification results match expectations

### Verify Results

Check that:

- All nodes show green checkmarks (successful execution)
- Gmail labels were applied correctly in your inbox
- Classifications match the email content:
  - Urgent emails → "urgent" priority
  - Complaints → "angry" sentiment
  - Questions → appropriate department routing
- Data appears in Google Sheets with all fields populated
- Confidence scores are reasonable (0.7-1.0 for clear cases)

---

## Step 13: Activate Your Workflow

### Go Live

Once testing is complete:

1. Toggle the "Active" switch in the top-right corner of the workflow canvas

2. Configure workflow settings (click workflow name → Settings):
   - **Execution timeout**: 5 minutes
   - **Retry on failure**: Yes (2 attempts)
   - **Retry wait time**: 5 seconds
   - **Save execution data**: Last 100 runs
   - **Error Workflow**: Optional (for error notifications)

3. Save the workflow (Ctrl/Cmd + S)

Your workflow is now live and will automatically:

- Check Gmail every minute for new emails
- Classify each email using AI
- Apply appropriate labels
- Log all classifications to Google Sheets
- Handle errors gracefully with retries

---

## Next Steps

Workflow complete! You've successfully:

- ✅ Built an email classification system
- ✅ Integrated AI for intelligent routing
- ✅ Tested with real emails
- ✅ Activated automatic processing

Ready for more? Try the [Challenge Tasks →](./challenge-tasks)
