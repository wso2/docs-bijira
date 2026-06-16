# Monetize an MCP Server with Stripe

## Overview

This guide shows you how to charge for an MCP Server using WSO2 API Platform's Stripe integration — without writing any billing code. The platform syncs usage to Stripe, handles payment processing, enforces subscription access, and gives consumers a self-service billing portal. By the end, you'll have a published Reading List MCP Server with Free and Pay-as-you-go subscription plans, a Stripe-powered checkout flow, and per-invocation metering that works automatically on every authenticated tool call made by an AI agent or MCP client.

---

## Key Concepts

Before you start, here are the WSO2 API Platform terms this guide uses:

**WSO2 API Platform** is the platform you'll use to create, publish, and monetize your MCP Server. The API Platform Console at [console.bijira.dev](https://console.bijira.dev) is the web interface where you do this work.

**MCP Server** is a managed Model Context Protocol endpoint that exposes one or more tools to AI agents and MCP clients. The platform can generate an MCP Server from an existing API contract or an HTTP backend, automatically deriving the tool schemas. The gateway enforces authentication, applies rate limits, and produces audit logs on every tool invocation — without any changes to your backend.

**Tool** is a single capability exposed by the MCP Server (for example, `listBooks` or `createBook`). Each authenticated tool invocation is metered as one unit of usage.

**Subscription plan** is a named pricing tier — Free, Flat, Unit, Volume, or Graduated — that controls which consumers can access an MCP Server and what they pay for it.

**Stripe integration** is connected at the organization level. Once configured, the platform automatically creates Stripe products, prices, customers, and subscriptions, and reports usage records to Stripe on your behalf.

**Developer Portal** is the self-service hub at [devportal.bijira.dev](https://devportal.bijira.dev) where consumers discover published MCP Servers, subscribe to plans, complete Stripe-powered checkout, and download invoices. You can also customize it into an MCP-only experience — an [MCP Hub](../../cloud/mcp-servers/devportal-mcp-hub.md).

**Application** is a client identity in WSO2 API Platform. You subscribe an application to an MCP Server under a specific plan, then generate OAuth2 credentials for that application.

**Billing & Usage** is the Developer Portal section where consumers track their tool consumption, view upcoming charges, download invoices, and manage or cancel subscriptions.

---

## Prerequisites

- A WSO2 API Platform account. Sign up for free at [console.bijira.dev](https://console.bijira.dev).
- A Stripe account with your Publishable Key and Secret Key. These are available in the Stripe Dashboard under **Developers > API Keys**.
- An MCP client for testing — the built-in MCP Playground in the Developer Portal, or an external client such as the VS Code Copilot Agent.

---

## Architecture

```
AI agents / MCP clients

    |  Streamable HTTP + OAuth2 bearer token
    v

+---------------------------+
|     WSO2 API Gateway      |
|  auth · rate limit · audit|
+---------------------------+

    |  HTTP                          |  usage records
    v                                v

Your backend service         +---------------------------+
                             |     Stripe                |
                             |  metering · invoicing     |
                             |  payment · portal         |
                             +---------------------------+
```

Consumers subscribe to a plan in the Developer Portal, pay via Stripe checkout, and connect their AI agent or MCP client with an OAuth2 bearer token. The gateway enforces authentication and rate limits on every tool invocation, then forwards the request to your backend. In parallel, the platform reports usage records to Stripe. Stripe handles invoicing, payment collection, and the consumer billing portal — WSO2 API Platform never touches payment details.

---

## Step 1: Create an Organization and Project

Go to the [API Platform Console](https://console.bijira.dev) and sign in with your Google, GitHub, or Microsoft account.

If this is your first time signing in, you'll be prompted to create an organization. Enter `sampleorganization` as the name, accept the privacy policy and terms of use, and click **Create**.

Once you're on the organization home page, create a project:

1. Click **+ Create Project**.
2. Enter the following details:

    | Field | Value |
    |---|---|
    | **Display Name** | Sample Project |
    | **Identifier** | sample-project |
    | **Description** | My sample project |

3. Click **Create**.

**Expected result:** The project home page opens.

---

## Step 2: Create and Deploy an MCP Server

Create an MCP Server from the Reading List OpenAPI spec. The platform generates the tool schemas automatically, and the gateway protects and meters every tool invocation.

1. On the project home page, select **MCP Server** and click **Import API Contract** under **Expose APIs as MCP Servers**.
2. Click **URL for API Contract**, paste the following URL, and click **Next**:

    ```
    https://raw.githubusercontent.com/wso2/bijira-samples/refs/heads/main/reading-list-api/openapi.yaml
    ```

3. On the **Create MCP Server from Contract** page, click **Create**.

**Expected result:** The MCP Server is created with tools auto-generated from the Reading List API spec.

![MCP Server created from the Reading List OpenAPI contract with tools auto-generated](../../assets/img/guides/monetization/mcp-monetization/create-mcp-server.png){.cInlineImage-full}

Then deploy the MCP Server to make it reachable:

1. In the left navigation menu, click **Deploy**.
2. Click **Deploy** in the **Development** card.
3. Click **Promote** to promote the MCP Server to Production. Select **Use Development endpoint configuration** and click **Next**.

**Expected result:** The **Production** card shows **Deployment Status** as **Active**.

![Deploy page showing Production card with Deployment Status as Active after MCP Server promotion](../../assets/img/guides/monetization/mcp-monetization/deploy-mcp-server.png){.cInlineImage-full}

---

## Step 3: Connect Stripe

Connect your Stripe account at the organization level. The platform uses these credentials to create Stripe products, prices, and usage records on your behalf — you don't write any billing code.

1. In the API Platform Console header, go to the **Organization** list and select your organization.
2. In the left navigation menu, click **Admin**, then click **Settings**.
3. Click the **Credentials** tab, then the **Stripe Credentials** sub-tab.
4. Click **Add Stripe Credentials**.
5. Enter your **Secret Key** and **Publishable Key** from the Stripe Dashboard.
6. Click **Save**.

**Expected result:** Your Stripe account is connected and ready to process payments for MCP Server subscriptions.

![Add Stripe Credentials panel showing Secret Key and Publishable Key fields](../../assets/img/guides/monetization/mcp-monetization/add-stripe-credentials.png){.cInlineImage-full}

!!! note
    You can use a Standard secret key or a Restricted secret key. For Restricted keys, see [Getting Started with API Monetization](../../cloud/api-monetization/getting-started.md) for the minimum permissions required.

---

## Step 4: Create Subscription Plans

Create two subscription plans: a free tier for developers to explore the MCP Server, and a paid pay-as-you-go tier for production use.

In the left navigation menu, click **Admin**, then click **Settings**. Click the **Subscription Plans** tab, then click **+ Create**.

**Create the Free plan:**

| Field | Value |
|---|---|
| **Name** | Free |
| **Description** | Explore the Reading List MCP Server at no cost |
| **Request Count** | 100 |
| **Request Count Time Unit** | Minute |
| **Pricing Model** | Free |

Click **Create**.

**Create the Pay-as-you-go plan:**

| Field | Value |
|---|---|
| **Name** | Pay-as-you-go |
| **Description** | Pay $0.02 per tool invocation, billed monthly |
| **Request Count** | 1000 |
| **Request Count Time Unit** | Minute |
| **Pricing Model** | Unit |
| **Currency** | USD |
| **Billing Period** | Monthly |
| **Unit Amount** | 0.02 |

Click **Create**.

**Expected result:** Both plans appear in the Subscription Plans list.

![Subscription Plans list showing the Free and Pay-as-you-go plans after creation](../../assets/img/guides/monetization/mcp-monetization/create-subscription-plans.png){.cInlineImage-full}

!!! note
    In usage-based models, a unit equals one MCP tool invocation. With the Unit model, the total charge is invocation count × unit price. For tiered pricing, use Volume or Graduated instead.

---

## Step 5: Assign Plans to the MCP Server

Enable your subscription plans on the Reading List MCP Server so consumers can discover and subscribe to them in the Developer Portal.

1. In the left navigation menu of your Reading List MCP Server, click **Manage**, then click **Monetize**.
2. Enable the toggle for **Free**.
3. Enable the toggle for **Pay-as-you-go**.
4. Click **Save**.

**Expected result:** Both plans are active on the MCP Server and will appear in the Developer Portal subscription dialog.

![Monetize page showing Free and Pay-as-you-go plan toggles enabled on the Reading List MCP Server](../../assets/img/guides/monetization/mcp-monetization/assign-plans-to-mcp.png){.cInlineImage-full}

!!! tip
    You can mix free and paid plans on the same MCP Server. This lets you offer a free tier for exploration alongside paid tiers for production, without managing separate MCP Servers.

---

## Step 6: Publish the MCP Server to the Developer Portal

Publish the MCP Server so consumers can discover it, review available plans, and subscribe.

1. In the left navigation menu, click **Develop**, then click **Lifecycle**.
2. Click **Publish**.
3. In the **Publish MCP Server** dialog, confirm the details and click **Confirm**.

**Expected result:** The lifecycle state changes to **Published** and the MCP Server appears in the Developer Portal.

![Publish MCP Server dialog showing the Reading List MCP Server details before confirming publication](../../assets/img/guides/monetization/mcp-monetization/publish-mcp.png){.cInlineImage-full}

!!! info
    To present a tailored, MCP-only experience to your consumers, configure the Developer Portal as an MCP Hub. See the [MCP Hub documentation](../../cloud/mcp-servers/devportal-mcp-hub.md).

---

## Step 7: Subscribe to the Paid Plan

As a consumer, subscribe to the Pay-as-you-go plan through the Developer Portal.

1. Go to [devportal.bijira.dev](https://devportal.bijira.dev) and sign in.
2. In the sidebar, click **MCP Servers**.
3. Find the Reading List MCP Server and click **Subscribe**.
4. In the **Choose Your Subscription Plan** dialog, select an application from the dropdown, or create one named `Reading List App`.
5. Click **Subscribe** on the **Pay-as-you-go** plan.
6. A Stripe checkout window opens. Enter your payment details and complete the payment.

**Expected result:** The application is subscribed to the Reading List MCP Server under the Pay-as-you-go plan. The Stripe checkout confirmation is shown.

![Stripe checkout confirmation after subscribing Reading List App to the Pay-as-you-go plan](../../assets/img/guides/monetization/mcp-monetization/subscribe-paid-plan.png){.cInlineImage-full}

!!! note
    Payments are processed by Stripe. WSO2 API Platform does not store your payment details. Billing and receipts are managed through Stripe.

---

## Step 8: Generate Keys and Invoke the MCP Server

Generate OAuth2 credentials for your application and make your first authenticated tool invocation.

1. In the Developer Portal, click **Applications** and open **Reading List App**.
2. Click **Manage Keys**.
3. On the **Production** tab, click **Generate Key**.
4. Copy the **Consumer Key** and **Consumer Secret**.
5. Click **Generate** to generate an access token and copy it.

**Expected result:** You have an access token ready to use when connecting your MCP client.

![Manage Keys page showing Consumer Key, Consumer Secret, and generated access token for Reading List App](../../assets/img/guides/monetization/mcp-monetization/generate-keys.png){.cInlineImage-full}

Now connect to the MCP Server and invoke a tool. The quickest way is the built-in MCP Playground in the Developer Portal:

1. Go to the MCP Server listing page and open the Reading List MCP Server.
2. Click **Documentation** to open the MCP Playground.
3. Paste your access token in the format `Bearer <YOUR-TOKEN>`.
4. Click **Connect** to establish a connection with the deployed MCP Server.
5. Click **List Tools**, select a tool such as `listBooks`, and click **Run Tool**.

**Expected result:** The tool returns a successful JSON result. Each successful tool invocation increments your usage meter in Stripe.

![Developer Portal MCP Playground showing Connected status, tools listed including listBooks, and a successful JSON tool result](../../assets/img/guides/monetization/mcp-monetization/invoke-mcp.png){.cInlineImage-full}

!!! tip
    To connect from an external client such as the VS Code Copilot Agent, copy the **MCP Server Configuration** from the MCP Server overview, add it to your client's `mcp.json`, and replace the token placeholder with the access token you generated. See [Connect the MCP Server with MCP Clients](../../cloud/mcp-servers/design-mcp-servers.md#connect-the-mcp-server-with-mcp-clients-ai-agents) for details.

!!! warning
    Bearer tokens expire after 3600 seconds by default. To extend the lifetime, click **Modify** on the Manage Keys page and increase the **Application Access Token Expiry Time** before generating.

---

## Step 9: View Billing and Usage

After invoking tools, check your usage, upcoming charges, and invoices from the Developer Portal.

1. In the Developer Portal, click your profile icon in the top right corner.
2. Click **Billing**.
3. On the **Usage Summary** tab, review your Total Billed Invocations, Active Subscriptions, and Estimated Cost for the current period.
4. Click the **Invoices** tab to view and download past invoices.
5. Click the **Billed Subscriptions** tab to see subscription details and click **Manage** to update or cancel.

**Expected result:** Your Reading List tool invocations appear in the usage breakdown with the Pay-as-you-go plan, and the estimated cost reflects your invocation count × $0.02.

![Billing page showing Usage Summary with invocation count and estimated cost for the Pay-as-you-go plan](../../assets/img/guides/monetization/mcp-monetization/view-billing-and-usage.png){.cInlineImage-full}

!!! note
    Allow a few minutes for usage to appear in the Billing page after the first invocation.

---

## Verify

1. Confirm authenticated invocations are billed. Run a tool from the MCP Playground and then check the Usage Summary — the invocation count should increment.

    **Expected result:** The invocation count in **Billing > Usage Summary** increases by the number of tool calls made.

2. Confirm unauthenticated connections are rejected. Attempt to connect to the MCP Server without a valid bearer token.

    **Expected result:** The connection fails with HTTP 401 Unauthorized.

3. Confirm subscription enforcement. In the Developer Portal, cancel the Pay-as-you-go subscription under **Billing > Billed Subscriptions > Manage > Cancel**. Then attempt to invoke a tool with the same token.

    **Expected result:** HTTP 403 Forbidden — the gateway revokes access when the subscription lapses.

---

## Troubleshooting

| Symptom | Resolution |
|---|---|
| Stripe Credentials save fails | Confirm your Secret Key and Publishable Key are from the same Stripe account and that the secret key has the required permissions. |
| Plans don't appear in Developer Portal subscription dialog | Confirm the plan toggles are enabled in **Manage > Monetize** and the MCP Server is in the **Published** lifecycle state. |
| Stripe checkout doesn't open | Confirm your Stripe account is active and not in restricted mode. Check the Stripe Dashboard for any pending account verification. |
| MCP client fails to connect with HTTP 401 | Confirm your access token is not expired and is sent in the `Bearer <token>` format. Generate a new token in **Manage Keys** and reconnect. |
| HTTP 403 after subscribing | Confirm the subscription is active in **Billing > Billed Subscriptions**. If payment failed, the subscription may be inactive. |
| Usage not appearing in Billing page | Allow a few minutes after invoking tools. Usage reporting to Stripe is near-real-time but not instantaneous. |
| Cannot cancel subscription | Subscription cancellation is available in the Developer Portal under **Billing > Billed Subscriptions > Manage**. Only the consumer who created the subscription can cancel it. |

---

## What You Learned

- Connected a Stripe account to WSO2 API Platform so the platform manages all billing infrastructure without custom code
- Created Free and Unit-priced subscription plans to offer a free tier alongside a pay-as-you-go production tier
- Assigned plans to the Reading List MCP Server and published it to the Developer Portal for consumer self-service
- Subscribed to a paid plan via a Stripe-powered checkout in the Developer Portal, with access granted immediately after payment
- Invoked a monetized MCP Server using OAuth2 credentials, with each tool call automatically metered and reported to Stripe
- Viewed real-time usage, invoices, and subscription management from the Developer Portal Billing page

---

## Next Steps

- **[Monetize a REST API](api-monetization.md)** — apply the same subscription and billing model to REST API requests
- **[Customize the Developer Portal as an MCP Hub](../../cloud/mcp-servers/devportal-mcp-hub.md)** — deliver a tailored, MCP-only discovery experience to your consumers
- **Add rate limiting tiers** — pair your subscription plans with burst control and per-plan quotas to protect your backend from overuse
- **Monitor MCP usage with analytics** — track invocation volume, error rates, and latency per plan in the API Platform Console analytics dashboard
