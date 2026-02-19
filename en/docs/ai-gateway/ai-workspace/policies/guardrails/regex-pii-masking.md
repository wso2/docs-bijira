# Regex PII Masking

The Regex PII Masking guardrail detects and masks Personally Identifiable Information (PII) using custom regular expression patterns. Because it relies only on regex rules, no external service or credentials are required.

It supports two modes:

- **Masking (reversible)** — Detected PII is replaced with a placeholder (e.g., `[EMAIL_0000]`). When applied to the request flow, the original values can be restored in the response.
- **Redaction (permanent)** — Detected PII is replaced with `*****` and cannot be restored.

## Configuration Parameters

| Parameter | Description |
|-----------|-------------|
| **Guardrail Name** | A unique name for this guardrail instance. Used for tracking and in intervention responses. |
| **PII Entities** | A list of PII entity definitions. Each entry requires a `piiEntity` (a name matching `^[A-Z_]+$`, e.g., `EMAIL`) and a `piiRegex` (the regex pattern to detect it). |
| **JSON Path** | A JSONPath expression to extract the field to scan (e.g., `$.messages[0].content`). If not specified, the entire payload is scanned. |
| **Redact PII** | When enabled, matched PII is permanently replaced with `*****`. When disabled, PII is masked with a reversible placeholder that can be restored in the response flow. |

## Add This Guardrail

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **Regex PII Masking** from the sidebar.
5. Fill in the configuration parameters, including the PII entity list.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## PII Entity Format

The `PII Entities` parameter accepts a JSON array. Each element must have:

- `piiEntity` — The entity label, uppercase letters and underscores only (e.g., `EMAIL`, `PHONE_NUMBER`)
- `piiRegex` — A valid regular expression to detect that entity

**Example:**

```json
[
  {
    "piiEntity": "EMAIL",
    "piiRegex": "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b"
  },
  {
    "piiEntity": "PHONE",
    "piiRegex": "\\b\\d{3}[-.]?\\d{3}[-.]?\\d{4}\\b"
  }
]
```

## Example: Redact Email Addresses from Requests

**Configuration:**

| Parameter | Value |
|-----------|-------|
| Guardrail Name | `Email Redactor` |
| PII Entities | `[{"piiEntity": "EMAIL", "piiRegex": "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b"}]` |
| JSON Path | `$.messages[0].content` |
| Redact PII | `true` |

**Sample request before guardrail:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Please send a summary to john.doe@example.com."
    }
  ]
}
```

**Payload forwarded to the LLM (after guardrail):**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Please send a summary to *****."
    }
  ]
}
```

## PII Masking with Restoration

To mask PII in the request and restore it in the response, add this guardrail to **both the request and response flows** with **Redact PII disabled** in both. The gateway will temporarily replace PII with reversible placeholders in the outgoing request, and then restore the original values when the LLM response comes back.

!!! warning
    If **Redact PII** is enabled on the response flow, PII is permanently removed from the response and cannot be restored.

## Related

- [Guardrails Overview](overview.md)
- [PII Masking (Guardrails AI)](pii-masking.md) — ML-based PII detection, no custom patterns needed
- [AWS Bedrock Guardrail](aws-bedrock-guardrail.md) — Cloud-based content safety including PII protection
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
