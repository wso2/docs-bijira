# API Key Auth

The API Key Auth policy validates incoming requests by checking for a valid API key in a specified header or query parameter. Requests that do not carry a recognized API key are rejected before reaching the upstream LLM provider.

## Configuration Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| **key**   | Yes | The name of the header or query parameter that carries the API key (e.g., `x-api-key`, `Authorization`). |
| **in**    | Yes | Where the key is sent: `header` or `query`. |

## Add This Policy

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **API Key Auth** from the sidebar.
5. Enter the **key** name and select the **in**(key location).
7. Click **Add**.
8. Deploy the provider or proxy to apply the changes.

## Behavior

- Requests with a valid API key are forwarded to the upstream LLM provider.
- Requests with a missing or invalid API key receive an HTTP `401 Unauthorized` response.

## Related

- [Guardrails Overview](overview.md)
- [JWT Auth](jwt-auth.md) — Token-based authentication using JWTs
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
