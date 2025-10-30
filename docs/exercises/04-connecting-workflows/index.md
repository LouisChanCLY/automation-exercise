---
layout: default
title: "Exercise 4: Connecting Workflows"
parent: Exercises
nav_order: 4
has_children: true
---

# Exercise 4: Connecting Multiple Workflows

{: .fs-9 }

Build an intelligent email response system by connecting three separate workflows together: a master orchestrator, an email classifier, and an LLM-as-a-judge response generator.
{: .fs-6 .fw-300 }

[Start Exercise](./overview){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Download Workflows](./downloads/){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 75-Minute Hands-On Exercise

This exercise teaches you to build complex automation systems by connecting multiple workflows together. Learn how to create modular, reusable workflows that can call each other, passing data between them to solve complex business problems.

### What You'll Build

- **Master orchestrator workflow** that fetches emails and coordinates other workflows
- **Email classification workflow** that categorizes incoming emails
- **LLM-as-a-judge response generator** that creates high-quality email replies
- **Workflow triggers** that allow workflows to call each other
- **Data passing** between workflows with structured inputs/outputs
- **End-to-end automation** that handles the entire email response process

### The Universal Pattern

You're learning the **Workflow Orchestration & Composition** pattern - think of it like a restaurant kitchen:

```mermaid
graph LR
    A[Master Workflow] --> B[Sub-Workflow 1]
    A --> C[Sub-Workflow 2]
    B --> D[Process Data]
    C --> D
    D --> E[Master Workflow]
    E --> F[Final Action]

    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#fff3e0
    style E fill:#e1f5fe
    style F fill:#e8f5e9
```

Just like a head chef (Master Workflow) coordinates with specialized stations (Sub-Workflows):
- The prep station chops vegetables (Classifier)
- The main kitchen cooks the dish (Response Generator)
- The head chef plates and serves (Final Action)

**Today's Implementation:**

```mermaid
graph TB
    A[Master: Fetch Email] --> B[Call Classifier Workflow]
    B --> C[Receive Classification]
    C --> D[Call Response Generator Workflow]
    D --> E[Receive Generated Response]
    E --> F[Master: Send Reply]

    style A fill:#e1f5fe
    style B fill:#fff3e0
    style D fill:#ffecb3
    style F fill:#e8f5e9
```

**Tomorrow's Applications:**

```mermaid
graph TD
    subgraph "Customer Support"
        CS[Ticket Router] --> CT[Classify Ticket]
        CT --> CR[Generate Response]
        CR --> CS2[Send & Track]
    end

    subgraph "Content Pipeline"
        CP[Content Planner] --> CG[Generate Content]
        CG --> CQ[Quality Check]
        CQ --> CP2[Publish]
    end

    subgraph "Data Processing"
        DP[Data Ingest] --> DT[Transform Data]
        DT --> DV[Validate Data]
        DV --> DS[Store Data]
    end
```

### Exercise Structure

<div class="grid">
  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>📚 Overview</h4>
      <p>Understanding workflow composition</p>
      <a href="./overview">Start here →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>⚙️ Part A: Setup</h4>
      <p>Prerequisites & configuration (15 min)</p>
      <a href="./part-a-setup">Configure →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🔧 Part B: Build & Test</h4>
      <p>Create workflows and connections (55 min)</p>
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
| [Overview](./overview) | Why workflow composition matters, architecture | 5 min |
| [Part A: Setup](./part-a-setup) | Prerequisites, API setup | 15 min |
| [Part B: Build & Test](./part-b-workflow) | Build three workflows and connect them | 55 min |
| [Challenges](./challenge-tasks) | Error handling, parallel execution, monitoring | Optional |

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
