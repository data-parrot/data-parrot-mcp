# Maintainer instructions

## Ownership and release boundary

This repository owns connection instructions and Gemini CLI package metadata for Data Parrot's hosted MCP service. Keep it small: no server implementation, build system, package dependencies, local bridge, duplicated tool schemas, or official Registry `server.json`.

The GitHub repository must remain **private until Chris explicitly signs off on public visibility**. Do not submit marketplace listings or add the `gemini-cli-extension` topic without explicit release authorization; that topic activates automatic gallery discovery once public. Do not change visibility as a workaround for testing Git installation.

The separate [Cursor/Grok Bot repository](https://github.com/data-parrot/cursor-grok-bot-mcp) is frozen. Read it for reference only; do not modify it. Its root Agent Plugin manifests do not belong here.

## Canonical information

- Endpoint: `https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp`
- [MCP overview](https://dataparrot.ai/docs/mcp)
- [Connection guide](https://dataparrot.ai/docs/mcp/connect)
- [Plans and permissions](https://dataparrot.ai/docs/mcp/faq)

Use the approved short and long descriptions in the README as the marketing copy. Check current source and product documentation before changing factual claims. Revenue data is read-only; workspace-binding and access-request operations have setup effects. Preserve the workspace-wide access disclosure and do not imply HubSpot per-user permissions are enforced.

`gemini-extension.json` version `1.0.0` is this connection package's version, independent of the hosted MCP implementation and official Registry versions. Update the package version when shipping a changed extension configuration; do not change other repositories' versions. If a release tag is later authorized, keep it aligned with the package version.

The current Gemini target is 0.59.0, using `type: "http"` with `url`. Cline IDE examples use `type: "streamableHttp"`, `disabled: false`, and `autoApprove: []`. Keep client examples separate and consistent across both guides. Do not add embedded credentials or auto-approval.

## Focused validation

Run from the repository root:

```bash
python3 -m json.tool gemini-extension.json > /dev/null
git diff --check
git diff --cached --check
git diff --cached
```

Also parse the JSON examples in both Markdown guides; verify the endpoint, client transport, and exact match between Gemini examples and the manifest's `mcpServers`. Confirm only intended package files are staged and no credentials or customer data are present. Check documentation links and the logo's PNG format and 400 × 400 dimensions.

For public endpoint checks, follow the unauthenticated MCP challenge to protected-resource and authorization-server metadata. Do not register OAuth clients or make authenticated customer-data calls during static validation. A browser GET returning 405 is not a complete MCP health check.

The initial review scope is static validation only. Cline installation, Gemini installation, authenticated OAuth, workspace access, token refresh, and a business-tool call remain untested until separately exercised and recorded with client versions. Never mark these complete based on JSON parsing or a generated chat answer.

## Repository settings

Use `main`, HTTPS origin, and inherited Git identity/signing settings. Pull requests, Issues, Discussions, Projects, Wiki, Downloads, Pages, and Actions are disabled. The PR creation policy is collaborators-only.

Two differences from the public Cursor/Grok Bot repository are required while private: the organization prohibits private repository forking, and GitHub does not support interaction limits on private repositories. Forking is disabled; no interaction restriction is active and there is no expiry. If public release is explicitly authorized later, configure the planned six-month collaborators-only interaction restriction during that release and record the returned expiry. Never change visibility to enable this setting.

Match the frozen repository's collaboration and merge settings when explicitly asked, preserving organization-enforced policies. Do not add collaborators, teams, protections, workflows, or templates as incidental setup. Current descriptive topics are `mcp`, `model-context-protocol`, and `hubspot`.

Commit and push only when authorized. Public release and marketplace distribution require their own explicit authorization.
