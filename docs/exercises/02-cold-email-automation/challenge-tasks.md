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

### The Goal

Extend your workflow to send personalized messages across multiple channels based on prospect preferences.

### Requirements

- Research which channels the prospect is active on
- Generate platform-specific content (LinkedIn, Twitter/X, Email)
- Route to appropriate channel based on research
- Maintain consistent messaging across platforms

### Implementation Hints

1. **Enhance Research Agent**: Add prompts to find social media profiles
2. **Add Switch Node**: Route based on preferred channel
3. **Platform-Specific Agents**: Create variations for each platform's style
4. **LinkedIn Integration**: Use HTTP Request node with LinkedIn API
5. **Twitter Integration**: Use Twitter node or API

### Success Criteria

- [ ] Identifies prospect's preferred communication channel
- [ ] Generates platform-appropriate content (280 chars for Twitter, professional for LinkedIn)
- [ ] Successfully sends via detected channel
- [ ] Falls back to email if no social presence found

---

## Challenge 2: A/B Testing System

### The Goal

Implement A/B testing to optimize your email performance over time.

### Requirements

- Create two email variations for each outreach
- Randomly assign prospects to version A or B
- Track performance metrics for each version
- Automatically select winning version after threshold

### Implementation Hints

1. **Duplicate Email Agent**: Create "Email Agent A" and "Email Agent B" with different prompts
2. **Add Random Router**: Use Math.random() in Code node to split traffic
3. **Enhanced Logging**: Add columns for version, open_rate, response_rate
4. **Performance Calculator**: Add workflow to analyze Sheets data weekly
5. **Auto-Optimization**: Update prompts based on winning version

### Success Criteria

- [ ] Generates two distinct email versions
- [ ] Evenly distributes prospects between versions
- [ ] Tracks version performance in Google Sheets
- [ ] Identifies statistically significant winner after 50+ sends

---

## Challenge 3: Smart Follow-Up Sequence

### The Goal

Build an automated follow-up system that sends contextual messages if no response is received.

### Requirements

- Track email opens and responses
- Send follow-up after 3 days of no response
- Each follow-up references previous context
- Maximum of 3 follow-ups then stop

### Implementation Hints

1. **Add Wait Node**: Delay 3 days after initial send
2. **Check Response**: Query Gmail for replies to thread ID
3. **Follow-up Agent**: Create agent that references previous email
4. **Sequence Counter**: Track follow-up number in Sheets
5. **Stop Condition**: Check if max follow-ups reached

### Success Criteria

- [ ] Waits appropriate time before follow-up
- [ ] Detects if prospect has responded
- [ ] Generates contextual follow-up referencing original
- [ ] Stops after 3 follow-ups or response

---

## Challenge 4: Industry-Specific Templates

### The Goal

Create specialized email templates for different industries, automatically selected based on prospect's company.

### Requirements

- Identify prospect's industry during research
- Maintain library of industry-specific approaches
- Select appropriate template and terminology
- Include industry-specific value propositions

### Implementation Hints

1. **Industry Classifier**: Add to research agent output
2. **Template Library**: Store in Google Sheets or JSON
3. **Dynamic Prompts**: Use Switch node to route by industry
4. **Industry Agents**: Create specialized agents per vertical
5. **Terminology Database**: Include industry-specific phrases

### Success Criteria

- [ ] Correctly identifies prospect's industry
- [ ] Applies industry-specific template
- [ ] Uses appropriate terminology and pain points
- [ ] Shows measurably better engagement rates

---

## Challenge 5: Sentiment-Aware Responses

### The Goal

Adjust email tone and approach based on prospect's recent public sentiment (from social media, news).

### Requirements

- Analyze sentiment from prospect's recent posts/news
- Adjust email tone to match or complement
- Reference specific content that shows awareness
- Maintain authenticity while adapting

### Implementation Hints

1. **Sentiment Analysis**: Add to research agent capabilities
2. **Tone Mapping**: Create tone variations (enthusiastic, empathetic, professional)
3. **Content References**: Extract specific quotes or achievements
4. **Dynamic Prompt**: Adjust based on sentiment score
5. **Validation**: Ensure tone remains appropriate

### Success Criteria

- [ ] Accurately detects prospect sentiment
- [ ] Generates tone-appropriate emails
- [ ] References specific content naturally
- [ ] Improves response rates vs generic approach

---

## Saving Your Work

After completing any challenge:

1. **Export Workflow**: In n8n, click ⋯ menu → Download → Save as JSON
2. **Commit to GitHub**: Save your workflow JSON files to your repository
3. **Document Changes**: Add notes explaining what you built and why

{: .highlight }
> **Pro Tip**: Each challenge teaches skills applicable far beyond cold email. Think about how these patterns apply to your specific use cases!
