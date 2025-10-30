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

## Overview

In this section, you'll set up the prerequisites needed for Exercise 4. Since this exercise builds on concepts from Exercise 3 and uses similar AI capabilities, much of the setup may already be complete.

**Time**: 15 minutes

## Prerequisites Checklist

### 1. n8n Platform Access

You need a working n8n instance (cloud or self-hosted).

- ✅ **Already have n8n?** Skip to next section
- ❌ **Need to set up n8n?** Follow the [n8n Setup Guide](../../common-prerequisites/n8n-setup)

**Verify**:
1. Log into your n8n instance
2. You can create new workflows
3. You can see the workflow canvas

### 2. Gmail API Access

You need Gmail API credentials to fetch and send emails.

- ✅ **Already have Gmail API configured?** Skip to next section
- ❌ **Need to set up Gmail?** Follow the [Gmail API Setup Guide](../../common-prerequisites/gmail-setup)

**Verify**:
1. In n8n, go to **Credentials** menu
2. You have a "Gmail OAuth2" credential
3. The credential shows "Connected" status
4. Test by adding a Gmail node to a blank workflow and connecting your account

**What you'll need**:
- Gmail account
- Google Cloud project with Gmail API enabled
- OAuth 2.0 credentials configured with n8n redirect URI

### 3. Google Gemini API

You need a Gemini API key for AI-powered classification and generation.

- ✅ **Already have Gemini API from Exercise 3?** You're good! Use the same credential
- ❌ **Need to set up Gemini?** Follow the [Gemini API Setup Guide](../../common-prerequisites/gemini-setup)

**Verify**:
1. In n8n, go to **Credentials** menu
2. You have a "Google PaLM API" or "Gemini API" credential
3. The API key is valid and has quota remaining
4. Test by adding a "Google Gemini Model" node to a workflow

**Get your API key**:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key" or "Create API Key"
4. Copy the API key
5. Add it to n8n credentials as "Google PaLM API"

### 4. Exercise 3 Completion (Recommended)

While not strictly required, completing Exercise 3 first will help you understand the LLM-as-a-judge pattern used in this exercise.

- ✅ **Completed Exercise 3?** Great! You'll recognize the response generator workflow
- ⚠️ **Skipped Exercise 3?** That's okay, but you may want to review the [Exercise 3 Overview](../03-llm-as-judge/overview) to understand the quality control concepts

## Understanding Workflow Communication

Before building, let's understand how workflows talk to each other in n8n.

### The Execute Workflow Trigger

This is the special node that allows one workflow to call another. Think of it like a function definition in programming.

**Key Concepts**:

1. **Calling Workflow (Master)**: Uses "Execute Workflow" node to call another workflow
2. **Called Workflow (Sub)**: Uses "Execute Workflow Trigger" node to receive the call
3. **Data Passing**: Caller sends data as "workflow inputs", receiver gets them as trigger output

**Visual Example**:

```
Master Workflow:
  [Some Node] → [Execute Workflow] → [Next Node]
                     ↓ calls
              Sub-Workflow
                     ↓
  [Execute Workflow Trigger] → [Do Work] → [Return Result]
```

### Why We Need Dual Triggers

In this exercise, our sub-workflows (Classifier and Response Generator) have **two triggers**:

1. **Form Trigger**: For standalone testing during development
2. **Execute Workflow Trigger**: For being called by the master workflow in production

**Why both?**

During development:
- You want to test the classifier without running the entire email system
- Form trigger lets you manually submit test data via a web form
- Fast iteration and debugging

In production:
- Master workflow calls the sub-workflow directly
- No manual intervention needed
- Execute Workflow Trigger receives data from master workflow

**Important**: Only ONE trigger activates per execution. When testing manually, the Form Trigger activates. When called by master workflow, the Execute Workflow Trigger activates.

### How Data Flows

#### Step 1: Master Workflow Sends Data

```json
{
  "node": "Execute Workflow",
  "parameters": {
    "workflowId": "123",  // ID of workflow to call
    "workflowInputs": {
      "values": [
        { "name": "email_subject", "value": "{{ $json.subject }}" },
        { "name": "email_body", "value": "{{ $json.body }}" }
      ]
    }
  }
}
```

#### Step 2: Sub-Workflow Receives Data

```json
{
  "node": "Execute Workflow Trigger",
  "parameters": {
    "workflowInputs": {
      "values": [
        { "name": "email_subject" },  // Declares it expects this input
        { "name": "email_body" }      // Declares it expects this input
      ]
    }
  }
}
```

The trigger outputs data accessible as:
- `$json.email_subject`
- `$json.email_body`

#### Step 3: Sub-Workflow Returns Data

The **last node's output** is automatically returned to the calling workflow!

```
Sub-workflow final node outputs:
{ "category": "support", "priority": "high" }

Master workflow receives this in the next node after Execute Workflow:
$json.category = "support"
$json.priority = "high"
```

## Test Your Setup

Let's verify everything is working before building the main workflows.

### Quick Test: Call a Simple Workflow

1. **Create Test Workflow 1** (will be called):
   - Add "Execute Workflow Trigger" node
   - Configure input: `name` (string)
   - Add "Set" node: Create field `greeting` with value `Hello, {{ $json.name }}!`
   - Save as "Test Sub-Workflow"
   - Activate the workflow

2. **Create Test Workflow 2** (will call):
   - Add "Manual Trigger" node
   - Add "Execute Workflow" node
   - In "Execute Workflow", select "Test Sub-Workflow"
   - Add workflow input: `name` with value `World`
   - Click "Test workflow"

3. **Verify**:
   - Execute Workflow node should output: `{ "greeting": "Hello, World!" }`
   - If you see this, workflow communication is working!

### Troubleshooting

| Problem | Solution |
|---------|----------|
| "Workflow not found" | Make sure sub-workflow is activated |
| "No trigger node" | Sub-workflow must have Execute Workflow Trigger |
| "No output received" | Sub-workflow must have at least one node after trigger |
| Can't select workflow | Refresh page, or copy workflow ID manually |

## Architecture Review

Before moving to Part B, let's review what we'll build:

### Workflow 1: Email Classifier (Sub-Workflow)

**Purpose**: Categorize incoming emails

**Triggers**:
- Form Trigger (for testing)
- Execute Workflow Trigger (for master workflow calls)

**Inputs**:
- `email_subject` (string)
- `email_body` (string)
- `email_sender` (string)

**Output**:
```json
{
  "category": "support" | "sales" | "general",
  "priority": "high" | "medium" | "low",
  "sentiment": "positive" | "neutral" | "negative"
}
```

### Workflow 2: Response Generator (Sub-Workflow)

**Purpose**: Generate quality-controlled email responses using LLM-as-a-judge

**Triggers**:
- Form Trigger (for testing)
- Execute Workflow Trigger (for master workflow calls)

**Inputs**:
- `Task Description` (string): What response to generate
- `How to Do It (Instructions)` (string): How to write the response
- `Success Criteria (How to Measure)` (string): Quality standards

**Output**:
```json
{
  "status": "success" | "failed",
  "output": "Generated email response text...",
  "evaluation_result": true | false,
  "feedback": "Quality evaluation feedback...",
  "retry_count": 3
}
```

### Workflow 3: Master Email Orchestrator

**Purpose**: Coordinate the entire email response process

**Trigger**:
- Gmail Trigger (on new email)

**Process**:
1. Fetch new email from Gmail
2. Execute Workflow → Email Classifier
3. Receive classification result
4. Execute Workflow → Response Generator (with classification context)
5. Receive generated response
6. Send reply via Gmail

**No output** (this is the end-to-end workflow)

## Pre-Setup Checklist

Before moving to Part B, confirm:

- ✅ n8n is accessible and working
- ✅ Gmail OAuth2 credential is connected
- ✅ Gemini API credential is configured
- ✅ You understand Execute Workflow Trigger concept
- ✅ You've tested calling one workflow from another (optional but recommended)
- ✅ You reviewed Exercise 3 concepts (recommended)

## What's Next

In Part B, we'll build all three workflows step-by-step:

1. **Email Classifier Workflow** - Categorize emails with AI
2. **Response Generator Workflow** - Generate quality-controlled responses
3. **Master Orchestrator Workflow** - Tie everything together

**Estimated time for Part B**: 55 minutes

---

[← Back to Overview](./overview){: .btn } [Continue to Part B: Build Workflows →](./part-b-workflow){: .btn .btn-primary }
