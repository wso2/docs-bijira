# LLM Proxies Overview

## Why a Proxy on Top of a Provider?

An **LLM Provider** connects the gateway to an upstream LLM service and can be called directly. An **LLM Proxy** adds a dedicated endpoint on top — with its own API keys, guardrails, and access controls.

The main benefit is isolation. A single provider can back multiple proxies: one for a customer-facing chatbot with strict guardrails, another for an internal tool with relaxed settings. Each proxy is independently configured, and swapping the underlying provider doesn't require any changes to the applications calling the proxy.

## What You Can Do with a Proxy

**Expose a controlled API endpoint**
The proxy gives you a stable URL your applications call. You control which resources (API paths) are exposed, and can enable or disable them without touching the upstream provider.

**Enforce authentication**
Require applications to present an API key before their requests are forwarded to the LLM. Keys are generated per proxy and expire after 90 days.

**Apply guardrails**
Attach content safety, PII masking, or semantic caching policies globally across all endpoints, or target them at specific resources only.

**Isolate environments and teams**
Create separate proxies for different teams, applications, or environments (dev, staging, production) — each with independent rate limits, guardrails, and access keys — all sharing the same provider backend.

**Switch providers without client changes**
Because applications call the proxy URL rather than the provider directly, you can swap the underlying LLM Provider (e.g., from OpenAI to Azure OpenAI) without any changes on the client side.

## Next Steps

- [Configure LLM Proxy](configure-proxy.md) — Step-by-step guide to create and deploy your first proxy
- [Manage Proxy](manage-proxy.md) — Update configuration, guardrails, and resources after deployment
