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

[Start Setup](./n8n-setup){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }

---

## Overview

Complete these prerequisites once, and you're ready for all 30+ exercises. This guide is broken into manageable sections that take 5-10 minutes each.

### What You'll Set Up

| Service | Purpose | Time |
|---------|---------|------|
| **[n8n Platform](./n8n-setup)** | Workflow automation platform | 5 min |
| **[Google Services](./google-setup)** | Connect Gmail & Sheets via n8n | 5 min |
| **[AI Services](./ai-services)** | Connect OpenRouter, Gemini, Perplexity | 10 min |
| **[GitHub Setup](./github-setup)** | Save workflows online | 10 min |

{: .important }
> **Do This First**: These prerequisites are required before starting any exercise. Once configured, you won't need to repeat these steps.

---

## Setup Path

Follow this recommended order:

```mermaid
graph LR
    A[n8n Platform<br/>Setup] --> B[Google Services<br/>Gmail & Sheets]
    B --> C[AI Services<br/>OpenRouter, Gemini, Perplexity]
    C --> D[Start Building<br/>Workflows]

    style A fill:#f3e5f5
    style B fill:#e1f5fe
    style C fill:#fff3e0
    style D fill:#c8e6c9
```

---

## Quick Navigation

<div class="grid">
  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>⚙️ n8n Platform</h4>
      <p>Workflow automation setup</p>
      <a href="./n8n-setup">Install →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🔐 Google Services</h4>
      <p>Gmail & Sheets via n8n OAuth</p>
      <a href="./google-setup">Connect →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>🤖 AI Services</h4>
      <p>OpenRouter, Gemini, Perplexity</p>
      <a href="./ai-services">Setup →</a>
    </div>
  </div>

  <div class="col-4 col-md-4 col-lg-4">
    <div class="card">
      <h4>📦 GitHub Setup</h4>
      <p>Save your workflows online</p>
      <a href="./github-setup">Configure →</a>
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

Start with n8n platform setup - it's the foundation for everything else.

[Begin with n8n Setup →](./n8n-setup){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }

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
