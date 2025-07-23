# Create an API Proxy for an Open AI API  

Follow the steps below to create an AI API:  

---

## 1. Access the Bijira Console

1. Sign in to the [Bijira Console](https://console.bijira.dev/) and select your project.  

---

## 2. Create an Open AI API


1. Click **+Create**.
2. Navigate to **Create an API Proxy for Third-Party APIs (Egress)** and click **AI APIs**.  
3. Select the **OpenAI Provider**. 

    ![Open-AI](../../assets/img/create-api-proxy/third-party-apis/ai-apis/create-open-ai.png)  

4. Configure the AI API details, such as:  
    - API Name  
    - Identifier  
    - Version  
    - AI Provider  
    - Target Endpoint  

    ![AI API Details](../../assets/img/create-api-proxy/third-party-apis/ai-apis/configure-ai-api-details.png)  

5. Click **Create** to finalize the AI API creation.  

   Once created, the overview page of the new API appears.  

---

## 3. Configure Backend Settings

1. In the left navigation menu, click **Develop**, then select **Policy**. 

    ![Policy](../../assets/img/create-api-proxy/third-party-apis/ai-apis/openai-policy-view.png)  

2. Click endpoint **Endpoint Configurations**
    ![Endpoint-config](../../assets/img/create-api-proxy/third-party-apis/ai-apis/openai-endpoint-policy.png)

3. Configure **Endpoint Configurations** to handle backend security authentication and authorization. 

     | **API Key Header**        | **API Key**         |
    | ---------------- | ----------------- |
    | Authorization | Bearer xxxxxxxxxxxxxxxxx    |
   

    ![Endpoint-config](../../assets/img/create-api-proxy/third-party-apis/ai-apis/openai-endpoint-config.png)


## 4. Deploy to development and Production Environments

1. In the left navigation menu, click **Deploy**, Deploy to Development environment

    ![Dev-config](../../assets/img/create-api-proxy/third-party-apis/ai-apis/deploy-dev.png)

2. Once it is deploy to development you can test it from Test Console.

3. When you need to promote to production environment you have to provide endponit credentials for production setup.

    ![Prod-config](../../assets/img/create-api-proxy/third-party-apis/ai-apis/deploy-prod.png)

---

## Next Steps

- **Test the AI API** to ensure it correctly forwards requests to the AI service. See [Test REST Endpoints via the OpenAPI Console](../../test-api-proxy/openapi-console.md).  

- **Publish the API for consumers** to enable integration into applications. See [Lifecycle Management](../../develop-api-proxy/lifecycle-management.md).  

By following these steps, you can efficiently integrate Open AI services into your Bijira environment and manage them with ease.  
