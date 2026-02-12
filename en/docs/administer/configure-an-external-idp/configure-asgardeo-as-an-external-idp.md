# Configure Asgardeo as an External Key Manager

Asgardeo is an identity-as-a-service (IDaaS) solution designed to create seamless login experiences for your applications. Asgardeo seamlessly integrates with Bijira, providing powerful API access control through the use of API scopes. This enables restricting API access to designated user groups. By configuring Asgardeo as an external key manager in Bijira, you can leverage your Asgardeo user stores to manage API access control effectively. This guide walks you through the steps to set up Asgardeo as your external key manager.

## Prerequisites

Before you proceed, be sure to complete the following:

- Create an Asgardeo application. You can follow the Asgardeo guide to [register a standard-based application](https://wso2.com/asgardeo/docs/guides/applications/register-standard-based-app/#register-an-application).

- Find the well-known URL:
  Go to the **info** tab of the Asgardeo application to view the endpoints and copy the **Discovery** endpoint.

- Find the Client ID:
  Go to the **Protocol** tab of the Asgardeo application and copy the **Client ID**.

## Step 1: Add Asgardeo as an external key manager in Bijira

Follow the steps below to add Asgardeo as an external key manager in Bijira:

1. Sign in to the Bijira Console at [https://console.bijira.dev/](https://console.bijira.dev).
2. In the left navigation menu, click **Admin** and then click **Settings**.
3. In the header, click the **Organization** list. This opens the organization-level settings page.
4. Click the **Key Managers** tab.
5. To add a key manager, click **+ Key Manager**.

    ![Key Managers tab](../../assets/img/administer/settings/external-km/add_external_km.png)

6. Click **Asgardeo**.

    ![Select Asgardeo](../../assets/img/administer/settings/external-km/add_external_km_asgardeo_select.png)

7. In the Asgardeo dialog that opens, specify a name and a description for the key manager.
8. In the **Well-Known URL** field, paste the well-known URL that you copied from your Asgardeo instance by following the prerequisites.
9. Leave the **Apply to all environments** checkbox selected. This allows you to use the tokens generated via this key manager to invoke APIs across all environments.

    ![Asgardeo configuration page 1](../../assets/img/administer/settings/external-km/add_external_km_asgardeo_page_1.png)

<!-- !!! note
     If you want to restrict the use of tokens generated via this key manager to invoke APIs in specific environments, clear the **Apply to all environments** checkbox and select the necessary environments from the **Environments** list. -->

10. Click **Next**. This displays the server endpoints that are useful to implement and configure authentication for your application.

    ![Asgardeo configuration page 2](../../assets/img/administer/settings/external-km/add_external_km_asgardeo_page_2.png)

11. Click **Add**.

Now you have configured Asgardeo as an external key manager in Bijira.

![Key Managers tab](../../assets/img/administer/settings/external-km/add_external_km_asgardeo_list.png)

## Step 2: Add Asgardeo as an external key manager in Bijira Developer Portal

Once the Asgardeo is configured as an external key manager in Bijira, it is necessary to configure it in the Bijira Developer Portal as well. For that, follow the steps below.


1. In the left navigation menu of the Bijira Console, click **Admin** and then click **Settings**.
2. Click the **Developer Portal** tab, then click the **Key Managers** tab. This page will list all the key managers available in Bijira.
3. Select the key manager you configured at [Step 1](#step-1-add-asgardeo-as-an-external-key-manager-in-bijira).
4. Click **Save**.

Now you have configured Asgardeo as an external key manager in Bijira Developer Portal as well.

![Key Managers tab](../../assets/img/administer/settings/external-km/add_external_km_asgardeo_devportal.png)

## What Next?

To secure API access with the above-configured Asgardeo as key manager, follow the steps mentioned [here](../../../develop-api-proxy/authentication-and-authorization/secure-api-access-with-asgardeo/).
