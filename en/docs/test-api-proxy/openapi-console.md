# Test REST Endpoints via the OpenAPI Console

Bijira offers an integrated OpenAPI Console to test REST endpoints for the API proxies you create and deploy. Since Bijira secures REST APIs with OAuth 2.0 authentication, the OpenAPI Console generates test keys to help you test your APIs.

Follow these steps to test a REST endpoint using the OpenAPI Console:

1. Go to the [Bijira Console](https://console.bijira.dev/) and log in.
2. Select the project and API which you want to test.
3. Click **Test** in the left navigation menu, then select **Console**. This will open the **OpenAPI Console** pane.
4. In the **OpenAPI Console** pane, select the desired environment from the drop-down menu.

    ![OpenAPI Console](../assets/img/test-api-proxy/openapi-console.png){.cInlineImage-full}

7. Expand the resource you want to test.
8. Click the **Try it out** button to enable testing.
9. Provide values for any parameters, if applicable.
10. Click **Execute**. The response will be displayed under the **Responses** section.

    ![OpenAPI Console Response](../assets/img/test-api-proxy/openapi-console-response.png){.cInlineImage-full}

