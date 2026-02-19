# Configure LLM Proxy

LLM Proxies provide a managed API gateway layer that routes requests to your configured LLM providers with built-in authentication, resource management, security policies, and guardrails.

## Prerequisites

!!! info "Before You Begin"
    - Access to Bijira Console with **Admin** or **Developer** role
    - At least one [configured and deployed LLM Provider](../llm-providers/configure-provider.md)

---

## Create a New Proxy

1. Navigate to **LLM** > **Proxies** in the left navigation menu.

2. Click **+ Create Proxy** button.

3. Fill in the required proxy details:

    1. **Name*** (Required): Enter a unique name for the proxy (e.g., `chat-api`, `text-generation-proxy`). The Proxy ID is auto-generated from the name (lowercase, hyphen-separated).

    2. **LLM Service Provider*** (Required): Select the LLM provider this proxy will route to from the dropdown (defaults to the latest updated provider).

    3. **Version*** (Required): The version is pre-filled (e.g., `v1.0`). You can edit this if needed.

    4. **Description** (Optional): Add a brief description to identify the proxy's purpose.

    5. **Context** (Optional): Enter the context path (default: `/`). This is the base path for proxy endpoints (normalized with "/" prefix).

4. Click **Create Proxy** to save the proxy.

---

## Add Guardrails (Optional)

You can attach policies and guardrails to your proxy that apply to all requests:

1. In the **Guardrails** tab, click **+ Add Guardrail**.

2. A sidebar will open showing available guardrails and policies.

3. Click on a guardrail to select it and configure its settings.

4. Click **Submit** to attach it to the proxy.

!!! tip "Advanced Settings"
    Each guardrail includes advanced configuration options that allow you to fine-tune its behavior. After selecting a guardrail, you can configure these settings before attaching it to the proxy.

!!! info
    Learn more about available guardrails in the [Guardrails Overview](../policies/guardrails/overview.md). For the full list of policies and their specifications, visit the [Policy Hub](https://wso2.com/api-platform/policy-hub/).

---

## Deploy Proxy to Gateway

After creating your proxy, you must deploy it to a gateway before it can be used.

!!! warning "Required Step"
    Your proxy will not be functional until it is deployed to at least one gateway.

1. Click the **Deploy to Gateway** button in the top-right corner of the proxy details page.

2. The **Deploy to Gateway** page opens, showing all available gateways. Use the search bar to find a specific gateway.

3. Each gateway card displays:
    - **Gateway name** and **status** (Active or Not Active)
    - **Current Deployment** identifier (if previously deployed)

4. Click **Deploy** next to the gateway you want to deploy to.

5. Once deployed, expand the gateway card to view deployment details:

    | Field | Description |
    |-------|-------------|
    | **Deployment Status** | Active or Inactive |
    | **Deployment ID** | Unique identifier for the deployment |
    | **Deployed** | Time since deployment |
    | **Stop** | Button to stop an active deployment |

6. The **API Deployment History** panel on the right shows the deployment timeline:
    - Deployment identifier and timestamp
    - Status tags (**Latest**, **Deployed**)

**To stop a deployment:**

Click the **Stop** button next to an active deployment to undeploy the proxy from that gateway.

Click **Back to LLM Proxy** to return to the proxy details page.

!!! info "Deployment Status"
    Monitor deployment progress on this page. Changes take effect within seconds of successful deployment.

---

## Next Steps

- [Manage Your Proxy](manage-proxy.md) - Configure provider, resources, security, and guardrails
- [Apply Policies](../policies/overview.md) - Learn about available policies for rate limiting and caching
