---
layout: default
title: "Exercise 2: AI Cold Email Automation"
parent: Exercises
nav_order: 2
has_children: true
---

# Exercise 2: AI-Powered Cold Email System

{: .fs-9 }

Build an intelligent cold email system that researches prospects and generates personalized outreach at scale.
{: .fs-6 .fw-300 }

[Start Exercise](./overview){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Download Workflow](./downloads/cold-email-automation.json){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 60-Minute Hands-On Exercise

This exercise teaches you to build an AI-powered cold outreach system that combines research, personalization, and automation. Perfect for sales teams, recruiters, and networkers.

### What You'll Build

- **Web form** for lead capture and campaign initiation
- **AI research agent** using Perplexity for prospect intelligence
- **Personalized email generator** with structured components
- **Automated sending** via Gmail with full tracking
- **Analytics dashboard** in Google Sheets

### The Universal Pattern

You're learning the **AI Research & Personalization** pattern:

```mermaid
graph LR
    A[Input] --> B[AI Research]
    B --> C[AI Generation]
    C --> D[Action]
    D --> E[Analytics]

    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#fff3e0
    style D fill:#f3e5f5
    style E fill:#e8f5e9
```

**Today's Implementation:**

```mermaid
graph LR
    F[Form] --> PR[Perplexity Research]
    PR --> EG[Email Generation]
    EG --> GS[Gmail Send]
    GS --> SL[Sheets Log]
```

**Tomorrow's Applications:**

```mermaid
graph TD
    subgraph "LinkedIn Outreach"
        LP[LinkedIn Profile] --> CR1[Company Research]
        CR1 --> CNR[Connection Request]
        CNR --> CRM[CRM Update]
    end

    subgraph "Job Applications"
        JP[Job Posting] --> CCR[Company Culture Research]
        CCR --> CL[Cover Letter]
        CL --> AS[Application Submit]
    end

    subgraph "Sales Pipeline"
        CD[Customer Data] --> MR[Market Research]
        MR --> PG[Proposal Generation]
        PG --> SN[Slack Notification]
    end

    subgraph "Event Follow-up"
        ER[Event Registration] --> AR[Attendee Research]
        AR --> PF[Personalised Follow-up]
        PF --> DE[Database Entry]
    end
```

### Exercise Structure

<div class="grid">
  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>📚 Overview</h4>
      <p>Understanding AI agents and research automation</p>
      <a href="./overview">Start here →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>⚙️ Part A: Setup</h4>
      <p>API keys & environment (20 min)</p>
      <a href="./part-a-setup">Configure →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🔧 Part B: Build & Test</h4>
      <p>Create, test, and activate (35 min)</p>
      <a href="./part-b-workflow">Build →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🏆 Challenges</h4>
      <p>Advanced personalization (optional)</p>
      <a href="./challenge-tasks">Level up →</a>
    </div>
  </div>
</div>

---

## Quick Navigation

| Section | Description | Duration |
|---------|-------------|----------|
| [Overview](./overview) | Why AI agents matter, learning outcomes, architecture | 5 min |
| [Part A: Setup](./part-a-setup) | Perplexity API, Gmail, Google Sheets setup | 20 min |
| [Part B: Build & Test](./part-b-workflow) | Agent configuration, prompt engineering, testing | 35 min |
| [Challenges](./challenge-tasks) | Multi-channel outreach, A/B testing, follow-ups | Optional |

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
