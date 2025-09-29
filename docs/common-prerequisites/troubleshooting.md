---
layout: default
title: Troubleshooting
parent: Common Prerequisites
nav_order: 6
---

# Troubleshooting Guide

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Google OAuth Issues

### "Access blocked: This app is blocked"

**Cause**: Email not in test users list

**Solution**:

1. Go to Google Cloud Console
2. APIs & Services → OAuth consent screen
3. Add your email to "Test users"
4. Try connecting again

---

### "Error 400: redirect_uri_mismatch"

**Cause**: n8n URL doesn't match Google's whitelist

**Solution**:

1. Copy the exact error URL shown
2. Google Cloud Console → Credentials
3. Edit your OAuth client
4. Add the exact redirect URI
5. Save and retry

**Common URIs to add**:

```
http://localhost:5678/rest/oauth2-credential/callback
https://[your-workspace].app.n8n.cloud/rest/oauth2-credential/callback
```

---

### "Insufficient permission" or "Scope not authorised"

**Cause**: Missing API scopes

**Solution**:

1. OAuth consent screen → Scopes
2. Add these scopes:
   - `gmail.modify`
   - `gmail.labels`
   - `spreadsheets`
   - `drive.file`
3. Remove and re-add credential in n8n
4. Re-authorise

---

## API Key Problems

### "Invalid API key" (Any Service)

**Common Causes & Fixes**:

| Issue | Check This |
|-------|-----------|
| Extra spaces | Remove spaces before/after key |
| Wrong key | Verify you copied the API key, not ID |
| Expired key | Regenerate in service dashboard |
| Wrong project | Ensure key is from correct project |

---

### "Quota exceeded" Errors

#### Google Services

**Gmail**: 250 quota units/second

- Solution: Add delays between operations
- Use batch operations where possible

**Sheets**: 100 requests/100 seconds

- Solution: Combine multiple operations
- Use append instead of multiple writes

#### AI Services

**Gemini**: 60 requests/minute

- Solution: Add 1-second delay between calls
- Upgrade to paid tier if needed

**OpenRouter**: Limited by credits

- Solution: Use free models (Gemma, Llama)
- Add credits if needed

---

## n8n Connection Issues

### "ECONNREFUSED" or Cannot Connect

**For Cloud Users**:

- Check internet connection
- Clear browser cache
- Try incognito mode
- Check if n8n.cloud is down

**For Self-Hosted**:

```bash
# Check if n8n is running
docker ps | grep n8n

# View logs
docker logs n8n

# Restart n8n
docker restart n8n
```

---

### Workflow Execution Errors

#### "Timeout" Errors

**Cause**: Operation taking too long

**Solutions**:

1. Settings → Workflow Settings
2. Increase timeout (default 5 min)
3. Break workflow into smaller parts
4. Add error handling

#### "Memory" Errors

**Cause**: Processing too much data

**Solutions**:

1. Limit data fetched (use pagination)
2. Process in batches
3. Upgrade n8n instance
4. Clear execution history

---

## Credential Test Failures

### Google Services Not Connecting

**Quick Fix Checklist**:

1. [ ] APIs enabled in Google Cloud?
2. [ ] OAuth consent configured?
3. [ ] Client ID/Secret correct?
4. [ ] Redirect URI matches?
5. [ ] Test user added?

**Reset Process**:

1. Delete credential in n8n
2. Revoke access in Google Account
3. Create new OAuth credentials
4. Re-add to n8n

---

### AI Services Not Responding

#### OpenRouter

```bash
# Test with curl
curl https://openrouter.ai/api/v1/models \
  -H "Authorization: Bearer YOUR_KEY"
```

Should return model list

#### Gemini

```bash
# Test with curl
curl "https://generativelanguage.googleapis.com/v1/models?key=YOUR_KEY"
```

Should return available models

#### Perplexity

```bash
# Test with curl
curl -X POST https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"sonar","messages":[{"role":"user","content":"test"}]}'
```

Should return response

---

## Common Error Messages

### Quick Reference Table

| Error | Service | Solution |
|-------|---------|----------|
| "Invalid credentials" | Any | Regenerate and update |
| "Rate limited" | Any API | Wait and retry |
| "Unauthorised" | Google | Re-authorise OAuth |
| "No data found" | Sheets | Check sheet exists |
| "Label not found" | Gmail | Create label first |
| "Model not found" | AI | Check model name |
| "Insufficient credits" | OpenRouter | Use free models |

---

## Getting Help

### Support Channels

1. **n8n Community**: [community.n8n.io](https://community.n8n.io)
   - Search existing issues
   - Post with workflow JSON
   - Include error messages

2. **Google Cloud Support**: [cloud.google.com/support](https://cloud.google.com/support)
   - Check service status
   - API documentation

3. **Course Support**:
   - Create issue in course repository
   - Include exercise number
   - Attach screenshots

### Information to Provide

When asking for help, include:

- Exercise number
- Error message (exact)
- Screenshot of issue
- Workflow JSON export
- What you've already tried

---

## Prevention Tips

### Avoid Future Issues

1. **Test incrementally** - Don't build entire workflow at once
2. **Save credentials** - Export for backup
3. **Document changes** - Note what worked
4. **Monitor quotas** - Set up alerts
5. **Use test data** - Don't test with production

---

## Still Stuck?

If you've tried everything:

1. Export your workflow
2. Document the exact error
3. Note what step fails
4. Post in community forum
5. Tag with #prerequisites

The community is helpful and responsive!

---

[Back to Prerequisites Overview →](./){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 }
