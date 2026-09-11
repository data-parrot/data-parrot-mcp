# Install the Data Parrot MCP connection

Use this guide to configure the hosted Data Parrot MCP server in Cline or Gemini CLI. There is no Data Parrot server package to install, build, or run locally.

**Status:** private review package. Public release requires Chris's explicit sign-off. These configurations have not been certified through authenticated client testing. The Gemini configuration targets version 0.59.0; no tested Cline version has been recorded yet.

## Service and prerequisites

- Name: `data-parrot`
- Endpoint: `https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp`
- Transport: Streamable HTTP
- Authentication: client-discovered OAuth with human browser sign-in and consent
- Access: a connected HubSpot account, a Data Parrot Pro or Max workspace, workspace membership, and MCP enabled for the user
- Client permission: the AI client or organization must allow this remote connection

Revenue data is read-only. The connection can access all Data Parrot data in the selected workspace, including synced HubSpot data. HubSpot per-user permissions are not synchronized or enforced through MCP.

Selecting or switching a workspace changes the connection binding. Requesting access records a request and contacts workspace administrators. Do not choose a workspace for the user or automatically request access.

## Configure only the intended client

Identify the target client and configuration scope before editing. If the request does not identify them, ask. Inspect existing settings first. Reuse a Data Parrot entry for the same endpoint, even if its display name differs. Preserve all unrelated settings, server entries, credentials, and approval policies. If a same-name entry points elsewhere, ask before replacing it.

Use the client's existing remote OAuth support. Do not request API keys, HubSpot private-app tokens, browser cookies, or pasted access tokens. Do not add a local bridge, shell startup command, environment variables, hardcoded OAuth endpoints, or blanket tool approval.

### Cline IDE extension

1. Open **MCP Servers → Remote Servers**.
2. Enter the name and endpoint above; choose **Streamable HTTP** and add the server.
3. If editing JSON instead, open the active file through **Configure MCP Servers** and merge this entry into `mcpServers`:

```json
{
  "mcpServers": {
    "data-parrot": {
      "type": "streamableHttp",
      "url": "https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

Use the exact Cline spelling `streamableHttp`, not `streamable-http`, `http`, or legacy SSE. This is an entry to merge, not a replacement settings file. Let Cline prompt the user for browser authentication.

### Gemini CLI 0.59.0

Choose one installation path. Inspect both existing extensions and the relevant Gemini settings before adding anything: an existing same-name settings entry overrides the extension's server configuration.

**Extension path:** with repository access and Git authentication already configured, run in a terminal:

```bash
gemini extensions install https://github.com/data-parrot/data-parrot-mcp
```

Let the user review the installation prompt. This downloads configuration files, not a server runtime. Do not bypass confirmation prompts or enable automatic updates as part of setup.

**Direct path:** merge the following into the chosen Gemini settings file's `mcpServers` object. User-level configuration is `~/.gemini/settings.json`; use project scope only when requested. No repository download is needed for this path.

```json
{
  "mcpServers": {
    "data-parrot": {
      "type": "http",
      "url": "https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp"
    }
  }
}
```

Restart Gemini CLI. Use `/mcp` to inspect the server and `/mcp auth data-parrot` when authentication is needed. If reusing another server name, use that name in the authentication command. Let the user finish sign-in and consent in their browser. For other Gemini versions, check that version's supported transport configuration before editing; do not silently substitute SSE.

## Check access and verify a real call

1. Confirm that authentication completed and the client exposes Data Parrot tools.
2. Call `get_data_parrot_access_status` when access or workspace selection is unresolved.
3. If a workspace must be selected, present the returned options and wait for the user's explicit choice. Use that choice to complete binding.
4. Ask: **Where will we land this month?**
5. Verify an actual successful Data Parrot business-tool call, the selected workspace, and the intended month. Do not claim success based only on generated chat text. Report an empty eligible dataset honestly.

Handle restricted access using the returned status and setup link. A valid login may still require membership, a Pro/Max workspace, a usable HubSpot connection, administrator-enabled MCP access, or workspace selection. Explain the next action to the user. Do not upgrade plans, change permissions, switch workspaces, reset bindings, or invoke `request_data_parrot_access` automatically.

If login cannot be completed, report configuration as prepared and authentication as pending. Do not extract credentials from another client to complete the test.

## Reconnect, remove, and get help

Use the client's reconnect or authentication controls after a failed or expired login. A normal unauthenticated MCP request can return 401 to start OAuth discovery. A browser GET can return 405; neither response alone establishes an outage.

Remove a direct connection through the client's MCP settings, preserving other entries. Remove the Gemini extension with `gemini extensions uninstall data-parrot`. Report what was configured, which checks actually ran, and any remaining access requirement. Never claim installation, token refresh, or a business call was tested unless it was observed.

- [Canonical connection guide](https://dataparrot.ai/docs/mcp/connect)
- [Plans, access, and permissions](https://dataparrot.ai/docs/mcp/faq)
- [Cline MCP documentation](https://docs.cline.bot/mcp/mcp-overview)
- [Gemini extension reference](https://geminicli.com/docs/extensions/reference/)
- [Gemini 0.59.0 transport implementation](https://github.com/google-gemini/gemini-cli/blob/v0.59.0/packages/core/src/tools/mcp-client.ts#L2237)
- [Support](mailto:support@dataparrot.ai) — include the client version and error, excluding credentials and customer data
