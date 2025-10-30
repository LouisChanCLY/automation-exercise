---
layout: default
title: Common Prerequisites
nav_order: 2
has_children: true
---

# Common Prerequisites & Service Setup

{: .fs-9 }

One-time setup guide for all services used across automation exercises.
{: .fs-6 .fw-300 }

[Start Setup](./google-setup){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Quick Checklist](./checklist){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Overview

Complete these prerequisites once, and you're ready for all 30+ exercises. This guide is broken into manageable sections that take 5-10 minutes each.

### What You'll Set Up

| Service | Purpose | Time |
|---------|---------|------|
| **[Google Cloud & OAuth](./google-setup)** | Authentication for Gmail, Sheets, Drive | 10 min |
| **[AI Services](./ai-services)** | OpenRouter, Gemini, Perplexity APIs | 10 min |
| **[n8n Platform](./n8n-setup)** | Workflow automation platform | 5 min |
| **[Credentials](./credentials)** | Connect everything in n8n | 10 min |
| **[GitHub Setup](./github-setup)** | Back up and version control workflows | 15 min |

{: .important }
> **Do This First**: These prerequisites are required before starting any exercise. Once configured, you won't need to repeat these steps.

---

## Setup Path

Follow this recommended order:

```mermaid
graph LR
    A[Google Cloud<br/>Setup] --> B[AI Services<br/>Setup]
    B --> C[n8n Platform<br/>Setup]
    C --> D[Add Credentials<br/>to n8n]
    D --> E[Verify<br/>Everything]

    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#f3e5f5
    style D fill:#e8f5e9
    style E fill:#c8e6c9
```

---

## Quick Navigation

<div class="grid">
  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🔐 Google & OAuth</h4>
      <p>Gmail, Sheets, Drive authentication</p>
      <a href="./google-setup">Configure →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🤖 AI Services</h4>
      <p>LLM APIs and research tools</p>
      <a href="./ai-services">Get API Keys →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>⚙️ n8n Platform</h4>
      <p>Workflow automation setup</p>
      <a href="./n8n-setup">Install →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🔗 Connect Everything</h4>
      <p>Add credentials to n8n</p>
      <a href="./credentials">Connect →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>📦 GitHub Setup</h4>
      <p>Back up your workflows</p>
      <a href="./github-setup">Set Up →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>✅ Verification</h4>
      <p>Test all connections</p>
      <a href="./verification">Verify →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🆘 Troubleshooting</h4>
      <p>Common issues & solutions</p>
      <a href="./troubleshooting">Get Help →</a>
    </div>
  </div>
</div>

---

## Why This Approach?

### OAuth Over App Passwords

{: .highlight }
> **Professional Best Practice**: OAuth provides better security, granular permissions, and works across all Google services with one setup. App passwords are deprecated and less secure.

### Benefits of Centralised Setup

- ✅ **One-time configuration** for all exercises
- ✅ **Single OAuth credential** for Gmail, Sheets, and Drive
- ✅ **Professional approach** suitable for production
- ✅ **Better security** with granular permissions
- ✅ **Easier troubleshooting** with clear separation

---

## Ready to Begin?

Start with Google Cloud setup - it's the foundation for everything else.

[Begin with Google Setup →](./google-setup){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }

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
