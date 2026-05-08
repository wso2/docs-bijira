# Get Started

Not sure where to begin? This page helps you find the right quick start guide based on what you are trying to do.

## What do you want to do?

### I want to manage and govern APIs through a UI
You want the full platform experience: a web console to create, deploy, test, and govern APIs visually.

**If you want WSO2 to host it (Cloud):**

| Guide | What you will do |
| :--- | :--- |
| [Publish your first API proxy →](cloud/introduction/quick-start-guide.md) | Create a REST API proxy, deploy it, and invoke it from the cloud console. Takes about 10 minutes. |
| [Publish your first LLM proxy →](cloud/ai-gateway/llm/quick-start-guide.md) | Set up a managed proxy to an LLM provider (such as OpenAI) with guardrails and rate limiting through the cloud UI. |
| [Publish your first MCP proxy →](cloud/ai-gateway/mcp/quick-start-guide.md) | Expose a REST API as an MCP tool that AI agents can discover and invoke, configured through the cloud console. |
| [Set up a hybrid gateway →](cloud/api-platform-gateway/getting-started.md) | Connect a self-hosted gateway to the cloud control plane so that API traffic stays in your infrastructure. |

**If you want to run it yourself (API Manager):**

| Guide | What you will do |
| :--- | :--- |
| [Install API Manager →](api-manager/overview.md) | Download and set up API Manager on Docker or Kubernetes. |
| [Publish your first API proxy →](api-manager/overview.md) | Create and deploy an API through the self-managed Publisher UI. |

### I want to run a standalone gateway (no UI, YAML and CLI only)
You want a lightweight gateway that you can download and run immediately. There is no control plane and no web console. Everything is configured through YAML files and CLI.

**For API traffic:**

| Guide | What you will do |
| :--- | :--- |
| [API Gateway: Setting up →](api-gateway/setup/storage-and-backends.md) | Install and configure the gateway runtime (Docker or binary). |
| [API Gateway: Getting started →](api-gateway/quick-start-guide.md) | Configure your first API proxy using YAML and start routing traffic. |

**For AI traffic (LLMs and MCP):**

| Guide | What you will do |
| :--- | :--- |
| [AI Gateway: Setting up →](ai-gateway/deployment-modes/kubernetes/overview.md) | Install and configure the AI Gateway runtime (Docker or binary). |
| [LLM Proxy: Quick start →](ai-gateway/llm-proxy/quick-start-guide.md) | Configure an LLM provider, apply a guardrail, and route your first LLM request. |
| [MCP Proxy: Quick start →](ai-gateway/mcp-proxy/quick-start-guide.md) | Expose a REST API as an MCP tool and invoke it through an MCP client. |

### I want to govern AI services at the organizational level
You already have gateways running and now want centralized management of LLM providers, MCP servers, guardrails, and cost controls across your organization.

| Guide | What you will do |
| :--- | :--- |
| [AI Workspace: Getting started →](cloud/ai-workspace/getting-started.md) | Set up an AI Workspace, connect it to an AI Gateway, and configure your first LLM provider with guardrails. |

### I want to set up a developer portal
You want external or internal developers to discover, subscribe to, and consume your APIs through a portal.

| Guide | What you will do |
| :--- | :--- |
| [API Portal: Quick start →](cloud/devportal/theming-devportal-with-ai.md) | Set up a developer portal, publish APIs for discovery, and configure developer self-service. |

### I want to monetize my APIs
You want to track API usage, set up paid subscription plans, and implement usage-based billing.

| Guide | What you will do |
| :--- | :--- |
| [Monetization: Getting started →](cloud/api-monetization/getting-started.md) | Connect Moesif, create a paid subscription plan, and start tracking API revenue. |

## After your first quick start
Once you have completed a quick start guide, here is where to go next:

| I want to... | Go here |
| :--- | :--- |
| Explore the full feature docs for my product | [Cloud](cloud/introduction/what-is-bijira.md) · [API Manager](api-manager/overview.md) · [API Gateway](api-gateway/overview.md) · [AI Gateway](ai-gateway/llm-proxy/quick-start-guide.md) |
| Follow end-to-end scenarios spanning multiple components | [Guides →](guides/ai-and-mcp/convert-rest-api-to-mcp-server.md) |
| Try runnable code samples | [Samples →](cloud/samples/samples-overview.md) |
| Understand platform concepts (organizations, projects, data planes) | [Concepts →](cloud/bijira-concepts/organization.md) |
| Browse reusable policies and guardrails | [Policy Hub →](policy-hub/overview.md) |
| Not sure which product is right for me | [Platform overview →](overview.md) |