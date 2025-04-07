# Bijira API Management Governance

API Management Governance consists of a set of processes, practices, roles, and responsibilities designed to ensure the effective and efficient management of APIs throughout their lifecycle. Establishing a governance strategy is essential for maintaining consistency, security, and compliance in API development, management, and consumption.

Implementing API governance provides the following benefits:

- **Security and Compliance** – Enforces authentication, authorization, and regulatory compliance requirements.
- **Consistency** – Standardizes API design, documentation, and versioning to maintain uniformity.
- **Performance and Reliability** – Enables monitoring, rate limiting, and policy enforcement to ensure optimal API performance.
- **Lifecycle Management** – Supports structured API development, deployment, deprecation, and retirement processes.
- **Collaboration** – Defines clear roles and responsibilities for API stakeholders, improving coordination.
- **Discoverability and Reusability** – Facilitates API cataloging and reuse to minimize redundant development efforts.
- **Business Agility** – Accelerates API delivery, helping organizations meet customer and partner needs efficiently.

Bijira API Management provides a comprehensive governance capabilities that powered by AI to evaluate API compliance with governance standards given in a form of natural language specification, and also spectral based compliance validation for rules defined in OpenAPI and AsyncAPI specifications.

This section outlines the governance concepts available in Bijira.

## Governance Concepts

API Management Governance build on the following concepts

### Ruleset

A ruleset is a collection of rules that define governance policies to be enforced on APIs. These rules cover various aspects of API management, including security, compliance, performance, and operational guidelines. Rulesets can be defined at the organization level and later applied through policies to ensure governance enforcement.

Each ruleset must have a unique name and may include a description to provide additional context. Rulesets are used to validate specific aspects of an API, including:

- **API Definition** – The OpenAPI or AsyncAPI definition that establishes the API contract.
- **API Metadata** – Information about the API, such as name, version, context, and other details.
- **API Documentation** – Documentation that provides usage guidelines and other relevant information about the API.

When defining a ruleset, the API type must be specified. Supported API types include:

- **REST API**
- **Async API**

### Documents

Documents are used to feed specifications and guidelines to the Bijira AI engine for compliance validation. Documents can be in the form of natural language specifications or OpenAPI/AsyncAPI specifications.

### Policy

A **policy** is a set of rulesets that define governance policies to be enforced on APIs. Policies can be created at the organization level and later applied to APIs to enforce security, compliance, performance, and other governance requirements. Policies act as high-level groupings of rules and can be used to categorize APIs, such as external APIs, internal APIs, and partner APIs.

Each policy must have a **unique name** and may include a **description** to provide additional context.

#### Policy Attachment and Labeling

Policies can be attached to one or more **labels** to categorize them effectively. Labels serve as a link between policies and APIs when a policy is assigned to a label, it is automatically applied to all APIs associated with that label.

#### Policy Enforcement

Policy enforcement is an integral part of policy definition and can be categorized into three types:

#### 1. Policy Enforcement on APIs

All the policies will be enforced on the API proxies when the proxies are updated.

#### 2. Rule Violation Level

Policies can be enforced based on the severity of rule violations. The supported levels include:

- **Error** – Indicates a critical violation.
- **Warn** – Indicates a warning that requires attention.
- **Info** – Provides informational messages about compliance.

#### 3. Rule Violation Action

Policies define actions to be taken when a rule violation is detected. The supported actions include:

- **Notify** – Alerts users about the violation. Notifications appear in compliance dashboards, allowing users to review and take necessary actions.
