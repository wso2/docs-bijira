# Secure API Access with Asgardeo

API security refers to the measures and practices used to protect Application Programming Interfaces (APIs) from potential threats and vulnerabilities. APIs are essential for enabling communication and data exchange between different software applications and services, making them a critical component in modern software development. However, their openness and accessibility can also make them targets for various security risks. Authentication and authorization are key aspects of API security. Authentication is ensuring that only authorized users or applications can access the API. This can involve using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization is controlling what authenticated users or applications are allowed to do within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions. 

Organizations using Asgardeo for identity and access management (IAM) can seamlessly integrate it with Bijira as an external Identity Provider (IdP). This guide will walk you through setting up Bijira to authenticate API invocations through Asgardeo which is configured as an external IdP.

This guide walks you through the following steps:

<!-- - Assign scopes to an API in Bijira.  -->
- Create an API in Asgardeo.
- Create an application in Asgardeo and consume the Asgardeo API.
- Create an application in Bijira and enable external IdP authentication.
- Invoke the API.

## Prerequisites

To follow this guide, you need to satisfy the following prerequisites:

- [Configured Asgardeo as an external IdP](../../administer/configure-an-external-idp/configure-asgardeo-as-an-external-idp.md) 
- If you don't already have an API Proxy in Bijira, [create API Proxy](../../../create-api-proxy/overview/).
- Deploy and publish your API. 

<!-- ## Step 1: Assign scopes to an API in Bijira

You can provide fine-grained access control to your API resources with scopes. Follow the steps below to assign a scope to the resources in the API:

1. In the **API Proxy Listing** pane, click on the API Proxy you want to attach scopes to.
2. In the left navigation menu, click **Deploy** and then **Configure & Deploy** in the **Build Area**.
3. Click **Next** to go to the **Endpoint Details** step. Expand the required endpoint if not already expanded. 
4. In the **Operation Level** security section, click on **Manage Permissions** button. 
5. In the **Manage Permissions** pane, enter the permission value and click **Add New**.
6. Click the copy icon in front of the added scope to copy the fully qualified name of the scope. Save this value for future reference. 
7. To attach a scope to a resource, click the **Select Permissions** list under the respective resource, and select the scopes you wish to attach.
8. Click **Deploy**.
9. In the left navigation, click **Manage** and then **Lifecycle**.
10. Click **Publish** and continue to publish your API to the Choreo Developer Portal.  -->


## Step 1: Create an API and an application in Asgardeo

 Follow the [Asgardeo API Authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/) to create an application and an API in Asgardeo and to enable API authorization.

!!! note
     <!-- - Use the fully qualified name of the scope when adding scopes.  -->
    - Do the following under the protocol tab:
        - Select `JWT` as the **Access Token**.
        - Select the appropriate grant types.
        - Copy the client ID and client secret of the application for future reference.

## Step 2: Create an application in Bijira and enable external IdP authentication

Follow the steps below to consume the Bijira API and use an external IdP for authentication:

1. Sign in to your organization in the Bijira Developer Portal at [https://devportal.bijira.dev](https://devportal.bijira.dev).
2. Click **Applications**. and then click **+Create**.
3. Enter a name for the application. 
4. Click **Create**.
5. Click on the newly created application.
6. At the top of the application page, under **OAuth2** click **Add Consumer Key**. 
7. Enter the **Client ID** you copied in [step 2](#step-2-create-an-api-and-an-application-in-asgardeo).
8. Click **+Add**.

    !!! note 
        - You can only use the Client ID in one application.
        - This will be visible only to organizations where you have configured external IdPs. 

9. Once successfully added, you will be shown a dialog which contains the Identity provider connection data.
10. You can click on the **Instructions** to view instructions to generate an access token.
11. Click **Subscribe to more APIs** button to explore the APIs and subscribe them through the application.

## Step 3: Invoke the Bijira API

1. On the Bijira Developer Portal, go to your application. 
2. On the top of the page, under **OAuth2**, click **View** to see the **Token Endpoint** URL.
3. Obtain an access token by invoking the token endpoint as follows:

    === "Format"

        ``` sh
        curl -X POST '<TOKEN_ENDPOINT>?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
         --header 'Content-Type: application/x-www-form-urlencoded' \
         --header 'Authorization: Basic <BASE64-ENCODED ASGARDEO_APP_CLIENT_ID:ASGARDEO_APP_CLIENT_SECRET>'
        ```

    === "Example"

        ``` sh
        curl -X POST 'https://dev.api.asgardeo.io/t/orgHandle/oauth2/token?grant_type=password&scope=<REQUIRED_SCOPES>&username=<USER_NAME>&password=<USER_PASSWORD>' \
        --header 'Content-Type: application/x-www-form-urlencoded' \
        --header 'Authorization: Basic <BASE64-ENCODED CLIENT_ID:CLIENT_SECRET>'
        ```

5. Once you receive the access token, you can [test invoking the resource using the OpenAPI console](../../../test-api-proxy/openapi-console/) in Bijira.
