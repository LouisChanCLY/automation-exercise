---
layout: default
title: "Challenge Tasks"
parent: "Exercise 1: Email Classification"
grand_parent: Exercises
nav_order: 5
---

# Challenge Tasks

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Ready to level up? These optional challenges extend your email classification system with practical, real-world features that demonstrate your ability to integrate multiple services and build production-ready automations.

---

## Challenge 1: Urgent Email Notifications

### Objective

Send instant notifications via Telegram or Slack when urgent/high-priority emails arrive.

### Requirements

- Detect urgent emails based on classification
- Send real-time alerts with email details
- Include sender, subject, and classification reason
- Support both Telegram and/or Slack

### Why This Matters

Many urgent emails get buried in inboxes. Push notifications ensure critical messages get immediate attention, regardless of whether someone is checking email.

### What You'll Learn

- Integrating notification services (Telegram/Slack)
- Creating conditional notification logic
- Formatting rich notifications with email context

---

## Challenge 2: Sentiment Trend Analysis

### Objective

Track sentiment changes over time per sender to identify escalating customer situations.

### Requirements

- Store historical sentiment data per sender
- Identify patterns indicating customer frustration
- Flag senders whose sentiment is declining
- Generate weekly trend reports

### Why This Matters

A customer who sends three emails with increasingly negative sentiment is likely to churn. Early detection allows proactive intervention.

### What You'll Learn

- Time-series data analysis in Google Sheets
- Pattern recognition across multiple communications
- Building early warning systems for customer health

---

## Challenge 3: Advanced Routing Rules

### Objective

Implement complex, context-aware routing that considers multiple factors beyond just classification.

### Requirements

- Time-based routing (business hours vs after-hours)
- VIP sender detection with special handling
- Keyword-triggered escalation
- Sender history consideration

### Why This Matters

Real email systems need sophisticated routing. VIP customers expect faster responses, after-hours emails may need different handling, and certain keywords always trigger escalation.

### What You'll Learn

- Multi-factor decision logic
- Building lookup tables (VIP lists)
- Time-aware automation
- Escalation pathways

---

## Challenge 4: Classification Confidence Tracking

### Objective

Monitor AI classification confidence and route low-confidence emails for human review.

### Requirements

- Extract confidence scores from AI responses
- Flag emails below confidence threshold (e.g., <70%)
- Create separate sheet/queue for human review
- Track accuracy by comparing AI vs human classification

### Why This Matters

AI isn't perfect. Production systems need to know when they're uncertain and defer to humans. Tracking these cases improves the system over time.

### What You'll Learn

- Quality gates in AI systems
- Human-in-the-loop patterns
- Accuracy measurement and improvement

---

## Challenge 5: Multi-Account Email Handling

### Objective

Extend the system to monitor and classify emails from multiple Gmail accounts.

### Requirements

- Connect 2+ Gmail accounts to n8n
- Classify emails from all accounts
- Track which account each email came from
- Maintain separate label/sheet tracking per account

### Why This Matters

Businesses often manage multiple email accounts (support@, sales@, info@). A single automation should handle all of them efficiently.

### What You'll Learn

- Multi-account authentication
- Data isolation and tracking
- Scaling workflows across accounts

---

## Saving Your Work

After completing any challenge, save your workflow to GitHub:

1. **Export Workflow**: In n8n, click ⋯ menu → Download → Save as JSON
2. **Commit to GitHub**: Follow the instructions in [Part B](./part-b-workflow) to push your workflow
3. **Document Changes**: Add a README explaining what you built

---

## Getting Help

Stuck on a challenge?

- Check n8n documentation for specific nodes
- Review Part B to see how similar patterns work
- Search n8n community forums for similar use cases
- Remember: The goal is to learn by trying, not to get it perfect
