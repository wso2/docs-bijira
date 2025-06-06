# Consume an API Key Secured Service

## Prerequisites

Before proceeding, ensure you have [Created an Application](../manage-applications/create-an-application.md) and [Subscribed to an API](../manage-subscriptions/subscribe-to-an-api.md) to consume.


## Creating an API Key

To consume an API secured with an API key, create an application in the Bijira Developer Portal and subscribe it to the API under a defined usage policy. The API key will then be associated with that specific application.

---

### Steps to Create an API Key

1. Navigate to the [Bijira Developer Portal](https://devportal.bijira.dev) and sign in.
2. Click on **Applications** in the Developer Portal sidebar.
3. Select the Application the desired API is subscribed to.
4. Under the **Subscribed APIs** section, click **Generate Key** button in the row corresponding to the desired API to generate its API key.
5. The API key will be generated with the scopes defined for the selected API.

## Consume an API

Use this API Key to authenticate API requests by including it in the `api-key` header when invoking the API.

Example:
```bash
curl -H "api-key: <YOUR_API_KEY>" -X GET "https://my-sample-api.bijiraapis.dev/greet"
```
