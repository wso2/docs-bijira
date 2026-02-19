# PII Masking

The PII Masking guardrail uses a fine-tuned [Guardrails AI](https://www.guardrailsai.com/) model to automatically detect and mask Personally Identifiable Information (PII) in request and response payloads — without requiring you to write custom regex patterns.

!!! info "Additional Configuration Required"
    This guardrail connects to the Guardrails AI service. Ensure your AI Gateway has network access to the Guardrails AI endpoint before enabling this guardrail.

It supports two modes:

- **Masking (reversible)** — Detected PII is replaced with a typed placeholder. When applied to the request flow, original values can be restored in the response.
- **Redaction (permanent)** — Detected PII is replaced with `*****` and cannot be restored.

## Configuration Parameters

| Parameter | Description |
|-----------|-------------|
| **Guardrail Name** | A unique name for this guardrail instance. Used for tracking and in intervention responses. |
| **PII Entities** | The categories of PII to detect and mask. Select from the entity types supported by the Guardrails AI model (e.g., `EMAIL`, `URL`, `PHONE_NUMBER`, `PERSON`, `CREDIT_CARD`). |
| **JSON Path** | A JSONPath expression to extract the field to scan (e.g., `$.messages[0].content`). If not specified, the entire payload is scanned. |
| **Redact PII** | When enabled, matched PII is permanently replaced with `*****`. When disabled, PII is masked with a reversible placeholder that can be restored in the response flow. Enable this on the **response flow** to prevent the LLM's output from leaking sensitive data to the client. |

## Add This Guardrail

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **PII Masking** from the sidebar.
5. Fill in the configuration parameters and select the PII entity types to detect.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## Example: Mask Emails and URLs

**Configuration:**

| Parameter | Value |
|-----------|-------|
| Guardrail Name | `PII Shield` |
| PII Entities | `EMAIL, URL` |
| JSON Path | `$.messages[0].content` |
| Redact PII | `true` |

**Sample request before guardrail:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Contact me at jane@example.com or visit https://example.com."
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
      "content": "Contact me at ***** or visit *****."
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
- [Regex PII Masking](regex-pii-masking.md) — Custom regex-based PII masking, no external service required
- [AWS Bedrock Guardrail](aws-bedrock-guardrail.md) — Cloud-based content safety including PII protection via AWS
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
