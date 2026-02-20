# Word Count Guardrail

The Word Count Guardrail validates the number of words in a payload or a specific JSON field. Use it to enforce content length policies — for example, limiting how long a user's prompt can be.

## Configuration Parameters

| Parameter | Description |
|-----------|-------------|
| **Guardrail Name** | A unique name for this guardrail instance. Used for tracking and in intervention responses. |
| **Minimum Word Count** | The minimum number of words the content must contain. |
| **Maximum Word Count** | The maximum number of words the content can contain. |
| **JSON Path** | A JSONPath expression to extract a specific field from the payload for validation (e.g., `$.messages[0].content`). If not specified, the entire payload is used. |
| **Invert the Guardrail Decision** | When enabled, the guardrail intervenes when the word count **is within** the specified range. When disabled, it intervenes when the word count is **outside** the range. |
| **Show Guardrail Assessment** | When enabled, the intervention response includes details about the violation. |

## Add This Guardrail

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **Word Count Guardrail** from the sidebar.
5. Fill in the configuration parameters.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## Example: Limit Prompt Length

The following configuration blocks prompts that exceed 10 words.

**Configuration:**

| Parameter | Value |
|-----------|-------|
| Guardrail Name | `Prompt Length Limit` |
| Minimum Word Count | `2` |
| Maximum Word Count | `10` |
| JSON Path | `$.messages[0].content` |
| Invert the Guardrail Decision | `false` |
| Show Guardrail Assessment | `true` |

**Sample request that would be blocked:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "This is a test message with more than 10 words in it, so it will be blocked."
    }
  ]
}
```

**Intervention response:**

```json
{
  "message": {
    "action": "GUARDRAIL_INTERVENED",
    "actionReason": "Violation of applied word count constraints detected.",
    "assessments": "Violation of word count detected. Expected between 2 and 10 words.",
    "direction": "REQUEST",
    "interveningGuardrail": "Prompt Length Limit"
  },
  "type": "WORD_COUNT_GUARDRAIL"
}
```

## Related

- [Guardrails Overview](overview.md)
- [Sentence Count Guardrail](sentence-count-guardrail.md)
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
