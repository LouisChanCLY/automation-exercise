---
layout: exercise
title: "Exercise 1: Email Classification"
description: Build an AI-powered email automation system
category: foundation
difficulty: beginner
time: 45 minutes
tools: [n8n, Gmail, OpenRouter, Google Sheets]
next: /exercises/02-social-media-monitor/
---

## 🎯 What You'll Build

In this hands-on exercise, you'll create a **smart email classification system** that automatically processes
incoming emails, understands their content using AI, and takes intelligent actions based on the message context.
By the end of this 45-minute session, you'll have a working automation that can:

- 📧 Monitor your Gmail inbox in real-time
- 🤖 Use AI to understand email priority, sentiment, and intent
- 🏷️ Automatically organise emails with smart labels
- 📊 Track all classifications for performance insights
- ⚡ Route urgent matters for immediate attention

## 💡 Why This Exercise Matters

### The Problem We're Solving

The average knowledge worker spends **28% of their workweek** managing email (McKinsey Global Institute).
For a team of 10 people, that's equivalent to having 3 full-time employees just reading and sorting emails.
This exercise teaches you to reclaim that time through intelligent automation.

### Real-World Applications

**Customer Support Teams:**

- Reduce first response time from hours to minutes
- Automatically escalate angry customers to senior agents
- Create support tickets without manual intervention
- Track sentiment trends to identify product issues early

**Sales Organisations:**

- Never miss a hot lead buried in hundreds of emails
- Automatically route enquiries to the right sales rep
- Trigger follow-up sequences based on email intent
- Prioritise high-value opportunities

**HR Departments:**

- Automatically categorise employee queries by urgency
- Route sensitive matters to appropriate personnel
- Track common questions to improve documentation
- Ensure compliance-related emails get immediate attention

**Personal Productivity:**

- Focus on what matters by having AI pre-sort your inbox
- Never miss important deadlines mentioned in emails
- Reduce email anxiety with automated acknowledgements
- Build a searchable database of all email interactions

## 🎓 Learning Outcomes

By completing this exercise, you will:

1. **Master API Integration** - Connect multiple cloud services using OAuth2 authentication
2. **Understand AI Prompting** - Write effective prompts that get consistent results from LLMs
3. **Build Conditional Logic** - Create intelligent routing based on AI classifications
4. **Implement Error Handling** - Ensure your automation runs reliably 24/7
5. **Design User Workflows** - Think systematically about process automation

## 📋 Prerequisites

**Required Skills:**

- Basic understanding of email and web applications
- Ability to follow step-by-step instructions
- No coding experience required (we'll provide all code snippets)

**Required Accounts (all free):**

- Gmail account with 2FA enabled
- Computer with modern web browser
- 45-60 minutes of uninterrupted time

**You DON'T Need:**

- Programming experience
- Technical background
- Paid software licenses
- Command line knowledge

## 🏗️ System Architecture

### High-Level Overview

```mermaid
graph TB
    A[Gmail Inbox] -->|New Email| B[n8n Trigger]
    B --> C[Data Preparation]
    C --> D[AI Classification]
    D --> E{Routing Logic}
    E -->|Urgent| F[Immediate Actions]
    E -->|High Priority| G[Fast Track]
    E -->|Angry Customer| H[De-escalation]
    E -->|Standard| I[Normal Processing]
    F --> J[Apply Labels]
    G --> J
    H --> J
    I --> J
    J --> K[Log to Sheets]
    K --> L[Analytics Dashboard]
```

### Data Flow Explanation

1. **Email Ingestion**: Gmail API polls for new messages every minute
2. **Data Extraction**: Essential fields (sender, subject, body) are extracted and cleaned
3. **AI Processing**: GPT-4o analyses content for priority, sentiment, and routing
4. **Decision Making**: Switch node routes based on classification results
5. **Action Execution**: Labels applied, logs created, notifications sent
6. **Performance Tracking**: All actions logged for continuous improvement

## 🚀 Why We Built It This Way

### Design Decisions Explained

**Why n8n?**

- Visual workflow builder perfect for beginners
- No code required for complex logic
- Free tier sufficient for learning
- Industry-standard tool used by 40,000+ companies

**Why Gmail API instead of IMAP?**

- More reliable and faster than traditional email protocols
- Rich metadata access (labels, threads, etc.)
- Better security through OAuth2
- Real-time webhook capabilities (for production)

**Why OpenRouter for AI?**

- Access to multiple AI models through one API
- Free tier includes powerful models
- No credit card required to start
- Fallback options if one model fails

**Why Google Sheets for logging?**

- Zero setup database
- Easy to share and visualise
- Familiar interface for non-technical users
- Free and reliable

## 📊 Success Metrics

After implementing this system, you should see:

- ⏱️ **90% reduction** in email triage time
- 🎯 **95% accuracy** in priority classification
- 😊 **Improved team morale** from reduced email overwhelm
- 📈 **Data-driven insights** into communication patterns
- 🚀 **Faster response times** for urgent matters

## ⚠️ Common Pitfalls to Avoid

1. **Over-engineering the prompt** - Start simple, iterate based on results
2. **Ignoring rate limits** - Plan for API quotas from day one
3. **Skipping error handling** - Build resilience from the start
4. **Not testing edge cases** - What happens with empty emails or attachments?
5. **Forgetting about privacy** - Never log sensitive information

---

## Detailed Implementation

### Phase 1: Core Components Setup

#### Gmail Trigger Configuration

**What We're Building:**
A reliable email monitoring system that checks for new messages every minute without overwhelming your Gmail API quota.

**Technical Details:**

- **OAuth2 Authentication**: Secure token-based access (no password storage)
- **Polling Frequency**: Every 60 seconds (optimal for free tier)
- **Smart Filtering**: Process only unread messages to avoid duplicates
- **Error Recovery**: Automatic retry on temporary failures

#### AI Classification Engine

**What We're Building:**
An intelligent classification system that understands context, not just keywords.

**Classification Dimensions:**

1. **Priority Classification** (Low/Medium/High/Urgent)
   - Urgent: Contains deadlines < 24 hours, critical keywords, VIP senders
   - High: Important but not time-critical, key stakeholders
   - Medium: Regular business matters, standard requests
   - Low: FYI, newsletters, non-actionable content

2. **Sentiment Analysis** (Positive/Neutral/Negative/Angry)
   - Positive: Praise, satisfaction, enthusiasm
   - Neutral: Factual, informational, procedural
   - Negative: Complaints, concerns, dissatisfaction
   - Angry: Strong language, threats, escalation needed

3. **Department Routing** (Sales/Support/Technical/HR/Finance/Other)
   - Sales: Pricing enquiries, demos, purchasing intent
   - Support: Help requests, bug reports, how-to questions
   - Technical: API issues, integration questions, feature requests
   - HR: Employment queries, policy questions, complaints
   - Finance: Invoicing, payments, billing issues

**The AI Prompt Strategy:**

```json
{
  "prompt": "You are an expert email classifier. Analyse this email and return ONLY valid JSON.",
  "criteria": {
    "priority": "Consider deadlines, sender importance, and action requirements",
    "sentiment": "Detect emotional tone beyond just positive/negative",
    "department": "Match content to most appropriate team",
    "confidence": "Rate your certainty (0.0-1.0)"
  },
  "instruction": "Be consistent and objective. When uncertain, choose the safest option."
}
```

#### Intelligent Routing Logic

**What We're Building:**
A decision tree that takes different actions based on email characteristics.

**Routing Rules Matrix:**

| Classification | Primary Action | Secondary Action | SLA |
|---------------|---------------|------------------|-----|
| Urgent + Angry | Immediate escalation | Manager notification | 15 min |
| Urgent + Any | Priority queue | Slack alert | 1 hour |
| High + Support | Create ticket | Assign to team | 4 hours |
| High + Sales | Add to CRM | Sales team notify | Same day |
| Angry + Any | De-escalation template | Senior staff alert | 30 min |
| Low + Any | Batch processing | Weekly digest | 1 week |

**Why This Routing Strategy:**

- Prevents important emails from being buried
- Ensures angry customers get immediate attention
- Optimises team workload distribution
- Creates audit trail for compliance

#### Automated Response System

**What We're Building:**
Multi-channel response system that acknowledges, tracks, and escalates appropriately.

**Response Actions by Priority:**

1. **Gmail Label System**
   - Visual inbox organisation
   - Quick filtering for manual review
   - Colour coding for at-a-glance priority

2. **Auto-Acknowledgements** (Support & Urgent only)
   - Confirms receipt within 60 seconds
   - Sets expectations for response time
   - Provides ticket number for tracking

3. **Calendar Integration** (Urgent items)
   - Creates follow-up reminders
   - Blocks time for important responses
   - Syncs with team calendars

4. **Performance Analytics**
   - Every classification logged with timestamp
   - Confidence scores tracked for model improvement
   - Response time metrics calculated automatically
   - Weekly reports on classification accuracy

---

## Complete Walkthrough

### Part A: Environment Setup (15 minutes)

#### Step 1: n8n Account Setup

1. Navigate to [n8n.io](https://n8n.io)
2. Click "Get started for free"
3. Create account with email verification
4. Choose workspace name (e.g., "ai-automation-course")
5. Select the "Starter" plan for this exercise

> ✅ **Checkpoint**: You should see the n8n workflow canvas

#### Step 2: OpenRouter API Setup

1. Open new tab: [openrouter.ai](https://openrouter.ai)
2. Sign up using Google/GitHub authentication
3. Navigate to "API Keys" in dashboard
4. Click "Create New Key"
5. Name it: "n8n-email-classifier"
6. **Important**: Copy and save the API key immediately (shown only once)

> ✅ **Checkpoint**: API key saved securely

#### Step 3: Gmail API Configuration

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project: "n8n-email-automation"
3. Enable Gmail API:
   - Search "Gmail API" in library
   - Click "Enable"

Step 4: Connect n8n with Gmail API:
Create a new Credential in n8n

Select Gmail OAuth2 API

Copy the OAuth Redirect URL

Go back to Google Cloud Console to Create credentials:

Go to "Credentials" → "Create Credentials" → "OAuth Client ID"
Application type: "Web application"
Name: "n8n Gmail Integration"
Authorized redirect URIs: paste the OAuth Redirect URL from earlier

Copy Client ID and Client Secret back into the n8n Credential page
Click Sign in with Google to connect n8n with Gmail API

If prompted “Google hasn’t verified this app”, click “Show Advanced” and click “Go to … …”

Click “Select all”

Once connected, it should show this:

✓ Checkpoint: OAuth2 credentials ready, Gmail API enabled

Part B: Workflow Construction (20 minutes)
Step 5: Create a new Workflow

Rename to n8n Email Automation
Step 6: Gmail Trigger Setup

In n8n, click the plus button in the top right corner
Search “Gmail”

Click “Gmail” and select “On message received” trigger

Configure trigger:
Credential: select the credential we created earlier
Poll Time: Every Minute
Event: "Message Received"
Simplify Output: Toggle OFF

Test: Click “Fetch Test Event” -
Test: Click "Listen for Event" - send test email to yourself

Step 7: Email Data Preparation

Add "Code" node after Gmail Trigger
Name it: "Prepare Email for AI"
Mode: “Run Once for Each Item”
Language: “Javascript”
Add this code:

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
  .split[/\r?\n-- \r?\n/](0)  // Remove signature
  .split[/On .+ wrote:/](0)    // Remove quoted text
  .trim();

// Truncate for API limits (first 1000 chars)
emailData.truncatedBody = emailData.cleanBody.substring(0, 1000);

return {
  json: emailData
};

Step 8: AI Classification Node

Add "Basic LLM Chain" node (under AI nodes)
Source for Prompt: “Define below”
Require Specific Output Format: toggle ON

Close the node. We will now add the Chat Model, and the Output Parser.

Click the “+” under Chat Model
Pick OpenRouter Chat Model

In the Openrouter node, choose the credentials we created earlier.
Scroll down to select “google/gemma-3-27b-it:free”

Click the “+” under Output Parser

Click Structured Output Parser
Put the following content as the JSON Example

{
  "priority": "",
  "sentiment": "",
  "department": "",
  "actionRequired": false,
  "confidence": 0.0,
  "reasoning": "Brief explanation"
}

Go back to the Basic LLM Chain node. Now, add the Prompt:

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

Step 9: Parse AI Response

Add "Edit Fields" node after Basic LLM Chain
 Name it: "Parse Classification"
 Operation: "Set Fields"
 Mode: "Manual Mapping"
Configure the following field assignments:
From the AI Classification (Basic LLM Chain output):
priority → ={{ $json.priority }}
sentiment → ={{ $json.sentiment }}
department → ={{ $json.department }}
actionRequired → ={{ $json.actionRequired }} (Type: Boolean)
confidence → ={{ $json.confidence }} (Type: Number)
reasoning → ={{ $json.reasoning }}
From the Email Data (Prepare Email for AI node):
emailId → ={{ $('Prepare Email for AI').item.json.messageId }}
subject → ={{ $('Prepare Email for AI').item.json.subject }}
sender → ={{ $('Prepare Email for AI').item.json.sender }}
senderName → ={{ $('Prepare Email for AI').item.json.senderName }}
Additional fields for error handling:
error → ={{ $json.error ? true : false }} (Type: Boolean)
This Edit Fields node will:
Extract the classification results from the Basic LLM Chain's structured output
Combine them with the original email data from the "Prepare Email for AI" node
Create a clean, unified data structure for the Switch node to use
The key difference from your example is that:
The Basic LLM Chain with Structured Output Parser outputs directly to $json (not $json.output)
We're adding the department field which was missing
We're using the correct node reference syntax $('Prepare Email for AI').item.json.fieldName

Step 10: Routing with Switch Node

Add "Switch" node
 Name it: "Route by Priority & Sentiment"
 Mode: "Rules"
 Options: Set "Fallback Output" to "extra"
Configure routing rules:
Output 1 - Urgent:
Conditions:
Priority equals "urgent"
Rename Output: Toggle ON
Output Name: "Urgent"
Output 2 - High Priority:
Conditions:
Priority equals "high"
Rename Output: Toggle ON
Output Name: "High Priority"
Output 3 - Angry Email:
Conditions:
Sentiment equals "angry"
Rename Output: Toggle ON
Output Name: "Angry Customers"
Output 4 - Low Priority:
Conditions:
Priority equals "low"
Rename Output: Toggle ON
Output Name: "Low Priority"
The fallback output (automatically created as "extra") will catch all medium priority and neutral sentiment emails.
How to add conditions in the Switch node:
Click "+ Add Rule" for each output
For each rule:
Set the Left Value to the field (e.g., {{ $json.priority }})
Choose the operator (equals)
Set the Right Value (e.g., "urgent")
Toggle "Rename Output" and give each output a descriptive name
The "extra" output will automatically handle any emails that don't match the rules
This simplified routing ensures:
Urgent emails get immediate attention
High-priority emails are fast-tracked
Angry customers get special handling
Low priority emails can be batched
Everything else (medium priority, neutral sentiment) follows standard processing

Step 11: Gmail Label Application

Creating Labels in Gmail (Prerequisites)
Open Gmail in your browser
Click the gear icon → "See all settings"
Go to "Labels" tab
Create these labels:
URGENT-SUPPORT
HIGH-PRIORITY
ANGRY-CUSTOMER
LOW-PRIORITY
STANDARD-PROCESSING
Configuring Gmail Nodes
For Urgent Output:
Operation: "Label Add"
Message ID: {{ $json.emailId }}
Labels: Select "URGENT-SUPPORT"
Now repeat the same for other labels
Real-World Impact
For Support Teams:
Urgent labels integrate with helpdesk software
Automatic ticket creation for high-priority items
SLA tracking becomes automated
For Sales Teams:
Hot leads are never missed
Follow-up reminders can be triggered
Response time metrics improve dramatically
For Management:
Real-time visibility into email volumes by priority
Can identify training needs (too many angry customers?)
Data-driven decisions about staffing

Step 12: Logging to Google Sheets

Add "Google Sheets" node at the end
Connect Google account
Configure:

Operation: "Append"
Document: Create "Email Classification Log"
Sheet: "Sheet1"
Data:

json{
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
Part C: Testing & Optimization (10 minutes)

Step 13: Comprehensive Testing

Send test emails covering all scenarios:

Urgent support request
Sales inquiry
Technical bug report
HR policy question
Angry customer complaint

Monitor execution:

Check execution history
Verify correct classification
Confirm labels applied
Review Google Sheets log

Step 14: Error Handling
Add error workflow:

Create "Error Workflow" in settings
Add Slack/Email notification for failures
Log errors to separate sheet

🏆 Challenge Tasks (If Completed Early)
Challenge 1: Multi-Language Support (15 min)
Objective: Enhance classifier to handle non-English emails
Requirements:

Detect email language using GPT-4o
Translate if needed before classification
Maintain original language in logs
Apply language-specific labels

Implementation hints:
javascript// Add to prompt:
"First, detect the language. If not English, translate before classifying.
Include detected language in response as 'detectedLanguage' field."

Challenge 2: Smart Auto-Reply System (20 min)
Objective: Generate contextual auto-replies for certain classifications
Requirements:

For "urgent + support" → Generate empathetic acknowledgment
For "sales + positive" → Generate enthusiastic follow-up
For "angry + any" → Generate de-escalation response
Save drafts in Gmail, don't auto-send

Advanced features:

Use sender history for personalization
Include relevant KB articles for support
Schedule follow-ups for sales leads
Escalation paths for angry customers

Challenge 3: Intelligent Thread Analysis (25 min)
Objective: Analyze entire email threads for context
Requirements:

Fetch full thread history using threadId
Analyze conversation progression
Detect escalation patterns
Identify resolution status
Generate thread summary

Key metrics to track:

Response time patterns
Sentiment evolution
Topic drift detection
Resolution indicators

Challenge 4: Advanced Analytics Dashboard (30 min)
Objective: Create real-time classification analytics
Requirements:

Connect to visualization tool (e.g., Retool)
Track classification distributions
Monitor AI confidence scores
Identify classification drift
Alert on unusual patterns

Visualizations needed:

Priority distribution pie chart
Sentiment trends over time
Department workload heatmap
Confidence score histogram
Error rate tracking

Questions anticipated
Technical Challenges

OAuth2 Confusion

"Why is the redirect URI failing?"
"What scopes do I actually need?"
"How do I refresh expired tokens?"

API Key Management

"Where do I store the OpenRouter API key in n8n?"
"How do I test without burning through credits?"
"What's the difference between test and production keys?"

JSON Parsing Issues

"Why isn't the Switch node recognizing my AI output?"
"How do I handle malformed JSON responses?"
"What's the correct JSONPath expression?"

Gmail API Limits

"Why am I hitting rate limits?"
"How many emails can I process per day?"
"What happens when quota is exceeded?"
