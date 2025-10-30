# Exercise 4: Workflow Downloads

This directory contains the workflow JSON files for Exercise 4: Connecting Workflows.

## Available Workflows

### 1. Email Response Generator (LLM-as-a-Judge)

**File**: `email-response-generator.json`

**Purpose**: Generates high-quality email responses using the LLM-as-a-judge pattern with iterative improvement.

**Features**:
- Two triggers: Form Trigger (for testing) and Execute Workflow Trigger (for master workflow calls)
- AI Generator agent that creates content
- AI Judge agent that evaluates quality
- Automatic retry loop (up to 10 iterations)
- Structured JSON output with pass/fail status

**Inputs** (when called by master workflow):
- `Task Description`: What response to generate
- `How to Do It (Instructions)`: How to write the response
- `Success Criteria (How to Measure)`: Quality standards

**Outputs**:
```json
{
  "status": "success" | "failed",
  "output": "Generated response text",
  "evaluation_result": true | false,
  "feedback": "Quality feedback",
  "retry_count": 2
}
```

**How to Import**:
1. In n8n, click **"..." menu** → **"Import from File"**
2. Select `email-response-generator.json`
3. Update Gemini API credentials
4. Activate the workflow

---

## Notes on the Dual-Trigger Pattern

### Why Each Workflow Has TWO Triggers

The Email Response Generator workflow includes **two separate triggers**:

1. **Form Trigger**: For standalone testing during development
2. **Execute Workflow Trigger**: For being called by the master workflow

### Why This Design?

**Problem**: You need to test workflows independently AND use them in a larger system.

**Solution**: Two triggers that serve different purposes:

#### During Development (Form Trigger)
- Access via web form URL
- Manually input test data
- Quickly iterate on prompts and logic
- Debug in isolation
- No need to run the entire email system

#### In Production (Execute Workflow Trigger)
- Activated when master workflow calls it
- Receives data programmatically
- No manual intervention needed
- Faster execution (no form rendering)
- Seamless integration

### How It Works

Only **ONE trigger activates per execution**:
- If you access the form URL → Form Trigger activates (walk-in customer)
- If master workflow calls it → Execute Workflow Trigger activates (catering order)

Think of it like a restaurant with two entrances:
- A **front door** (Form Trigger) for regular customers to walk in and order
- A **back door with an intercom** (Execute Workflow Trigger) for the head chef to request dishes for catering

### The Critical Role of "Execute Workflow Trigger"

Without the **"When Executed by Another Workflow"** trigger node, the workflow **cannot be called** by other workflows!

**Why?**
- Workflows need a "listening" point to receive requests from other workflows
- The Execute Workflow Trigger is that listening point (like the intercom speaker at the back door)
- It declares what information the workflow needs to receive
- It makes the workflow available for other workflows to use

**Think of it like a phone system:**

**WITHOUT Execute Workflow Trigger (doesn't work):**
- You have a specialized team (response generator)
- But they don't have a phone
- The manager (master workflow) can't call them for help
- The team can only work when they walk in themselves

**WITH Execute Workflow Trigger (works!):**
- The specialized team has a phone (Execute Workflow Trigger)
- The phone rings when the manager needs their help
- The manager can tell them exactly what's needed
- The team does the work and calls back with the results
- Everyone can work together efficiently!

### Best Practice

Always include both triggers in reusable workflows:
1. **Form Trigger**: For testing and manual use
2. **Execute Workflow Trigger**: For automation and workflow composition

This makes your workflows:
- ✅ Testable independently
- ✅ Reusable across multiple master workflows
- ✅ Easy to debug
- ✅ Production-ready

---

## Additional Workflows

### Email Classifier Workflow

**Status**: Build manually following Part B instructions

This workflow should be built following the step-by-step instructions in Part B. It includes:
- Form Trigger for testing
- Execute Workflow Trigger for master workflow calls
- AI classification logic
- Structured output (category, priority, sentiment)

### Master Email Orchestrator

**Status**: Build manually following Part B instructions

This is the main workflow that ties everything together. It includes:
- Gmail Trigger
- Execute Workflow nodes to call sub-workflows
- Data formatting and preparation
- Email sending logic

---

## Import Instructions

### Step 1: Import Response Generator

1. Download `email-response-generator.json`
2. In n8n: **Workflows** → **"..." menu** → **Import from File**
3. Select the JSON file
4. Rename if desired: `Email Response Generator`

### Step 2: Configure Credentials

1. Update Google Gemini API credentials:
   - Click on "Google Gemini Model" node
   - Select your Gemini API credential
   - Repeat for "Google Gemini Judge Model" node

2. Save the workflow

### Step 3: Activate

1. Click the **"Active"** toggle to activate
2. Test using the Form Trigger URL
3. Verify it can be called by other workflows

### Step 4: Build Other Workflows

Follow the instructions in Part B to build:
- Email Classifier workflow
- Master Email Orchestrator workflow

---

## Testing Your Imported Workflows

### Test Response Generator Standalone

1. Open the workflow
2. Click on "Form Trigger" node
3. Copy the **"Test URL"**
4. Open URL in browser
5. Submit test form:
   - **Task**: `Write a thank you email to a customer`
   - **Instructions**: `Professional, warm tone. Mention specific achievement. 100-150 words.`
   - **Criteria**: `Must be professional, specific, 100-150 words, grammatically perfect`
6. Wait for response (10-30 seconds)
7. Verify you receive quality-controlled output

### Test Response Generator from Another Workflow

1. Create a test workflow with **Manual Trigger**
2. Add **Execute Workflow** node
3. Select `Email Response Generator`
4. Configure inputs:
   ```
   Task Description: "Write a support email"
   How to Do It: "Empathetic, helpful, provide steps"
   Success Criteria: "Professional, helpful, clear steps"
   ```
5. Execute and verify response is returned

---

## Troubleshooting

### "Workflow not found" Error

**Cause**: Response Generator workflow is not activated

**Solution**:
1. Open the Response Generator workflow
2. Click **"Active"** toggle
3. Try calling it again

### "Missing credentials" Error

**Cause**: Gemini API credentials not configured

**Solution**:
1. Go to **Credentials** in n8n
2. Add "Google PaLM API" credential with your Gemini API key
3. Update nodes to use this credential

### "No trigger found" Error

**Cause**: Execute Workflow Trigger is missing or misconfigured

**Solution**:
1. Verify "When Executed by Another Workflow" node exists
2. Check that workflow inputs are defined:
   - Task Description
   - How to Do It (Instructions)
   - Success Criteria (How to Measure)

### Workflow Returns No Data

**Cause**: Last node doesn't output data

**Solution**:
1. Ensure the workflow ends with a node that outputs data
2. In Response Generator, it should be "Edit Fields2" node
3. Test the workflow standalone first

---

## Next Steps

After importing and configuring:

1. ✅ Test Response Generator standalone (Form Trigger)
2. ✅ Test Response Generator via Execute Workflow
3. 🔨 Build Email Classifier (follow Part B)
4. 🔨 Build Master Orchestrator (follow Part B)
5. ✅ Connect all three workflows
6. ✅ Test end-to-end email automation

---

[Back to Exercise 4](../index) | [Part B: Build Instructions](../part-b-workflow)
