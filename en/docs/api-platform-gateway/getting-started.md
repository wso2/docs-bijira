# Getting Started with Self-Hosted Gateway

This guide walks you through setting up a Bijira Self-Hosted Gateway in your environment. Follow these quick steps to get your gateway running and connected to Bijira's control plane.

!!! note
    This feature is currently available in the **US region** only.

## Overview

The Self-Hosted Gateway enables you to run the Bijira API Gateway in your own infrastructure while maintaining centralized management through Bijira's control plane. This guide covers the fastest way to get started.


## Prerequisites

Before you begin, ensure you have:

- **cURL** installed
- **unzip** installed
- **Docker** installed and running (for Quick Start)
- **Docker Compose** installed

## Create a Self-Hosted Gateway in Bijira Console

1. Sign in to [Bijira Console](https://console.bijira.dev).
2. Go to **Organization Level** in Bijira.
3. From the left navigation, select **Admin** → **Gateways**.

    ![Gateway List Empty](../../assets/img/api-platform-gateway/gateway/gateway-list-empty.png)

4. Select the **API Platform** tab.
5. Click **+ Add Self-Hosted Gateway**.
6. Provide the following details:

    - **Name**: A unique name for your gateway
    - **Description**: Optional description
    - **URL**: The URL where your gateway will be accessible (e.g., `https://localhost:8443`)
    - **Associated Environment**: Select the environment for this gateway

    ![Gateway Add](../../assets/img/api-platform-gateway/gateway/gateway-add.png)

7. Click **Add** and you will be navigated to the Gateway View Page.

## Setup Gateway

1. Next, download, set up, and start the gateway on your machine by following the steps in the **Quick Start** section or the detailed instructions below (Steps 1–4).

    !!! note
        Be sure to copy the commands from the Quick Start section, since the keys are auto-generated for you.

    ![Gateway View1](../../assets/img/api-platform-gateway/gateway/gateway-view1.png)
    ![Gateway View2](../../assets/img/api-platform-gateway/gateway/gateway-view2.png)


    ### Step 1: Download the Gateway

    Run this command in your terminal to download the gateway:

    ```bash
    curl -sLO https://github.com/wso2/api-platform/releases/download/gateway/v0.9.0/gateway-v0.9.0.zip && \
    unzip gateway-v0.9.0.zip
    ```

    ### Step 2: Configure the Gateway

    Run this command to create the gateway configuration with your environment variables:

    ```bash
    cat > gateway-v0.9.0/configs/keys.env << 'ENVFILE'
    MOESIF_KEY=<your-moesif-key>
    GATEWAY_CONTROLPLANE_HOST=connect.bijira.dev
    GATEWAY_REGISTRATION_TOKEN=<your-gateway-token>
    ENVFILE
    ```

    Once you copy the above command from the screen, the `<your-moesif-key>` and `<your-gateway-token>` placeholders will be populated and the `gateway-v0.9.0/configs/keys.env` file will be created with these environment variables.

    ### Step 3: Start the Gateway

    Navigate to the gateway directory and start it using Docker Compose:

    ```bash
    cd gateway-v0.9.0
    docker compose --env-file configs/keys.env up
    ```

    ### Step 4: Verify the Gateway

    Check that the gateway is running and connected:

    ```bash
    # Check container status
    docker compose ps

    # Check gateway health
    curl http://localhost:9002/health
    ```

    The gateway should show as **Active** in the Bijira Console under **Gateways**.

## Add API and Invoke

### Step 1: Create an API Proxy.

In this guide, you will specify a URL to an OpenAPI definition of a sample API to create an API proxy.

1. Navigate to **projects**.


    ![Navigate Project](../../assets/img/api-platform-gateway/gateway/navigate-project.png)


2. To create a new project for your APIs, click **+ Create Project** and follow the setup steps. Otherwise, select **Default** to continue with the default project.

    ![Select Project](../../assets/img/api-platform-gateway/gateway/select-project.png)

3. Select **Import API Contract**.

    ![Select Import API Contract](../../assets/img/api-platform-gateway/gateway/select-import-api-flow.png)

4. Select **URL** option and provide the following URL to import the API contract:

    ```text
    https://raw.githubusercontent.com/wso2/bijira-samples/refs/heads/main/reading-list-api/openapi.yaml   
    ```

5. Click **Next** and edit pre-defined values as needed. You can keep the default values for this sample.

    ![Import API Contract](../../assets/img/api-platform-gateway/gateway/create-api-contract-url.png)

6. Select the **Gateway Type** as the **Self-Hosted Gateway**

    ![API Add](../../assets/img/api-platform-gateway/gateway/add-api.png)

6. Click **Create** to create the API Proxy. Wait for the setup to complete and you will be navigated to the API Overview Page.

    ![API Overview](../../assets/img/api-platform-gateway/gateway/api-overview.png)

### Step 2: Deploy the API Proxy (Optional)

!!! note
    This step is **optional** at this stage, as the API is deployed to the gateway by default. However, if you make any changes to the API, you must redeploy it.
    
    To redeploy, navigate to the **Deploy page** of the API Proxy and click **Deploy**.

1. Navigate to the **Deploy** page of the API Proxy. 

    ![API Deploy](../../assets/img/api-platform-gateway/gateway/api-deploy.png)

2. Click **Deploy**.

## Test the API Proxy

1. Navigate to the **Test --> cURL** page of the API Proxy.

    ![API Test](../../assets/img/api-platform-gateway/gateway/api-try-out.png)

2. Use the **cURL** for relevant resource to test the API Proxy.

## Next Steps

Your Self-Hosted Gateway is now running! Here's what to do next:

- **Configure Policies**: Apply policies through the [Adding and Managing Policies](manage-policies.md) guide
- **Monitor**: View gateway health and metrics using [Analytics](analytics.md)

## Alternative Deployment Options

For production environments or specific infrastructure requirements, see the detailed configuration guide:

- [Setting Up](setting-up.md): Configure on Virtual Machine, Docker, or Kubernetes with tabs for each infrastructure option

## Troubleshooting

If the gateway doesn't connect:

1. **Verify the token**: Ensure the gateway token is correctly set in `keys.env`
2. **Check network connectivity**: The gateway needs outbound HTTPS access to `*.bijira.dev`
3. **View logs**: Run `docker compose logs -f` to see gateway logs
4. **Check firewall**: Ensure port 8443 is accessible

For more troubleshooting help, see [Troubleshooting](troubleshooting.md).
