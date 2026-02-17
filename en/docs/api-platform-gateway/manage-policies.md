# Adding and Managing Policies

This guide explains how to add and manage policies for your Self-Hosted Gateway using Bijira's unified control plane.

## Overview

Policies allow you to enforce security, rate limiting, transformation, and other governance requirements on your APIs. With the Self-Hosted Gateway, you manage policies centrally through Bijira's Policy Hub, and they are automatically synchronized to your gateway.

## Adding Policies to an API

To add policies to an API deployed on your Self-Hosted Gateway:

1. Sign in to the [Bijira Console](https://console.bijira.dev).
2. Select your organization and project.
3. Navigate to the API proxy you want to configure.
4. Click **Develop** in the left navigation, then select **Policies**.

    ![Policy Page](../../assets/img/api-platform-gateway/gateway/policy-page.png)

5. Choose the policy flow for API level or Resource Level:

    ![Policy Flow](../../assets/img/api-platform-gateway/gateway/policy-flow.png)

6. Click **+ Add Policy** and select the policy type.

    ![Policy Flow](../../assets/img/api-platform-gateway/gateway/policy-select.png)

7. Configure the policy parameters.

    ![Policy Flow](../../assets/img/api-platform-gateway/gateway/policy-configure.png)

8. Click **Add** to apply the policy.
9. Then **Save** the API.
10. Deploy the API changes to the Gateway.

## Available Policy Types

Navigate to [API Platform Policy Hub](https://wso2.com/api-platform/policy-hub/) to discover available policies.

## What's Next?

- [Analytics](analytics.md): Monitor API traffic and performance
- [Troubleshooting](troubleshooting.md): Common issues and solutions
