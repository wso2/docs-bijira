# Test APIs with Bijira API Chat

Testing APIs is an essential step in the API development process. Bijira simplifies the testing task by allowing you to engage with your APIs using natural language through Bijira API Chat. It eliminates manual test scenario creation and JSON payload accuracy concerns. It enables easy API communication using human language and requires no coding for handling sequences with multiple resource calls. This makes your API testing efficient and user-friendly.


!!! info
    This feature is available for REST API Proxy components and Service components with REST endpoints.

Follow the steps below to test an API with API Chat: 

1. Sign in to the [Bijira Console](https://console.bijira.dev/).
2. Select the project and API which you want to test.
3. On the left navigation, click **Test** and then click **API Chat**. This opens the **API Chat** pane.
4. You can enter your query in natural language and execute it. For example, if you have a resource like `POST /books` and `GET /books`, you can input the following query and execute it to obtain results.
    ```
    "Add a new book titled 'The Hobbit' by 'J. R. R. Tolkien' to the reading list and verify if it was successfully added." 
    ```
The resources are executed sequentially based on your query. Alternatively, you can use the sample queries available to try out API Chat. 

    ![API Chat Results](../assets/img/test-api-proxy/api-chat-result.png){.cInlineImage-full}
