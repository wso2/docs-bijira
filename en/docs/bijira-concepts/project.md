# Projects in Bijira

Projects are a core organizational unit in Bijira, designed to group related components and resources that together represent a cloud-native application or solution. This document provides a comprehensive overview of projects in Bijira, including their structure and the deployment.

---

## What is a Project?

A **project** in Bijira is a logical grouping of API Proxies that typically work together to deliver a business capability. Projects help organize development, deployment, and management workflows for cloud-native applications. Each project is isolated from others, ensuring clear boundaries for resources, permissions, and deployments.

---

## Project Structure and Components

A project may include:

- **API Proxies**: Managed APIs that expose services securely.
- **MCP Servers**: Managed MCP servers to be consumed by AI agents.

All components within a project can be managed together, versioned, and deployed as a unit.

---

## Deployment Model

At deployment time, all components in a project are deployed into a single namespace within a Kubernetes cluster. This provides:
- **Resource isolation**: Each project runs in its own namespace, preventing interference between projects.
- **Flexible exposure**: Components can be exposed to the public internet, internally to the organization, or privately within the project only.
- **Unified management**: Bijira provides tools to manage deployments, scaling, and monitoring for all project components.

A project in Bijira is represented as a **cell** in the [Cell-based architecture](https://github.com/wso2/reference-architecture/blob/master/reference-architecture-cell-based.md), which enables modular, scalable, and secure application design.

![Project](../assets/img/bijira-concepts/project.png){.cInlineImage-full}
