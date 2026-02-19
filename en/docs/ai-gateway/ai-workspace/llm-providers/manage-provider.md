# Manage LLM Provider

After deploying your LLM Provider, manage its configuration through the provider details page. This guide covers all management operations organized by tab.

!!! info "On This Page"
    **Provider Configuration:**
    
    - [Connection](#connection) - Endpoint and authentication settings
    - [Access Control](#access-control) - Enable/disable API endpoints
    - [Security](#security) - Application authentication setup
    - [Rate Limiting](#rate-limiting) - Token usage controls
    - [Guardrails](#guardrails) - Content safety and compliance
    - [Models](#models) - Available AI models
    
    **Lifecycle Operations:**
    
    - [Redeploy Provider](#redeploy-provider) - Push configuration updates
    - [Delete Provider](#delete-provider) - Remove provider permanently

---

## Access Provider Details

1. Navigate to **AI Workspace** > **LLM Providers**.

2. Click on a provider name to open its details page.

The provider details page shows:

- Provider name, version, and template type
- Creation and last updated timestamps  
- Six management tabs (Connection, Access Control, Security, Rate Limiting, Guardrails, Models)
- **Deploy to Gateway** button in the top right

## Connection

<div style="border-left: 4px solid #2196F3; padding-left: 16px; margin-bottom: 24px;">

Manage upstream endpoint configuration and authentication credentials for the LLM provider.

</div>

### Provider Endpoint

**Upstream URL** - Where API requests are forwarded to:

| Provider Type | URL Configuration |
|---------------|-------------------|
| OpenAI, Anthropic, Gemini, Mistral AI | Pre-configured (read-only) |
| Azure OpenAI, Azure AI Foundry | Custom URL (editable) |

**To update:**

1. Modify the **Provider Endpoint** field
2. Click **Save**

### Authentication

Configure how the gateway authenticates with the upstream provider:

- **Authentication Type**: Usually `api-key` (set by template)
- **Credentials**: Your provider API key
    - Click the 👁️ icon to show/hide the value
    - Update and click **Save** to change credentials

### OpenAPI Specification

**Spec URL** - The OpenAPI specification for importing API resources:

- Can be a URL or file upload
- Automatically populates the Access Control resources list
- Re-import to refresh available endpoints

---

## Access Control

<div style="border-left: 4px solid #4CAF50; padding-left: 16px; margin-bottom: 24px;">

Control which API endpoints are accessible through this provider. Also referred to as the **Resources** tab.

</div>

### Import API Specification

The provider's OpenAPI spec defines available endpoints:

1. Spec is automatically loaded from the provider template
2. Click **Import Specification** to manually import or refresh
3. All API paths and methods are extracted and listed

### Enable/Disable Resources

Control endpoint availability:

- **Toggle switches**: Enable/disable individual resources
- **Effect**: Disabled resources are blocked at the gateway
- **Apply**: Changes take effect immediately on next request

---

## Security

<div style="border-left: 4px solid #FF9800; padding-left: 16px; margin-bottom: 24px;">

Configure how applications authenticate when accessing this provider through the gateway.

</div>

### API Key Authentication

Set up the API key that client applications must provide:

| Field | Description | Example |
|-------|-------------|---------|
| **Authentication Type** | Authentication method | `apiKey` (default) |
| **API Key Name** | Header or query parameter name | `x-api-key`, `apikey`, `Authorization` |
| **Key Location** | Where clients send the key | `Header` (recommended) or `Query` |

**To configure:**

1. Select **Authentication Type**: `apiKey`
2. Enter **API Key Name** that applications will use
3. Choose **Key Location**:
    - **Header** - Sent in HTTP request header (most secure)
    - **Query** - Sent as URL query parameter (less secure)
4. Click **Save**

---

## Rate Limiting

<div style="border-left: 4px solid #9C27B0; padding-left: 16px; margin-bottom: 24px;">

Control request and token consumption to prevent cost overruns and ensure fair usage across all consumers.

</div>

The Rate Limiting tab provides two independent sections: **Backend** and **Per Consumer**.

| Section | Controls | Protects |
|---------|----------|----------|
| **Backend** | Requests from the gateway to the upstream LLM provider | Your provider API credentials and total spend |
| **Per Consumer** | Requests from client applications to the gateway | Fair usage across all consumers |

Both sections support two configuration modes:

- **Provider-wide** — A single limit applied across all API endpoints.
- **Per Resource** — Individual limits per API endpoint (e.g., chat completions vs. embeddings).

!!! note
    Provider-wide and Per Resource modes are mutually exclusive per section. Clear existing limits before switching modes.

### Limit Criteria

Each section lets you configure:

| Criterion | Description |
|-----------|-------------|
| **Request Count** | Maximum number of requests within the reset duration |
| **Token Count** | Maximum number of tokens (prompt + completion) within the reset duration |
| **Cost** | Cost-based limiting *(Coming soon)* |

For each enabled criterion, set the **Quota** and **Reset Duration** (`second`, `minute`, `hour`, or `all`).

### Provider-wide Configuration

1. Select **Provider-wide** in the Backend or Per Consumer section.
2. Enable **Request Count** and/or **Token Count**.
3. Enter the **Quota** and select the **Reset Duration** for each criterion.
4. Click **Save**.

### Per Resource Configuration

1. Select **Per Resource** in the Backend or Per Consumer section.
2. Expand **Limit per Resource** to set default limits for all endpoints:
    - Enable the criteria and configure **Quota** and **Reset Duration**.
3. To override limits for a specific endpoint, expand that resource row and configure it separately.
4. Click **Save**.

!!! tip "Cost Control Best Practices"
    Set conservative backend limits first to protect your provider credentials. Monitor actual usage via the Insights dashboard before increasing limits. Use Per Resource mode only when endpoints have significantly different usage patterns.

**Learn more:** [Token-Based Rate Limiting](../policies/token-based-rate-limit.md)

---

## Guardrails

<div style="border-left: 4px solid #F44336; padding-left: 16px; margin-bottom: 24px;">

Attach and configure guardrails to enforce content safety, compliance, and quality standards.

</div>

### View Attached Guardrails

The tab displays all guardrails currently attached to the provider:

- **Guardrail name** and type
- **Configuration status** and parameters
- **Enable/disable toggles** for quick activation control

### Add a Guardrail

**To attach a new guardrail:**

1. Click **+ Add Guardrail**
2. A sidebar opens showing available guardrail types
3. Select a guardrail (e.g., PII Masking, Content Filter, Semantic Cache)
4. Configure the guardrail settings:
    - Fill in required parameters
    - Expand **Advanced Settings** for additional options
5. Click **Add** to attach it to the provider

### Configure Guardrails

**To modify an existing guardrail:**

- Click on the guardrail to expand its settings
- Update parameters as needed
- Changes are auto-saved and apply immediately

!!! tip "Advanced Settings"
    Each guardrail includes advanced configuration options such as custom thresholds, severity levels, and execution phases. Click **Advanced Settings** when configuring.

!!! warning "Production Impact"
    Guardrail changes apply immediately to all deployed gateways. Test thoroughly in a non-production environment before enabling strict guardrails.

**Learn more:** [Guardrails Overview](../policies/guardrails/overview.md). For the full policy catalog, visit the [Policy Hub](https://wso2.com/api-platform/policy-hub/).

---

## Models

<div style="border-left: 4px solid #00BCD4; padding-left: 16px; margin-bottom: 24px;">

Configure which AI models are accessible through this provider.

</div>

### View Available Models

The tab shows all models currently available:

- **Model names** (e.g., `gpt-4`, `gpt-3.5-turbo`, `claude-3-opus`)
- **Model descriptions** and capabilities
- **Enable/disable status** for each model

### Add Models

**To add new models:**

1. Click **Add model provider**
2. Select a provider from the list to import its model catalog
3. Click **Add**
4. The models are added and enabled by default

### Enable/Disable Models

Control which models applications can access:

- **Toggle switches**: Enable/disable individual models
- **Effect**: Disabled models are blocked at the gateway
- Applications attempting to use disabled models will receive an error

---

## 🔄 Lifecycle Operations

---

### Redeploy Provider

Push configuration changes to deployed gateways.

**When to redeploy:**

- After updating connection settings
- After modifying rate limits or guardrails  
- After enabling/disabling resources or models

**To redeploy:**

1. Click **Deploy to Gateway** (top right corner)
2. Select the gateway(s) to deploy to
3. Review the changes summary
4. Click **Deploy**

!!! info "Deployment Status"
    Monitor deployment progress in the notification panel. Changes take effect within seconds of successful deployment.

---

### Delete Provider

Permanently remove the provider and all its configurations.

**To delete:**

1. Navigate to **AI Workspace** > **LLM Providers**
2. Find the provider in the list
3. Click the **Delete** or **🗑️** icon
4. Review the warning and confirm deletion

!!! danger "⚠️ Warning: Irreversible Action"
    Deleting a provider will:
    
    - ❌ Remove it from all deployed gateways **immediately**
    - ❌ Break any LLM Proxies using this provider
    - ❌ Break applications consuming this provider
    - ❌ Delete all configuration (guardrails, rate limits, models)
    - ❌ **Cannot be undone**
    
    **Before deleting:** Update all dependent proxies and applications to use alternative providers.

---

## Next Steps

- [Configure LLM Proxy](../llm-proxies/create-proxy.md) - Configure and deploy proxy endpoints using your provider
- [Policies Overview](../policies/overview.md) - Explore all available guardrails and policies
- [Guardrails Overview](../policies/guardrails/overview.md) - Configure content safety and compliance rules
