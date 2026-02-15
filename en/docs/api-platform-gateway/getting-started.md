# Getting Started with Self-Hosted Gateway

This guide walks you through setting up a Bijira Self-Hosted Gateway in your environment. Follow these quick steps to get your gateway running and connected to Bijira's control plane.

## Overview

The Self-Hosted Gateway enables you to run the Bijira API Gateway in your own infrastructure while maintaining centralized management through Bijira's control plane. This guide covers the fastest way to get started.

## Prerequisites

Before you begin, ensure you have:

- **cURL** installed
- **unzip** installed
- **Docker** installed and running (for Quick Start)

## Step 1: Create a Self-Hosted Gateway in Bijira Console

1. Sign in to [Bijira Console](https://console.bijira.dev).
2. Navigate to **Gateways** from the left navigation.
3. Select the **API Platform** tab.
4. Click **+ Add Self-Hosted Gateway**.
5. Provide the following details:
   - **Name**: A unique name for your gateway
   - **Description**: Optional description
   - **URL**: The URL where your gateway will be accessible (e.g., `https://localhost:8443`)
   - **Associated Environment**: Select the environment for this gateway
6. Click **Create**.

## Step 2: Copy the Gateway Registration Token

After creating the gateway, you'll see the **Gateway Registration Token**. 

!!! warning "Important"
    This token is shown only once. Ensure it is securely saved before leaving the page.

Copy the token and store it securely. You'll need it to configure the gateway.

## Step 3: Download the Gateway

Run this command in your terminal to download the gateway:

```bash
curl -sLO https://github.com/wso2/api-platform/releases/download/gateway/v0.8.1/gateway-v0.8.1.zip && \
unzip gateway-v0.8.1.zip
```

## Step 4: Configure the Gateway

Run this command to create the gateway configuration with your environment variables:

```bash
cat > gateway-v0.8.1/configs/keys.env << 'ENVFILE'
BIJIRA_GATEWAY_TOKEN=<your-gateway-token>
ENVFILE
```

Replace `<your-gateway-token>` with the token you copied in Step 2.

## Step 5: Start the Gateway

Navigate to the gateway directory and start it using Docker Compose:

```bash
cd gateway-v0.8.1
docker compose up -d
```

## Step 6: Verify the Gateway

Check that the gateway is running and connected:

```bash
# Check container status
docker compose ps

# Check gateway health
curl -k https://localhost:8443/health
```

The gateway should show as **Active** in the Bijira Console under **Gateways**.

## Next Steps

Your Self-Hosted Gateway is now running! Here's what to do next:

- **Deploy APIs**: Deploy your API proxies to the environment associated with this gateway
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
