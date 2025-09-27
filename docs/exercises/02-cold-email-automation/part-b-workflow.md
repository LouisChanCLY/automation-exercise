---
layout: default
title: "Part B: Build & Test"
parent: "Exercise 2: AI Cold Email Automation"
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

### The Universal Pattern You're Building

{: .important }
> **AI Research & Personalization Pattern**: You're creating a system that researches any subject and generates personalized content. While we use cold emails today, this same structure works for proposals, cover letters, social media outreach, or any research-driven content generation.

The pattern components:

1. **Data Collection** (Form) → Could be API, database, CSV
2. **AI Research** (Perplexity) → Could be Google, internal docs, CRM
3. **Content Generation** (Gemini) → Could be GPT-4, Claude, Llama
4. **Action** (Gmail) → Could be Slack, SMS, API call
5. **Analytics** (Sheets) → Could be database, dashboard, webhook

---

## Step 1: Create Your Workflow Canvas

### Initialize the Workspace

1. Log into your n8n instance
2. Click "Add Workflow"
3. Name it: "AI Cold Email Automation"
4. Click "Create"

{: .note }
> **Canvas Tips**: Use Ctrl/Cmd+S to save frequently. Arrange nodes left-to-right for clarity.

---

## Step 2: Form Trigger Setup

### Create Lead Capture Form

{: .note }
> **What's a Form Trigger?** It creates a web form that anyone can fill out to trigger your workflow. Perfect for collecting data without requiring API knowledge.

1. Add "Form Trigger" node (type "form" in search)
2. Configure the form:
   - **Form Title**: "Lead Information"
   - **Form Description**: "Enter prospect details for personalized outreach"

3. Add form fields by clicking "Add Field":

   **Field 1 - Name:**
   - Label: "Name"
   - Type: Text
   - Required: Yes

   **Field 2 - Company:**
   - Label: "Company"
   - Type: Text
   - Required: No

   **Field 3 - Email:**
   - Label: "Email"
   - Type: Email
   - Required: Yes

   **Field 4 - Context:**
   - Label: "Key Points / Context"
   - Type: Text Area
   - Required: Yes
   - Placeholder: "What's your goal with this outreach?"

4. Click "Save" and copy the form URL from "Production URL"

{: .highlight }
> **Test Your Form**: Open the URL in a browser. You should see your custom form!

---

## Step 3: AI Research Agent

### Configure Perplexity Research

{: .note }
> **Understanding AI Agents**: Unlike basic LLM nodes, agents can use tools autonomously. They decide when and how to search based on your instructions.

1. Add "AI Agent" node
2. Name it: "AI Agent - Research Prospect"
3. Configure:
   - **Type**: "Tools Agent"
   - **Prompt Type**: "Define Below"

4. In the **Prompt** field, enter:

{% raw %}

```
Research the following person/company and find relevant information for a personalized cold email:

Name: {{ $json.Name }}
Company: {{ $json.Company }}
Email: {{ $json.Email }}
Context: {{ $json['Key Points / Context'] }}

Use the Perplexity tool to find:
1. Recent news or achievements about them or their company
2. Their business challenges or interests
3. Common connections or shared interests
4. Any relevant context for personalization

Provide a concise research summary focusing on information useful for email personalization.
```

{% endraw %}

### Add Perplexity Tool

1. Click the "+" under Tools
2. Select "Perplexity" from the list
3. Configure:
   - **Credential**: Select your Perplexity credential
   - **Model**: "sonar" (fast and efficient)
   - **Search Recency**: "month" (recent information)

### Add Language Model

1. Click the "+" under Chat Model
2. Select "Google Gemini Chat Model"
3. Configure:
   - **Credential**: Your Gemini credential
   - **Model**: "gemini-pro" or "gemini-1.5-flash"
   - **Temperature**: 0.7 (balanced creativity)

{: .tip }
> **Pin Output During Development**: After testing once, pin the agent output to save API calls while building the rest of your workflow.

---

## Step 4: Email Generation Agent

### Create Email Crafting Agent

{: .note }
> **Why Two Agents?** Separation of concerns - one agent researches, another writes. This makes each agent better at its specific task and easier to debug.

1. Add another "AI Agent" node
2. Name it: "AI Agent - Craft Email"
3. Configure the prompt:

{% raw %}

```
Based on the research about {{ $('On form submission').item.json.Name }}, create a personalized cold email.

Research findings:
{{ $('AI Agent - Research Prospect').item.json.output }}

Original context: {{ $('On form submission').item.json['Key Points / Context'] }}

Create a cold email that:
1. Opens with a personalized hook based on the research
2. Shows understanding of their situation or interests
3. Presents a clear value proposition
4. Has a specific, low-commitment call-to-action
5. Stays under 150 words
6. Feels genuine and conversational, not templated

Format the output with clear sections for subject, hook, body, and CTA.
```

{% endraw %}

### Add Output Parser for Structure

{: .important }
> **Structured Output**: We need consistent email components for reliable automation. The output parser ensures the AI returns data in the exact format we need.

1. Click "+" under Output Parser
2. Select "Structured Output Parser"
3. Add this JSON schema:

```json
{
  "type": "object",
  "properties": {
    "subject": {
      "type": "string",
      "description": "Compelling subject line under 60 characters"
    },
    "hook": {
      "type": "string",
      "description": "Personalized opening line based on research"
    },
    "body": {
      "type": "string",
      "description": "Main value proposition and context"
    },
    "cta": {
      "type": "string",
      "description": "Specific call-to-action"
    }
  },
  "required": ["subject", "hook", "body", "cta"]
}
```

### Connect Language Model

Use the same Gemini model (it's already configured from the first agent).

---

## Step 5: Gmail Integration

### Send Personalized Emails

{: .note }
> **Email Composition**: We'll combine the AI-generated components into a professional email.

1. Add "Gmail" node
2. Name it: "Send Email via Gmail"
3. Configure:
   - **Operation**: "Send"
   - **Credential**: Your Gmail credential

4. Set email fields using expressions:

{% raw %}

- **To**: `{{ $('On form submission').item.json.Email }}`
- **Subject**: `{{ $json.output.subject }}`
- **Message Type**: "Text" (or HTML for formatting)
- **Message**:

   ```
   {{ $json.output.hook }}

   {{ $json.output.body }}

   {{ $json.output.cta }}

   Best regards,
   [Your Name]
   ```

{% endraw %}

{: .warning }
> **Sender Reputation**: Start with a few test emails. Sudden high volume can trigger spam filters.

---

## Step 6: Metadata Enrichment

### Prepare Data for Logging

{: .note }
> **Why Enrich?** We need to combine data from multiple nodes into a single record for our analytics spreadsheet.

1. Add "Set" node (or "Edit Fields" in newer versions)
2. Name it: "Enrich with Metadata"
3. Add these field assignments:

{% raw %}

```javascript
// Prospect Information
timestamp: {{ new Date().toISOString() }}
prospect_name: {{ $('On form submission').item.json.Name }}
prospect_email: {{ $('On form submission').item.json.Email }}
company: {{ $('On form submission').item.json.Company }}

// Research & Email Content
research_summary: {{ $('AI Agent - Research Prospect').item.json.output }}
email_subject: {{ $('AI Agent - Craft Email').item.json.output.subject }}
email_hook: {{ $('AI Agent - Craft Email').item.json.output.hook }}
email_body: {{ $('AI Agent - Craft Email').item.json.output.body }}
email_cta: {{ $('AI Agent - Craft Email').item.json.output.cta }}

// Workflow Metadata
workflow_id: {{ $execution.id }}
sent_status: "sent"
```

{% endraw %}

---

## Step 7: Analytics Logging

### Track Everything in Sheets

1. Add "Google Sheets" node
2. Name it: "Log to Google Sheets"
3. Configure:
   - **Operation**: "Append"
   - **Credential**: Your Sheets credential
   - **Document**: Select your "Cold Email Tracking" spreadsheet
   - **Sheet**: "Sheet1"
   - **Mapping Mode**: "Auto-map Input Data"

{: .note }
> **Auto-mapping**: Since we named our fields to match the spreadsheet columns, they'll map automatically.

---

## Step 8: Connect the Workflow

### Link All Nodes

Connect nodes in this sequence:

```
Form Trigger → Research Agent → Email Agent → Gmail → Enrich → Sheets
                      ↓                ↓
                 Perplexity Tool   Output Parser
                      ↓                ↓
                 Gemini Model     Gemini Model
```

---

## Step 9: Test & Activate

### Test Your Workflow

1. Click "Test Workflow"
2. Open your form URL
3. Submit test data:
   - Name: "Test User"
   - Company: "Test Company"
   - Email: <your-email@gmail.com>
   - Context: "Testing the automation"

4. Watch the execution:
   - Research agent should find information
   - Email agent should craft personalized content
   - Email should arrive in your inbox
   - Data should appear in Google Sheets

### Troubleshooting

| Issue | Solution |
|-------|----------|
| Research returns generic results | Add more specific search instructions to agent prompt |
| Email too generic | Ensure research data is passing to email agent |
| Gmail fails | Check credentials, verify email address format |
| Sheets not updating | Verify column names match exactly |

### Go Live

Once tested successfully:

1. Toggle "Active" switch
2. Share your form URL with team
3. Monitor Google Sheets for results

{: .highlight }
> **Success!** You've built an AI system that researches and personalizes at scale!

---

## Next Steps

Your workflow is complete! You've successfully:

- ✅ Built an autonomous research agent
- ✅ Created personalized content generation
- ✅ Integrated multiple AI models
- ✅ Automated the entire outreach process

### What You've Really Learned

The **AI Research & Personalization** pattern you've mastered can be applied to:

1. **Job Applications**: Research company → Generate cover letter
2. **Sales Proposals**: Research client → Create proposal
3. **Content Creation**: Research topic → Generate article
4. **Customer Support**: Research issue → Generate solution

{: .tip }
> **Your Turn**: What other use cases can you think of for this pattern?

---

## Download Complete Workflow

### Import Pre-Built Template

Save time with our complete workflow:

[📥 Download Cold Email Workflow](./downloads/cold-email-automation.json){: .btn .btn-primary }

To import:

1. Open n8n
2. Click "Import Workflow"
3. Select the downloaded file
4. Update all credentials
5. Test and activate

Ready for more? Try the [Challenge Tasks →](./challenge-tasks)
