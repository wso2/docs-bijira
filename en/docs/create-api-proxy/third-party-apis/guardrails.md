# AI Guardrails

Guardrails are a set of guidelines and best practices designed to ensure the safe and effective use of AI systems. They help mitigate risks and promote responsible AI usage. Bijira provides 3 types of guardrails to enhance the security and reliability of AI APIs:

- **Basic Guardrails**: These are the foundational security measures that apply to all AI APIs, ensuring a baseline level of protection.
    - [Regex Guardrail](guardrails/basic-guardrails/regex-guardrail.md)
    - [Word Count Guardrail](guardrails/basic-guardrails/word-count-guardrail.md)
    - [Sentence Count Guardrail](guardrails/basic-guardrails/sentence-count-guardrail.md)
    - [Content Length Guardrail](guardrails/basic-guardrails/content-length-guardrail.md)
    - [URL Guardrail](guardrails/basic-guardrails/url-guardrail.md)
    - [Regex PII Masking](guardrails/basic-guardrails/regex-pii-masking.md)
- **Advanced Guardrails**: For more sophisticated AI applications that require enhanced flexibility and control, Bijira integrates with Guardrails AI—an extensible framework that enables seamless integration of complex AI models and services. This framework allows you to leverage open-source fine-tuned language models to implement advanced guardrails tailored to your specific requirements.
    - [PII Masking](guardrails/advanced-guardrails/pii-masking.md)
- **Third Party Guardrail Integrations**: These are integrations with third-party services that offer additional security and compliance features for AI APIs.
    - [Azure Content Safety Content Moderation](guardrails/third-party-guardrail-integrations/azure-content-safety-content-moderation.md)
    - [AWS Bedrock Guardrails](guardrails/third-party-guardrail-integrations/aws-bedrock-guardrail.md)
