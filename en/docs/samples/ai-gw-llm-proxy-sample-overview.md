# LLM Proxy — API Key Auth and Token-Based Rate Limiting Sample

> **Sample source:** [wso2/api-platform — samples/ai-gw-llm-proxy](https://github.com/wso2/api-platform/tree/main/samples/ai-gw-llm-proxy)
>
> ```bash
> git clone https://github.com/wso2/api-platform.git
> cd api-platform/samples/ai-gw-llm-proxy
> ```

## Overview

This guide is for platform engineers and API developers who want to control access to LLM APIs and enforce usage quotas.

When your application routes LLM traffic through the WSO2 AI Gateway, you can attach policies that enforce API key authentication and cap token consumption at the gateway layer. This sample sets up a local Docker stack that demonstrates both policies working together against a mock OpenAI compatible endpoint, giving you a reproducible environment to understand and test each behavior before deploying to production.

No real OpenAI API key or cloud account is required. All LLM traffic is handled by a local WireMock container that returns a fixed mock response.

---

## What You Will Learn

By working through this sample you will understand how to:

- Configure **API key authentication** — enforce that every request carries a valid API key before it reaches the upstream LLM provider
- Apply **token-based rate limiting** — cap the number of tokens a caller can consume within a time window, and return a `429 Too Many Requests` when the quota is exhausted

---

## Scenario — API Key Auth and Token-Based Rate Limiting

**Problem:** An unprotected LLM proxy allows any caller to send unlimited requests, risking abuse, runaway costs, and provider rate limit violations.

**What this scenario does:** The gateway sits in front of a mock OpenAI backend. Every incoming request must carry a valid `api_key` header — invalid keys are rejected with `401 Unauthorized`. For authenticated requests, the gateway tracks the number of tokens returned by the upstream provider and enforces a quota of 30 total tokens per minute. The mock always returns exactly 30 tokens, so the first request exhausts the quota and the second request within the same window is rejected with `429 Too Many Requests`.

---

## Expected Results

After running `sh test.sh` you should observe the following.

### API Key Auth and Rate Limiting

Two requests are sent back to back using the registered API key. The first request succeeds and the second is rate limited.

```
=== WSO2 AI Gateway — LLM Proxy Test ===

Target  : https://localhost:8443/assistant/chat/completions
API Key : demo ****
Payload : {"model":"gpt-4o-mini","messages":[{"role":"user","content":"Test call"}]}

=== Test 1: Valid API key — expect HTTP 200 ===
Status   : HTTP 200
✔  HTTP 200 received as expected

=== Test 2: Token quota exceeded — expect HTTP 429 ===
Status   : HTTP 429
✔  HTTP 429 received as expected

✔  PASSED — Rate limiting is working correctly.
```

---

## Prerequisites

| Tool | Purpose |
|---|---|
| Docker and Docker Compose | Runs the gateway stack and mock backend |
| `curl` or `wget` | Downloads the gateway distribution |
| `unzip` | Extracts the distribution |

No API keys or cloud accounts are required.

---

## Files

```
setup.sh                        Automated setup (download → start → register resources → wait for readiness)
test.sh                         Policy verification (auth + rate limiting)
teardown.sh                     Automated teardown (stop stack → remove containers and volumes)
inject-mock.sh                  Registers the LLM provider, proxy, and API key via the management API
provider.yaml                   LLM provider definition (mock upstream, token-based rate limit policy)
proxy.yaml                      LLM proxy definition (API key auth policy)
wiremock/mappings/
  openai-mock.json              Fixed mock LLM response returning 30 total tokens
.env.example                    Configurable API key and port settings
```

---

## Setup

```bash
cp .env.example .env
sh setup.sh
```

The script performs these steps in order:

1. Downloads `wso2apip-ai-gateway-1.1.0.zip` (skipped if already present)
2. Extracts the distribution
3. Starts the WireMock mock LLM backend container
4. Starts the WSO2 AI Gateway stack via Docker Compose
5. Waits for the gateway controller to return HTTP `200` on the health endpoint
6. Registers the LLM provider, LLM proxy, and inbound API key via the management API
7. Polls the traffic endpoint until routes are live and the auth policy is enforcing

### Endpoints After Setup

| Endpoint | URL |
|---|---|
| Gateway proxy (HTTPS) | `https://localhost:8443/assistant/chat/completions` |
| Gateway health | `http://localhost:9094/health` |
| Management API | `http://localhost:9090/api/management/v0.9` |
| Mock LLM backend | `http://localhost:8082` |

---

## Try It Manually

Once `setup.sh` completes, you can exercise the gateway directly from your terminal.

**Call 1 — within quota (expect `200`):**

```bash
curl -sk -w "\n→ HTTP %{http_code}" -X POST https://localhost:8443/assistant/chat/completions \
  -H "api_key: demo-api-key" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Hello"}]}'
```

**Call 2 — immediately after, quota exhausted (expect `429`):**

```bash
curl -sk -w "\n→ HTTP %{http_code}" -X POST https://localhost:8443/assistant/chat/completions \
  -H "api_key: demo-api-key" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Hello"}]}'
```

**Call with an invalid key (expect `401`):**

```bash
curl -sk -w "\n→ HTTP %{http_code}" -X POST https://localhost:8443/assistant/chat/completions \
  -H "api_key: wrong-key" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Hello"}]}'
```

> The rate limit window is fixed at 1 minute.

---

## Running the Tests

```bash
sh test.sh
```

The test script fires two back-to-back requests with the registered API key and asserts the first returns `200` and the second returns `429`.

---

## Teardown

```bash
sh teardown.sh
```

Stops and removes all containers and volumes in one pass.

---

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| `setup.sh` hangs at health check | Gateway images are still pulling — wait and retry |
| `setup.sh` hangs at route polling | xDS sync between controller and runtime is delayed — wait; the default timeout is 60s |
| Both calls return `200` | Rate limit quota not registering — re-run `sh inject-mock.sh` and retry |
| Both calls return `401` | API key was not registered or does not match `.env` — re-run `sh setup.sh` |
| Both calls return `404` | Routes not yet synced to Envoy — wait a few seconds and retry |
| `docker compose up` fails with port conflict | A port (8443, 9090, 8082) is already in use — check `docker ps` and stop conflicting containers |
