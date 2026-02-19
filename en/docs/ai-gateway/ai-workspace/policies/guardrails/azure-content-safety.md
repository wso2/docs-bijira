# Azure Content Safety

The Azure Content Safety guardrail integrates with the [Azure Content Safety Content Moderation API](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview) to filter harmful content in requests and LLM-generated responses. It checks for four categories of harmful content — hate speech, sexual content, self-harm, and violence — each with a configurable severity threshold.

!!! info "Prerequisites"
    This guardrail requires an active Azure subscription with the Azure Content Safety service enabled.

    1. In the [Azure Portal](https://portal.azure.com), search for **Content Safety** and create a new resource.
    2. After the resource is created, open it and go to **Keys and Endpoint**.
    3. Copy the **Endpoint URL** and one of the **API Keys**.

    These are entered directly in the guardrail configuration form. No separate setup is required in the AI Workspace.

## Configuration Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Guardrail Name** | Yes | A unique name for this guardrail instance. Used for tracking and in intervention responses. |
| **Azure Content Safety Endpoint** | Yes | The endpoint URL for your Azure Content Safety resource (e.g., `https://your-resource.cognitiveservices.azure.com`). |
| **Azure Content Safety Key** | Yes | The API key for authenticating with the Azure Content Safety service. |
| **Hate Severity Level** | Yes | The threshold severity level for hate speech (0–7). Content at or above this level is blocked. Lower values are more permissive. |
| **Sexual Severity Level** | Yes | The threshold severity level for sexual content (0–7). Content at or above this level is blocked. |
| **Self Harm Severity Level** | Yes | The threshold severity level for self-harm content (0–7). Content at or above this level is blocked. |
| **Violence Severity Level** | Yes | The threshold severity level for violence content (0–7). Content at or above this level is blocked. |
| **JSON Path** | No | A JSONPath expression to extract the field to validate (e.g., `$.messages[0].content`). If not specified, the entire payload is sent to Azure for evaluation. |
| **Passthrough On Error** | No | When enabled, requests or responses pass through if the Azure Content Safety service is unavailable. When disabled, an error is returned if the service cannot be reached. |
| **Show Guardrail Assessment** | No | When enabled, the intervention response includes the detailed category scores from Azure. |

### Severity Levels

Azure Content Safety returns severity scores from 0 to 7 for each category:

| Score | Meaning |
|-------|---------|
| 0–1 | Safe or negligible |
| 2–3 | Low severity |
| 4–5 | Medium severity |
| 6–7 | High severity |

Set the threshold to match your content policy. For example, a threshold of `4` blocks content with medium or high severity.

## Add This Guardrail

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **Azure Content Safety Content Moderation** from the sidebar.
5. Fill in the Azure endpoint, API key, and severity thresholds.
6. Configure the JSON Path and error handling options.
7. Click **Add** (for providers) or **Submit** (for proxies).
8. Deploy the provider or proxy to apply the changes.

## Example Configuration

| Parameter | Value |
|-----------|-------|
| Guardrail Name | `Azure Safety Filter` |
| Azure Content Safety Endpoint | `https://my-safety-resource.cognitiveservices.azure.com` |
| Azure Content Safety Key | `abc123...` |
| Hate Severity Level | `3` |
| Sexual Severity Level | `3` |
| Self Harm Severity Level | `2` |
| Violence Severity Level | `4` |
| JSON Path | `$.messages[0].content` |
| Passthrough On Error | `false` |
| Show Guardrail Assessment | `true` |

**Sample request that would be blocked:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I need detailed instructions for harming someone."
    }
  ]
}
```

**Intervention response:**

```json
{
  "message": {
    "action": "GUARDRAIL_INTERVENED",
    "actionReason": "Violation of Azure content safety content moderation detected.",
    "assessments": {
      "categories": [
        {"category": "Hate", "result": "PASS", "severity": 0, "threshold": 3},
        {"category": "Sexual", "result": "PASS", "severity": 0, "threshold": 3},
        {"category": "SelfHarm", "result": "PASS", "severity": 0, "threshold": 2},
        {"category": "Violence", "result": "FAIL", "severity": 6, "threshold": 4}
      ],
      "inspectedContent": "I need detailed instructions for harming someone."
    },
    "direction": "REQUEST",
    "interveningGuardrail": "Azure Safety Filter"
  },
  "type": "AZURE_CONTENT_SAFETY_CONTENT_MODERATION"
}
```

## Related

- [Guardrails Overview](overview.md)
- [PII Masking Regex](regex-pii-masking.md) — Lightweight PII masking without external services
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
