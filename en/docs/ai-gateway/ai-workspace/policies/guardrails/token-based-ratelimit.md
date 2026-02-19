# Token Based Rate Limit

The Token Based Rate Limit policy enforces rate limits based on LLM token consumption rather than request count. It tracks prompt tokens, completion tokens, and total tokens separately, allowing fine-grained control over how much token capacity is consumed within a time window.

!!! info "Built-in Rate Limiting vs. Token Based Rate Limit Policy"
    The AI Workspace also has a first-class **Rate Limiting** tab on LLM Providers that provides request and token limits with Backend and Per Consumer scopes. The Token Based Rate Limit policy is a lower-level alternative that can be attached through the Guardrails interface with direct control over prompt token, completion token, and total token limits.

## Configuration Parameters

You can configure limits for any combination of the three token categories. At least one category must be specified.

### Prompt Token Limits

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Count** | Yes | Maximum number of prompt tokens allowed within the duration. |
| **Duration** | Yes | The time window for the limit (e.g., `60s`, `1m`, `1h`). |

### Completion Token Limits

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Count** | Yes | Maximum number of completion tokens allowed within the duration. |
| **Duration** | Yes | The time window for the limit (e.g., `60s`, `1m`, `1h`). |

### Total Token Limits

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Count** | Yes | Maximum combined prompt + completion tokens allowed within the duration. |
| **Duration** | Yes | The time window for the limit (e.g., `60s`, `1m`, `1h`). |

## Add This Policy

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **Token Based Rate Limit** from the sidebar.
5. Configure limits for prompt tokens, completion tokens, total tokens, or any combination.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## Behavior

- The policy reads the token usage from the LLM provider's response (`usage.prompt_tokens`, `usage.completion_tokens`, `usage.total_tokens`).
- When any configured limit is exceeded within its time window, subsequent requests receive HTTP `429 Too Many Requests`.
- Token counts are tracked per route or API.

## Related

- [Guardrails Overview](overview.md)
- [Rate Limit - Basic](basic-rate-limit.md) — Simple request count-based rate limiting
- [Token-Based Rate Limiting](../token-based-rate-limit.md) — Built-in rate limiting with Backend and Per Consumer scopes
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
