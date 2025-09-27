---
layout: default
title: "Exercise 1: Email Classification"
parent: Exercises
nav_order: 1
has_children: true
---

# Exercise 1: Email Classification System

{: .fs-9 }

Build an intelligent email classification system that automatically processes, categorizes, and routes emails using AI.
{: .fs-6 .fw-300 }

[Start Exercise](./overview){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Download Workflow](./downloads/email-classification-workflow.json){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 45-Minute Hands-On Exercise

This exercise teaches you to build a production-ready email automation system that combines Gmail, AI classification, and smart routing. Perfect for beginners, no coding experience required.

### What You'll Build

- **Real-time email monitoring** with Gmail API
- **AI-powered classification** using natural language processing
- **Intelligent routing system** based on priority and sentiment
- **Automated labeling** for inbox organization

### The Universal Pattern

You're learning the **Intelligent Triage & Routing** pattern:

```
[Data Source] → [AI Analysis] → [Smart Routing] → [Different Actions]
```

**Today's Implementation:**

- Gmail → AI Classification → Switch Node → Labels & Logging

**Tomorrow's Applications:**

- Support Tickets → Categorization → Priority Routing → Team Assignment
- Error Logs → Severity Analysis → Alert Rules → Incident Creation
- Documents → Content Type → Approval Flow → Processing Pipeline

### Exercise Structure

<div class="grid">
  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>📚 Overview</h4>
      <p>Understanding the why and how</p>
      <a href="./overview">Start here →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>⚙️ Part A: Setup</h4>
      <p>Environment & prerequisites (15 min)</p>
      <a href="./part-a-setup">Configure →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🔧 Part B: Build & Test</h4>
      <p>Create, test, and activate (25 min)</p>
      <a href="./part-b-workflow">Build →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🏆 Challenges</h4>
      <p>Advanced extensions (optional)</p>
      <a href="./challenge-tasks">Level up →</a>
    </div>
  </div>
</div>

---

## Quick Navigation

| Section | Description | Duration |
|---------|-------------|----------|
| [Overview](./overview) | Why this matters, learning outcomes, architecture | 5 min |
| [Part A: Setup](./part-a-setup) | Account creation, API configuration, prerequisites | 15 min |
| [Part B: Build & Test](./part-b-workflow) | Node creation, AI integration, testing, activation | 25 min |
| [Challenges](./challenge-tasks) | Multi-language, auto-reply, analytics | Optional |

---

<style>
.grid {
  display: flex;
  flex-wrap: wrap;
  margin: -0.5rem;
}

.col-4 {
  flex: 0 0 50%;
  padding: 0.5rem;
}

.card {
  background: #f7f7f7;
  border: 1px solid #e1e4e8;
  border-radius: 6px;
  padding: 1.5rem;
  height: 100%;
}

.card h4 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  color: #0366d6;
}

.card p {
  margin-bottom: 0.5rem;
  color: #586069;
}

.card a {
  font-weight: 600;
}

@media (max-width: 768px) {
  .col-4 {
    flex: 0 0 100%;
  }
}
</style>
