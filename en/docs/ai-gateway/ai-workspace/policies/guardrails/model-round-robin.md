# Model Round Robin

The Model Round Robin policy distributes requests across multiple AI models using round-robin selection. If a model returns a server error (`5xx`) or a rate limit response (`429`), it can be temporarily suspended so that traffic automatically shifts to the remaining healthy models.

## Configuration Parameters

### Models (Required)

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Models** | Yes | The list of model names to balance across (e.g., `gpt-4o`, `gpt-4-turbo`). |

### Failure Handling

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| **Suspend Duration** | No | `0` (disabled) | Number of seconds to suspend a model after it returns a `5xx` or `429` response. While suspended, the model is skipped in round-robin selection. Set to `0` to disable suspension. |

### Request Model Location

These parameters tell the policy where in the request the model name appears so that it can be replaced with the selected round-robin model.

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Location** | Yes | Where the model is specified: `payload` (JSON body), `header`, `queryParam`, or `pathParam`. |
| **Identifier** | Yes | The JSONPath expression, header name, query parameter name, or path parameter name used to locate the model value. For example: `$.model` for a JSON body field. |

## Add This Policy

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **Model Round Robin** from the sidebar.
5. Add the models to balance across.
6. Optionally, set a **Suspend Duration** to handle model failures gracefully.
7. Configure the **Request Model Location** so the policy knows where to replace the model name.
8. Click **Add** (for providers) or **Submit** (for proxies).
9. Deploy the provider or proxy to apply the changes.

## Behavior

- On each request, the policy selects the next available model in round-robin order.
- The model value in the request (at the configured location) is replaced with the selected model name before forwarding upstream.
- If a model returns a `5xx` or `429` response and **Suspend Duration** is set, the model is suspended for that duration and subsequent requests skip it.
- If all models are suspended, the gateway returns `503 Service Unavailable`.

## Related

- [Guardrails Overview](overview.md)
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
