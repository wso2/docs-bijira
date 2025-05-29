# Secure API Access with Bijira STS

API security refers to the measures and practices used to protect Application Programming Interfaces (APIs) from potential threats and vulnerabilities. APIs are essential for enabling communication and data exchange between different software applications and services, making them a critical component in modern software development. However, their openness and accessibility can also make them targets for various security risks. Authentication and authorization are key aspects of API security. Authentication is ensuring that only authorized users or applications can access the API. This can involve using API keys, tokens, or more advanced authentication methods like OAuth 2.0. Authorization is controlling what authenticated users or applications are allowed to do within the API. Authorization mechanisms restrict access to specific resources and actions based on user roles or permissions. 

Bijira's built-in Secure Token Service can seamlessly integrate with Bijira APIs to provide authentication and authorization. This guide will walk you through setting up Bijira STS to authenticate API invocations.

This guide walks you through the following steps:

<!-- - Assign scopes to an API in Bijira.  -->
- Create an API in Asgardeo.
- Create an application in Asgardeo and consume the Asgardeo API.
- Create an application in Bijira and enable external IdP authentication.
- Invoke the API with scopes.

## Prerequisites

To follow this guide, you need to satisfy the following prerequisites:

- If you don't already have an API Proxy in Bijira, [create API Proxy](../../../create-api-proxy/overview/).
- Deploy and publish your API. 

!!! note
    It is important to note that Bijira STS token can be only be used for client authentication. If you have a requirement for end user authentication, it is necessary to use external IdP such as Asgardeo. For more information about secure API access with Asgardeo, refer [Secure API Access with Asgardeo](../../authentication-and-authorization/secure-api-access-with-asgardeo/)

<!-- ## Step 1: Assign scopes to an API in Bijira

You can provide fine-grained access control to your API resources with scopes. Follow the steps below to assign a scope to the resources in the API:

!!! note
    Defining permissions for Services other than Ballerina and API Proxy is supported via the OpenAPI Definition.

    - Define your permissions under the `components.securitySchemes` and `security` sections in your OpenAPI document.
    - Assign the appropriate permissions to each operation using the `security` property at the resource level.
    - Commit the OpenAPI document to the repo.

1. In the **Component Listing** pane, click on the component you want to attach scopes to.
2. In the left navigation menu, click **Deploy** and then **Configure & Deploy** in the **Set Up** area. (For Proxy apis, click **Configure & Deploy** in the **Build Area** and skip the Step 3 below)
3. Click **Next** to go to the **Endpoint Details** step. Expand the required endpoint if not already expanded. 
4. In the **Operation Level** security section, click on **Manage Permissions** button. 
5. In the **Manage Permissions** pane, enter the permission value and click **Add New**.
6. Click the copy icon in front of the added scope to copy the fully qualified name of the scope. Save this value for future reference. 
7. To attach a scope to a resource, click the **Select Permissions** list under the respective resource, and select the scopes you wish to attach.
8. Click **Deploy**.
9. In the left navigation, click **Manage** and then **Lifecycle**.
10. Click **Publish** and continue to publish your API to the Choreo Developer Portal.  -->


<!-- ## Step 1: Create an API and an application in Asgardeo

 Follow the [Asgardeo API Authorization guide](https://wso2.com/asgardeo/docs/guides/api-authorization/) to create an application and an API in Asgardeo and to enable API authorization.

!!! note
     - Use the fully qualified name of the scope when adding scopes. 
     - Do the following under the protocol tab:
        - Select `JWT` as the **Access Token**.
        - Select the appropriate grant types.
        - Copy the client ID and client secret of the application for future reference. -->

## Step 1: Create an application in Bijira and enable external IdP authentication

Follow the steps below to consume the Bijira API using Bijira STS.

1. Sign in to your organization in the Bijira Developer Portal at [https://devportal.bijira.dev](https://devportal.bijira.dev).
2. Click **Applications**. and then click **+Create**.
3. Enter a name for the application. 
4. Click **Create**.
5. Click on the newly created application.
6. At the top of the application page, under **OAuth2** click **Generate**. This will generatae consumer keys for the application.
7. Once successfully generated, you will be shown a dialog which contains the Identity provider connection data.
8. Click on the **Generate Token** button to generate an access token. Please make sure to copy the access token to use in step 2.
9. Click **Subscribe to more APIs** button to explore the APIs and subscribe them through the application.

## Step 2: Invoke the Bijira API

1. Once you receive the access token, you can [test invoking the resource using the OpenAPI console](../../../test-api-proxy/openapi-console/) in Bijira.
