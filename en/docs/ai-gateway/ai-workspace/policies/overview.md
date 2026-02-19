# Policies Overview

The AI Workspace provides built-in policies that let you govern how traffic flows through your LLM Providers and LLM Proxies. Policies can be applied at the provider level (affecting all proxies that use the provider) or at the proxy level (scoped to a specific proxy or individual endpoints).

## Available Policies

| Policy | Description |
|--------|-------------|
| [Token-Based Rate Limit](token-based-rate-limit.md) | Control LLM token consumption to manage costs and ensure fair usage across consumers. |
| [Guardrails](guardrails/overview.md) | Enforce content safety, compliance, and quality standards on requests and responses. |

## Where Policies are Applied

Policies are configured through the management tabs of your LLM Providers and LLM Proxies:

- **LLM Provider** — Rate limits and guardrails configured on a provider apply to all proxies that use it. Guardrails can be applied globally (all endpoints) or per resource (specific endpoints).
- **LLM Proxy** — Guardrails configured on a proxy can be applied globally (all endpoints) or per resource (specific endpoints).

When both provider-level and proxy-level policies are active, they are both enforced. Provider-level policies act as a baseline, and proxy-level policies add additional protection.

## Policy Hub

All guardrail policies in the AI Workspace are powered by the [Policy Hub](https://wso2.com/api-platform/policy-hub/). The Policy Hub is a central registry of all available policies and their latest versions.

Visit the [Policy Hub](https://wso2.com/api-platform/policy-hub/) to explore all available guardrails, their documentation, and configuration schemas.

## Next Steps

- [Token-Based Rate Limit](token-based-rate-limit.md) — Set token usage limits for backend and per-consumer traffic
- [Guardrails Overview](guardrails/overview.md) — Explore available guardrails and how to configure them
