# JWT Auth

The JWT Auth policy validates JSON Web Tokens (JWTs) on incoming requests. It supports remote JWKS endpoints and local certificates, and can validate standard claims (issuer, audience, expiry), required scopes, and custom claims. Validated claim values can be forwarded to downstream services as request headers.

!!! info "Prerequisites"
    Before configuring this policy, you need a JWT issuer — an identity provider (IdP) such as Keycloak, Auth0, Okta, Azure AD, or WSO2 Identity Server — that issues signed JWTs to your client applications.

    You will need one of the following from your IdP:

    - **JWKS endpoint URL** — The URL where the IdP publishes its public signing keys (e.g., `https://your-idp.com/.well-known/jwks.json`). This is the recommended option for most IdPs.
    - **Local certificate** — A PEM-encoded public certificate, if your IdP is not publicly accessible or does not expose a JWKS endpoint.

    These are configured directly in the policy form when you add the guardrail. No separate setup is required.

## Configuration Parameters

### Token Location

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| **Header Name** | No | `Authorization` | The HTTP header that carries the JWT. |
| **Auth Header Scheme** | No | `Bearer` | The prefix expected before the token value (e.g., `Bearer <token>`). |
| **On Failure Status Code** | No | `401` | HTTP status code returned when authentication fails. |

### Key Managers (Required)

At least one key manager must be configured. A key manager tells the policy how to obtain the public key used to verify token signatures.

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Name** | Yes | A unique identifier for this key manager. |
| **Issuer** | No | The expected `iss` claim value for tokens validated by this key manager. |
| **JWKS Remote URI** | Conditional | URL of the remote JWKS endpoint (e.g., `https://accounts.google.com/.well-known/jwks.json`). Required if not using a local certificate. |
| **JWKS Certificate Path** | No | Path to a CA certificate for the JWKS endpoint (used for self-signed certificates). |
| **Local Certificate** | Conditional | A PEM-encoded public certificate for offline token validation. Use this instead of a remote JWKS URI when the provider is not publicly accessible. |

### Token Validation

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| **Validate Issuer** | No | `true` | Reject tokens whose `iss` claim does not match a configured key manager's issuer. |
| **Issuers** | No | (none) | Additional accepted issuer values. |
| **Audiences** | No | (none) | Required `aud` claim values. Tokens must contain at least one of the listed audiences. |
| **Required Scopes** | No | (none) | OAuth 2.0 scopes that must be present in the token. |
| **Required Claims** | No | (none) | Key-value pairs of claim names and expected values that must all be present in the token. |
| **Allowed Algorithms** | No | `RS256, ES256` | JWT signing algorithms to accept. |
| **Leeway** | No | `30s` | Tolerance window for token expiry and `nbf` (not-before) validation (e.g., `30s`, `1m`). |

### Claim Forwarding

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Claim Mappings** | No | A map of JWT claim names to request header names. Matched claim values are forwarded as headers to the upstream LLM provider. |
| **User ID Claim** | No | The claim to use as the user identifier for analytics (default: `sub`). |

### JWKS Caching

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| **JWKS Cache TTL** | No | `5m` | How long to cache the JWKS response (e.g., `5m`, `1h`). |
| **JWKS Fetch Timeout** | No | `5s` | Timeout for fetching the JWKS endpoint. |
| **JWKS Fetch Retry Count** | No | `3` | Number of retries on JWKS fetch failure. |

## Add This Policy

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **JWT Auth** from the sidebar.
5. Configure at least one key manager with a JWKS remote URI or a local certificate.
6. Set any additional validation parameters (audiences, scopes, claim mappings).
7. Click **Add** (for providers) or **Submit** (for proxies).
8. Deploy the provider or proxy to apply the changes.

## Behavior

- Requests with a valid, unexpired JWT that satisfies all configured validations are forwarded upstream.
- Requests with a missing, expired, or invalid JWT receive an HTTP `401 Unauthorized` response (or the configured failure status code).
- Configured claim mappings are applied on successful validation — the claim values are added as request headers before the request reaches the upstream LLM.

## Related

- [Guardrails Overview](overview.md)
- [API Key Auth](api-key-auth.md) — Simpler API key-based authentication
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
