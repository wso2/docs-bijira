# Subscription-based APIs

A **subscription-based** API is a published API proxy that has one or more **subscription plans** assigned. Subscription plans define quotas, rate limits, and related controls at the organization level. When consumers use the API Platform Developer Portal, they choose an API, subscribe to the API with a plan, and generate Subscription Token according to your plan rules.

This model fits APIs where you need tiered access, usage limits, or clear commercial separation between consumer applications.

## Before you begin

- Organization administrators have created subscription plans. See [Create API Subscription Plans](../../administer/settings/create-api-subscription-plans.md).
- The API proxy is deployed to your **Self-Hosted Gateway** and behaves correctly. See [Getting Started with Self-Hosted Gateway](../getting-started.md).

## Assign subscription plans to the API

1. Sign in to the [API Platform Console](https://console.bijira.dev/).
2. Select the project and the API proxy.
3. Go to **Manage** → **Monetize**.
4. Enable the **Subscription Plan Status** toggle for each plan you want to offer for this API by toggling **Enabled** field.

    ![Enable Subscription Plans](../../../assets/img/api-platform-gateway/subscriptions/subscription-plan-enable.png)

For detailed steps and field behavior, see [Assign Subscription Plans to APIs](../../develop-api-proxy/subscription-plans.md).

## Assign Subscription Validation Policy to the API

1. Go to **Develop** → **Policies**.

    ![Policies Overview](../../../assets/img/api-platform-gateway/subscriptions/policies-overview.png)

2. Select **Subscription Validation** policy.

    ![Select Sub Val Policy](../../../assets/img/api-platform-gateway/subscriptions/select-sub-val-policy.png)

3. (Optional) Configure Subscription Header/Cookie value in the policy Advanced Section.

    ![Select Sub Val Policy Advanced](../../../assets/img/api-platform-gateway/subscriptions/select-sub-val-policy-advanced.png)

4. Click **Add** to attach the policy to API level policy.

5. Click **Save** to save the API.

    ![Policies Save](../../../assets/img/api-platform-gateway/subscriptions/policy-save.png)

## Deploy the API

1. Go to **Deploy** and click **Deploy**.

    ![Deploy API](../../../assets/img/api-platform-gateway/subscriptions/deploy-api.png)

## Publish the API

1. Go to **Manage** → **Lifecycle**.

    ![LifeCycle Created](../../../assets/img/api-platform-gateway/subscriptions/lifecycle-created.png)

2. Click **Publish**.
3. In the publish dialog, confirm the display name and production endpoint and click **Confirm**. The lifecycle state becomes **Published**.

    ![LifeCycle Published](../../../assets/img/api-platform-gateway/subscriptions/lifecycle-published.png)

## Subscribe to the API

1. Navigate to Developer Portal by clicking **Developer Portal**.

    ![Navigate to Devportal](../../../assets/img/api-platform-gateway/subscriptions/navigate-devportal.png)

2. Consumers can find the API in the Developer Portal by going to **APIs**.
3. Select the API and click **Subscribe**.

    ![Select API to Subscribe](../../../assets/img/api-platform-gateway/subscriptions/select-api-to-subscribe.png)

4. Pick a Subscription plan and click **Subscribe**.

    ![Select Plan to Subscribe](../../../assets/img/api-platform-gateway/subscriptions/select-plan-to-subscribe.png)

5. You will receive a Subscription Token.

    ![Receive Subscription Token](../../../assets/img/api-platform-gateway/subscriptions/recieve-sub-token.png)

## Invoke the API

1. Receive the **cURL** to invoke the API using the Subscription Token by navigating to the **Documentation**.

    ![Document API](../../../assets/img/api-platform-gateway/subscriptions/document-api.png)

2. Invoke the API.

    #### Sample Request

    ```bash
    curl --request GET \
    --url <api-invocation-url> \
    --header 'Accept: application/json' \
    --header 'Subscription-Key: <subscription-token>' -k
    ```

    #### Sample Response

    ![Invoke API](../../../assets/img/api-platform-gateway/subscriptions/invoke-api.png)



## Related documentation

- [Publish APIs overview](overview.md)
- [Subscription-less APIs](subscription-less-apis.md)
- [Create API Subscription Plans](../../administer/settings/create-api-subscription-plans.md)
- [Assign Subscription Plans to APIs](../../develop-api-proxy/subscription-plans.md)
