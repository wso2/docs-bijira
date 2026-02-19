# URL Guardrail

The URL Guardrail extracts URLs from a payload and validates them by checking their accessibility through a DNS lookup or connection attempt. Use it to prevent requests or responses containing broken or unreachable links.

## Configuration Parameters

| Parameter | Description |
|-----------|-------------|
| **Guardrail Name** | A unique name for this guardrail instance. Used for tracking and in intervention responses. |
| **Perform DNS Lookup** | When enabled, validates URLs using a DNS lookup. When disabled, performs a connection attempt instead. DNS lookups are faster but less thorough. |
| **Connection Timeout** | Timeout in milliseconds for DNS lookups or connection attempts. If not set, a default timeout is used. |
| **JSON Path** | A JSONPath expression to extract URLs from the payload (e.g., `$.messages[0].content`). If not specified, the entire payload is scanned for URLs. |
| **Show Guardrail Assessment** | When enabled, the intervention response includes the list of invalid URLs detected. |

## Add This Guardrail

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **URL Guardrail** from the sidebar.
5. Fill in the configuration parameters.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## Example: Block Responses with Invalid URLs

The following configuration validates URLs in LLM responses.

**Configuration:**

| Parameter | Value |
|-----------|-------|
| Guardrail Name | `Response URL Validator` |
| Perform DNS Lookup | `false` |
| Connection Timeout | `5000` |
| JSON Path | `$.choices[0].message.content` |
| Show Guardrail Assessment | `true` |

**Sample response that would be blocked:**

```json
{
  "choices": [
    {
      "message": {
        "content": "Check these links: https://foo.bar.baz and http://invalid-host.example"
      }
    }
  ]
}
```

**Intervention response:**

```json
{
  "message": {
    "action": "GUARDRAIL_INTERVENED",
    "actionReason": "Violation of url validity detected.",
    "assessments": {
      "invalidUrls": [
        "https://foo.bar.baz",
        "http://invalid-host.example"
      ],
      "message": "One or more URLs in the payload failed validation."
    },
    "direction": "RESPONSE",
    "interveningGuardrail": "Response URL Validator"
  },
  "type": "URL_GUARDRAIL"
}
```

## Related

- [Guardrails Overview](overview.md)
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
