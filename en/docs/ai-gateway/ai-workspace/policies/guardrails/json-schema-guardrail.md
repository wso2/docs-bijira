# JSON Schema Guardrail

The JSON Schema Guardrail validates request or response payloads against a [JSON Schema](https://json-schema.org/). Use it to enforce that LLM inputs or outputs conform to a specific structure or data format before they reach the LLM or the client.

## Configuration Parameters

The JSON Schema Guardrail accepts separate configurations for the `request` and `response` flows. At least one of `request` or `response` must be configured.

### Request / Response Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Schema** | Yes | A valid JSON Schema string that the payload must conform to. |
| **JSON Path** | No | A JSONPath expression to extract a specific field for validation (e.g., `$.messages[0].content`). If not specified, the entire payload is validated against the schema. |
| **Invert the Guardrail Decision** | No | When enabled, the guardrail intervenes when the payload **passes** schema validation (i.e., blocks valid payloads). Useful for filtering out well-formed but undesirable content. |
| **Show Guardrail Assessment** | No | When enabled, the intervention response includes the schema validation error details. |

## Add This Guardrail

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **JSON Schema Guardrail** from the sidebar.
5. Configure the schema and optional parameters for the request flow, response flow, or both.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## Example: Enforce Request Payload Structure

The following configuration validates that the request body contains a `messages` array where each item has a `role` and a `content` string.

**Request Schema:**

```json
{
  "type": "object",
  "required": ["messages"],
  "properties": {
    "messages": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["role", "content"],
        "properties": {
          "role": { "type": "string" },
          "content": { "type": "string" }
        }
      }
    }
  }
}
```

**Sample request that would be blocked (missing `role`):**

```json
{
  "messages": [
    {
      "content": "Hello, how are you?"
    }
  ]
}
```

**Intervention response:**

```json
{
  "message": {
    "action": "GUARDRAIL_INTERVENED",
    "actionReason": "Violation of JSON schema detected.",
    "assessments": "messages.0: role is required",
    "direction": "REQUEST",
    "interveningGuardrail": "JSON Schema Guardrail"
  },
  "type": "JSON_SCHEMA_GUARDRAIL"
}
```

## Related

- [Guardrails Overview](overview.md)
- [Regex Guardrail](regex-guardrail.md) — Pattern-based content blocking
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
