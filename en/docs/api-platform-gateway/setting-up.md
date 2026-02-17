# Setting Up

This guide provides detailed instructions for deploying the Bijira Self-Hosted Gateway in production environments. Choose the infrastructure option that matches your environment.

!!! tip "Quick Start"
    If you're just getting started, see the [Getting Started](getting-started.md) guide for a quick setup.

## Setup Instructions

=== "Virtual Machine"

    ### Prerequisites

    - cURL installed
    - unzip installed
    - A Docker-compatible container runtime such as:
        - Docker Desktop (Windows / macOS)
        - Rancher Desktop (Windows / macOS)
        - Colima (macOS)
        - Docker Engine + Compose plugin (Linux)

    Ensure `docker` and `docker compose` commands are available:

    ```bash
    docker --version
    docker compose version
    ```

    ### Step 1: Download the Gateway

    Run this command in your terminal to download the gateway:

    ```bash
    curl -sLO https://github.com/wso2/api-platform/releases/download/gateway/v0.8.6/gateway-v0.8.6.zip && \
    unzip gateway-v0.8.6.zip
    ```

    ### Step 2: Configure the Gateway

    Run this command to create `gateway-v0.8.6/configs/keys.env` with the required environment variables:

    ```bash
    cat > gateway-v0.8.6/configs/keys.env << 'ENVFILE'
    MOESIF_KEY=<your-moesif-key>
    GATEWAY_CONTROLPLANE_HOST=connect.choreo.dev
    GATEWAY_REGISTRATION_TOKEN=<your-gateway-token>
    ENVFILE
    ```

    ### Step 3: Start the Gateway

    1. Navigate to the gateway folder:

        ```bash
        cd gateway-v0.8.6
        ```

    2. Run this command to start the gateway using the `configs/keys.env` file created in Step 2:

        ```bash
        docker compose --env-file configs/keys.env up
        ```

    To run in detached mode (background):

    ```bash
    docker compose --env-file configs/keys.env up -d
    ```

    ### Step 4: Verify the Gateway

    Check that the gateway is running:

    ```bash
    docker compose ps
    ```

    ### Stopping the Gateway

    To stop the gateway:

    ```bash
    docker compose down
    ```

=== "Docker"

    ### Prerequisites

    - cURL installed
    - unzip installed

    ### Step 1: Download the Gateway

    Run this command in your terminal to download the gateway:

    ```bash
    curl -sLO https://github.com/wso2/api-platform/releases/download/gateway/v0.8.6/gateway-v0.8.6.zip && \
    unzip gateway-v0.8.6.zip
    ```

    ### Step 2: Configure the Gateway

    Run this command to create `gateway-v0.8.6/configs/keys.env` with the required environment variables:

    ```bash
    cat > gateway-v0.8.6/configs/keys.env << 'ENVFILE'
    MOESIF_KEY=<your-moesif-key>
    GATEWAY_CONTROLPLANE_HOST=connect.choreo.dev
    GATEWAY_REGISTRATION_TOKEN=<your-gateway-token>
    ENVFILE
    ```

    !!! warning "Important"
        Replace `<your-gateway-token>` with the Gateway Registration Token from the Bijira Console. This token is shown only once, so ensure you copy it before leaving the page.

    ### Step 3: Start the Gateway

    1. Navigate to the gateway folder:

        ```bash
        cd gateway-v0.8.6
        ```

    2. Run this command to start the gateway using the `configs/keys.env` file created in Step 2:

        ```bash
        docker compose --env-file configs/keys.env up
        ```

    To run in detached mode (background):

    ```bash
    docker compose --env-file configs/keys.env up -d
    ```

    ### Step 4: Verify the Gateway

    Check that the gateway is running:

    ```bash
    docker compose ps
    ```

    ### Stopping the Gateway

    To stop the gateway:

    ```bash
    docker compose down
    ```

=== "Kubernetes"

    ### Prerequisites

    - cURL installed
    - unzip installed
    - Kubernetes 1.32+
    - Helm 3.18+

    ### Installing the Chart

    Run this command to install the gateway chart with control plane configurations:

    ```bash
    helm install gateway oci://ghcr.io/wso2/api-platform/helm-charts/gateway --version 0.8.6 \
      --set gateway.controller.controlPlane.host="connect.choreo.dev" \
      --set gateway.controller.controlPlane.port=443 \
      --set gateway.controller.controlPlane.token.value="your-gateway-token"
    ```

    !!! warning "Important"
        Replace `your-gateway-token` with the Gateway Registration Token from the Bijira Console. This token is shown only once, so ensure you copy it before leaving the page.

    ### Customizing the Installation

    You can create a `values.yaml` file for more advanced configuration:

    ```yaml
    gateway:
      controller:
        controlPlane:
          host: "platform-api.preview-dv.choreo.dev"
          port: 443
          token:
            value: "<your-gateway-token>"
      replicas: 2
      resources:
        requests:
          cpu: "500m"
          memory: "512Mi"
        limits:
          cpu: "2000m"
          memory: "2Gi"

    service:
      type: LoadBalancer
      httpPort: 80
      httpsPort: 443

    autoscaling:
      enabled: true
      minReplicas: 2
      maxReplicas: 10
      targetCPUUtilizationPercentage: 70
    ```

    Then install with:

    ```bash
    helm install gateway oci://ghcr.io/wso2/api-platform/helm-charts/gateway --version 0.8.6 \
      -f values.yaml
    ```

    ### Verifying the Installation

    Check that the gateway pods are running:

    ```bash
    kubectl get pods -l app=gateway
    ```

    ### Upgrading the Gateway

    To upgrade to a new version:

    ```bash
    helm upgrade gateway oci://ghcr.io/wso2/api-platform/helm-charts/gateway --version <new-version> \
      -f values.yaml
    ```

    ### Uninstalling the Gateway

    To remove the gateway from your cluster:

    ```bash
    helm uninstall gateway
    ```

## What's Next?

- [Adding and Managing Policies](manage-policies.md): Configure and enforce policies
- [Analytics](analytics.md): Monitor API traffic and performance
- [Troubleshooting](troubleshooting.md): Common issues and solutions
