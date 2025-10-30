---
layout: default
title: "Exercise 3: LLM as a Judge"
parent: Exercises
nav_order: 3
has_children: true
---

# Exercise 3: LLM as a Judge System

{: .fs-9 }

Build an AI quality control system where one LLM generates content and another LLM evaluates it, providing feedback and iterating until quality standards are met.
{: .fs-6 .fw-300 }

[Start Exercise](./overview){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Download Workflow](./downloads/llm-judge-workflow.json){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 60-Minute Hands-On Exercise

This exercise teaches you to build a self-improving content generation system using the "LLM as a Judge" pattern. Learn how to create AI workflows that evaluate and iterate on their own output until quality standards are met.

### What You'll Build

- **Web form interface** for task submission
- **Content generation** with Google Gemini AI
- **Quality evaluation** using a strict judge AI
- **Iterative improvement** with feedback loops (up to 10 retries)
- **Form-based output** with immediate results
- **Loop control** with pass/fail criteria

### The Universal Pattern

You're learning the **AI Quality Control & Iteration** pattern:

```mermaid
graph LR
    A[Generate Content] --> B[Evaluate Quality]
    B --> C{Pass?}
    C -->|No| D[Provide Feedback]
    D --> A
    C -->|Yes| E[Final Output]

    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#f3e5f5
    style E fill:#e8f5e9
```

**Today's Implementation:**

```mermaid
graph LR
    A1[Form Input] --> B1[Generator AI]
    B1 --> C1[Judge AI]
    C1 --> D1{Pass?}
    D1 -->|No & < 10| E1[Feedback Loop]
    E1 --> B1
    D1 -->|Yes| F1[Return to Form]
    D1 -->|No & = 10| F1
```

**Tomorrow's Applications:**

```mermaid
graph TD
    subgraph "Content Marketing"
        CM[Generate Copy] --> CE[Evaluate Brand Voice]
        CE --> CI[Iterate Until Perfect]
    end

    subgraph "Code Review"
        CG[Generate Code] --> CR[Review Quality]
        CR --> CF[Fix Issues]
    end

    subgraph "Customer Service"
        RG[Generate Response] --> RS[Check Tone/Accuracy]
        RS --> RR[Refine Message]
    end
```

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
      <p>Create, test, and activate (40 min)</p>
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
| [Part A: Setup](./part-a-setup) | Prerequisites check, Google Sheets setup | 15 min |
| [Part B: Build & Test](./part-b-workflow) | Build generator, judge, loop logic, and test | 40 min |
| [Challenges](./challenge-tasks) | Multi-criteria evaluation, A/B testing, prompt optimization | Optional |

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
