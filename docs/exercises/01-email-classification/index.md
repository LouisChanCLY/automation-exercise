---
layout: default
title: "Exercise 1: Email Classification"
parent: Exercises
nav_order: 1
has_children: true
---

# Exercise 1: Email Classification System

{: .fs-9 }

Build an intelligent email classification system that automatically processes, categorises, and routes emails using AI.
{: .fs-6 .fw-300 }

---

## 45-Minute Hands-On Exercise

This exercise teaches you **dynamic routing** - a fundamental automation pattern where different situations get handled differently automatically. Perfect for beginners, no coding experience required.

**The Problem:** Professionals receive 50-150 emails daily. Manual sorting is time-consuming, important messages get buried, and urgent requests slip through. You need an intelligent system that automatically understands and routes emails based on content, not just rules.

**Why Dynamic Routing Matters:**

Instead of one giant AI trying to handle everything, you'll learn to **divide and conquer**:

- ✅ **More reliable**: Simpler logic means fewer failures
- ✅ **Faster**: Each AI handles one specific task, not everything
- ✅ **Easier to debug**: Know exactly which step failed
- ✅ **Easy to enhance**: Add new categories without breaking existing logic

This is how professional automations work in the real world.

### What You'll Build

A complete automation workflow featuring:

- **Real-time email monitoring** with Gmail API
- **AI-powered classification** using natural language processing
- **Intelligent routing system** based on priority and sentiment
- **Automated labelling** for inbox organisation
- **Analytics logging** to Google Sheets

```mermaid
graph LR
    A[Gmail Inbox] --> B[AI Classifier]
    B --> C[Smart Router]
    C --> D[Labels & Logging]

    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#f3e5f5
    style D fill:#e8f5e9
```

### Skills You'll Demonstrate

By completing this exercise, you will have demonstrated:

- **AI Integration**: Connecting and using language models for text classification
- **API Orchestration**: Working with Gmail API, AI services, and Google Sheets
- **Workflow Design**: Building multi-step automation with conditional logic
- **Data Processing**: Extracting, transforming, and routing information

### The Pattern You'll Master

The **Intelligent Triage & Routing** pattern you'll learn applies to:

- **Customer Support**: Categorise tickets, assign priority, route to specialists
- **Error Monitoring**: Analyse logs, determine severity, trigger alerts
- **Document Processing**: Classify documents, route for approval, track workflow
- **Social Media**: Monitor mentions, detect sentiment, escalate issues
- **Lead Qualification**: Score leads, categorise inquiries, assign to sales team

### Exercise Structure

<div class="grid">
  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>⚙️ Part A: Setup</h4>
      <p>Environment & prerequisites (15 min)</p>
      <a href="./part-a-setup">Start here →</a>
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
