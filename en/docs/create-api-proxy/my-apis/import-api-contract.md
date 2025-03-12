# Import API Contract

An API proxy acts as an intermediary between an existing API and Bijira, intercepting all requests made to the API.It also functions as a managed API, allowing you to apply essential API management features such as security policies and rate limiting.

In this guide, you will:

- Create an API proxy.
- Configure and Deploy the API proxy.
- Test the API proxy to verify its functionality.

### Prerequisites

- A valid Bijira account with available resource quota.

### Create an API Proxy

In this guide, you will specify a URL to an OpenAPI definition of a sample API to create an API proxy.

1. Go to [https://console.bijira.dev/](https://console.bijira.dev/) and sign in. This opens the project home page.
2. Select **Import API Contract**.
3. Select **URL** option and provide the following URL to import the API contract from the GitHub repository:
   ```
   https://raw.githubusercontent.com/wso2/bijira-samples/refs/heads/main/reading-list-api/open-api.yaml
   ```
5. Click **Next** and edit pre-defined values as needed. You can keep the default values for this sample.
6. Click **Create** to create the API Proxy. Wait for the setup to complete.

### Configure and Deploy the API Proxy

1. Navigate to the **Deploy** page of the API Proxy.
2. Select **Configure and Deploy** option from the **Deploy** dropdown and click **Configure and Deploy** button.
3. Select **External** as API Access Mode.
4. Click **Deploy**.

### Test the API Proxy 

1. Navigate to the **Test --> OpenAPI Console** page of the API Proxy.
2. Use the OpenAPI Console to test the API Proxy.

### API Proxy Behavior

The Reading List API Proxy provides the following functionality:

- **GET /books**: Returns a list of pre-defined books with a warning that changes are not persisted.
- **POST /books**: Adds a new book to the reading list (without including `id` in the request body). Returns the created book along with a warning that changes are not persisted.
- **PUT /books/{id}**: Updates the status of an existing book. The request body only includes the `status` to update, and the `id` is passed in the URL. Returns the updated book with a warning.
- **GET /books/{id}**: Retrieves a book by its `id`. If the `id` does not exist, a 404 error is returned.
- **DELETE /books/{id}**: Deletes a book by its `id`.