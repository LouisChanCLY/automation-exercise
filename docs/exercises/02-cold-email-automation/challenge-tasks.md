---
layout: default
title: Challenge Tasks
parent: "Exercise 2: AI Cold Email Automation"
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

These challenges extend your cold email system with advanced features. Each builds on the **AI Research & Personalization** pattern you've learned.

---

## Challenge 1: Multi-Channel Outreach

### Objective

Extend your workflow to send personalised messages across multiple channels based on prospect preferences.

### Requirements

- Research which channels the prospect is active on
- Generate platform-specific content (LinkedIn, Twitter/X, Email)
- Route to appropriate channel based on research
- Maintain consistent messaging across platforms

### Why This Matters

Most professionals have preferred communication channels. Reaching them where they're most active increases response rates significantly.

### What You'll Learn

- Multi-platform integration patterns
- Content adaptation for different channels
- Dynamic routing based on research insights
- Fallback logic when preferred channels aren't available

### Success Criteria

- ✅ Identifies prospect's preferred communication channel
- ✅ Generates platform-appropriate content (280 chars for Twitter, professional for LinkedIn)
- ✅ Successfully sends via detected channel
- ✅ Falls back to email if no social presence found

---

## Challenge 2: A/B Testing System

### Objective

Implement A/B testing to optimise your email performance over time.

### Requirements

- Create two email variations for each outreach
- Randomly assign prospects to version A or B
- Track performance metrics for each version
- Automatically select winning version after threshold

### Why This Matters

What works for one audience might not work for another. A/B testing lets you systematically improve your messaging based on real data, not guesses.

### What You'll Learn

- Statistical testing in automated workflows
- Random assignment and traffic splitting
- Performance tracking and analysis
- Data-driven optimisation patterns

### Success Criteria

- ✅ Generates two distinct email versions
- ✅ Evenly distributes prospects between versions
- ✅ Tracks version performance in Google Sheets
- ✅ Identifies statistically significant winner after 50+ sends

---

## Challenge 3: Smart Follow-Up Sequence

### Objective

Build an automated follow-up system that sends contextual messages if no response is received.

### Requirements

- Track email opens and responses
- Send follow-up after 3 days of no response
- Each follow-up references previous context
- Maximum of 3 follow-ups then stop

### Why This Matters

Most successful cold outreach requires 3-5 touches. Automated follow-ups dramatically increase response rates whilst respecting prospect's time and attention.

### What You'll Learn

- Time-based automation with Wait nodes
- Gmail API for checking email responses
- Contextual message generation referencing history
- Stopping conditions to avoid spam

### Success Criteria

- ✅ Waits appropriate time before follow-up
- ✅ Detects if prospect has responded
- ✅ Generates contextual follow-up referencing original
- ✅ Stops after 3 follow-ups or response

---

## Challenge 4: Industry-Specific Templates

### Objective

Create specialised email templates for different industries, automatically selected based on prospect's company.

### Requirements

- Identify prospect's industry during research
- Maintain library of industry-specific approaches
- Select appropriate template and terminology
- Include industry-specific value propositions

### Why This Matters

Generic emails feel like spam. Industry-specific language shows expertise and relevance, dramatically increasing engagement from qualified prospects.

### What You'll Learn

- Industry classification using AI research
- Template management and dynamic selection
- Context-aware content generation
- Domain-specific personalisation

### Success Criteria

- ✅ Correctly identifies prospect's industry
- ✅ Applies industry-specific template
- ✅ Uses appropriate terminology and pain points
- ✅ Shows measurably better engagement rates

---

## Challenge 5: Sentiment-Aware Responses

### Objective

Adjust email tone and approach based on prospect's recent public sentiment (from social media, news).

### Requirements

- Analyse sentiment from prospect's recent posts/news
- Adjust email tone to match or complement
- Reference specific content that shows awareness
- Maintain authenticity whilst adapting

### Why This Matters

Reaching out to someone celebrating a win requires different tone than someone facing challenges. Sentiment awareness makes outreach feel timely and empathetic, not robotic.

### What You'll Learn

- Sentiment analysis in research workflows
- Dynamic tone adjustment based on context
- Emotional intelligence in automation
- Balance between personalisation and authenticity

### Success Criteria

- ✅ Accurately detects prospect sentiment
- ✅ Generates tone-appropriate emails
- ✅ References specific content naturally
- ✅ Improves response rates vs generic approach

---

## Saving Your Work

After completing any challenge:

1. **Export Workflow**: In n8n, click ⋯ menu → Download → Save as JSON
2. **Commit to GitHub**: Save your workflow JSON files to your repository
3. **Document Changes**: Add notes explaining what you built and why

{: .highlight }
> **Pro Tip**: Each challenge teaches skills applicable far beyond cold email. Think about how these patterns apply to your specific use cases!
