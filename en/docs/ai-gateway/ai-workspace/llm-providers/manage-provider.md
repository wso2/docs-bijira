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

Control token consumption and prevent cost overruns with two independent rate limiting views.

</div>

### Overview: Two Rate Limiting Views

The Rate Limiting tab provides **two side-by-side sections**:

| View | Purpose | Protects |
|------|---------|----------|
| **Backend** | Limits gateway → upstream provider calls | Your provider API credentials |
| **Per Consumer** | Limits application → provider calls | Fair usage across consumers |

### Backend Rate Limits

Controls calls **from the gateway to the upstream provider**.

**Configuration Modes:**

=== "Provider-wide"
    Single rate limit for **all requests** to the provider.
    
    Best for: Simple setups, consistent usage patterns

=== "Per Resource"
    Different rate limits for **each endpoint** (e.g., chat vs embeddings).
    
    Best for: Different costs per endpoint, granular control

**Adding a Backend Rate Limit:**

1. Select mode: **Provider-wide** or **Per Resource**
2. If Per Resource: Expand the endpoint to limit
3. Click **+ Add Rate Limit**
4. Configure:
    - **Limit**: Max tokens (e.g., `100000`)
    - **Time Window**: `hourly`, `daily`, or `monthly`
5. Click **Save**

---

### Per Consumer Rate Limits

Controls calls **from applications/users to the provider**.

**Configuration Modes:**

=== "Provider-wide"
    Single limit per consumer across **all endpoints**.
    
    Best for: Simple consumer quotas, uniform limits

=== "Per Resource"  
    Different limits per consumer for **each endpoint**.
    
    Best for: Granular per-consumer, per-endpoint control

**Adding a Consumer Rate Limit:**

1. Select mode: **Provider-wide** or **Per Resource**
2. If Per Resource: Expand the endpoint to limit
3. Click **+ Add Rate Limit**
4. Configure:
    - **Limit**: Max tokens per consumer (e.g., `50000`)
    - **Time Window**: `hourly`, `daily`, or `monthly`
5. Click **Save**

---

### Managing Rate Limits

- **Edit**: Click a rate limit to modify its values
- **Delete**: Click delete icon to remove
- **Auto-save**: Changes apply automatically

!!! tip "Cost Control Best Practices"
    **Backend Limits:**
    
    - Set conservative limits to protect your provider credentials
    - Monitor actual usage before increasing limits
    
    **Consumer Limits:**
    
    - Ensure fair usage across all applications
    - Start with Provider-wide for simplicity
    - Use Per Resource when endpoints have different token costs
    
    📊 **Track usage:** Monitor through the Insights dashboard and adjust as needed

**Learn more:** [Token-Based Rate Limiting Policy](../policies/token-based-rate-limit.md)

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

**Learn more:** [Guardrails Overview](../policies/guardrails/overview.md)

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
- [Configure Policies](../policies/overview.md) - Explore all available guardrails and policies
- [Monitor Usage](../../monitor-and-insights.md) - Track performance, costs, and token consumption
