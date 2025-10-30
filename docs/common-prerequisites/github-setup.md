---
layout: default
title: GitHub Setup
parent: Common Prerequisites
nav_order: 5
---

# GitHub Setup

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Set up GitHub to save your n8n workflow files online. Think of GitHub like Google Drive, but made for workflow files.

**Time Required**: 15 minutes

{: .important }
> **Why GitHub?**: Save your workflows online so you don't lose them. You can also share them with others.

{: .highlight }
> **Simple Point-and-Click**: This guide uses GitHub Desktop, a simple app. No coding knowledge needed!

---

## What You'll Learn

- ✅ Create a free GitHub account
- ✅ Install GitHub Desktop (simple app)
- ✅ Create a folder for your workflows
- ✅ Save your workflows online

---

## Part 1: Create a GitHub Account

### Step-by-Step Account Creation

1. **Go to GitHub**
   - Visit [github.com](https://github.com)
   - Click "Sign up" in the top-right corner

2. **Enter Your Email**
   - Use an email you check regularly
   - You'll need to verify it later
   - Click "Continue"

3. **Create a Password**
   - Use a strong password (at least 15 characters)
   - Mix uppercase, lowercase, numbers, and symbols
   - Click "Continue"

4. **Choose a Username**
   - This will be your public identity (e.g., `john-smith-automation`)
   - Can only contain letters, numbers, and hyphens
   - Pick something professional (you might use this for work!)
   - Click "Continue"

5. **Verify You're Human**
   - Complete the puzzle or challenge
   - Click "Create account"

6. **Verify Your Email**
   - Check your email for a code from GitHub
   - Enter the 6-digit code
   - Your account is now active!

{: .highlight }
> **Success**: You now have a GitHub account! Bookmark `github.com/[your-username]` - this is your profile page.

---

## Part 2: Install GitHub Desktop

GitHub Desktop is a free application that makes working with Git simple - just click buttons instead of typing commands!

### Download and Install

#### For Windows

1. **Download GitHub Desktop**
   - Go to [desktop.github.com](https://desktop.github.com)
   - Click "Download for Windows"
   - File downloads: `GitHubDesktopSetup.exe`

2. **Install**
   - Double-click the downloaded file
   - Installation runs automatically (no choices needed!)
   - GitHub Desktop opens when complete

3. **Sign in to GitHub**
   - Click "Sign in to GitHub.com"
   - Enter your GitHub username and password
   - Click "Authorize desktop"
   - Your browser opens → Click "Authorize"
   - Return to GitHub Desktop

4. **Enter Your Information**
   - **Name**: Your name
   - **Email**: Same email you used for GitHub
   - Click "Finish"

{: .highlight }
> **Success!** GitHub Desktop is installed and ready to use.

---

#### For macOS

1. **Download GitHub Desktop**
   - Go to [desktop.github.com](https://desktop.github.com)
   - Click "Download for macOS"
   - File downloads: `GitHubDesktop-arm64.dmg` or `GitHubDesktop-x64.dmg`

2. **Install**
   - Open the downloaded `.dmg` file
   - Drag GitHub Desktop to Applications folder
   - Open Applications → Double-click GitHub Desktop
   - Click "Open" when macOS asks for confirmation

3. **Sign in to GitHub**
   - Click "Sign in to GitHub.com"
   - Enter your GitHub username and password
   - Click "Authorize desktop"
   - Your browser opens → Click "Authorize"
   - Return to GitHub Desktop

4. **Enter Your Information**
   - **Name**: Your name
   - **Email**: Same email you used for GitHub
   - Click "Finish"

{: .highlight }
> **Success!** GitHub Desktop is installed and ready to use.

---

## Part 3: Create Your First Folder

A repository (or "repo") is like a folder on GitHub where you'll save your workflows.

### Create and Publish Repository

1. **Open GitHub Desktop**

2. **Create New Repository**
   - Click "File" → "New repository"
   - Or press `Ctrl+N` (Windows) / `Cmd+N` (macOS)

3. **Fill in Repository Details**:

   **Name**: `n8n-workflows`

   **Description**: `My n8n automation workflow backups`

   **Local Path**: Where to save on your computer
   - **Windows Default**: `C:\Users\[YourName]\Documents\GitHub`
   - **macOS Default**: `/Users/[YourName]/Documents/GitHub`
   - Click "Choose..." to pick a different location

   **Initialize this repository with a README**: ✅ Check this box

   **Git Ignore**: None

   **License**: MIT License (optional, good for open-source)

4. **Create Repository**
   - Click "Create repository"
   - Your repository is created on your computer!

5. **Publish to GitHub**
   - Look for the "Publish repository" button at the top
   - A window appears with options:
     - **Name**: `n8n-workflows` (already filled)
     - **Description**: (already filled)
     - **Keep this code private**: ✅ Check this if your workflows contain sensitive info
     - Leave unchecked if you want to share your learning publicly
   - Click "Publish repository"
   - Your repository is now on GitHub!

{: .highlight }
> **Quick Tip**: Click "Repository" → "Show in Explorer" (Windows) or "Show in Finder" (macOS) to see your repository folder.

{: .important }
> **Public vs Private**: Choose Private if your workflows will contain API keys or sensitive data. Choose Public if you want to build a portfolio and share your learning.

---

## Part 4: Save Your First Workflow to GitHub

Now let's back up an n8n workflow!

### Step 1: Export Workflow from n8n

1. **Open Your Workflow in n8n**
   - Go to your n8n instance
   - Open any workflow you've created

2. **Download the Workflow**
   - Click the "⋮" menu (three dots) in the top-right
   - Select "Download"
   - Your browser downloads a `.json` file (e.g., `My_workflow.json`)

3. **Find the Downloaded File**
   - Usually in your Downloads folder
   - Optionally rename it to something descriptive:
     - `email-classification.json`
     - `llm-judge-workflow.json`

---

### Step 2: Organize Your Workflows (Recommended)

Create folders to organize your workflows by exercise:

1. **Open Your Repository Folder**
   - In GitHub Desktop, click "Repository" → "Show in Explorer/Finder"
   - This opens your `n8n-workflows` folder

2. **Create Folder Structure**
   - Create a new folder called `exercises`
   - Inside `exercises`, create: `01-email-classification`
   - You can create more as needed: `02-cold-email`, `03-llm-judge`, etc.

3. **Move Your Workflow File**
   - Move the downloaded JSON file from Downloads
   - Put it in the appropriate exercise folder
   - Example: `n8n-workflows/exercises/01-email-classification/workflow.json`

**Your folder structure should look like:**
```
n8n-workflows/
├── README.md
└── exercises/
    ├── 01-email-classification/
    │   └── workflow.json
    ├── 02-cold-email/
    │   └── workflow.json
    └── 03-llm-judge/
        └── workflow.json
```

---

### Step 3: Commit and Push to GitHub

Now let's save these changes to GitHub!

1. **Open GitHub Desktop**
   - GitHub Desktop automatically detects the new file!
   - You'll see it listed under "Changes" on the left side

2. **Review Your Changes**
   - **Left panel**: Shows all files that changed
     - ✓ `exercises/01-email-classification/workflow.json`
   - **Right panel**: Shows what was added (in green)
   - Click on a file name to see details

3. **Write a Short Description**
   - Look at the bottom-left corner
   - Type a simple description like: `Add email workflow`

4. **Save to GitHub**
   - Click the blue "Commit to **main**" button
   - Then click "Push origin" at the top
   - Wait a few seconds for the upload

6. **Verify on GitHub**
   - Click "Repository" → "View on GitHub"
   - Your browser opens showing your repository
   - You should see your new `exercises` folder and workflow file!

{: .highlight }
> **Congratulations!** You've backed up your first workflow to GitHub. It's now safely stored in the cloud with full version history!

---

## Part 5: How to Save Workflows

Follow these simple steps each time you complete a workflow:

**1. Download from n8n**
- Open your workflow in n8n
- Click ⋮ menu → Download
- Save the JSON file

**2. Move to Your Folder**
- Move the file from Downloads
- Put it in your exercise folder in `n8n-workflows`

**3. Open GitHub Desktop**
- GitHub Desktop will automatically see the new file

**4. Save It**
- Write a simple description (e.g., `Add Exercise 1`)
- Click "Commit to main"
- Click "Push origin"
- Done! ✅

{: .highlight }
> **That's it!** Takes about 30 seconds once you get the hang of it.


---

## What You've Accomplished

✅ Created a GitHub account
✅ Installed GitHub Desktop
✅ Created a folder for your workflows
✅ Saved your first workflow online

---

## Next Steps

Now that GitHub is set up:

1. **Continue with Other Prerequisites**
   - Set up the other services you'll need
   - [Back to Prerequisites →](./index)

2. **Start the Exercises**
   - Begin building workflows
   - Save each workflow to GitHub
   - [View All Exercises →](../exercises/)

---

[← Back to Prerequisites](./index){: .btn }
