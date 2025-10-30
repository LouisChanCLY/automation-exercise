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

### Build Steps

#### Step 1: Create New Workflow

1. Click **"+ Add workflow"** in n8n
2. Name it: `Email Classifier`
3. Save the workflow

#### Step 2: Add Form Trigger (For Testing)

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

**Important**: Both triggers are now in your workflow. Only ONE will activate per execution:
- **Form Trigger** activates when you access the form URL
- **Execute Workflow Trigger** activates when called by master workflow

#### Step 4: Add AI Classification Node

1. Add **"AI Agent"** node after the triggers
2. Configure:
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
     - **Model**: `gemini-1.5-flash` (or your preferred model)

#### Step 5: Parse and Format Output

1. Add **"Code"** node after AI Agent
2. Configure:
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

### Build Steps

#### Option A: Import from Exercise 3 (Recommended)

If you completed Exercise 3:

1. Go to Exercise 3 workflow
2. Click **"..."** menu → **"Duplicate"**
3. Rename to: `Email Response Generator`
4. Verify it has both:
   - Form Trigger
   - Execute Workflow Trigger
5. No changes needed - it already has the quality control loop!

#### Option B: Import from JSON (Quick Start)

1. Download the workflow JSON file (link below)
2. In n8n, click **"..."** → **"Import from File"**
3. Select the downloaded JSON file
4. Rename to: `Email Response Generator`
5. Update Gemini credentials if needed
6. Save and activate

[Download Response Generator JSON](./downloads/email-response-generator.json)

#### Option C: Build from Scratch (Detailed)

This option is covered in Exercise 3. Follow these steps if you haven't done Exercise 3:

1. Create workflow with Form Trigger
2. Add Execute Workflow Trigger with inputs:
   - `Task Description`
   - `How to Do It (Instructions)`
   - `Success Criteria (How to Measure)`
3. Add initialization node for variables (retry_count, max_retries, previous_feedback)
4. Add AI Generator agent
5. Add AI Judge agent with structured output parser
6. Add loop logic with retry counter and max retries check
7. Return final output

See [Exercise 3 Build Guide](../03-llm-as-judge/part-b-workflow) for detailed instructions.

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

### Build Steps

#### Step 1: Create New Workflow

1. Click **"+ Add workflow"** in n8n
2. Name it: `Master Email Orchestrator`
3. Save the workflow

#### Step 2: Add Gmail Trigger

1. Add **"Gmail Trigger"** node
2. Configure:
   - **Trigger On**: `New Email`
   - **Credential**: Select your Gmail OAuth2 credential
   - **Event**: `Message Received`
   - **Label Names or IDs**: Leave empty (or specify a label like "Auto-Respond")
   - **Simple**: Toggle ON

#### Step 3: Extract Email Data

1. Add **"Set"** node after Gmail Trigger
2. Configure to extract and format email data:
   - **Name**: `Extract Email Data`
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

1. Add **"Execute Workflow"** node
2. Configure:
   - **Name**: `Call Classifier`
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

1. Add **"Code"** node after the classifier
2. Configure:
   - **Name**: `Prepare Response Instructions`
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

1. Add **"Execute Workflow"** node
2. Configure:
   - **Name**: `Call Response Generator`
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

1. Add **"Set"** node
2. Configure:
   - **Name**: `Format Reply`
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

1. Add **"IF"** node after Format Reply
2. Configure:
   - **Name**: `Check Quality Passed`
   - **Conditions**:
     - Condition 1:
       - **Field**: `={{ $json.quality_status }}`
       - **Operation**: `Equal`
       - **Value**: `success`

3. This ensures we only send emails that passed quality control

#### Step 9: Send Reply Email

1. Add **"Gmail"** node connected to the **true** output of IF node
2. Configure:
   - **Resource**: `Message`
   - **Operation**: `Send`
   - **Credential**: Select your Gmail OAuth2 credential
   - **To**: `={{ $json.to }}`
   - **Subject**: `={{ $json.subject }}`
   - **Email Type**: `Text`
   - **Message**: `={{ $json.reply_text }}`
   - **Options**:
     - **Thread ID**: `={{ $('Extract Email Data').item.json.thread_id }}` (replies in same thread)

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
