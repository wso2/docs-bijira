# Create an API Proxy from a GitHub Repository Source

An API proxy acts as an intermediary between an existing API and Bijira, intercepting all requests made to the API. It also functions as a managed API, allowing you to apply essential API management features such as security policies and rate limiting.

## Prerequisites

1. If you're signing in to the Bijira Console for the first time, create an organization:
    1. Go to [Bijira Console](https://console.bijira.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

    This creates the organization and opens the **Project Home** page of the default project created for you.

2. Fork the [Bijira samples repository](https://github.com/wso2/bijira-samples), which contains the [sample proxy source](https://github.com/wso2/bijira-samples/tree/main/reading-list-api).

## Configure component.yaml

When creating an API proxy from a GitHub repository, you must include a `component.yaml` configuration file in your repository. This file must be located at `.choreo/component.yaml` within your API directory.

### Required Configuration

The `component.yaml` file for API proxies must include the following structure:

```yaml
proxy:
  type: REST
  schemaFilePath: openapi.yaml
```

### Configuration Fields

| **Field** | **Required** | **Description** |
|-----------|--------------|-----------------|
| `proxy.type` | Required | The type of API proxy. Supported values are: <br>- `REST` - For REST APIs (uses OpenAPI specification) <br>- `WS` - For WebSocket APIs (uses AsyncAPI specification) |
| `proxy.schemaFilePath` | Required | The path to your API specification file relative to the API directory. For REST APIs, this should point to your OpenAPI specification file (e.g., `openapi.yaml`). For WebSocket APIs, this should point to your AsyncAPI specification file (e.g., `asyncapi.yaml`). |

!!! note
    The `component.yaml` file must be present in the `.choreo` directory within your API directory for Bijira to successfully build and deploy your API proxy from GitHub.

## Step 1: Create an API proxy

You can create an API proxy either by selecting the source from a GitHub repository, uploading an OpenAPI specification file, or providing an OpenAPI specification URL. This guide demonstrates how to create an API proxy using a GitHub repository as the source.

1. Go to the [Bijira Console](https://console.bijira.dev/) and sign in. This opens the project home page.
2. If you already have one or more components in your project, click **+ Create**. Otherwise, proceed to the next step.
3. Select Import API Contract and click on GitHub tab.
4. Click on **Authorize With GitHub** card under **Connect a Git Repository** section to connect your GitHub account.
    - If you haven’t connected your GitHub repository to Bijira, enter your GitHub credentials and select the repository you forked in the prerequisites section to install the [Bijira GitHub App](https://github.com/marketplace/choreo-apps).

    !!! note
        The **Bijira GitHub App** requires the following permissions:
         - Read and write access to code and pull requests.
         - Read access to issues and metadata.

        You can [revoke access](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/reviewing-your-authorized-integrations#reviewing-your-authorized-github-apps) if needed. Write access is only used for sending pull requests; Bijira will not push changes directly to your repository.

    !!! note
        If you are the owner of the GitHub organization and need to authorize the Bijira GitHub App on behalf of your collaborators, you can install the Bijira GitHub App directly in your organization via [install App](https://github.com/marketplace/choreo-apps).

5. Enter the following repository details:

    | **Field**              | **Value**          |
    |------------------------|--------------------|
    | **Organization**       | Your GitHub account|
    | **Repository**         | bijira-samples     |
    | **Branch**             | **`main`**         |
    | **API Directory**      | /reading-list-api |


    ![Create API from Github](../../../assets/img/create-api-proxy/import-from-github/api_from_github_select_repo.png)

    !!! note
        To select the relevant directory, click on the **Edit** action next to the **API Directory** input field. Then, enter `reading-list-api` as the directory name to quickly search and locate the correct directory.

6. Specify the following values as Proxy Metadata:

    | **Field**       | **Value**                                  |
    |-----------------|--------------------------------------------|
    | **Name**     | `Reading List API`                                   |
    | **Version**     | `1.0`                                      |
    | **Target**      | `https://apis.bijira.dev/samples/reading-list-api-service/v1.0`|

7. Click **Create**. This creates the API proxy component and takes you to the **Overview** page.

!!! note
    The API contract cannot be modified after proxy creation. Therefore, any changes to the API contract in the GitHub repository will not apply to the created proxy.

## Step 2: Build and Deploy the API proxy

!!! info
    A build starts automatically when you create the API proxy, and you will be redirected to the **Overview** page.

1. In the left navigation menu, click **Deploy**.
2. If the build is in progress, you can view the Build information.

![Create API from Github](../../../assets/img/create-api-proxy/import-from-github/api_from_github_build_page.png)


 <!-- keep list -->
3. Once the build is completed, in the deploy navigation menu, in the **Build Area** card, click **Configure & Deploy**. 
   This opens the **Configure & Deploy** pane. <br><br>
4. Select **External** as the **API Access Mode** and click **Deploy**. The **Development** card indicates the **Deployment Status** as **Active** when the API proxy is successfully deployed.

![Create API from Github](../../../assets/img/create-api-proxy/import-from-github/api_from_github_deploy_page.png)

Now, you are ready to test the API proxy. You can test the API via the [OpenAPI Console](../../../test-api-proxy/openapi-console/) provided in Bijira