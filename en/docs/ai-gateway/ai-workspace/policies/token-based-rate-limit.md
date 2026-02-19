# Token-Based Rate Limiting

AI services bill on a per-token basis, so uncontrolled usage can lead to unexpected costs. Token-based rate limiting lets you set caps on how many requests or tokens can be consumed within a given time window on the backend (gateway to upstream provider).

## Overview

The AI Workspace supports two rate limiting scopes:

| Scope | Controls | Protects | Status |
|-------|----------|----------|--------|
| **Backend** | Requests from the gateway to the upstream LLM provider | Your provider API credentials and total spend | Available |
| **Per Consumer** | Requests from client applications to the gateway | Fair usage across all consumers | *Coming soon* |

!!! info "Per Consumer Rate Limiting — Coming Soon"
    Per consumer rate limiting is not yet available. Only the **Backend** scope is currently configurable.

Both scopes support two configuration modes:

| Mode | Description |
|------|-------------|
| **Provider-wide** | A single limit applied across all API endpoints of the provider |
| **Per Resource** | Individual limits configured per API endpoint (e.g., chat completions vs. embeddings) |

!!! note
    Provider-wide and Per Resource modes are mutually exclusive per scope. Once you configure limits in one mode, you must clear them before switching to the other.

## Limit Criteria

Each rate limit configuration supports the following criteria:

| Criterion | Description |
|-----------|-------------|
| **Request Count** | Maximum number of requests allowed within the time window |
| **Token Count** | Maximum number of tokens (combined prompt + completion) allowed within the time window |
| **Cost** | Cost-based limiting *(Coming soon)* |

You can enable Request Count, Token Count, or both simultaneously.

## Reset Duration

For each enabled criterion, you configure a **Quota** and a **Reset Duration**:

| Field | Description |
|-------|-------------|
| **Quota** | The maximum value allowed (number of requests or tokens) |
| **Reset Duration** | How long before the quota resets — `second`, `minute`, `hour` |

## Configure Rate Limiting on an LLM Provider

Rate limits configured on an LLM Provider apply to all LLM Proxies that use that provider.

1. Navigate to **AI Workspace** > **LLM Providers**.
2. Click on the provider name to open its details page.
3. Go to the **Rate Limiting** tab.

The tab is divided into two sections — **Backend** and **Per Consumer**. Only the Backend section is currently configurable; Per Consumer is coming soon.

### Provider-wide Mode

Applies a single rate limit across all endpoints of the provider.

1. Select **Provider-wide** under the Backend section.
2. Enable **Request Count**, **Token Count**, or both.
3. For each enabled criterion, set:
    - **Quota** — The maximum allowed value (e.g., `1000` requests or `500000` tokens)
    - **Reset Duration** — The time window: `second`, `minute`, `hour`
4. Click **Save**.

### Per Resource Mode

Applies individual rate limits to each API endpoint. Use this when different endpoints have significantly different usage costs (e.g., chat completions vs. embeddings).

In Per Resource mode, the configuration panel includes:

- **Limit per Resource** — A default limit that applies to all resources that do not have a specific override.
- **Individual resource rows** — Expand a specific endpoint to configure limits that apply only to that endpoint.

**To configure:**

1. Select **Per Resource** under the Backend section.
2. Expand **Limit per Resource** to set the default limits:
    - Enable **Request Count** and/or **Token Count**.
    - For each enabled criterion, set the **Quota** and **Reset Duration**.
3. To override the default for a specific endpoint, expand that resource row and configure it the same way.
4. Click **Save**.

!!! tip "Best Practice"
    Start with conservative backend limits to protect your provider credentials, then monitor actual usage from the Insights dashboard before increasing them. Switch to Per Resource only when endpoints have significantly different usage patterns.

## Related

- [Manage LLM Provider](../llm-providers/manage-provider.md#rate-limiting) — Full rate limiting configuration reference
- [Guardrails Overview](guardrails/overview.md) — Content safety and compliance policies
