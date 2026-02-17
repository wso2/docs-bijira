# Configure LLM Provider

LLM Providers allow you to connect AI service platforms like OpenAI, Anthropic, and others to the AI Workspace. Once configured, you can use these providers across multiple LLM Proxies.

## Prerequisites

- Access to Bijira Console with Admin or Developer role
- API credentials for your LLM provider (API key, access tokens, etc.)

## Add a New Provider

1. Navigate to **AI Workspace** in your Bijira dashboard.
2. Select **Service Providers** from the menu.
3. Click **+ Add New Provider** and choose your provider type (e.g., **OpenAI**, **Anthropic**).

   ![Select LLM Provider](../../../assets/img/ai-gateway/ai-workspace/llm-provider/select-llm-provider-type.png)

## Configure Provider Details

After selecting your provider type, fill in the provider configuration form:

   ![Select LLM Provider](../../../assets/img/ai-gateway/ai-workspace/llm-provider/llm-provider-details.png)

### Basic Information

1. **Name*** (Required): Enter a unique name for the provider (e.g., `openai-production`, `anthropic-dev`).

2. **Version*** (Required): The version is pre-filled (e.g., `v1.0`). You can edit this if needed.

3. **Description** (Optional): Add a description to identify the provider's purpose.

4. **Context** (Optional): Enter the context path (default: `/`). This is the base context for the provider.

### Authentication

The authentication fields vary depending on the provider you selected:

=== "OpenAI"
    **API Key*** (Required): Enter your OpenAI API key (starts with `sk-proj-` or `sk-`).
    
    !!! info
        OpenAI's endpoint URL is pre-configured automatically.

=== "Anthropic"
    **API Key*** (Required): Enter your Anthropic API key (starts with `sk-ant-`).
    
    !!! info
        Anthropic's endpoint URL is pre-configured automatically.

=== "Gemini"
    **API Key*** (Required): Enter your Google AI API key.
    
    !!! info
        Gemini's endpoint URL is pre-configured automatically.

=== "Mistral AI"
    **API Key*** (Required): Enter your Mistral AI API key.
    
    !!! info
        Mistral AI's endpoint URL is pre-configured automatically.

=== "Azure OpenAI"
    1. **Upstream URL*** (Required): Enter your Azure OpenAI resource endpoint (e.g., `https://your-resource.openai.azure.com/`).
    2. **API Key*** (Required): Enter your Azure OpenAI API key.

=== "Azure AI Foundry"
    1. **Upstream URL*** (Required): Enter your Azure AI Foundry endpoint URL.
    2. **API Key*** (Required): Enter your Azure AI Foundry API key.

### Add Guardrails (Optional)

You can attach policies and guardrails to your provider that apply to all requests:

1. In the **Guardrails** section of the form, click **+ Add Guardrail**.

2. A sidebar will open showing available guardrails and policies.

3. Click on a guardrail to select it and configure its settings.

4. Click **Add** to attach it to the provider.

!!! tip "Advanced Settings"
    Each guardrail includes advanced configuration options that allow you to fine-tune its behavior. After selecting a guardrail, you can configure these settings before attaching it to the provider.

!!! info
    Learn more about each policy in the [Policies section](../policies/overview.md).

## Save Provider

1. After configuring all settings and adding guardrails (if needed), click **Add Provider**.

2. You'll see a confirmation message indicating the provider was created successfully.

3. The provider will appear in the providers list.

## Deploy Provider to Gateway

After creating your provider, you must deploy it to a gateway before it can be used.

!!! warning "Required Step"
    Your provider will not be functional until it is deployed to at least one gateway.

1. Click the **Deploy to Gateway** button in the top right corner.

2. Click **Deploy** on one or more gateways from the available list.

3. Wait for the deployment to complete. The status will change to **Deployed**.

## Next Steps

- [Configure LLM Proxy](../llm-proxies/create-proxy.md) - Configure and deploy a proxy endpoint using your provider
- [Manage Provider](manage-provider.md) - Configure access control, security, rate limiting, and more