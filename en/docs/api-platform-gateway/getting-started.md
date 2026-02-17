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

    ![Gateway List Empty](../../assets/img/api-platform-gateway/gateway/gateway-list-empty.png)

3. Select the **API Platform** tab.
4. Click **+ Add Self-Hosted Gateway**.
5. Provide the following details:

    - **Name**: A unique name for your gateway
    - **Description**: Optional description
    - **URL**: The URL where your gateway will be accessible (e.g., `https://localhost:8443`)
    - **Associated Environment**: Select the environment for this gateway

    ![Gateway Add](../../assets/img/api-platform-gateway/gateway/gateway-add.png)

6. Click **Add**.

## Follow the instructions in Quick Start Guide

![Gateway View1](../../assets/img/api-platform-gateway/gateway/gateway-view1.png)
![Gateway View2](../../assets/img/api-platform-gateway/gateway/gateway-view2.png)

### Step 1: Download the Gateway

Run this command in your terminal to download the gateway:

```bash
curl -sLO https://github.com/wso2/api-platform/releases/download/gateway/v0.8.4/gateway-v0.8.4.zip && \
unzip gateway-v0.8.4.zip
```

### Step 2: Configure the Gateway

Run this command to create the gateway configuration with your environment variables:

```bash
cat > gateway-v0.8.4/configs/keys.env << 'ENVFILE'
MOESIF_KEY=<your-moesif-key>
GATEWAY_CONTROLPLANE_HOST=connect.choreo.dev
GATEWAY_REGISTRATION_TOKEN=<your-gateway-token>
ENVFILE
```

Once you copy the above command displayed in the console `<your-moesif-key>` and `<your-gateway-token>` will be populated and gateway-v0.8.4/configs/keys.env file will be created with these environment variables.

### Step 3: Start the Gateway

Navigate to the gateway directory and start it using Docker Compose:

```bash
cd gateway-v0.8.4
docker compose --env-file configs/keys.env up
```

### Step 4: Verify the Gateway

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
