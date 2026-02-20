# CORS

The CORS policy handles Cross-Origin Resource Sharing for your LLM Provider or Proxy. It validates the `Origin` header on incoming requests and sets the appropriate `Access-Control-*` response headers. Preflight `OPTIONS` requests are handled automatically and do not reach the upstream LLM provider.

## Configuration Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| **Allowed Origins** | Yes      | `["*"]` | List of allowed origins. Supports wildcard `"*"` to permit all origins. |
| **Allowed Methods** | No       | `GET, POST, PUT, DELETE, OPTIONS` | HTTP methods that are allowed for cross-origin requests. |
| **Allowed Headers** | No       | (none) | Request headers allowed in cross-origin requests. Use `"*"` to allow all headers. |
| **Exposed Headers** | No       | (none) | Response headers that browsers are permitted to access. |
| **Max Age** | No       | (not set) | Duration in seconds that browsers can cache preflight responses. |
| **Allow Credentials** | No       | `false` | Whether to allow cookies and credentials in cross-origin requests. Cannot be `true` when **Allowed Origins**, **Allowed Headers**, or **Allowed Methods** use wildcard `"*"`. |
| **Forward Preflight** | No       | `false` | When enabled, preflight requests that fail CORS validation are forwarded to the upstream instead of being rejected. |

## Add This Policy

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **CORS** from the sidebar.
5. Configure the allowed origins, methods, and headers.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Deploy the provider or proxy to apply the changes.

## Behavior

- **Preflight requests** (`OPTIONS`) receive a `204 No Content` response with the appropriate CORS headers. They are not forwarded upstream.
- **Actual requests** from allowed origins have the CORS response headers added.
- Requests from disallowed origins are rejected.

!!! warning "Credentials and wildcards"
    Setting `allowCredentials: true` while using wildcard `"*"` for origins, methods, or headers violates the CORS specification and will cause a configuration error.

## Related

- [Guardrails Overview](overview.md)
- [API Key Auth](api-key-auth.md) — API key-based access control
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
