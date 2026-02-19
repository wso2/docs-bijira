# Sentence Count Guardrail

The Sentence Count Guardrail validates the number of sentences in a payload or a specific JSON field. Use it to enforce policies on the structural complexity of prompts or responses.

## Configuration Parameters

| Parameter | Description |
|-----------|-------------|
| **Guardrail Name** | A unique name for this guardrail instance. Used for tracking and in intervention responses. |
| **Minimum Sentence Count** | The minimum number of sentences the content must contain. |
| **Maximum Sentence Count** | The maximum number of sentences the content can contain. |
| **JSON Path** | A JSONPath expression to extract a specific field from the payload for validation (e.g., `$.messages[0].content`). If not specified, the entire payload is used. |
| **Invert the Guardrail Decision** | When enabled, the guardrail intervenes when the sentence count **is within** the specified range. When disabled, it intervenes when the sentence count is **outside** the range. |
| **Show Guardrail Assessment** | When enabled, the intervention response includes details about the violation. |

## Add This Guardrail

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **Sentence Count Guardrail** from the sidebar.
5. Fill in the configuration parameters.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## Example: Limit Prompt to 3 Sentences

The following configuration blocks prompts with more than 3 sentences.

**Configuration:**

| Parameter | Value |
|-----------|-------|
| Guardrail Name | `Sentence Limit` |
| Minimum Sentence Count | `1` |
| Maximum Sentence Count | `3` |
| JSON Path | `$.messages[0].content` |
| Invert the Guardrail Decision | `false` |
| Show Guardrail Assessment | `true` |

**Sample request that would be blocked:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "This is sentence one. This is sentence two. This is sentence three. This is sentence four."
    }
  ]
}
```

**Intervention response:**

```json
{
  "message": {
    "action": "GUARDRAIL_INTERVENED",
    "actionReason": "Violation of applied sentence count constraints detected.",
    "assessments": "Violation of sentence count detected. Expected between 1 and 3 sentences.",
    "direction": "REQUEST",
    "interveningGuardrail": "Sentence Limit"
  },
  "type": "SENTENCE_COUNT_GUARDRAIL"
}
```

## Related

- [Guardrails Overview](overview.md)
- [Word Count Guardrail](word-count-guardrail.md)
- [Content Length Guardrail](content-length-guardrail.md)
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
