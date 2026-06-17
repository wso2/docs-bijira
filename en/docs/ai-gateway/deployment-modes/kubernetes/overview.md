---
title: "AI Gateway Kubernetes Deployment Modes"
description: "Choose between standalone and operator-managed Kubernetes deployment modes for API Platform AI Gateway."
canonical_url: https://wso2.com/api-platform/docs/ai-gateway/deployment-modes/kubernetes/overview/
md_url: https://wso2.com/api-platform/docs/ai-gateway/deployment-modes/kubernetes/overview.md
tags:
  - ai-gateway
  - kubernetes
  - deployment
author: WSO2 API Platform Documentation Team
last_updated: 2026-06-16
content_type: "overview"
---

# API Platform Kubernetes Gateway (V2.0.0)

API Platform Gateway is the latest evolution of the WSO2 Kubernetes gateway(APK) experience.  
If you are coming from WSO2 Kubernetes Gateway `1.3.0`, treat this as the successor track with a broader API Platform integration model and improved Kubernetes-native workflows.

- Previous generation (reference): [WSO2 APK 1.3.0 docs](https://apk.docs.wso2.com/en/latest/)
- Current generation: API Platform Kubernetes Gateway V2.0.0 (this documentation set)

## What Is New in V2.0.0

- Unified API Platform gateway model for both standalone and operator-driven deployments.
- Native support for Kubernetes Operator workflows and GitOps-style resource management.
- Flexible API exposure model:
  - API Platform CRDs (`APIGateway`, `RestApi`, and related CRDs)
  - Kubernetes Gateway API (`GatewayClass`, `Gateway`, `HTTPRoute`, optional `APIPolicy`)
- Improved extensibility for policies and secret/config-based parameter references.

## Deployment Modes

Choose one of the following modes based on your operational model.

### 1) Kubernetes Standalone Mode

Use this mode when you only need the gateway runtime and manage it directly via the gateway Helm chart.

- Installs gateway components without the gateway operator.
- Best for simpler setups or environments where operator lifecycle management is not required.
- Guide: [`kubernetes-standalone.md`](./kubernetes-standalone.md)

### 2) Kubernetes Operator Mode

Use this mode when you want operator-managed lifecycle, declarative resources, and automation.

- Installs the Gateway Operator via Helm.
- Supports:
  - API Platform CRD path (`APIGateway` + `RestApi`)
  - Kubernetes Gateway API path (`Gateway` + `HTTPRoute`)
- Guide: [`gateway-operator.md`](./gateway-operator.md)

## How to Choose a Mode

- Choose **Standalone Mode** if your priority is a lightweight gateway runtime install with Helm-managed values.
- Choose **Operator Mode** if your priority is Kubernetes-native reconciliation, GitOps workflows, multi-resource lifecycle automation, and CRD-based API management.

## Next Steps
Learn more about the deployment modes:

- [Standalone mode](./kubernetes-standalone.md)
- [Kubernetes Operator mode](./gateway-operator.md)