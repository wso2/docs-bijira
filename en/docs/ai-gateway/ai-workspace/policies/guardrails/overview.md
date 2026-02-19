# Guardrails Overview

Guardrails are policies that you attach to LLM Providers and LLM Proxies to control how traffic flows through the AI Gateway. They can enforce authentication, apply rate limits, manage cross-origin access, inspect content for safety and compliance, enhance prompts, and cache responses — all without changes to client applications.

## How Guardrails Work

When a guardrail is attached to an LLM Provider or Proxy, the AI Gateway runs it on every request and response. What the guardrail does depends on its type:

| Guardrail type | Behavior |
|----------------|----------|
| **Security & Access Control** (API Key Auth, JWT Auth, CORS) | Validates the request and rejects it with `401` or `403` if authentication or origin checks fail. |
| **Traffic Management** (Rate Limit - Basic, Token Based Rate Limit) | Counts requests or token usage and rejects excess traffic with `429 Too Many Requests`, including a `Retry-After` header. |
| **Prompt Enhancement** (Prompt Decorator, Prompt Template) | Modifies the request payload before forwarding it upstream. Does not block requests. |
| **Content Safety** (Semantic Prompt Guard, Azure Content Safety) | Inspects content and blocks violating requests or responses with `422 Unprocessable Entity`. |
| **PII Masking** (PII Masking Regex) | Detects and masks sensitive information in the request or response. Does not block — the modified payload is forwarded normally. |
| **Model Round Robin** | Rewrites the model in the request and routes to the next available model. Does not block requests. |
| **Semantic Cache** | Returns a cached LLM response (`200`) for semantically similar requests, bypassing the upstream LLM entirely. |

## Applying Guardrails

Guardrails can be configured on both LLM Providers and LLM Proxies:

| Level | Scope | Best For |
|-------|-------|----------|
| **LLM Provider** | All proxies using the provider | Organization-wide policies (e.g., authentication, PII masking) |
| **LLM Proxy (Global)** | All endpoints of the proxy | Proxy-wide rules (e.g., content filters for a specific app) |
| **LLM Proxy (Per Resource)** | A single endpoint within the proxy | Endpoint-specific rules (e.g., stricter limits on sensitive endpoints) |

When guardrails are configured at multiple levels, all of them are evaluated. Provider-level guardrails run first, followed by proxy-level guardrails.

### How to Add a Guardrail

**On an LLM Provider:**

1. Navigate to **AI Workspace** > **LLM Providers**.
2. Click on the provider name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail**.
5. Select a guardrail from the sidebar panel.
6. Configure the guardrail parameters.
7. Click **Add**.
8. Click **Deploy to Gateway** to apply the changes.

**On an LLM Proxy:**

1. Navigate to **AI Workspace** > **LLM Proxies**.
2. Click on the proxy name.
3. Go to the **Guardrails** tab.
4. To add a guardrail to all endpoints, click **+ Add Guardrail** under **Global Guardrails**.
5. To add a guardrail to a specific endpoint, expand the resource under **Resource-wise Guardrails** and click **+ Add Guardrail**.
6. Select a guardrail from the sidebar panel.
7. Configure the guardrail parameters.
8. Click **Submit**.
9. Save the proxy configuration and redeploy as needed.

## Available Guardrails

### Security & Access Control

These guardrails control who can access the LLM Provider or Proxy and from where.

| Guardrail | Description |
|-----------|-------------|
| [API Key Auth](api-key-auth.md) | Validate incoming requests using an API key from a header or query parameter. |
| [JWT Auth](jwt-auth.md) | Validate JWT tokens with support for remote JWKS endpoints, claim validation, and claim forwarding. **Requires a key manager configuration.** |
| [CORS](cors.md) | Handle cross-origin resource sharing — validate `Origin` headers and respond to preflight requests. |

### Traffic Management

These guardrails control the rate and volume of traffic flowing through the gateway.

| Guardrail | Description |
|-----------|-------------|
| [Rate Limit - Basic](basic-rate-limit.md) | Enforce a simple request count limit within a configurable time window. |
| [Token Based Rate Limit](token-based-ratelimit.md) | Enforce rate limits based on LLM token consumption (prompt tokens, completion tokens, or total tokens). |
| [Model Round Robin](model-round-robin.md) | Distribute requests across multiple AI models using round-robin selection, with automatic model suspension on failures. |

### Prompt Enhancement

These guardrails modify or transform prompts before they reach the LLM.

| Guardrail | Description |
|-----------|-------------|
| [Prompt Decorator](prompt-decorator.md) | Prepend or append text or chat messages to every request — useful for injecting system instructions or safety guidelines. |
| [Prompt Template](prompt-template.md) | Apply reusable parameterized prompt templates. Clients reference templates by name and pass parameters, which the gateway substitutes before forwarding to the LLM. |

### Content Safety

These guardrails inspect content to detect and block unsafe, non-compliant, or sensitive information.

| Guardrail | Description |
|-----------|-------------|
| [Semantic Prompt Guard](semantic-prompt-guard.md) | Allow or deny prompts based on semantic similarity to a configured list of allowed/denied phrases. **Requires an embedding provider (OpenAI, Mistral AI, or Azure OpenAI).** |
| [PII Masking Regex](regex-pii-masking.md) | Detect and mask Personally Identifiable Information (PII) using configurable regular expression patterns. No external service required. |
| [Azure Content Safety Content Moderation](azure-content-safety.md) | Use Azure Content Safety to detect hate speech, sexual content, self-harm, and violence. **Requires an Azure Content Safety subscription.** |

### Performance

These guardrails optimize LLM usage and reduce costs.

| Guardrail | Description |
|-----------|-------------|
| [Semantic Cache](semantic-cache.md) | Cache LLM responses and serve them for semantically similar future requests — reducing latency and API costs. **Requires an embedding provider and a vector database (Redis or Milvus).** |

## Guardrail Intervention Response

When a content safety guardrail intervenes, it returns an error response with the following structure:

```json
{
  "message": {
    "action": "GUARDRAIL_INTERVENED",
    "actionReason": "<reason for intervention>",
    "assessments": "<detailed assessment (if Show Guardrail Assessment is enabled)>",
    "direction": "REQUEST or RESPONSE",
    "interveningGuardrail": "<guardrail name>"
  },
  "type": "<GUARDRAIL_TYPE>"
}
```

## Learn More

The [Policy Hub](https://wso2.com/api-platform/policy-hub/) is the central registry for all guardrail policies. It contains full documentation, configuration schemas, and the latest versions of each guardrail.
