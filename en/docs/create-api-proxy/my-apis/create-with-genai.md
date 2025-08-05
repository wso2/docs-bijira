# Create API with Generative AI

An API proxy acts as an intermediary between an existing API and Bijira, intercepting all requests made to the API.It also functions as a managed API, allowing you to apply essential API management features such as security policies and rate limiting.

## Prerequisites

- If you're signing in to the Bijira Console for the first time, create an organization:
    1. Go to [Bijira Console](https://console.bijira.dev/) and sign in using your preferred method.
    2. Enter a unique organization name. For example, `Stark Industries`.
    3. Read and accept the privacy policy and terms of use.
    4. Click **Create**.

  This creates the organization and opens the **Project Home** page of the default project created for you.

## Create an API Proxy

In this guide, you will create an API proxy with AI.

1. Go to [Bijira Console](https://console.bijira.dev/) and sign in. This opens the project home page.
2. If you already have one or more components in your project, click + Create. Otherwise, proceed to the next step.
3. Select **Create with GenAI**.
4. Click **Create an E-Learning Platform API**.
5. Click **Next**.
6. Add the Description as `Sample proxy for E-Learning Platform`
7. Click **Create** to create the API Proxy. Wait for the setup to complete.

## Configure and Deploy the API Proxy

1. Navigate to the **Deploy** page of the API Proxy.
2. Select **Configure and Deploy** option from the **Deploy** dropdown and click **Configure and Deploy** button.
3. Select **External** as API Access Mode.
4. Click **Deploy**.

## Test the API Proxy

1. Navigate to the **Test --> Console** page of the API Proxy.
2. Use the OpenAPI Console to test the API Proxy.

## Promote the API Proxy to Production and Publish the API proxy

1. Navigate to the **Deploy** page of the API Proxy.
2. Select **Promote to Production**.
3. In the left navigation menu, click **Lifecycle** under **Develop**. This takes you to the **Lifecycle** page.
4. Click **Publish**.
5. In the **Publish API** dialog, click **Confirm** to proceed with publishing the API. If you want to change the display name, make the necessary changes and then click **Confirm**. This sets the API lifecycle state to **Published**.