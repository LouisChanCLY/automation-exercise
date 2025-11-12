---
layout: default
title: "Part B: Build & Test"
parent: "Exercise 4: Connecting Workflows"
grand_parent: Exercises
nav_order: 3
---

# Part B: Build & Test Workflows

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

In this section, you'll build three interconnected workflows that work together to create an intelligent email response system.

**Time**: 55 minutes

**What You'll Build**:

1. Email Classifier Workflow (15 min)
2. Response Generator Workflow (15 min)
3. Master Orchestrator Workflow (20 min)
4. End-to-End Testing (5 min)

---

## Workflow 1: Email Classifier

### Purpose

This workflow categorizes incoming emails into types (support, sales, general inquiry) and assigns priority levels.

### Workflow Components

| Node Type | Purpose | Configuration |
|-----------|---------|---------------|
| **Form Trigger** | Test interface for standalone use | Fields: Email Subject, Email Body, Sender Email |
| **Execute Workflow Trigger** | Receives data from master workflow | Inputs: email_subject, email_body, email_sender |
| **AI Agent** | Classifies email into categories | Classification prompt, returns category/priority/sentiment |
| **Code (Parse Output)** | Extract structured classification | Parse JSON from AI output, handle errors gracefully |

### Build Steps

#### Step 1: Create New Workflow

1. Click **"+ Add workflow"** in n8n
2. Name it: `Email Classifier`
3. Save the workflow

#### Step 2: Add Form Trigger (For Testing)

{: .note }
> **Development Best Practice**: Always add a Form Trigger for testing sub-workflows independently. This lets you test the classifier without needing the master workflow running.

1. Click **"+"** to add a node
2. Search for **"Form Trigger"**
3. Select **"Form Trigger"**
4. Configure:
   - **Form Title**: `Email Classification Test`
   - **Form Description**: `Test email classification`
   - **Form Fields**:
     - Field 1:
       - **Field Label**: `Email Subject`
       - **Field Type**: `Text`
       - **Required**: Yes
     - Field 2:
       - **Field Label**: `Email Body`
       - **Field Type**: `Textarea`
       - **Required**: Yes
     - Field 3:
       - **Field Label**: `Sender Email`
       - **Field Type**: `Email`
       - **Required**: Yes
   - **Response Mode**: `Last Node`

5. Copy the **Test URL** for later testing

#### Step 3: Add Execute Workflow Trigger (For Master Workflow)

{: .highlight }
> **Workflow Orchestration Pattern**: The Execute Workflow Trigger allows other workflows to call this one like a function. It receives typed inputs and returns structured outputs, enabling modular, reusable workflow design.

1. Click **"+"** to add a node
2. Search for **"Execute Workflow Trigger"**
3. Select **"When Executed by Another Workflow"**
4. Configure:
   - **Workflow Inputs**:
     - Input 1:
       - **Name**: `email_subject`
     - Input 2:
       - **Name**: `email_body`
     - Input 3:
       - **Name**: `email_sender`

5. Note: This trigger will receive data when the master workflow calls this workflow

{: .tip }
> **Dual Trigger Pattern**: Both triggers coexist in the same workflow, but only ONE activates per execution:
>
> - **Form Trigger**: Activates when you access the test form URL (for development)
> - **Execute Workflow Trigger**: Activates when called by the master workflow (for production)
>
> This pattern gives you the best of both worlds: easy testing AND production integration.

#### Step 4: Add AI Classification Node

### Add and Connect the Node

{: .note }
> **Smart Field Mapping**: Notice the expression pattern `{{ $json['Email Subject'] || $json.email_subject }}`. This handles both triggers elegantly:
>
> - Form Trigger outputs: `Email Subject`, `Email Body`, `Sender Email` (with spaces)
> - Execute Workflow Trigger outputs: `email_subject`, `email_body`, `email_sender` (without spaces)
>
> The `||` (OR) operator tries the first format, then falls back to the second. This makes your workflow work with BOTH triggers without duplicating logic.

1. Add **"AI Agent"** node to your canvas
2. **Connect it**: Drag a connection line from **either trigger** to this new node (both triggers connect to the same downstream nodes)
3. Name it: `AI Agent - Classify Email`

### Configure the Node

1. Configure:
   - **Prompt Type**: `Define below`
   - **Text**:

   ```
   You are an email classification expert. Analyze the following email and classify it.

   Email Subject: {{ $json['Email Subject'] || $json.email_subject }}
   Email Body: {{ $json['Email Body'] || $json.email_body }}
   Sender: {{ $json['Sender Email'] || $json.email_sender }}

   Classify this email into one of these categories:
   - support: Technical issues, account problems, how-to questions
   - sales: Product inquiries, pricing questions, purchase interest
   - general: General questions, feedback, other topics

   Also determine:
   - Priority: high (urgent/angry), medium (normal), low (casual inquiry)
   - Sentiment: positive, neutral, negative

   Respond with ONLY valid JSON in this exact format:
   {
     "category": "support",
     "priority": "high",
     "sentiment": "negative"
   }
   ```

3. Connect **Google Gemini Model** to the AI Agent:
   - Click the **connection dot** on the right side of AI Agent
   - Select **"Google Gemini Chat Model"**
   - Configure:
     - **Credential**: Select your Gemini API credential
     - **Model**: `gemini-2.5-flash`

#### Step 5: Parse and Format Output

### Add and Connect the Node

{: .note }
> **Handling AI Variability**: AI models sometimes add extra text before/after JSON, or occasionally fail to produce valid JSON. This parsing node:
>
> 1. Extracts JSON even when surrounded by text
> 2. Provides sensible fallback values if parsing fails
> 3. Returns clean, predictable data structure for downstream nodes
>
> This defensive programming pattern prevents your automation from breaking when AI output varies.

1. Add **"Code"** node to your canvas
2. **Connect it**: Drag a connection line from **AI Agent** to this new node
3. Name it: `Parse Classification`

### Configure the Node

1. Configure:
   - **Mode**: `Run Once for All Items`
   - **Language**: `JavaScript`
   - **Code**:

   ```javascript
   // Parse the AI output to extract JSON
   const aiOutput = items[0].json.output;

   // Try to extract JSON from the output
   let classification;
   try {
     // Look for JSON in the output
     const jsonMatch = aiOutput.match(/\{[\s\S]*\}/);
     if (jsonMatch) {
       classification = JSON.parse(jsonMatch[0]);
     } else {
       // Fallback if no JSON found
       classification = {
         category: "general",
         priority: "medium",
         sentiment: "neutral"
       };
     }
   } catch (error) {
     // Fallback on error
     classification = {
       category: "general",
       priority: "medium",
       sentiment: "neutral"
     };
   }

   return [{
     json: {
       category: classification.category,
       priority: classification.priority,
       sentiment: classification.sentiment,
       timestamp: new Date().toISOString()
     }
   }];
   ```

#### Step 6: Save and Activate

1. Click **"Save"** button
2. Click **"Active"** toggle to activate the workflow
3. Note the workflow URL or ID (you'll need this for the master workflow)

### Test the Classifier

1. Open the Form Trigger test URL
2. Submit test data:
   - **Email Subject**: `Can't login to my account`
   - **Email Body**: `I've been trying to log in for the past hour but keep getting an error message. This is urgent as I need to access my account for work.`
   - **Sender Email**: `frustrated.user@example.com`

3. Expected output:

   ```json
   {
     "category": "support",
     "priority": "high",
     "sentiment": "negative"
   }
   ```

---

## Workflow 2: Response Generator (LLM-as-a-Judge)

### Purpose

This workflow generates high-quality email responses using the LLM-as-a-judge pattern from Exercise 3.

### Workflow Components

| Node Type | Purpose | Configuration |
|-----------|---------|---------------|
| **Form Trigger** | Test interface for standalone use | Fields: Task Description, Instructions, Success Criteria |
| **Execute Workflow Trigger** | Receives task from master workflow | Inputs: Task Description, Instructions, Success Criteria |
| **Set (Initialize)** | Set up loop counters and tracking | retry_count, max_retries (10), previous_feedback |
| **AI Agent (Generator)** | Create response content | Dynamic prompt incorporating task and feedback |
| **AI Agent (Judge)** | Evaluate response quality | Structured output: {passed: boolean, feedback: string} |
| **IF (Check Pass)** | Quality gate decision | If evaluation_result = true |
| **Set (Increment Retry)** | Update loop variables | retry_count++, store previous_feedback |
| **IF (Max Retries)** | Loop control | If retry_count >= max_retries |
| **Set (Mark Status)** | Set final status | status: "success" or "failed" |

### Build Steps

{: .note }
> **Exercise Focus**: This exercise teaches workflow orchestration, not the LLM-as-judge pattern (which you learned in Exercise 3).

#### Build from Exercise 3 Guide

Follow the [Exercise 3 Build Guide](../03-llm-as-judge/part-b-workflow) to build this workflow with these requirements:

1. Create workflow with **Form Trigger**
2. Add **Execute Workflow Trigger** with inputs:
   - `Task Description`
   - `How to Do It (Instructions)`
   - `Success Criteria (How to Measure)`
3. Add initialization node for variables (retry_count, max_retries, previous_feedback)
4. Add AI Generator agent
5. Add AI Judge agent with structured output parser
6. Add loop logic with retry counter and max retries check
7. Return final output

{: .highlight }
> **Time-Saving Alternative**: If you've already completed Exercise 3, you can duplicate that workflow:
>
> 1. Go to Exercise 3 workflow in n8n
> 2. Click **"..."** menu → **"Duplicate"**
> 3. Rename to: `Email Response Generator`
> 4. Verify it has both triggers (Form + Execute Workflow)
>
> This saves time whilst letting you focus on learning workflow orchestration in the master workflow.

### Test the Response Generator

1. Open the Form Trigger test URL (or test with Execute Workflow in another workflow)
2. Submit test data:
   - **Task Description**: `Write a response to a customer who can't log in`
   - **How to Do It**: `Write a professional, empathetic email that:
     1. Acknowledges the frustration
     2. Provides 3 troubleshooting steps
     3. Offers direct support contact if steps don't work
     4. Keep it under 150 words`
   - **Success Criteria**: `Must include:
     - Empathetic opening
     - Exactly 3 numbered troubleshooting steps
     - Support contact information
     - Professional yet friendly tone
     - 100-150 words
     - No spelling errors`

3. Wait for the workflow to complete (may take 10-30 seconds)
4. Expected output:

   ```json
   {
     "status": "success",
     "output": "Dear Customer,\n\nI understand how frustrating...",
     "evaluation_result": true,
     "retry_count": 2
   }
   ```

---

## Workflow 3: Master Email Orchestrator

### Purpose

This is the main workflow that ties everything together. It fetches emails, calls the classifier, calls the response generator, and sends replies.

### Workflow Components

| Node Type | Purpose | Configuration |
|-----------|---------|---------------|
| **Gmail Trigger** | Monitor inbox for new emails | Event: New Email, Poll interval: every minute |
| **Set (Extract Data)** | Extract email fields | subject, body_plain, sender, message_id, thread_id |
| **Execute Workflow (Classifier)** | Call email classification workflow | Pass: email_subject, email_body, email_sender |
| **Code (Prepare Instructions)** | Build response instructions | Create task, instructions, criteria based on category |
| **Execute Workflow (Generator)** | Call response generation workflow | Pass: Task Description, Instructions, Success Criteria |
| **Set (Format Reply)** | Format final email reply | Extract: reply_text, subject, to, quality_status |
| **IF (Quality Check)** | Verify response passed quality gate | If quality_status = "success" |
| **Gmail (Send Reply)** | Send automated response | Send to original sender in same thread |
| **Notification Node** | Alert on failed quality check | Notify for manual review when quality fails |

### Build Steps

#### Step 1: Create New Workflow

1. Click **"+ Add workflow"** in n8n
2. Name it: `Master Email Orchestrator`
3. Save the workflow

#### Step 2: Add Gmail Trigger

{: .highlight }
> **Polling Triggers**: The Gmail Trigger polls your inbox every minute for new emails. When it detects new messages, it starts the workflow for each email. This polling approach works reliably without needing complex webhook setup, making it perfect for learning and prototyping.

1. Add **"Gmail Trigger"** node to your canvas
2. Configure:
   - **Trigger On**: `New Email`
   - **Credential**: Select your Gmail OAuth2 credential
   - **Event**: `Message Received`
   - **Label Names or IDs**: Leave empty (or specify a label like "Auto-Respond")
   - **Simple**: Toggle ON

#### Step 3: Extract Email Data

### Add and Connect the Node

{: .note }
> **Data Shaping**: Gmail returns complex email objects with many fields. This Set node extracts only the essential fields we need, making downstream nodes simpler and data flow clearer. It's like defining a clean API contract between workflow stages.

1. Add **"Set"** node to your canvas
2. **Connect it**: Drag a connection line from **Gmail Trigger** to this new node
3. Name it: `Extract Email Data`

### Configure the Node

1. Configure to extract and format email data:
   - **Assignments**:
     - Assignment 1:
       - **Name**: `subject`
       - **Value**: `={{ $json.subject }}`
     - Assignment 2:
       - **Name**: `body_plain`
       - **Value**: `={{ $json.plainContent || $json.snippet }}`
     - Assignment 3:
       - **Name**: `sender`
       - **Value**: `={{ $json.from }}`
     - Assignment 4:
       - **Name**: `message_id`
       - **Value**: `={{ $json.messageId }}`
     - Assignment 5:
       - **Name**: `thread_id`
       - **Value**: `={{ $json.threadId }}`

#### Step 4: Call Email Classifier Workflow

### Add and Connect the Node

{: .highlight }
> **Workflow Orchestration**: This is where the magic happens! The Execute Workflow node calls your Email Classifier workflow like a function call in programming. Data flows from this "parent" workflow to the "child" workflow, which processes it and returns results. This pattern lets you build complex systems from simple, testable components.

1. Add **"Execute Workflow"** node to your canvas
2. **Connect it**: Drag a connection line from **Extract Email Data** to this new node
3. Name it: `Call Classifier`

### Configure the Node

1. Configure:
   - **Source**: `Database`
   - **Workflow**: Select `Email Classifier` workflow
   - **Workflow Inputs**:
     - Input 1:
       - **Name**: `email_subject`
       - **Value**: `={{ $json.subject }}`
     - Input 2:
       - **Name**: `email_body`
       - **Value**: `={{ $json.body_plain }}`
     - Input 3:
       - **Name**: `email_sender`
       - **Value**: `={{ $json.sender }}`

3. **Test this step**: Click "Test step" to verify the classifier is called and returns classification data

#### Step 5: Prepare Response Generation Instructions

### Add and Connect the Node

{: .note }
> **Dynamic Prompt Engineering**: Instead of static instructions, this node generates different prompts based on the email classification. Support emails get troubleshooting-focused instructions, sales emails get benefit-focused instructions. This contextual adaptation produces higher-quality, more appropriate responses.

1. Add **"Code"** node to your canvas
2. **Connect it**: Drag a connection line from **Call Classifier** to this new node
3. Name it: `Prepare Response Instructions`

### Configure the Node

1. Configure:
   - **Mode**: `Run Once for All Items`
   - **Language**: `JavaScript`
   - **Code**:

   ```javascript
   // Get classification results
   const category = items[0].json.category;
   const priority = items[0].json.priority;
   const sentiment = items[0].json.sentiment;

   // Get original email data (from Extract Email Data node)
   const originalEmail = {
     subject: $('Extract Email Data').item.json.subject,
     body: $('Extract Email Data').item.json.body_plain,
     sender: $('Extract Email Data').item.json.sender
   };

   // Define response instructions based on category
   let taskDescription, instructions, successCriteria;

   if (category === "support") {
     taskDescription = `Write a helpful support response to this email:

       Subject: ${originalEmail.subject}
       Body: ${originalEmail.body}

       The customer seems ${sentiment} and this is ${priority} priority.`;

     instructions = `Write a professional support email that:
       1. Acknowledges the issue empathetically
       2. Provides clear troubleshooting steps or solution
       3. Offers additional support contact if needed
       4. Maintains a helpful, professional tone
       5. Keep it concise (150-250 words)`;

     successCriteria = `The response must:
       - Start with empathetic acknowledgment
       - Provide actionable troubleshooting steps (numbered list)
       - Include support contact information
       - Be 150-250 words
       - Have professional yet friendly tone
       - Be grammatically perfect`;

   } else if (category === "sales") {
     taskDescription = `Write a sales response to this inquiry:

       Subject: ${originalEmail.subject}
       Body: ${originalEmail.body}

       The prospect seems ${sentiment}.`;

     instructions = `Write a sales email that:
       1. Thanks them for their interest
       2. Highlights key product benefits relevant to their inquiry
       3. Provides next steps (demo, call, more info)
       4. Includes clear call-to-action
       5. Keep it persuasive but not pushy (150-250 words)`;

     successCriteria = `The response must:
       - Thank the prospect warmly
       - Mention at least 2 specific product benefits
       - Include clear next step / call-to-action
       - Be 150-250 words
       - Sound enthusiastic but professional
       - Be grammatically perfect`;

   } else {
     // general
     taskDescription = `Write a general response to this email:

       Subject: ${originalEmail.subject}
       Body: ${originalEmail.body}`;

     instructions = `Write a professional email that:
       1. Acknowledges their message
       2. Addresses their question or provides relevant information
       3. Offers to help further if needed
       4. Maintains a friendly, professional tone
       5. Keep it concise (100-200 words)`;

     successCriteria = `The response must:
       - Acknowledge their message
       - Provide helpful information
       - Sound professional yet friendly
       - Be 100-200 words
       - Be grammatically perfect`;
   }

   return [{
     json: {
       taskDescription,
       instructions,
       successCriteria,
       category,
       priority,
       sentiment,
       originalSubject: originalEmail.subject,
       originalSender: originalEmail.sender
     }
   }];
   ```

#### Step 6: Call Response Generator Workflow

### Add and Connect the Node

1. Add **"Execute Workflow"** node to your canvas
2. **Connect it**: Drag a connection line from **Prepare Response Instructions** to this new node
3. Name it: `Call Response Generator`

### Configure the Node

1. Configure:
   - **Source**: `Database`
   - **Workflow**: Select `Email Response Generator` workflow
   - **Workflow Inputs**:
     - Input 1:
       - **Name**: `Task Description`
       - **Value**: `={{ $json.taskDescription }}`
     - Input 2:
       - **Name**: `How to Do It (Instructions)`
       - **Value**: `={{ $json.instructions }}`
     - Input 3:
       - **Name**: `Success Criteria (How to Measure)`
       - **Value**: `={{ $json.successCriteria }}`

3. **Test this step**: Verify the response generator is called and returns generated email

#### Step 7: Format Reply Email

### Add and Connect the Node

1. Add **"Set"** node to your canvas
2. **Connect it**: Drag a connection line from **Call Response Generator** to this new node
3. Name it: `Format Reply`

### Configure the Node

1. Configure:
   - **Assignments**:
     - Assignment 1:
       - **Name**: `reply_text`
       - **Value**: `={{ $json.output }}`
     - Assignment 2:
       - **Name**: `subject`
       - **Value**: `=Re: {{ $('Prepare Response Instructions').item.json.originalSubject }}`
     - Assignment 3:
       - **Name**: `to`
       - **Value**: `={{ $('Prepare Response Instructions').item.json.originalSender }}`
     - Assignment 4:
       - **Name**: `quality_status`
       - **Value**: `={{ $json.status }}`
     - Assignment 5:
       - **Name**: `retry_count`
       - **Value**: `={{ $json.retry_count }}`

#### Step 8: Add Quality Check (Optional but Recommended)

### Add and Connect the Node

{: .highlight }
> **Quality Gates in Production**: Never send automated emails without quality checks! The LLM-as-a-judge pattern in the Response Generator ensures high quality, but this gate prevents sending if something went wrong. Failed responses get flagged for human review instead of embarrassing your business with poor-quality emails.

1. Add **"IF"** node to your canvas
2. **Connect it**: Drag a connection line from **Format Reply** to this new node
3. Name it: `Check Quality Passed`

### Configure the Node

1. Configure:
   - **Conditions**:
     - Condition 1:
       - **Field**: `={{ $json.quality_status }}`
       - **Operation**: `Equal`
       - **Value**: `success`

3. This ensures we only send emails that passed quality control

#### Step 9: Send Reply Email

### Add and Connect the Node

{: .note }
> **Conversation Threading**: Setting the **Thread ID** is crucial - it makes your reply appear in the same email conversation thread instead of starting a new one. This keeps communication organised and contextual, just like when humans reply to emails manually.

1. Add **"Gmail"** node to your canvas
2. **Connect it**: Drag a connection line from the **true** output (green dot) of the **IF** node to this new node
3. Name it: `Send Reply`

### Configure the Node

1. Configure:
   - **Resource**: `Message`
   - **Operation**: `Send`
   - **Credential**: Select your Gmail OAuth2 credential
   - **To**: `={{ $json.to }}`
   - **Subject**: `={{ $json.subject }}`
   - **Email Type**: `Text`
   - **Message**: `={{ $json.reply_text }}`
   - **Options**:
     - **Thread ID**: `={{ $('Extract Email Data').item.json.thread_id }}`

#### Step 10: Handle Failed Quality (False Branch)

1. Add **"Send Email"** or **"Slack"** node connected to the **false** output of IF node
2. Configure to notify you when quality check fails:
   - Send email to yourself
   - Subject: `Failed email response - manual review needed`
   - Body with original email details and why it failed

#### Step 11: Save and Activate

1. Click **"Save"** button
2. Click **"Active"** toggle to activate the workflow
3. The workflow will now automatically process new emails!

### Full Workflow Summary

Your master workflow should look like this:

```
[Gmail Trigger]
  ↓
[Extract Email Data]
  ↓
[Call Classifier]
  ↓
[Prepare Response Instructions]
  ↓
[Call Response Generator]
  ↓
[Format Reply]
  ↓
[Check Quality Passed]
  ├─ true → [Send Reply via Gmail]
  └─ false → [Notify for Manual Review]
```

---

## End-to-End Testing

### Test Scenario 1: Support Email

1. Send an email to your Gmail account:

   ```
   Subject: Cannot access dashboard
   Body: Hi, I've been trying to log into my dashboard for the past 30 minutes but keep getting "Invalid credentials" error. I'm sure my password is correct. Please help!
   ```

2. Watch the master workflow execute:
   - Gmail trigger receives email
   - Classifier categorizes as "support" / "high" priority
   - Response generator creates quality-controlled reply
   - Gmail sends reply

3. Check your email - you should receive an automated, helpful support response!

### Test Scenario 2: Sales Inquiry

1. Send an email to your Gmail account:

   ```
   Subject: Interested in your Enterprise plan
   Body: Hello, I'm interested in learning more about your Enterprise plan features. Could you provide pricing and setup information?
   ```

2. Expected behavior:
   - Classified as "sales"
   - Response includes product benefits and next steps
   - Enthusiastic but professional tone

### Test Scenario 3: General Question

1. Send an email to your Gmail account:

   ```
   Subject: Quick question about your company
   Body: Hi, I was wondering if you have any office locations in New York?
   ```

2. Expected behavior:
   - Classified as "general"
   - Friendly, informative response
   - Offers further assistance

### Debugging Tips

| Issue | Solution |
|-------|----------|
| Classifier not called | Verify Email Classifier is activated, Execute Workflow Trigger exists |
| No response generated | Check Response Generator is activated, inputs match trigger configuration |
| Gmail not sending | Verify Gmail credential is connected, check quota limits |
| Wrong classification | Improve classifier prompt with more examples |
| Poor response quality | Adjust success criteria in Prepare Response Instructions code |

---

## Workflow Optimization

### Monitor Performance

1. Go to **Executions** tab in n8n
2. View execution history for all three workflows
3. Check execution times and error rates

### Improve Response Quality

You can improve responses by:

1. **Better Success Criteria**: Add more specific requirements in Prepare Response Instructions
2. **Increase Max Retries**: Modify Response Generator to allow more iterations
3. **Different AI Models**: Try GPT-4, Claude, or other models for generation/judging
4. **Add Examples**: Include example responses in the instructions

### Add Features

Ideas for extending the system:

- **Priority Queue**: Handle high-priority emails first
- **Language Detection**: Respond in the sender's language
- **Attachment Handling**: Process documents/images in emails
- **Sentiment Response**: Adjust tone based on sender sentiment
- **Template Library**: Use pre-written templates for common scenarios

---

## Success Checklist

You've successfully completed Part B when:

- ✅ Email Classifier workflow is built and activated
- ✅ Classifier correctly categorizes test emails
- ✅ Response Generator workflow is built and activated
- ✅ Generator creates quality-controlled responses
- ✅ Master Orchestrator workflow is built and activated
- ✅ End-to-end flow works: email → classify → generate → send
- ✅ Test emails receive appropriate automated responses
- ✅ All three workflows show in execution history
- ✅ Quality checks work (failed responses don't get sent)

---

## What's Next?

Now that you have a working multi-workflow system, you can:

1. **Test with real emails**: Let it run on your actual inbox
2. **Monitor and refine**: Watch execution logs and improve prompts
3. **Add more workflows**: Create specialized response generators for different categories
4. **Try the challenges**: Implement advanced patterns like error handling and parallel execution

---

## Push Your Workflows to GitHub

### Export and Save Your Work

Now that you've built all three workflows, it's important to save them to your GitHub repository. This creates a backup and allows you to track changes over time.

#### Step 1: Export Your Workflows from n8n

For each of your three workflows, repeat these steps:

1. Open the workflow in n8n
2. Click the **three-dot menu** (⋮) in the top-right corner
3. Select **"Download"** or **"Export workflow"**
4. Save the JSON files to your computer with descriptive names:
   - `email-classifier-workflow.json`
   - `email-response-generator-workflow.json`
   - `master-email-orchestrator-workflow.json`

{: .note }
> **Tip**: The exported files contain your entire workflow structures, but credentials are not included for security reasons.

#### Step 2: Upload to GitHub via UI

1. **Navigate to your GitHub repository** in your web browser
2. **Go to the workflows folder** (or create one if it doesn't exist):
   - Click **"Add file"** → **"Create new file"**
   - Type `workflows/` in the filename field to create the folder
3. **Upload your workflows**:
   - Click **"Add file"** → **"Upload files"**
   - Drag and drop all three JSON files, or click to browse
   - Alternatively, upload them one by one using **"Create new file"** and paste the JSON content
4. **Commit your changes**:
   - Add a commit message: `Add Exercise 4 workflows - Connecting Workflows`
   - Choose **"Commit directly to the main branch"** or create a new branch
   - Click **"Commit changes"**

{: .highlight }
> **Success!** Your workflows are now safely stored in GitHub and can be shared with others or imported into a different n8n instance.

{: .important }
> **Best Practice**: Consider adding a README.md in your workflows folder explaining what each workflow does and how they connect to each other. This will help anyone (including your future self!) understand your automation system.

---

[← Back to Part A](./part-a-setup){: .btn } [Continue to Challenges →](./challenge-tasks){: .btn .btn-primary }
