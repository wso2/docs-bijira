# Configure Custom External Identity Provider (IdP)

If your organization uses Asgardeo or Microsoft Azure Active Directory (Azure AD) for identity and access management, follow the platform-specific guides below to add them as an External IdP in Bijira.

- [Configure Asgardeo as an External IdP](configure-asgardeo-as-an-external-idp.md)
- [Configure Azure as an External IdP](configure-azure-ad-as-an-external-idp.md)

If you use any other Identity Provider, you can still integrate it with Bijira provided it supports standard OIDC/OAuth2 endpoints. Integrating a custom IdP allows you to enforce API access using scopes and restrict access to specific user groups. This guide walks you through the steps to set up the external IdP.

## Prerequisites

Before you try out this guide, be sure you have the following:

- The IdP’s `Well‑Known URL` (to import configuration automatically).
- Administrator access to your Bijira organization and to the IdP.

## Step 1: Add custom external IdP in Bijira

Follow the steps below to add a custom IdP in Bijira:

1. Sign in to the Bijira Console at [https://console.bijira.dev/](https://console.bijira.dev).
2. In the left navigation menu, click **Settings**.
3. In the header, click the **Organization** list. This will open the organization level settings page.
4. On the **Application Security** tab, click **Identity Providers** and then click **+ Identity Provider**.
5. Select  **Custom** as the Identity Provider.
6. Provide a name and a description for the IdP.
7. Obtain the `Well-Known URL` of your IdP and Provide it under Well-Known URL.
8. Leave the **Apply to all environments** checkbox selected. However, if you want to restrict the use of the external IdP to a certain environment, you can select them from the **Environments** list.
9. Click **Next**.
10. The next page will list all the relevant configurations extracted from the `Well-Known URL`. Review the configurations and click **Add**.

Now you have configured your custom IdP as an external IdP in Bijira.

## Step 2: Add the external IdP in Bijira Developer Portal¶

Once the IdP is configured as an external IdP in Bijira, it is necessary to configure it in the Bijira Developer Portal as well. For that, follow the steps below.

1. In the left navigation menu of the Bijira Console, click **Admin** and then click **Settings**.
2. Click the **Developer Portal** tab, then click the **Identity Providers** tab. This page will list all the Identity providers available in Bijira.
3. Select the Identity Provider you configured at [Step 1](#step-1-add-custom-external-idp-in-bijira).
4. Click **Save**.

Now you have configured your IdP as an external IdP in Bijira Developer Portal as well.

## What Next?

To secure API access with the above-configured Identity Provider follow the steps mentioned [here](../../develop-api-proxy/authentication-and-authorization/secure-api-access-with-external-idp.md).