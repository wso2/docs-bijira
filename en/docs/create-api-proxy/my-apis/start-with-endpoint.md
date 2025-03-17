# Create API proxy from Start with Endpoint

An API proxy acts as an intermediary between an existing API and Bijira, intercepting all requests made to the API.It also functions as a managed API, allowing you to apply essential API management features such as security policies and rate limiting.

## Prerequisites

- A valid Bijira account with available resource quota.

## Create an API Proxy

In this guide, you will create an API proxy from the Scratch.

1. Go to [https://console.bijira.dev/](https://console.bijira.dev/) and sign in. This opens the project home page.
2. If you already have one or more components in your project, click + Create. Otherwise, proceed to the next step.
3. Select **Start with Endpoint**.
4. Provide the following URL as the **Endpoint URL**.

   ```
   https://raw.githubusercontent.com/wso2/bijira-samples/refs/heads/main/reading-list-api/open-api.yaml
   ```

5. Click **Next**.
6. Specify the following values as API proxy details:

    | **Field**       | **Value**                                  |
    |-----------------|--------------------------------------------|
    | **Name**     | `Reading List API`                            |
    | **Identifier**     | `reading-list-api-uy`                   |
    | **Version**     | `1.0`                                      |
    | **Base Path**     | `/default/reading-list-api-uy/v1.0`      |
    | **Description**      | `This is a sample proxy that manages a list of reading items.` |
    | **Access Mode**      | `External` |

7. Click **Create** to create the API Proxy. Wait for the setup to complete.

## Configure and Deploy the API Proxy

1. Navigate to the **Deploy** page of the API Proxy.
2. Select **Configure and Deploy** option from the **Deploy** dropdown and click **Configure and Deploy** button.
3. Select **External** as API Access Mode.
4. Click **Deploy**.

## Test the API Proxy

1. Navigate to the **Test --> Console** page of the API Proxy.
2. Use the OpenAPI Console to test the API Proxy.

## Publish the API proxy

1. In the left navigation menu, click **Lifecycle** under **Develop**. This takes you to the **Lifecycle** page.
2. Click **Publish**.
3. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API. If you want to change the display name, make the necessary changes and then click **Confirm**. This changes the API lifecycle state to **Published**.
