# Policies Overview

The AI Workspace provides built-in policies that let you govern how traffic flows through your LLM Providers and LLM Proxies. Policies can be applied at the provider level (affecting all proxies that use the provider) or at the proxy level (scoped to a specific proxy or individual endpoints).

## Guardrails

Guardrails enforce content safety and compliance on requests and responses.

| Guardrail | Description |
|-----------|-------------|
| [Semantic Prompt Guard](guardrails/semantic-prompt-guard.md) | Block or allow prompts based on semantic similarity to configured phrases. |
| [PII Masking Regex](guardrails/regex-pii-masking.md) | Detect and mask PII in requests and responses using regex patterns. |
| [Azure Content Safety](guardrails/azure-content-safety.md) | Filter harmful content using Azure Content Safety moderation. |
| [AWS Bedrock Guardrail](guardrails/aws-bedrock-guardrail.md) | Content safety and PII protection via AWS Bedrock Guardrails. |
| [Word Count](guardrails/word-count-guardrail.md) | Enforce word count limits on prompts or responses. |
| [Sentence Count](guardrails/sentence-count-guardrail.md) | Enforce sentence count limits on prompts or responses. |
| [Semantic Cache](other-policies/semantic-cache.md) | Cache LLM responses and serve them for semantically similar requests. |

## Other Policies

| Policy | Description |
|--------|-------------|
| [Token-Based Rate Limit](other-policies/token-based-rate-limit.md) | Limit request count and token consumption via the built-in Rate Limiting tab or the Token Based Rate Limit policy. |
| [Rate Limit - Basic](other-policies/basic-rate-limit.md) | Enforce a simple request count limit within a time window. |
| [Model Round Robin](other-policies/model-round-robin.md) | Distribute requests across multiple models in round-robin order. |
| [Prompt Decorator](other-policies/prompt-decorator.md) | Prepend or append content to every request. |
| [Prompt Template](other-policies/prompt-template.md) | Apply reusable parameterized prompt templates to requests. |

## Where Policies are Applied

Policies are configured through the management tabs of your LLM Providers and LLM Proxies:

- **LLM Provider** — Rate limits and guardrails configured on a provider apply to all proxies that use it. Guardrails can be applied globally (all endpoints) or per resource (specific endpoints).
- **LLM Proxy** — Guardrails configured on a proxy can be applied globally (all endpoints) or per resource (specific endpoints).

When both provider-level and proxy-level policies are active, they are both enforced. Provider-level policies act as a baseline, and proxy-level policies add additional protection.

## Policy Hub

All guardrail policies in the AI Workspace are powered by the [Policy Hub](https://wso2.com/api-platform/policy-hub/). The Policy Hub is a central registry of all available policies and their latest versions.

Visit the [Policy Hub](https://wso2.com/api-platform/policy-hub/) to explore all available guardrails, their documentation, and configuration schemas.

## Next Steps

- [Token-Based Rate Limit](guardrails/token-based-rate-limit.md) — Set token usage limits for backend and per-consumer traffic
- [Guardrails Overview](guardrails/overview.md) — Explore available guardrails and how to configure them
