# Managing API Workflows

As a portal admin, you can create, edit, publish, and control the visibility of API Workflows. This page covers the full workflow lifecycle from an admin perspective.


## Creating a Workflow

1. In the Developer Portal, navigate to **Admin - Settings** and select the portal.
2. Open the **API Workflows** section.
3. Click **Create Workflow**.
4. Fill in the workflow details:

| Field | Description |
|---|---|
| **Name** | A short, task-oriented name (e.g., "Place an Order", "Register a Webhook") |
| **Handle** | A URL-safe identifier used in API endpoints. Auto-generated from the name — edit if needed. |
| **Description** | One to two sentences explaining the goal of the workflow and when to use it |
| **Arazzo Specification** | The machine-readable workflow definition in Arazzo format |
| **Agent Prompt** | Natural language guidance for AI agents on when and how to invoke the workflow |
| **Source Descriptions** | References to the API specifications used within the workflow |

<!-- Screenshot: Create Workflow form with fields filled in -->

5. Click **Save as Draft** to save without publishing, or **Publish** to make the workflow live immediately.


## Editing a Workflow

1. Navigate to **API Workflows** in the admin console.
2. Select the workflow you want to edit.
3. Make your changes in the editor.
4. Click **Save** to update a published workflow, or **Save as Draft** to unpublish it while editing.

<!-- Screenshot: Workflow editor with Arazzo spec and agent prompt fields visible -->


## Publishing and Unpublishing

Workflows must be explicitly published to become visible to consumers. Draft workflows are only visible within the admin console.

To publish a workflow:

1. Open the workflow in the admin console.
2. Click **Publish**.

To unpublish:

1. Open the workflow.
2. Click **Unpublish** (or **Save as Draft**). The workflow is removed from the portal and from `llms.txt` / `api-workflows.md` immediately.

<!-- Screenshot: Workflow detail in admin console showing Publish / Unpublish button -->


## Controlling Visibility

Visibility is controlled independently for human users and AI agents.

### Portal UI Visibility

Determines whether the workflow appears in the developer portal for human users.

- **Visible** — appears in the portal's API Workflows section and in search results
- **Hidden** — not shown in the portal UI; still accessible via direct URL if the consumer has the handle

### Agent Visibility

Determines whether the workflow is exposed to AI agents via machine-readable surfaces.

- **Visible** — included in `llms.txt` and `api-workflows.md`
- **Hidden** — excluded from agent-facing surfaces; human users can still see it in the portal UI

<!-- Screenshot: Visibility settings panel on the workflow detail page showing Portal UI and Agent Visibility toggles -->

## Deleting a Workflow

Deleting a workflow permanently removes it and all its associated data.

1. Open the workflow in the admin console.
2. Click **Delete**.
3. Confirm the deletion.

!!! warning
    This action cannot be undone. If agents or developers are actively using the workflow, consider unpublishing it instead of deleting it.
