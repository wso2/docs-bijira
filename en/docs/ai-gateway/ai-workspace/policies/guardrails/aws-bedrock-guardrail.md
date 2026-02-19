# AWS Bedrock Guardrail

The AWS Bedrock Guardrail integrates with [AWS Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) to perform real-time content safety validation and PII protection. Through a configured Bedrock Guardrail resource, it can detect and block harmful content (hate speech, sexual content, self-harm, violence) and mask or redact PII in both requests and responses.

!!! info "Additional Configuration Required"
    This guardrail requires an active AWS account, an existing Bedrock Guardrail resource, and valid AWS credentials. Set up your Bedrock Guardrail in the AWS Console before configuring this guardrail.

## Prerequisites

Before adding this guardrail:

1. **Create a Bedrock Guardrail** — In your AWS Console, navigate to Amazon Bedrock > Guardrails and create a guardrail with your desired content policies.
2. **Note the Guardrail ID and Version** — You will need these when configuring the guardrail in Bijira.
3. **Prepare AWS credentials** — You need either:
    - An AWS Access Key ID and Secret Access Key (with permission to call Bedrock), or
    - An IAM role ARN that the gateway can assume.

## Configuration Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| **Guardrail Name** | Yes | A unique name for this guardrail instance. Used for tracking and in intervention responses. |
| **AWS Guardrail ID** | Yes | The ID of the Bedrock Guardrail resource (from the AWS Console). |
| **AWS Guardrail Version** | Yes | The version of the Bedrock Guardrail resource (e.g., `DRAFT` or a version number). |
| **AWS Guardrail Region** | Yes | The AWS region where the Bedrock Guardrail is deployed (e.g., `us-east-1`). |
| **AWS Access Key ID** | Conditional | The AWS Access Key ID for authentication. Required if not using a role. |
| **AWS Secret Access Key** | Conditional | The AWS Secret Access Key for authentication. Required if not using a role. |
| **AWS Session Token** | No | An optional session token for temporary credentials. |
| **AWS Role ARN** | No | The ARN of an IAM role to assume instead of using access keys directly. |
| **AWS Role Region** | No | The AWS region for role assumption. |
| **AWS Role External ID** | No | An external ID for cross-account role assumption. |
| **JSON Path** | No | A JSONPath expression to extract the field to validate (e.g., `$.messages[0].content`). If not specified, the entire payload is sent to Bedrock for evaluation. |
| **Redact PII** | No | When enabled, PII detected by Bedrock is permanently replaced with `*****`. When disabled, PII is masked with a reversible placeholder that can be restored in the response. |
| **Passthrough On Error** | No | When enabled, requests or responses are passed through if the Bedrock service is unavailable. When disabled, an error is returned if Bedrock cannot be reached. |
| **Show Guardrail Assessment** | No | When enabled, the intervention response includes the full Bedrock assessment (topic violations, content categories, etc.). |

## Add This Guardrail

1. Navigate to **AI Workspace** > **LLM Providers** or **LLM Proxies**.
2. Click on the provider or proxy name.
3. Go to the **Guardrails** tab.
4. Click **+ Add Guardrail** and select **AWS Bedrock Guardrail** from the sidebar.
5. Fill in the AWS credentials and Bedrock Guardrail details.
6. Configure the JSON Path, PII behavior, and error handling options.
7. Click **Add** (for providers) or **Submit** (for proxies).
8. Deploy the provider or proxy to apply the changes.

## Example Configuration

| Parameter | Value |
|-----------|-------|
| Guardrail Name | `Bedrock Safety Guard` |
| AWS Guardrail ID | `abc1234567890xyz` |
| AWS Guardrail Version | `1` |
| AWS Guardrail Region | `us-east-1` |
| AWS Access Key ID | `AKIAIOSFODNN7EXAMPLE` |
| AWS Secret Access Key | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| JSON Path | `$.messages[0].content` |
| Redact PII | `false` |
| Passthrough On Error | `false` |
| Show Guardrail Assessment | `true` |

**Sample request that would be blocked:**

```json
{
  "messages": [
    {
      "role": "user",
      "content": "How do I gamble on illegal sports betting sites?"
    }
  ]
}
```

**Intervention response:**

```json
{
  "message": {
    "action": "GUARDRAIL_INTERVENED",
    "actionReason": "Violation of AWS Bedrock Guardrails detected.",
    "assessments": {
      "topicPolicy": {
        "topics": [
          {
            "action": "BLOCKED",
            "name": "Illegal Activities",
            "type": "DENY"
          }
        ]
      }
    },
    "direction": "REQUEST",
    "interveningGuardrail": "Bedrock Safety Guard"
  },
  "type": "AWS_BEDROCK_GUARDRAIL"
}
```

## PII Masking with Restoration

To mask PII using Bedrock in the request and restore it in the response, add this guardrail to **both the request and response flows** with **Redact PII disabled** in both flows.

!!! warning
    If **Redact PII** is enabled on the response flow, PII is permanently removed from the response and cannot be restored.

## Related

- [Guardrails Overview](overview.md)
- [Regex PII Masking](regex-pii-masking.md) — Lightweight PII masking without external services
- [Azure Content Safety](azure-content-safety.md) — Alternative cloud-based content safety guardrail
- [Policy Hub](https://wso2.com/api-platform/policy-hub/) — Full policy specification and latest version
