# Securing APIs with a JWT Key Manager

A self-hosted Gateway can validate JWT access tokens issued by an external OIDC identity provider (for example, WSO2 Identity Server). You register the provider as a **key manager** in the Gateway's `config.toml`, then attach the `jwt-auth` policy to an API and reference that key manager by name. The Gateway verifies each token's signature against the provider's JWKS endpoint — it never calls the provider per request, and the provider does not need to know about the Gateway.

This guide uses WSO2 Identity Server as the example provider.

## Prerequisites

- A self-hosted Gateway (Gateway Controller + Gateway Runtime).
- An OIDC identity provider that issues **JWT** (not opaque) access tokens signed with an asymmetric algorithm (RS256/ES256 are accepted by default). In WSO2 Identity Server, set the application's access token type to **JWT**.
- The provider's issuer value and JWKS endpoint. For WSO2 Identity Server these are typically `https://<is-host>:9443/oauth2/token` and `https://<is-host>:9443/oauth2/jwks`.

## 1. Register the key manager

Add a key manager entry to the Gateway `config.toml`:

```toml
[[policy_configurations.jwtauth_v1.keymanagers]]
name = "wso2is"
issuer = "https://localhost:9443/oauth2/token"

[policy_configurations.jwtauth_v1.keymanagers.jwks.remote]
uri = "https://host.docker.internal:9443/oauth2/jwks"
skipTlsVerify = true
```

| Field | Description |
|-------|-------------|
| `name` | Unique name for the key manager. The `jwt-auth` policy references it by this value. |
| `issuer` | Expected `iss` claim in the token. Must match exactly; omit to validate on signature alone. |
| `jwks.remote.uri` | Provider's JWKS endpoint. Fetched by the Gateway Runtime, so use a host it can resolve (e.g. `host.docker.internal` for a host-bound provider). |
| `skipTlsVerify` | Skip TLS verification for the JWKS fetch. Development only; for production use `certificatePath` with a CA. |

Restart the Gateway Runtime to apply the change. If the Runtime runs in Docker and the provider is on the host, ensure the `gateway-runtime` service can resolve the host (for example, `extra_hosts: ["host.docker.internal:host-gateway"]`).

To verify reachability, the JWKS endpoint should return a key set from within the Runtime container:

```bash
docker exec <gateway-runtime-container> curl -sk https://host.docker.internal:9443/oauth2/jwks
```

## 2. Secure an API with the jwt-auth policy

Attach the `jwt-auth` policy to an API (or a specific operation) and reference the key manager by name:

```yaml
operations:
  - method: GET
    path: /protected
    policies:
      - name: jwt-auth
        version: v1
        params:
          issuers:
            - wso2is
```

Deploy the API to the Gateway. The `jwt-auth` policy validates the token's algorithm, expiry, issuer, signature (using the key manager's JWKS), and any configured audiences, scopes, or claims.

## 3. Test

Obtain a JWT from the identity provider, then call the API through the Gateway:

```bash
TOKEN=$(curl -sk -u '<client_id>:<client_secret>' \
  -d 'grant_type=client_credentials' \
  https://localhost:9443/oauth2/token | sed -E 's/.*"access_token":"([^"]+)".*/\1/')

curl -i http://localhost:8080/<context>/<version>/protected \
  -H "Authorization: Bearer $TOKEN"
```

A valid token returns the upstream response. A missing or invalid token returns `401` with `Authentication failed`.

## Notes

- The JWKS is cached (default 5 minutes), so the provider is contacted only periodically rather than on every request.
- `issuer` is a string comparison against the token's `iss`; `jwks.remote.uri` is a network call. They may legitimately use different hostnames (for example, `localhost` in the token versus `host.docker.internal` for the fetch).
- For the full list of `jwt-auth` parameters and key manager options, see the [jwt-auth policy](https://wso2.com/api-platform/policy-hub/policies/jwt-auth) and the [config template](https://github.com/wso2/api-platform/blob/main/gateway/configs/config-template.toml).
