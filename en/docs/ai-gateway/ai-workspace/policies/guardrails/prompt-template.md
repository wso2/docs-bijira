# Prompt Template

The Prompt Template policy applies reusable, parameterized prompt templates to requests. Instead of sending a raw prompt, clients send a template reference (`template://<name>?param=value`) and the gateway substitutes the parameters into the configured template before forwarding the request to the LLM.

## Configuration Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Templates** | Yes | A list of named templates. Each template has a **name** (identifier) and a **prompt** string containing placeholders in the format `[[parameter-name]]`. |

### Template Placeholder Syntax

Use `[[parameter-name]]` inside the prompt string to mark substitution points:

```
Translate the following text from [[from]] to [[to]]: [[text]]
```

When a client calls `template://translate?from=English&to=Spanish&text=Hello`, the policy replaces each placeholder with the corresponding query parameter value.

## Add This Policy

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **Prompt Template** from the sidebar.
5. Add one or more templates, each with a name and prompt string using `[[param]]` placeholders.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## Example: Translation Template

**Configured template:**

| Field | Value |
|-------|-------|
| Name | `translate` |
| Prompt | `Translate the following text from [[from]] to [[to]]: [[text]]` |

**Client request body:**

```json
{
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": "template://translate?from=English&to=Spanish&text=Hello, how are you?"
    }
  ]
}
```

**Request forwarded to LLM:**

```json
{
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": "Translate the following text from English to Spanish: Hello, how are you?"
    }
  ]
}
```

## Related

- [Guardrails Overview](overview.md)
- [Prompt Decorator](prompt-decorator.md) — Inject fixed content into prompts without client-side changes
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
