# LLM Instructions

LLM Instructions allow portal admins to provide AI agents with high-level context about the developer portal — what APIs are available, how the portal is organized, and any conventions or constraints agents should follow when interacting with it.

These instructions are published as part of the portal's `llms.txt` file, which is the primary entry point for AI agents discovering the portal's capabilities.

## What Are LLM Instructions?

LLM Instructions are free-form natural language text written by the portal admin. They appear at the top of `llms.txt` and are read by agents before they navigate the rest of the portal's content.

Use this space to tell agents:

- What the portal covers and what kind of APIs it exposes
- How APIs are organized (by product area, team, lifecycle stage, etc.)
- Any authentication conventions agents should be aware of
- Which workflows are the recommended starting points for common tasks
- Any limitations or usage policies agents should respect

Well-written LLM instructions reduce agent errors and improve the quality of AI-assisted integrations by giving agents the orientation they need upfront, rather than leaving them to infer context from individual API specs.

## Writing Effective LLM Instructions

### Describe the portal's purpose and scope

Start with a one-paragraph summary of what the portal covers. Agents use this to decide whether this portal is relevant to the task they are trying to accomplish.

**Example:**

> This developer portal exposes the APIs for the Acme Commerce Platform — a set of services covering product catalog management, order processing, inventory, and customer accounts. All APIs require OAuth 2.0 authentication using the client credentials flow.

### Orient agents to the API landscape

If the portal contains many APIs, describe how they are grouped or how they relate to each other. This helps agents avoid calling the wrong API for a task.

**Example:**

> APIs are organized into three domains: **Catalog** (read-only product and category data), **Commerce** (order creation and fulfillment), and **Identity** (customer and account management). Most workflows span the Commerce and Catalog domains.

### Highlight key workflows

If there are published API Workflows that cover the most common tasks, mention them by name. Agents that are aware of these workflows will prefer them over improvising their own call sequences.

**Example:**

> For placing an order end-to-end, use the **Place Order Workflow**. For managing webhook registrations, use the **Register Webhook Workflow**. These cover the most common integration patterns and include step-by-step Arazzo specifications.

### Include any constraints or policies

If there are rate limits, usage policies, or environments agents should be aware of, state them here.

**Example:**

> The sandbox environment is available at `https://sandbox-api.acme.com`. Use it for all testing. Production endpoints are at `https://api.acme.com` and require a production client ID.

---

## Configuring LLM Instructions

LLM Instructions are configured at the portal (view) level in the admin settings.

1. In the admin console, navigate to **Developer Portal** and select the portal you want to configure.
2. Open the **Settings** tab.
3. Select **LLM Instructions**.
4. Enter your instructions in the text editor.
5. Click **Save**.

<!-- Screenshot: Admin settings page showing the LLM Instructions text editor -->

Changes take effect immediately — the updated instructions are reflected in `llms.txt` as soon as you save.

## Previewing the Output

To verify how your instructions appear to agents, fetch the portal's `llms.txt` directly:

```
GET /{orgName}/views/{viewName}/llms.txt
```

Your LLM Instructions will appear at the top of the file, followed by the portal's API and workflow index.

<!-- Screenshot: llms.txt output in a browser showing LLM Instructions at the top -->
