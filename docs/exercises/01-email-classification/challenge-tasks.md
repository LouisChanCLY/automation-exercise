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

Ready to level up? These optional challenges extend your email classification system with advanced features. Each challenge includes hints but encourages independent problem-solving.

---

## Challenge 1: Multi-Language Support

### Objective

Enhance your classifier to handle emails in multiple languages.

### Requirements

- Detect email language automatically
- Translate non-English emails before classification
- Respond in the sender's language
- Support at least 3 languages

### Implementation Hints

1. **Language Detection**

   ```javascript
   // Add to Prepare Email node
   const detectLanguage = (text) => {
     // Use patterns or API
     const patterns = {
       spanish: /¿|ñ|á|é|í|ó|ú/i,
       french: /ç|è|é|à|ù/i,
       german: /ä|ö|ü|ß/i
     };
     // Return detected language
   };
   ```

2. **Translation Integration**
   - Add Google Translate node before AI
   - Store original and translated versions
   - Pass language context to AI

3. **Multilingual Prompts**

   ```
   Analyze this email (Language: {{language}}):
   Original: {{originalText}}
   Translated: {{translatedText}}

   Respond with classification in English
   ```

### Success Criteria

- Correctly identifies language in 90%+ cases
- Maintains classification accuracy across languages
- Logs language distribution in sheets

---

## Challenge 2: Smart Auto-Reply

### Objective

Generate and send contextual auto-replies based on classification.

### Requirements

- Create response templates per category
- Personalize with sender name and context
- Include relevant links/resources
- Track response effectiveness

### Implementation Hints

1. **Template System**

   ```javascript
   const templates = {
     urgent_support: `
       Hi {{senderName}},

       We've received your urgent request about {{subject}}.
       A support specialist will contact you within 15 minutes.

       Ticket #: {{ticketId}}
       Priority: URGENT
     `,
     sales_inquiry: `
       Thank you for your interest in our enterprise solutions...
     `
   };
   ```

2. **AI-Generated Responses**
   - Use AI to draft personalized replies
   - Include classification confidence check
   - Only auto-reply if confidence > 0.8

3. **Response Tracking**
   - Log all auto-replies sent
   - Track open/click rates
   - Measure response times

### Success Criteria

- Sends appropriate responses 100% of the time
- Reduces average response time by 80%
- Maintains professional tone

---

## Challenge 3: Sentiment Trend Analysis

### Objective

Build a dashboard showing sentiment trends over time.

### Requirements

- Track sentiment changes per sender
- Identify escalation patterns
- Predict potential churn
- Generate weekly reports

### Implementation Hints

1. **Historical Tracking**

   ```javascript
   // Store in sheets with structure:
   const sentimentHistory = {
     sender: email,
     date: timestamp,
     sentiment: score,
     trend: calculateTrend(previousScores)
   };
   ```

2. **Trend Calculation**
   - Compare last 5 emails from sender
   - Calculate sentiment trajectory
   - Flag concerning patterns

3. **Visualization**
   - Use Google Sheets charts
   - Create sentiment heatmap
   - Show department-wise trends

### Success Criteria

- Accurately tracks sentiment over time
- Identifies 80%+ of escalating situations
- Provides actionable insights

---

## Challenge 4: Advanced Routing Rules

### Objective

Implement complex, conditional routing based on multiple factors.

### Requirements

- Time-based routing (business hours)
- Sender history consideration
- Content keyword triggers
- VIP sender detection

### Implementation Hints

1. **Business Hours Check**

   ```javascript
   const isBusinessHours = () => {
     const now = new Date();
     const hour = now.getHours();
     const day = now.getDay();
     return (day >= 1 && day <= 5) && (hour >= 9 && hour <= 17);
   };
   ```

2. **VIP Detection**
   - Maintain VIP email list in sheets
   - Check sender against list
   - Apply special handling rules

3. **Keyword Triggers**

   ```javascript
   const urgentKeywords = [
     'urgent', 'asap', 'immediately',
     'critical', 'emergency', 'down'
   ];
   const hasUrgentKeyword = urgentKeywords.some(
     keyword => body.toLowerCase().includes(keyword)
   );
   ```

### Success Criteria

- Routes 100% accurately based on rules
- Handles edge cases gracefully
- Maintains audit trail

---

## Challenge 5: Performance Analytics

### Objective

Create comprehensive analytics showing system performance.

### Requirements

- Processing time metrics
- Classification accuracy tracking
- Cost per email calculation
- ROI demonstration

### Implementation Hints

1. **Performance Metrics**

   ```javascript
   const metrics = {
     startTime: Date.now(),
     endTime: null,
     processingTime: null,
     apiCalls: 0,
     apiCost: 0,
     accuracy: null
   };
   ```

2. **Accuracy Validation**
   - Implement feedback mechanism
   - Allow manual correction
   - Calculate accuracy scores

3. **Dashboard Creation**
   - Use Google Data Studio
   - Connect to sheets data
   - Create real-time visualizations

### Success Criteria

- Tracks all key metrics
- Provides real-time insights
- Demonstrates clear ROI

---

## Bonus Challenge: Custom AI Model

### Objective

Replace OpenRouter with a custom-trained model.

### Requirements

- Train model on your email data
- Implement via HuggingFace
- Compare accuracy metrics
- Optimize for speed

### Implementation Hints

1. **Data Collection**
   - Export classified emails
   - Create training dataset
   - Label minimum 500 examples

2. **Model Training**
   - Use AutoML tools
   - Fine-tune BERT/DistilBERT
   - Deploy to HuggingFace

3. **Integration**

   ```javascript
   // Replace OpenRouter with HuggingFace
   const customModel = {
     endpoint: 'your-model-endpoint',
     apiKey: 'your-api-key',
     maxTokens: 512
   };
   ```

### Success Criteria

- Achieves 90%+ accuracy
- Processes in <2 seconds
- Costs less than OpenRouter

---

## Submission Guidelines

If you complete any challenges:

1. **Document Your Solution**
   - Screenshot your workflow
   - Export and share the JSON
   - Write brief explanation

2. **Share Results**
   - Post in course forum
   - Include metrics/screenshots
   - Help other students

3. **Get Feedback**
   - Request code review
   - Ask for optimization tips
   - Celebrate success!

---

## What's Next?

Completed all challenges? You're ready for:

- Exercise 2: Social Media Monitor
- Exercise 3: Document Processor
- Building your own automation ideas

Remember: The best automation is one that solves YOUR specific problem. Use these skills to build something valuable for your work or life!
