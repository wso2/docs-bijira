# JWT Auth

The JWT Auth policy validates JSON Web Tokens (JWTs) on incoming requests. The gateway verifies the token's signature, expiry, issuer, audience, scopes, and required claims.

## Configuration Parameters

All parameters are optional.

| Parameter | Default | Description |
|-----------|---------|-------------|
| **Issuers** | — | Accepted issuer values. If omitted, the `iss` claim is matched against configured key managers. |
| **Audiences** | — | Required `aud` claim values. At least one must be present in the token. |
| **Required Scopes** | — | OAuth 2.0 scopes that must be present in the token. |
| **Required Claims** | — | Claim name–value pairs that must all be present in the token. |
| **Claim Mappings** | — | Map JWT claim names to request headers forwarded to the upstream LLM. |
| **Auth Header Prefix** | `Bearer` | The prefix expected before the token value (e.g., `Bearer <token>`). |
| **User ID Claim** | `sub` | The claim used as the user identifier for analytics. |

## Add This Policy

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **JWT Auth** from the sidebar.
5. Optionally expand **Advanced Settings** to configure audiences, scopes, claim mappings, etc.
6. Click **Add** (for providers) or **Submit** (for proxies).
7. Redeploy the provider or proxy to apply the changes.

## Behavior

- Requests with a valid, unexpired JWT that satisfies all configured validations are forwarded upstream.
- Requests with a missing, expired, or invalid JWT receive HTTP `401 Unauthorized`.

## Related

- [Guardrails Overview](overview.md)
- [API Key Auth](api-key-auth.md) — Simpler API key-based authentication
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
