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

### The Universal Pattern You're Learning

{: .important }
> **This Isn't Just About Email**: You're learning a fundamental automation archetype: **Intelligent Triage & Routing**. This pattern applies to ANY incoming data stream that needs classification and different handling based on its characteristics.

The pattern has four core components:

1. **Data Ingestion** (Gmail Trigger) → Could be webhooks, forms, APIs, databases
2. **AI Classification** (LLM Chain) → Categorise based on ANY criteria you define
3. **Intelligent Routing** (Switch) → Send different types to different processes
4. **Action & Logging** (Labels/Sheets) → Could be tickets, alerts, workflows, databases

### Real-World Applications of This Pattern

**Customer Support System:**

- **Input**: Support tickets via API
- **Classification**: Bug report, feature request, complaint, praise
- **Actions**: Create Jira ticket, alert product team, route to senior support, send to marketing

**Error Log Monitor:**

- **Input**: Application logs from CloudWatch
- **Classification**: Critical, warning, info, debug
- **Actions**: Page on-call engineer, create incident, log to database, ignore

**Social Media Monitor:**

- **Input**: Twitter/LinkedIn mentions
- **Classification**: Customer complaint, sales lead, PR crisis, positive feedback
- **Actions**: Alert PR team, add to CRM, escalate to legal, share with team

**Document Processing:**

- **Input**: Uploaded invoices/receipts
- **Classification**: Expense type, department, approval needed
- **Actions**: Route for approval, auto-approve small amounts, flag anomalies

{: .note }
> **Why Email?** We use email classification as our example because everyone understands email. But once you grasp this pattern, you can apply it to any data stream in your organisation.

Now we'll build this pattern step-by-step, and you'll see how easily each component can be swapped for your specific use case.

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

{: .note }
> **What's a Trigger?** Triggers are special nodes that start workflows automatically when something happens (like receiving an email). They're different from regular nodes because they "listen" for events rather than processing data.

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

{: .note }
> **Why Use a Code Node?** While n8n has built-in nodes for many tasks, the Code node gives you flexibility to transform data exactly how you need it. It's perfect for cleaning text, extracting specific fields, and preparing data for AI processing.

1. Add "Code" node after Gmail Trigger (click the + on the connection)
2. Name it: "Code" (or "Prepare Email for AI")
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
> **Why clean the data?** AI models work better with clean, focussed text without signatures or quoted content.

---

## Step 8: AI Classification Node

### Configure the AI Model

{: .note }
> **Understanding LLM Chains**: The Basic LLM Chain combines three components: an output parser (to structure the response), a prompt (your instructions), and a language model (the AI). We configure them in this order because defining the output structure first helps write better prompts, and the model selection comes last as it's often interchangeable.

1. Add "Basic LLM Chain" node (under AI nodes)
2. Configure initial settings:
   - **Source for Prompt**: "Define below"
   - **Require Specific Output Format**: Toggle ON

   ![Basic LLM Chain Node](./images/workflow/08-llm-chain-node.png)

3. Now we'll configure the three components in logical order: Output Parser → Prompt → Model

### Step 1: Define Output Structure (Parser)

{: .important }
> **Why Output Parser First?** Structured output is crucial for automation. JSON schemas ensure AI responses are predictable, parseable, and can integrate with databases, APIs, and downstream processes. Without structured output, you'd need complex text parsing that breaks easily.

1. Click the "+" under Output Parser

   ![Output Parser Selection](./images/workflow/12-output-parser-selection.png)

2. Select "Structured Output Parser"
3. Configure the schema:
   - **Schema Type**: Manual
   - **Input Schema**: Add this JSON Schema:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "priority": {
      "type": "string",
      "enum": ["urgent", "high", "medium", "low"]
    },
    "actionRequired": {
      "type": "boolean"
    },
    "confidence": {
      "type": "number"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": ["priority", "actionRequired", "confidence", "reasoning"],
  "additionalProperties": false
}
```

{: .note }
> **Schema Benefits**: This structure guarantees the AI returns data your Switch node can read. The schema acts as a contract between the AI and your workflow, preventing errors from unexpected response formats.

### Step 2: Write the Prompt

Now that we've defined what output we expect, we can write a prompt that produces it.

In the Basic LLM Chain node, enter this prompt in the "Prompt" text field:

{% raw %}

```
Email from: {{ $json.senderName }} <{{ $json.sender }}>
Subject: {{ $json.subject }}
Body: {{ $json.truncatedBody }}

Classify as:
1. Priority: "urgent" | "high" | "medium" | "low"
2. Action Required: true | false
3. Confidence Score: 0.0-1.0
4. Reasoning: Brief explanation of classification
```

{% endraw %}

   ![LLM Chain Prompt](./images/workflow/07-llm-chain-prompt.png)

{: .important }
> **Critical**: Copy this prompt exactly as shown above, including the spaces inside `{{ }}`. These field references pull data from the "Prepare Email for AI" node. The prompt should appear in n8n's interface with the variable references highlighted in a different colour.

{: .tip }
> **Save API Tokens During Development**: After testing the Basic LLM Chain node once, click the pin icon 📌 in the output panel to save the result. This prevents repeated API calls (and token consumption) while you build the rest of your workflow. Remember to unpin before going live!

### Step 3: Select the AI Model

Finally, we choose which AI model will process our prompt.

1. Click the "+" under Chat Model to see available language models

   ![Language Models Menu](./images/workflow/09-language-models-menu.png)

2. Select "OpenRouter Chat Model" from the list
3. Configure:
   - **Credential**: Choose the OpenRouter credential
   - **Model**: Select "google/gemma-3-27b-it:free"

   ![OpenRouter Model Selection](./images/workflow/10-openrouter-model-select.png)

{: .note }
> **Why Model Last?** The beauty of this setup is model flexibility. You can easily swap between GPT-4, Claude, Gemma, or any other model without changing your prompt or output structure. Start with free models for testing, upgrade to premium models for production.

---

## Step 9: First Edit Fields Node

### Extract AI Classification Results

{: .note }
> **Edit Fields Node**: This node extracts and prepares data for routing. We'll create a clean dataset with just the fields we need.

1. Add "Edit Fields" node after Basic LLM Chain
2. Configure:
   - **Assignments Mode**: Manual
   - Add these fields:

{% raw %}

- `priority` → `{{ $json.output.priority }}`  (Type: String)
- `confidence` → `{{ $json.output.confidence }}`  (Type: Number)
- `reasoning` → `{{ $json.output.reasoning }}`  (Type: String)
- `sender` → `{{ $('Prepare Email for AI').item.json.sender }}`  (Type: String)
- `subject` → `{{ $('Prepare Email for AI').item.json.subject }}`  (Type: String)
- `messageId` → `{{ $('Prepare Email for AI').item.json.messageId }}`  (Type: String)
{% endraw %}

---

## Step 10: Routing with Switch Node

### Create Priority-Based Routing

{: .note }
> **Simplified Routing**: We're focusing on the most important emails - urgent and high priority. Everything else goes to standard processing.

1. Add "Switch" node after Edit Fields
2. Name it: "Route by Priority"
3. Configure:
   - **Mode**: "Rules"
   - **Fallback Output**: "Extra Output"

4. Add routing rules:

**Output 1 - Urgent Support:**

{% raw %}

- Left Value: `{{ $json.priority }}`
- Operator: equals
- Right Value: `urgent`
- Rename Output: "Urgent Support"
{% endraw %}

**Output 2 - High Priority:**

{% raw %}

- Left Value: `{{ $json.priority }}`
- Operator: equals
- Right Value: `high`
- Rename Output: "High Priority"
{% endraw %}

---

## Step 11: Gmail Label Application

### Apply Priority Labels

{: .note }
> **Label Strategy**: We'll apply labels to urgent and high-priority emails. Standard emails can use a "No Operation" node to skip labelling.

**Prerequisites - Create Labels in Gmail:**

1. Open Gmail in your browser
2. Click the gear icon → "See all settings"
3. Go to "Labels" tab
4. Create these labels:
   - URGENT-SUPPORT
   - HIGH-PRIORITY

**Configure Gmail Nodes in n8n:**

**For Urgent Support Output:**

1. Add "Gmail" node connected to "Urgent Support" output
2. Name it: "Add label to message"
3. Configure:
   - Operation: "Add Labels"
{% raw %}
   - Message ID: `{{ $('Edit Fields').item.json.messageId }}`
{% endraw %}
   - Labels: Select "URGENT-SUPPORT"

**For High Priority Output:**

1. Add "Gmail" node connected to "High Priority" output
2. Name it: "Add label to message1"
3. Configure:
   - Operation: "Add Labels"
{% raw %}
   - Message ID: `{{ $('Edit Fields').item.json.messageId }}`
{% endraw %}
   - Labels: Select "HIGH-PRIORITY"

**For Fallback (Extra) Output:**

1. Add "No Operation, do nothing" node
2. Connect to the "extra" output
3. This skips labelling for standard emails

---

## Step 12: Second Edit Fields Node

### Consolidate All Data for Logging

{: .note }
> **Data Consolidation**: This second Edit Fields node combines all email metadata with AI classification results before sending to Google Sheets.

1. Add another "Edit Fields" node
2. Name it: "Edit Fields1"
3. Connect both Gmail nodes to this Edit Fields node
4. Configure these field assignments:

{% raw %}
**Core Fields:**

- `messageId` → `{{ $('Edit Fields').item.json.messageId }}`  (Type: String)
- `threadId` → `{{ $json.threadId }}`  (Type: String)
- `receivedDate` → `{{ $('Prepare Email for AI').item.json.receivedDate }}`  (Type: String)
- `sender` → `{{ $('Prepare Email for AI').item.json.sender }}`  (Type: String)
- `senderName` → `{{ $('Prepare Email for AI').item.json.senderName }}`  (Type: String)
- `subject` → `{{ $('Prepare Email for AI').item.json.subject }}`  (Type: String)
- `processed_date` → `{{ DateTime.now().toISO() }}`  (Type: String)

**Classification Fields:**

- `priority` → `{{ $('Edit Fields').item.json.priority }}`  (Type: String)
- `confidence` → `{{ $('Edit Fields').item.json.confidence }}`  (Type: Number)
- `reasoning` → `{{ $('Edit Fields').item.json.reasoning }}`  (Type: String)
{% endraw %}

{: .note }
> **Why Edit Fields?** This node consolidates all data paths from the Switch node into a single stream for Google Sheets. This is crucial for API optimisation - instead of making multiple Google Sheets API calls from different branches, we make just one call per email processed.

---

## Step 13: Logging to Google Sheets

### Create Analytics Dashboard

{: .note }
> **Google Sheets as a Database**: For simple automation projects, Google Sheets acts as a free, visual database. It's perfect for logging, analytics, and sharing data with non-technical stakeholders who are comfortable with spreadsheets.

**First, prepare your Google Sheet:**

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet named "Email Classification Log"
3. In the first row, add these column headers:
   - messageId
   - threadId
   - receivedDate
   - sender
   - senderName
   - subject
   - processed_date
   - priority
   - confidence
   - reasoning

**Then configure the Google Sheets node in n8n:**

1. Add "Google Sheets" node connected to "Edit Fields1" node
2. Name it: "Append or update row in sheet"
3. When prompted, connect your Google account
4. Configure the node:
   - **Operation**: "Append or Update"
   - **Document**: Select "Email Classification Log" from dropdown
   - **Sheet**: "Sheet1"
   - **Columns**:
     - **Mapping Mode**: "Auto-Map Input Data"
     - **Matching Columns**: `messageId` (prevents duplicate entries)
   - The schema will auto-populate from your sheet headers

{: .note }
> **Auto-Mapping**: Since we prepared all fields in the Edit Fields node with matching column names, Google Sheets will automatically map them to the correct columns.

{: .important }
> **API Rate Limits**: Google Sheets has quota limits (300 requests per minute for free accounts). By consolidating all paths through Edit Fields into a single Google Sheets node, we ensure only one API call per email, preventing rate limit errors even during high email volumes.

---

## Step 14: Test & Activate Your Workflow

### Test Your Workflow

1. Click "Test Workflow" button in n8n
2. Send yourself a test email with a clear subject like "URGENT: Test message"
3. Wait for the workflow to execute (it checks Gmail every minute)
4. Verify:
   - The email received the correct Gmail label
   - Data appeared in your Google Sheets log

### Go Live

Once your test succeeds:

1. Toggle the "Active" switch in the top-right corner of the workflow canvas
2. Save the workflow (Ctrl/Cmd + S)

Your workflow is now live and will automatically:

- Check Gmail every minute for new emails
- Classify each email using AI
- Apply appropriate labels
- Log all classifications to Google Sheets

---

## Next Steps

Workflow complete! You've successfully:

- ✅ Built an email classification system
- ✅ Integrated AI for intelligent routing
- ✅ Tested with real emails
- ✅ Activated automatic processing

### What You've Really Learned

More importantly, you've mastered the **Intelligent Triage & Routing** pattern. You now know how to:

1. **Ingest** data from any source (not just email)
2. **Classify** it using AI based on custom criteria
3. **Route** different types to different handling processes
4. **Log** everything for analytics and compliance

{: .highlight }
> **Your Turn**: Think about your work or studies. What repetitive classification task could you automate using this pattern? Customer feedback? Bug reports? Document sorting? The same workflow structure applies - just swap the nodes!

---

## Download Complete Workflow

### Import Pre-Built Template

Save time by importing our complete workflow:

1. Download the workflow JSON file:
   - [📥 Download Email Classification Workflow](./downloads/email-classification-workflow.json)

2. Import into n8n:
   - Open n8n
   - Click "Workflows" → "Import"
   - Select the downloaded JSON file
   - Click "Import"

3. Update credentials:
   - Gmail OAuth2 connection
   - OpenRouter API key
   - Google Sheets OAuth2 connection

4. Update label IDs:
   - Check your Gmail label IDs
   - Update in each Gmail node

{: .warning }
> **Important**: The imported workflow uses placeholder credentials. You must update them with your own before testing.

Ready for more? Try the [Challenge Tasks →](./challenge-tasks)
