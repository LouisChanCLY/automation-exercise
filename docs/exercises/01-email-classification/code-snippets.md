# Code Snippets for Exercise 1

## JavaScript Code for Email Data Preparation

```javascript
// Extract and clean email data
const emailData = {
  sender: $input.item.json.from.value[0].address,
  senderName: $input.item.json.from.value[0].name || 'Unknown',
  subject: $input.item.json.subject,
  body: $input.item.json.text || $input.item.json.snippet,
  receivedDate: $input.item.json.date,
  messageId: $input.item.json.id,
  threadId: $input.item.json.threadId
};

// Clean body text (remove signatures, quotes)
emailData.cleanBody = emailData.body
  .split(/\r?\n-- \r?\n/)[0]  // Remove signature
  .split(/On .+ wrote:/)[0]    // Remove quoted text
  .trim();

// Truncate for API limits (first 1000 chars)
emailData.truncatedBody = emailData.cleanBody.substring(0, 1000);

return {
  json: emailData
};
```

## JSON Output Schema for AI Classification

```json
{
  "priority": "urgent|high|medium|low",
  "sentiment": "positive|neutral|negative|angry",
  "department": "sales|support|technical|hr|finance|other",
  "actionRequired": true,
  "confidence": 0.95,
  "reasoning": "Brief explanation of classification logic"
}
```

## AI Prompt Template

```text
Analyze this email and classify it. Return ONLY valid JSON.

Email from: {{$json.senderName}} <{{$json.sender}}>
Subject: {{$json.subject}}
Body: {{$json.truncatedBody}}

Classify as:
1. Priority: "urgent" | "high" | "medium" | "low"
2. Sentiment: "positive" | "neutral" | "negative" | "angry"
3. Department: "sales" | "support" | "technical" | "hr" | "finance" | "other"
4. Action Required: true | false
5. Confidence Score: 0.0-1.0
```

## Switch Node Routing Expression

```javascript
// For Urgent Priority Output
{{ $json.priority === 'urgent' }}

// For Angry Customer Output
{{ $json.sentiment === 'angry' }}

// For High Priority Support
{{ $json.priority === 'high' && $json.department === 'support' }}
```

## Google Sheets Data Mapping

```javascript
{
  "Timestamp": "={{ new Date().toISOString() }}",
  "Sender": "={{ $json.sender }}",
  "Subject": "={{ $json.subject }}",
  "Priority": "={{ $json.priority }}",
  "Sentiment": "={{ $json.sentiment }}",
  "Department": "={{ $json.department }}",
  "Action Required": "={{ $json.actionRequired }}",
  "Confidence": "={{ $json.confidence }}",
  "Reasoning": "={{ $json.reasoning }}"
}
```
