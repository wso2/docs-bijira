# Import a Third-Party API Contract

Bijira provides built-in support for multiple well-known third-party APIs through the **Bijira Marketplace**. However, if you need to create an API proxy for a third-party API that is not available in the Bijira Marketplace, you can do so by importing its API contract.  

## Steps to Create an API Proxy by Importing an API Contract  

Follow these steps to create an API proxy for a third-party API by importing its API contract:  

### 1. Access the Bijira Console

1. Sign in to the [Bijira Console](https://console.bijira.dev/) and select your project.  

### 2. Import the API Contract

1. Click **+Create**.
2. Navigate to **Create an API Proxy for Third-Party APIs (Egress)** and click **Import API Contract**.  
3. On the **Create API Proxy from Contract** page, provide the API contract using one of the following methods:  
    - URL for the API contract  
    - Upload an API contract file  
    - Provide a GitHub repository URL  
    - Import from SwaggerHub  
4. Click **Next**.

### 3. Configure API Proxy Details

1. Update the required API proxy details, including:  
    - API Name  
    - Identifier  
    - Version  
    - Target  
2. Review and confirm the configuration settings.  
3. Click **Create** to finalize the API proxy creation.  

   Once created, the overview page of the new API proxy appears.  

### 4. Configure Backend Settings

1. In the left navigation menu, click **Develop**, then select **Policy**.  
2. Depending on the third-party API requirements, configure **Endpoint Configurations** or set up an **API-level mediation policy** to handle authentication and authorization.  

### Next Steps

- **Test the API proxy** to ensure it correctly forwards requests to the third-party API. See [Test REST Endpoints via the OpenAPI Console](../../test-api-proxy/openapi-console.md).  
- **Apply additional policies** if needed (e.g., rate limiting, security policies). See [Policy Overview](../../develop-api-proxy/policy/attach-and-manage-policies.md#attach-a-policy).  
- **Publish the API for consumers.** See [Lifecycle Management](../../develop-api-proxy/lifecycle-management.md).  

By following these steps, you can seamlessly integrate third-party APIs into your Bijira environment and manage them efficiently.  
