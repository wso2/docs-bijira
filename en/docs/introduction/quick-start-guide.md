# Quick Start Guide

Bijira simplifies securely exposing existing services as managed APIs. It also allows you to manage all aspects of an API's lifecycle, security, throttling, and governance, so you can focus on service development.

In this tutorial, you will use Bijira to expose a service as an API proxy and publish it to the Bijira Developer Portal for application developers to consume.

## Prerequisites

1. If you're signing in to the Bijira Console for the first time, create an organization:
    1. Go to [https://console.bijira.dev/](https://console.bijira.dev/) and sign in using your Google, GitHub, or Microsoft account.
    2. Enter a unique organization name.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the organization home page.

## Step 1: Create a Project

1. Go to [https://console.bijira.dev/](https://console.bijira.dev/) and sign in. This opens the organization home page.
2. On the organization home page, click **+ Create Project**.
3. Enter the following details:

    !!! info
        The **Name** field must be unique and cannot be changed after creation.

    | **Field**                | **Value**                          |
    |--------------------------|------------------------------------|
    | **Project Display Name** | Book List Project                  |
    | **Name**                 | book-list-project                  |
    | **Project Description**  | My sample project                  |

4. Click **Create**. This creates the project and takes you to the project home page.

## Step 2: Create an API Proxy

1. On the project home page, click **Import API Contract** under **Create an API Proxy for My API (Ingress)**.
2. Click **Try with Sample URL** and click **Next**.
3. **Create API Proxy from Contract** page will be opened. Click **Create** to complete the API proxy creation process. 
    ![Create API Proxy from Contract](../../assets/img/introduction/create-api-proxy-from-contract.png)

## Step 3: Deploy the API Proxy

1. In the left navigation menu, click **Deploy**.
2. In the **Build Area** card, click **Configure & Deploy**. This opens the **Configure & Deploy** pane.
3. Select **External** to make the API publicly accessible, and then click **Deploy**.

    ![CConfigure and Deploy](../../assets/img/introduction/configure-and-deploy.png)
    Once the deployment is complete, the **Development** card indicates the **Deployment Status** as **Active**.

Now you are ready to test the API proxy.

## Step 4: Test the API Proxy

You can test the API proxy in the development environment before promoting it to production. Bijira provides the following options to test your API proxy:

- OpenAPI Console
- cURL
- API Chat

In this guide, you will use the OpenAPI Console.

1. In the left navigation menu, click **Test** and then click **OpenAPI Console**.

    !!! tip
        Since the API proxy is secured when deployed, you will need a key to invoke it. Bijira automatically generates a key when you navigate to the **OpenAPI Console** pane.

2. In the **OpenAPI Console** pane, select **Development** from the environment drop-down list.
3. Expand the `GET /books` method and click **Try it Out** to test it.
4. Click **Execute**. You will see a response similar to the following:

    ![API proxy response](../../assets/img/introduction/test-response.png)

    This indicates that your API proxy is working as expected.

## Step 5: Promote the API Proxy to Production

Once you verify that the API proxy is working as expected in the development environment, you can promote it to production.

1. In the left navigation menu, click **Deploy**.
2. In the **Development** card, click **Promote**.
3. In the **Configure & Deploy** pane, select the option **Use Development endpoint configuration** and click **Next**.

    !!! tip
        If you want to specify a different endpoint for your production environment, you can make the change in the **Configure & Deploy** pane.

    The **Production** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed to production.

    If you want to verify that the API proxy is working as expected in production, you can test the API in the production environment.

Now that your API is deployed in both development and production environments and can be invoked, the next step is to publish it so that consumers can discover and subscribe to it.

## Step 6: Publish the API Proxy

1. In the left navigation menu, click **Develop** and then click **Lifecycle**. This opens the **Lifecycle** page, where you can see the different lifecycle stages of the API. The current lifecycle stage is **Created**.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API with the specified display name. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.

You can observe that the API lifecycle stage has changed to **Published**. Now the API is available for consumption. API consumers can consume the API via the Bijira Developer Portal.

## Step 7: Invoke the API

<!-- TODO: Need to improve the documentation after devportal is refined with snaps and steps -->
To generate credentials for the published API and invoke it via the Developer Portal, follow these steps.

1. In the **Lifecycle Management** pane, click **Go to DevPortal**. This takes you to the Petstore API published to the Bijira Developer Portal.
    ![Go to DevPortal](../../assets/img/introduction/go-to-developer-portal.png)
2. Subscribe to the API and Generate credentials.
    1. In the Developer Portal left navigation menu, click **Applications**.
    2. Click **Create Application**.
    3. Add a sample application name and click **Save**.
    4. Click **+ Add API** under **APIs** section.
    5. Choose API Name and Subscription Plan and click **Save**. Now your application is subscribed to the published API with your selected subscription plan.
    6. Open the created application and click **OAuth2 Keys** under **Tokens**.
    7. Click **Generate Keys**. If you want to configure Advanced Configurations expand the **Advanced Configurations** section and configure the values. Bijira generates new tokens and populates the **Consumer Key** and **Consumer Secret** fields.
    8. Click **Generate Token**. This will generate an access token that you can use to invoke APIs. Copy the generated access token.
3. Invoke the API:
    1. Go to the APIs listing page using the left navigation menu.
    2. Click **Overview** to open your API.
    3. Click **Documentation** to open the swagger definition of the API.
    4. Select the API resource that you want to invoke.
    5. Paste your copied access token with following format: `Bearer <ACCESS_TOKEN>`
    6. Click **Send API Request**.

Now you have successfully created, deployed, tested, and published an API proxy using Bijira.
