---
layout: default
title: Challenge Tasks
parent: "Exercise 4: Connecting Workflows"
grand_parent: Exercises
nav_order: 4
---

# Challenge Tasks

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Ready to level up your workflow orchestration skills? These challenge tasks will help you build production-ready features and handle complex scenarios.

**Difficulty Levels**:

- ⭐ Beginner-Friendly
- ⭐⭐ Intermediate
- ⭐⭐⭐ Advanced

---

## Challenge 1: Error Handling & Retry Logic ⭐⭐

### Problem

Currently, if a sub-workflow fails (classifier or response generator), the entire master workflow fails with no graceful fallback.

### Goal

Implement robust error handling with retry logic and fallback responses.

### Tasks

1. **Add Error Trigger to Sub-Workflows**
   - In Email Classifier: Add error trigger node that returns default classification
   - In Response Generator: Add error trigger that returns generic response

2. **Implement Retry Logic in Master Workflow**
   - Wrap Execute Workflow nodes in error handling
   - Retry failed workflow calls up to 3 times
   - Add delay between retries (2s, 4s, 8s)

3. **Fallback Responses**
   - If classifier fails 3 times: Default to "general" category
   - If generator fails 3 times: Send pre-written template response

4. **Error Notifications**
   - Send Slack/email notification when errors occur
   - Include error details for debugging

### Success Criteria

- ✅ System continues working even when sub-workflows fail
- ✅ Failed executions are retried automatically
- ✅ Fallback responses are used when all retries exhausted
- ✅ You receive notifications for failures

### Hints

- Use the **IF** node to check for error conditions
- Use **Wait** node to add delays between retries
- Use **$executionSuccess** variable to detect failures
- Store retry count in Set node variables

---

## Challenge 2: Parallel Classification ⭐⭐⭐

### Problem

Currently, the master workflow calls the classifier, waits for result, then continues. For complex scenarios, you might want multiple classifiers running simultaneously.

### Goal

Run multiple classification workflows in parallel and combine their results.

### Tasks

1. **Create Additional Classifier Workflows**
   - Sentiment Classifier: Analyzes emotional tone
   - Urgency Classifier: Determines response urgency
   - Language Classifier: Detects email language

2. **Parallel Execution in Master Workflow**
   - Use **Split In Batches** or multiple Execute Workflow nodes
   - Call all classifiers simultaneously
   - Collect all results

3. **Merge Classification Results**
   - Combine outputs from all classifiers
   - Create unified classification object
   - Handle conflicting classifications (e.g., majority vote)

4. **Adaptive Response Generation**
   - Pass combined classification to response generator
   - Adjust response based on multiple signals (sentiment + urgency + category)

### Success Criteria

- ✅ Multiple classifiers run in parallel (not sequential)
- ✅ Total execution time reduced compared to sequential
- ✅ All classification results are merged correctly
- ✅ Response adapts to combined insights

### Hints

- Use **Split In Batches** with batch size 1 to trigger parallel executions
- Use **Merge** node to combine parallel results
- Use **Code** node to implement voting logic for conflicts

---

## Challenge 3: Workflow Version Management ⭐⭐

### Problem

When you update a sub-workflow, all master workflows immediately use the new version. This can break production if the update has bugs.

### Goal

Implement workflow versioning with A/B testing capabilities.

### Tasks

1. **Create Workflow Versions**
   - Duplicate Response Generator workflow
   - Name them: `Response Generator v1` and `Response Generator v2`
   - Make improvements to v2

2. **A/B Testing in Master Workflow**
   - Add logic to randomly select which version to call (50/50 split)
   - Log which version was used for each email
   - Track performance metrics (quality score, retry count)

3. **Performance Comparison**
   - After 20 emails, compare both versions
   - Which has better quality scores?
   - Which has fewer retries?
   - Which is faster?

4. **Gradual Rollout**
   - Adjust split to 80% v2, 20% v1
   - Eventually migrate 100% to v2

### Success Criteria

- ✅ Two versions of response generator running simultaneously
- ✅ Random selection between versions
- ✅ Performance metrics logged and comparable
- ✅ Gradual rollout implemented

### Hints

- Use **IF** node with condition `{{ Math.random() < 0.5 }}` for random selection
- Use **Sheets** or **Database** to log version and performance
- Use **Set** node to add version identifier to execution data

---

## Challenge 4: Dynamic Workflow Routing ⭐⭐⭐

### Problem

All emails use the same response generator. Different email types (support, sales, VIP) might benefit from specialized generators.

### Goal

Route to different response generator workflows based on classification results.

### Tasks

1. **Create Specialized Response Generators**
   - Support Response Generator: Technical, helpful tone
   - Sales Response Generator: Persuasive, benefit-focused
   - VIP Response Generator: Personalized, premium service tone

2. **Dynamic Routing in Master Workflow**
   - After classification, use **Switch** node to route by category
   - Call appropriate response generator for each category
   - Handle edge cases (unknown categories)

3. **Custom Success Criteria Per Category**
   - Support: Must include troubleshooting steps
   - Sales: Must include call-to-action
   - VIP: Must address by name, mention account history

4. **Fallback Chain**
   - If specialized generator fails, fall back to generic generator
   - Maintain quality standards across all paths

### Success Criteria

- ✅ Multiple specialized response generators created
- ✅ Master workflow routes dynamically based on classification
- ✅ Each category gets appropriate specialized response
- ✅ Fallback works when specialized generator unavailable

### Hints

- Use **Switch** node with `$json.category` to route
- Each Switch output connects to different Execute Workflow node
- Use **Merge** node after all paths to combine results

---

## Challenge 5: Execution Monitoring Dashboard ⭐⭐

### Problem

You can't easily see system performance, success rates, or response times across all workflows.

### Goal

Create a monitoring dashboard that tracks key metrics.

### Tasks

1. **Add Logging Workflow**
   - Create new workflow: `Execution Logger`
   - Receives execution data from all workflows
   - Stores in Google Sheets or database

2. **Log Key Metrics**
   - For each email processed:
     - Timestamp
     - Classification (category, priority, sentiment)
     - Response quality (passed/failed, retry count)
     - Execution time
     - Errors (if any)

3. **Call Logger from Master Workflow**
   - After each execution (success or fail)
   - Use Execute Workflow to call logger
   - Don't block master workflow (async call)

4. **Create Dashboard in Sheets**
   - Total emails processed
   - Success rate %
   - Average response quality score
   - Most common categories
   - Average execution time
   - Error rate by workflow

### Success Criteria

- ✅ All executions logged automatically
- ✅ Dashboard shows real-time metrics
- ✅ Can identify performance bottlenecks
- ✅ Error patterns are visible

### Hints

- Use **HTTP Request** node to send async logs (fire-and-forget)
- Use Google Sheets formulas for dashboard calculations
- Use **Code** node to calculate execution time

---

## Challenge 6: Human-in-the-Loop for Uncertain Cases ⭐⭐⭐

### Problem

Some emails are ambiguous or sensitive. The system should ask for human approval before sending responses in certain cases.

### Goal

Implement human review for high-risk or uncertain classifications.

### Tasks

1. **Define Review Criteria**
   - High priority + negative sentiment = requires review
   - VIP senders = always require review
   - Quality failed after 5+ retries = requires review
   - Uncertain classification (AI confidence < 70%) = requires review

2. **Create Approval Workflow**
   - Sends Slack message or email with:
     - Original email
     - Proposed classification
     - Generated response
     - Approve / Reject / Edit buttons

3. **Modify Master Workflow**
   - After response generation, check review criteria
   - If review needed: Call approval workflow and wait
   - If approved: Send email
   - If rejected: Log for manual handling

4. **Approval Timeout**
   - If no response in 1 hour: Escalate to manager
   - If no response in 4 hours: Send default response

### Success Criteria

- ✅ High-risk cases trigger human review
- ✅ Reviewer can approve/reject/edit response
- ✅ Approved responses are sent automatically
- ✅ Timeout escalation works

### Hints

- Use **Webhook** node to receive approval responses
- Use **Wait** node with resume trigger for approval
- Use **IF** node to check review criteria
- Use **Slack** or **Email** for approval requests

---

## Challenge 7: Multi-Language Support ⭐⭐⭐

### Problem

Emails may arrive in different languages. Responses should be in the same language as the original email.

### Goal

Detect email language and generate responses in that language.

### Tasks

1. **Create Language Detection Workflow**
   - Receives email text
   - Uses AI to detect language
   - Returns language code (en, es, fr, de, etc.)

2. **Modify Classification to Include Language**
   - Call language detector before or alongside classifier
   - Pass language info to response generator

3. **Update Response Generator Prompts**
   - Add instruction: "Respond in {language}"
   - Validate response is in correct language (judge checks this)

4. **Test with Multiple Languages**
   - Send emails in Spanish, French, German
   - Verify responses are in matching language
   - Verify quality is maintained across languages

### Success Criteria

- ✅ System detects email language accurately
- ✅ Responses generated in same language as input
- ✅ Quality standards maintained across languages
- ✅ Works for at least 3 different languages

### Hints

- Use AI prompt: "Detect the language of this text. Respond with only the ISO 639-1 language code."
- Pass language code to generator: `"Respond in {{ $json.language }}"`
- Test with Google Translate to verify language

---

## Challenge 8: Response Template Library ⭐

### Problem

Some email types (password reset, order confirmation) should use consistent templates rather than generating from scratch each time.

### Goal

Create a template library for common email types.

### Tasks

1. **Create Template Storage**
   - Use Google Sheets or JSON file
   - Store templates for:
     - Password reset
     - Order confirmation
     - Shipping notification
     - Account created
     - General support

2. **Add Template Matching**
   - After classification, check if email matches a template scenario
   - If match: Fetch template
   - If no match: Use response generator

3. **Template Variable Replacement**
   - Templates have placeholders: `{{customer_name}}`, `{{order_id}}`, etc.
   - Extract values from original email
   - Replace placeholders with actual values

4. **Quality Check Templates**
   - Even templates go through judge validation
   - Ensure personalization is appropriate

### Success Criteria

- ✅ Template library created with 5+ templates
- ✅ System correctly matches emails to templates
- ✅ Variables are extracted and replaced
- ✅ Templates are faster than full generation

### Hints

- Use **Google Sheets** node to fetch templates
- Use **Code** node for variable extraction with regex
- Use `string.replace()` for placeholder replacement

---

## Bonus Challenge: Full Customer Support System ⭐⭐⭐

### Goal

Combine multiple challenges to build a production-ready customer support automation system.

### Features to Implement

1. **Multi-stage classification** (parallel)
2. **Dynamic workflow routing** (specialized generators)
3. **Error handling** (retry + fallback)
4. **Human-in-the-loop** (high-risk review)
5. **Multi-language support**
6. **Template library** (for common cases)
7. **Monitoring dashboard** (performance metrics)
8. **Version management** (A/B testing)

### Success Criteria

- ✅ System handles 100+ emails per day
- ✅ 90%+ automation rate (humans only review 10%)
- ✅ Sub-2-minute response time
- ✅ 95%+ quality score on responses
- ✅ Full visibility into system performance

---

## Saving Your Work

After completing any challenge:

1. **Export Workflows**: In n8n, export all modified workflows to JSON
2. **Commit to GitHub**: Save your workflow files to your repository
3. **Document Changes**: Explain your multi-workflow architecture decisions

---

[← Back to Part B](./part-b-workflow){: .btn } [Back to Exercise Index](../index){: .btn }
