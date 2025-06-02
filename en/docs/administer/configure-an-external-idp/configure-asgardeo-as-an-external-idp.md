# Configure Asgardeo as an External Identity Provider (IdP)

Asgardeo is an identity-as-a-service (IDaaS) solution designed to create seamless login experiences for your applications. Asgardeo seamlessly integrates with Bijira, providing powerful API access control through the use of API scopes. This enables restricting API access to designated user groups. By configuring Asgardeo as an external IdP in Bijira, you can leverage your Asgardeo user stores to manage API access control effectively. This guide walks you through the steps to set up Asgardeo as your external IdP.

## Prerequisites

Before you proceed, be sure to complete the following:

- Create an Asgardeo application. You can follow the Asgardeo guide to [register a standard-based application](https://wso2.com/asgardeo/docs/guides/applications/register-standard-based-app/#register-an-application).

- Find the well-known URL:
  Go to the **info** tab of the Asgardeo application to view the endpoints and copy the **Discovery** endpoint.

- Find the Client ID:
  Go to the **Protocol** tab of the Asgardeo application and copy the **Client ID**.

## Step 1: Add Asgardeo as an external IdP in Bijira

Follow the steps below to add Asgardeo as an external IdP in Bijira:

1. Sign in to the Bijira Console at [https://console.bijira.dev/](https://console.bijira.dev).
2. In the left navigation menu, click **Admin** and then click **Settings**.
3. In the header, click the **Organization** list. This opens the organization-level settings page. 
4. Click the **Application Security** tab and then click the **Identity Providers** tab.
5. To add an identity provider, click **+ Identity Provider**.
6. Click **Asgardeo**. 
7. In the Asgardeo dialog that opens, specify a name and a description for the IdP. 
8. In the **Well-Known URL** field, paste the well-known URL that you copied from your Asgardeo instance by following the prerequisites. 
9. Leave the **Apply to all environments** checkbox selected. This allows you to use the tokens generated via this IdP to invoke APIs across all environments.

    <!-- !!! note
         If you want to restrict the use of tokens generated via this IdP to invoke APIs in specific environments, clear the **Apply to all environments** checkbox and select the necessary environments from the **Environments** list. -->

10. Click **Next**. This displays the server endpoints that are useful to implement and configure authentication for your application.
11. Click **Add**. 

Now you have configured Asgardeo as an external IdP in Bijira.

## Step 2: Add Asgardeo as an external IdP in Bijira Developer Portal

Once the Asgardeo is configured as an external IdP in Bijira, it is necessary to configure it in the Bijira Developer Portal as well. For that, follow the steps below.

1. In the left navigation menu of the Bijira Console, click **Admin** and then click **Settings**.
2. Click the **Developer Portal** tab, then click the **Identity Providers** tab. This page will list all the Identity providers available in Bijira.
3. Select the Identity Provider you configured at [Step 1](#step-1-add-asgardeo-as-an-external-idp-in-bijira).
4. Click **Save**.

Now you have configured Asgardeo as an external IdP in Bijira Developer Portal as well.