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
5. Choose the policy flow:
    - **Request Flow**: Policies applied before the request reaches the backend
    - **Response Flow**: Policies applied before the response reaches the client
6. Click **+ Add Policy** and select the policy type.
7. Configure the policy parameters.
8. Click **Save** to apply the policy.

## Available Policy Types

### Security Policies

| Policy | Description |
|--------|-------------|
| **OAuth2** | Validate OAuth2 access tokens |
| **API Key** | Authenticate requests using API keys |
| **JWT Validation** | Validate and decode JWT tokens |
| **Mutual TLS** | Require client certificates for authentication |
| **CORS** | Configure Cross-Origin Resource Sharing |

### Traffic Management Policies

| Policy | Description |
|--------|-------------|
| **Rate Limiting** | Limit the number of requests per time period |
| **Quota** | Set usage quotas for API consumers |
| **Spike Arrest** | Protect against traffic spikes |
| **Circuit Breaker** | Prevent cascading failures |

### Transformation Policies

| Policy | Description |
|--------|-------------|
| **Header Transformation** | Add, modify, or remove headers |
| **Payload Transformation** | Transform request/response payloads |
| **URL Rewrite** | Rewrite request URLs |

## Policy Synchronization

Policies configured in the Bijira Console are automatically synchronized to your Self-Hosted Gateway:

1. **Real-time sync**: Policy changes are pushed to connected gateways within seconds.
2. **Offline resilience**: If the gateway loses connection, it continues to enforce the last known policies.
3. **Version control**: Policy versions are tracked for audit and rollback purposes.

### Verifying Policy Sync

To verify that policies are synchronized to your gateway:

```bash
# Check gateway logs for policy sync events
docker compose logs | grep -i "policy"
```

You should see log entries indicating successful policy synchronization:

```
INFO  Policies synchronized successfully
INFO  Applied 3 policies to API: my-api
```

## Configuring Rate Limiting

Rate limiting is one of the most common policies. Here's how to configure it:

1. Navigate to your API proxy in the Bijira Console.
2. Go to **Develop** > **Policies**.
3. In the **Request Flow**, click **+ Add Policy**.
4. Select **Rate Limiting**.
5. Configure the rate limit:
    - **Requests**: Number of requests allowed
    - **Time Unit**: Second, Minute, Hour, or Day
    - **Key Type**: Per API, Per Application, or Per User
6. Click **Save**.

### Example Rate Limit Configuration

```yaml
# 100 requests per minute per application
requestsPerUnit: 100
unit: MINUTE
keyType: APPLICATION
```

## Configuring API Key Authentication

To require API key authentication:

1. Navigate to your API proxy.
2. Go to **Develop** > **Policies**.
3. In the **Request Flow**, click **+ Add Policy**.
4. Select **API Key**.
5. Configure:
    - **Header Name**: The header containing the API key (default: `X-API-Key`)
    - **Query Parameter**: Alternative query parameter name
6. Click **Save**.

## Managing Policy Priorities

When multiple policies are applied, they execute in order:

1. Drag and drop policies in the policy list to change their order.
2. Security policies typically run first.
3. Transformation policies run after security validation.

## Troubleshooting Policies

### Policy Not Applied

If a policy doesn't seem to be working:

1. **Check sync status**: Verify the gateway has synchronized policies.
2. **Review logs**: Check gateway logs for policy errors.
3. **Test with curl**: Use verbose mode to see applied headers:
   ```bash
   curl -v https://your-gateway/api/resource
   ```

### Rate Limit Not Working

If rate limiting isn't enforced:

1. Verify the policy is attached to the correct API.
2. Check the key type matches your test scenario.
3. Ensure the gateway has connectivity to the control plane.

## What's Next?

- [Analytics](analytics.md): Monitor API traffic and performance
- [Troubleshooting](troubleshooting.md): Common issues and solutions
