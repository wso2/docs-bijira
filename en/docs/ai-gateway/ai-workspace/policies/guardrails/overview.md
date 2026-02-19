# Guardrails Overview

Guardrails inspect and act on the content of requests and responses flowing through the AI Gateway — detecting unsafe content, masking sensitive data, and caching responses. They run without any changes to client applications.

## Available Guardrails

| Guardrail | Description |
|-----------|-------------|
| [Semantic Prompt Guard](semantic-prompt-guard.md) | Block or allow prompts based on semantic similarity to configured phrases. Requires an embedding provider. |
| [PII Masking Regex](regex-pii-masking.md) | Detect and mask Personally Identifiable Information (PII) using regex patterns. No external service required. |
| [Azure Content Safety](azure-content-safety.md) | Filter harmful content (hate, sexual, self-harm, violence) using Azure Content Safety. Requires an Azure subscription. |
| [Semantic Cache](semantic-cache.md) | Cache LLM responses and serve them for semantically similar future requests. Requires an embedding provider and vector database. |

## How Guardrails Work

| Guardrail | Behavior |
|-----------|----------|
| **Semantic Prompt Guard** | Blocks requests with `422 Unprocessable Entity` if the prompt is semantically similar to a denied phrase, or not similar enough to any allowed phrase. |
| **PII Masking Regex** | Masks PII in the request before forwarding upstream. In masking mode, original values are restored in the response. Does not block requests. |
| **Azure Content Safety** | Blocks requests or responses with `422 Unprocessable Entity` if content meets or exceeds a configured severity threshold. |
| **Semantic Cache** | Returns a cached LLM response (`200`) for semantically similar requests, bypassing the upstream LLM entirely. |

## Applying Guardrails

Guardrails can be configured on both LLM Providers and LLM Proxies:

| Level | Scope | Best For |
|-------|-------|----------|
| **LLM Provider (Global)** | All endpoints, across all proxies using the provider | Organization-wide policies applied uniformly (e.g., PII masking) |
| **LLM Provider (Per Resource)** | A specific endpoint, across all proxies using the provider | Endpoint-specific provider-level rules |
| **LLM Proxy (Global)** | All endpoints of the proxy | Proxy-wide rules (e.g., content filters for a specific app) |
| **LLM Proxy (Per Resource)** | A specific endpoint within the proxy | Endpoint-specific rules scoped to a single proxy |

When guardrails are configured at multiple levels, all of them are evaluated. Provider-level guardrails run first, followed by proxy-level guardrails.

### How to Add a Guardrail

**On an LLM Provider:**

1. Navigate to **AI Workspace** > **LLM Providers**.
2. Click on the provider name.
3. Go to the **Guardrails** tab.
4. To add a guardrail to all endpoints, click **+ Add Guardrail** under **Global Guardrails**.
5. To add a guardrail to a specific endpoint, expand the resource card and click **+ Add Guardrail**.
6. Select a guardrail from the sidebar panel.
7. Configure the guardrail parameters.
8. Click **Add**.
9. Click **Deploy to Gateway** to apply the changes.

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

## Guardrail Intervention Response

When a guardrail blocks a request or response, it returns the following structure:

```json
{
  "type": "<GUARDRAIL_TYPE>",
  "message": {
    "action": "GUARDRAIL_INTERVENED",
    "interveningGuardrail": "<guardrail name>",
    "direction": "REQUEST or RESPONSE",
    "actionReason": "<reason for intervention>",
    "assessments": "<detailed assessment (if Show Assessment is enabled)>"
  }
}
```

## Learn More

The [Policy Hub](https://wso2.com/api-platform/policy-hub/) is the central registry for all guardrail policies. It contains full documentation, configuration schemas, and the latest versions of each guardrail.
