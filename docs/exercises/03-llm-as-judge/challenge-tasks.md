---
layout: default
title: Challenge Tasks
parent: "Exercise 3: LLM as a Judge"
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

Ready to take your LLM as a Judge workflow to the next level? These challenge tasks introduce advanced patterns used in production AI systems.

Each challenge builds on the core workflow you've created and introduces new concepts applicable across many AI automation scenarios.

---

## Challenge 1: Multi-Variant Generation with Best-of-N Selection

**Difficulty**: Intermediate | **Time**: 30 minutes

### The Pattern

Instead of iterating on a single piece of content, generate multiple variants in parallel and have the judge select the best one.

### Real-World Application

- **A/B Testing**: Generate 3-5 email subject lines, pick the most engaging
- **Content Optimization**: Create multiple blog intros, select the most compelling
- **Ad Copy**: Generate variants with different angles, choose highest-scoring

### Implementation Steps

1. **Modify Generator**:
   - Add a **Loop** node before Generator
   - Set loop count to 3-5 variants
   - Generate unique content each iteration (add randomness prompt)

2. **Collect All Variants**:
   - Use **Aggregate** node to collect all generated variants
   - Each variant passes through Judge individually

3. **Select Winner**:
   - Add **Code** node to compare all scores
   - Return variant with highest overall score
   - Log all variants and scores for analysis

4. **Enhanced Logging**:
   - Track which variant won
   - Log scores for all variants
   - Identify patterns in winning content

### Success Criteria

- ✅ Generate 5 variants for same topic
- ✅ Judge evaluates each independently
- ✅ System selects highest-scoring variant
- ✅ Google Sheets shows all variants and winner

### Bonus

Add diversity check: Ensure variants are meaningfully different (not just minor wording changes).

---

## Challenge 2: Ensemble Judging with Multiple Evaluators

**Difficulty**: Advanced | **Time**: 45 minutes

### The Pattern

Use multiple judge LLMs with different perspectives, then aggregate their scores for more robust evaluation.

### Real-World Application

- **Balanced Evaluation**: Reduce bias by using multiple models with different perspectives, increasing reliability and consistency
- **Multi-Stakeholder Review**: Different judges represent different stakeholders (technical for accuracy, marketing for brand guidelines and tone of voice, legal for compliance)
- **Confidence Scoring**: High agreement = high confidence, disagreement = needs human review

### Implementation Steps

1. **Create Multiple Judge Branches**:
   - Add 3 parallel Judge LLM nodes
   - Judge 1: **Technical Accuracy** (Claude 3.5 Sonnet)
   - Judge 2: **Creative Appeal** (GPT-4o)
   - Judge 3: **Brand Alignment** (Gemini Pro)

2. **Different Evaluation Criteria**:
   - Each judge uses specialized criteria
   - Technical: Accuracy, clarity, completeness
   - Creative: Engagement, originality, emotional appeal
   - Brand: Tone of voice, brand guidelines, messaging consistency, company standards compliance

3. **Aggregate Scores**:
   - Collect all judge outputs
   - Calculate weighted average
   - Measure inter-judge agreement (variance)

4. **Confidence Threshold**:
   - If judges agree (variance < 10): High confidence, auto-approve
   - If judges disagree (variance > 20): Flag for human review

### Success Criteria

- ✅ Three judges evaluate same content independently
- ✅ Scores aggregated with confidence metric
- ✅ Low-confidence results flagged
- ✅ Log includes per-judge breakdown

### Bonus

Add a "meta-judge" that reviews cases where judges strongly disagree and makes final call.

---

## Challenge 3: Adaptive Quality Thresholds

**Difficulty**: Intermediate | **Time**: 30 minutes

### The Pattern

Dynamically adjust quality thresholds based on content type, iteration count, or historical performance.

### Real-World Application

- **Content Urgency**: Lower thresholds for time-sensitive content
- **Learning System**: Start strict, relax as system learns what works
- **Progressive Enhancement**: First pass for "good enough", second pass for "excellent"

### Implementation Steps

1. **Add Content Type Classifier**:
   - Add field to Manual Trigger: `content_type` (marketing, technical, internal, external)
   - Add field: `urgency` (low, medium, high, critical)

2. **Dynamic Threshold Logic**:

```javascript
// Calculate adaptive threshold
const baseThreshold = 80;

// Adjust for content type
const contentAdjustment = {
  'marketing': 5,      // Higher standards for customer-facing
  'technical': 0,      // Standard for technical docs
  'internal': -5,      // Lower for internal use
  'external': 10       // Highest for external communications
};

// Adjust for urgency
const urgencyAdjustment = {
  'low': 5,           // More time to perfect
  'medium': 0,        // Standard
  'high': -5,         // Accept good enough
  'critical': -10     // Ship quickly
};

const adjustedThreshold = baseThreshold
  + (contentAdjustment[content_type] || 0)
  + (urgencyAdjustment[urgency] || 0);

return { threshold: Math.max(70, Math.min(95, adjustedThreshold)) };
```

**Progressive Standards**:

- Iteration 1-2: Use adjusted threshold
- Iteration 3-4: Relax by 5 points
- Iteration 5: Accept best attempt

**Log Threshold Decisions**:

- Track which thresholds were applied
- Analyze success rates by content type

### Success Criteria

- ✅ Threshold adjusts based on input parameters
- ✅ Progressive relaxation prevents infinite loops
- ✅ All threshold decisions logged
- ✅ Analysis shows impact on success rates

---

## Challenge 4: Self-Optimizing Prompts

**Difficulty**: Expert | **Time**: 60 minutes

### The Pattern

Automatically improve generator prompts based on what produces high-scoring outputs.

### Real-World Application

- **Prompt Engineering at Scale**: Test dozens of prompt variations
- **Continuous Improvement**: System learns what works over time
- **Personalization**: Adapt prompts to specific use cases or audiences

### Implementation Steps

1. **Create Prompt Variants Table**:
   - Google Sheet: `Prompt Performance Tracker`
   - Columns: prompt_id, prompt_text, avg_score, success_rate, usage_count

2. **A/B Test Prompts**:
   - Load 3-5 prompt variants from sheet
   - Randomly select which to use for each run
   - Track performance per prompt

3. **Performance Analysis**:
   - After 20 runs per prompt, calculate:
     - Average score
     - Success rate (% passing threshold)
     - Iteration efficiency (avg iterations to pass)

4. **Automatic Promotion**:
   - Top-performing prompt becomes default
   - Low performers retired or refined
   - New variants generated by meta-LLM based on what works

5. **Meta-Prompt Generator**:
   - Analyze successful prompts
   - Generate new variants to test
   - Continuous experimentation loop

### Success Criteria

- ✅ System tests multiple prompt variants
- ✅ Performance metrics tracked per prompt
- ✅ Best prompt auto-selected
- ✅ New variants generated automatically

### Bonus

Implement "multi-armed bandit" algorithm for exploration vs exploitation balance.

---

## Challenge 5: Multi-Criteria Conditional Evaluation

**Difficulty**: Advanced | **Time**: 45 minutes

### The Pattern

Different content types require different evaluation criteria. Route to specialized judges based on content characteristics.

### Real-World Application

- **Content Hub**: Blog posts, social media, emails each judged differently
- **Industry Compliance**: Legal, medical, financial content has mandatory criteria
- **Audience Segmentation**: B2B vs B2C content evaluated with different priorities

### Implementation Steps

1. **Content Type Detection**:
   - Add LLM node to classify content type
   - Output: blog_post, social_media, email, technical_doc, marketing_copy

2. **Specialized Judge Routing**:

```javascript
// Define criteria sets per content type
const criteriaByType = {
  blog_post: {
    criteria: ['SEO_optimization', 'readability', 'engagement', 'structure'],
    threshold: 80,
    max_length: 1500
  },
  social_media: {
    criteria: ['virality', 'clarity', 'cta_strength', 'hashtag_quality'],
    threshold: 75,
    max_length: 280
  },
  email: {
    criteria: ['subject_line', 'personalization', 'clarity', 'cta'],
    threshold: 85,
    max_length: 300
  },
  technical_doc: {
    criteria: ['accuracy', 'completeness', 'code_examples', 'clarity'],
    threshold: 90,
    max_length: 2000
  }
};
```

**Dynamic Judge Prompts**:

- Load appropriate criteria for detected type
- Adjust weights and thresholds
- Use type-specific examples in judge prompt

**Type-Specific Validations**:

- Blog posts: Check for headers, bullet points, conclusion
- Social media: Validate character count, hashtag usage
- Emails: Verify subject line, personalization tokens
- Technical docs: Check for code blocks, error handling

### Success Criteria

- ✅ Content type auto-detected
- ✅ Appropriate judge criteria applied
- ✅ Type-specific validations pass
- ✅ Logging shows which criteria set used

---

## Putting It All Together: Production-Grade System

### The Ultimate Challenge

Combine all challenges into a production-ready content generation system:

1. **Multi-Variant Generation** (Challenge 1)
2. **Ensemble Judging** (Challenge 2)
3. **Adaptive Thresholds** (Challenge 3)
4. **Self-Optimizing Prompts** (Challenge 4)
5. **Smart Routing** (Challenge 5)

### Architecture

```mermaid
graph TB
    Input[Content Request] --> Classifier[Classify Type]
    Classifier --> PromptSelector[Select Best Prompt]
    PromptSelector --> MultiGen[Generate 5 Variants]
    MultiGen --> PreValidate[Pre-validate Common Issues]
    PreValidate --> Ensemble[3 Judge Ensemble]
    Ensemble --> Aggregate[Aggregate Scores]
    Aggregate --> Adaptive{Meets Adaptive Threshold?}
    Adaptive -->|Yes| Approve[Auto-Approve]
    Adaptive -->|No & Budget OK| Iterate[Regenerate with Feedback]
    Iterate --> MultiGen
    Approve --> Learn[Update Prompt Performance]
    Learn --> Analytics[Dashboard & Reports]
```

### Metrics to Track

- **Quality**: Average scores, pass rates
- **Efficiency**: Iterations to success, time per piece
- **Cost**: API spend per content, cost per quality point
- **Learning**: Prompt improvement, issue reduction

---

## Resources

### Learning Materials

- [Constitutional AI Paper](https://arxiv.org/abs/2212.08073) - Foundation for LLM as a Judge
- [RLAIF: Reinforcement Learning from AI Feedback](https://arxiv.org/abs/2309.00267)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Tools

- **n8n Community**: [community.n8n.io](https://community.n8n.io)
- **Prompt Testing**: [PromptFoo](https://promptfoo.dev/)
- **LLM Observability**: [Langfuse](https://langfuse.com/)

---

## Saving Your Work

After completing any challenge:

1. **Export Workflow**: In n8n, click ⋯ menu → Download → Save as JSON
2. **Commit to GitHub**: Save your workflow JSON files to your repository
3. **Document Changes**: Add notes explaining your approach and learnings

---

[← Back to Part B](./part-b-workflow){: .btn .mr-2 }
[Back to Exercise Overview](./index){: .btn }
