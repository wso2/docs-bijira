# Content Length Guardrail

The Content Length Guardrail validates the byte size of a payload or a specific JSON field. Use it to cap the size of requests or responses passing through the gateway.

## Configuration Parameters

| Parameter | Description |
|-----------|-------------|
| **Guardrail Name** | A unique name for this guardrail instance. Used for tracking and in intervention responses. |
| **Minimum Content Length** | The minimum byte length the content must contain. |
| **Maximum Content Length** | The maximum byte length the content can contain. |
| **JSON Path** | A JSONPath expression to extract a specific field from the payload for validation (e.g., `$.messages[0].content`). If not specified, the entire payload is used. |
| **Invert the Guardrail Decision** | When enabled, the guardrail intervenes when the content length **is within** the specified range. When disabled, it intervenes when the content length is **outside** the range. |
| **Show Guardrail Assessment** | When enabled, the intervention response includes details about the violation. |

## Add This Guardrail

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **Content Length Guardrail** from the sidebar.
5. Fill in the configuration parameters.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## Example: Cap Request Payload Size

The following configuration blocks requests where the message content exceeds 100 bytes.

**Configuration:**

| Parameter | Value |
|-----------|-------|
| Guardrail Name | `Request Size Limit` |
| Minimum Content Length | `10` |
| Maximum Content Length | `100` |
| JSON Path | `$.messages[0].content` |
| Invert the Guardrail Decision | `false` |
| Show Guardrail Assessment | `true` |

**Sample request that would be blocked:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "This is a test message that exceeds the maximum byte length defined in the content length guardrail policy."
    }
  ]
}
```

**Intervention response:**

```json
{
  "message": {
    "action": "GUARDRAIL_INTERVENED",
    "actionReason": "Violation of applied content length constraints detected.",
    "assessments": "Violation of content length detected. Expected between 10 and 100 bytes.",
    "direction": "REQUEST",
    "interveningGuardrail": "Request Size Limit"
  },
  "type": "CONTENT_LENGTH_GUARDRAIL"
}
```

## Related

- [Guardrails Overview](overview.md)
- [Word Count Guardrail](word-count-guardrail.md)
- [Sentence Count Guardrail](sentence-count-guardrail.md)
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
