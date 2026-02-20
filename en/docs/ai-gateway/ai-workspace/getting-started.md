# Getting Started

The AI Workspace enables you to manage AI gateways, LLM providers, and LLM proxies. Follow these steps to get started.

## Step 1: Create an AI Gateway

An AI gateway is the runtime that processes and routes requests between your applications and LLM providers. You need at least one gateway before configuring providers or proxies.

1. Navigate to **AI Gateways** in the left navigation menu.
2. Click **+ Add AI Gateway**.
3. Fill in the **Name**, **URL**, and **Associated Environment**.
4. Click **Add Gateway**.
5. Copy the **Gateway Registration Token** and follow the setup instructions to start the gateway runtime.
6. Once connected, the gateway status changes from **Inactive** to **Active**.

For detailed instructions, see [AI Gateways](ai-gateways/setting-up.md).

## Step 2: Configure an LLM Provider

An LLM provider connects the AI Workspace to an AI service platform like OpenAI, Anthropic, or Azure OpenAI.

1. Navigate to **LLM** > **Service Provider**.
2. Click **+ Add New Provider** and select your provider type.
3. Fill in the **Name**, **Version**, and **API Key**.
4. Click **Add Provider**.
5. Click **Deploy to Gateway** and deploy to your active gateway.

For detailed instructions, see [Configure LLM Provider](llm-providers/configure-provider.md).

## Step 3: Create an LLM Proxy

An LLM proxy is a managed API endpoint that routes requests to your provider with built-in security, guardrails, and policies.

1. Navigate to **LLM** > **Proxies**.
2. Click **+ Create Proxy**.
3. Fill in the **Name**, select your **LLM Service Provider**, and set the **Version**.
4. Click **Create Proxy**.
5. Click **Deploy to Gateway** and deploy to your active gateway.
6. Click **Generate API Key** to get credentials for calling the proxy.

For detailed instructions, see [Configure LLM Proxy](llm-proxies/configure-proxy.md).

## What's Next

- [Manage your provider](llm-providers/manage-provider.md) — Configure connection, access control, security, rate limiting, guardrails, and models
- [Manage your proxy](llm-proxies/manage-proxy.md) — Configure provider settings, resources, security, and guardrails

