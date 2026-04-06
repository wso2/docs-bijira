# MCP Proxies Overview

## What is Model Context Protocol?

MCP is a JSON-RPC–based protocol designed to standardize how applications interact with large language models (LLMs). It enables sharing of contextual information—such as local files, databases, or APIs—with LLMs, while also allowing applications to expose tools and capabilities for AI-driven workflows and integrations.

MCP follows a host–client–server architecture and supports two primary transport mechanisms: stdio and streamable HTTP. While stdio is commonly used for local communication between clients and servers on the same machine, in most cases, these servers should be deployed in remote environments with proper authorization controls, ensuring that LLM applications can securely access the data.

For more information, refer to the official [specification](https://modelcontextprotocol.io/introduction).

## What is an MCP Proxy?

An MCP Proxy lets you connect the gateway to an upstream MCP Server. The MCP Clients can connect to the dedicated endpoint provided by the gateway to connect to your upstream MCP Server.
The proxy allows you to apply various policies which allow you to control the MCP traffic through the gateway.

## What does an MCP Proxy offer?

While MCP defines an RPC-based communication model between agents and tools, it does not fully address the complexities of real-world enterprise environments.

- **Enforce Security**: Managing authentication, authorization
- **Apply Policies**: Enforcing various policies to control MCP traffic
- **Observability**: Gaining visibility into what tools, servers are being called, what's causing errors and much more.

MCP Proxy will address these challenges providing built-in security, governance, and observability for all MCP communication.

## Next Steps

- [Configure MCP Proxy](configure-proxy.md) — Step-by-step guide to create and deploy your first proxy
- [Apply Policies](apply-policies) — Apply policies after deployment