# Install the Data Parrot MCP connection

Use this guide to connect an AI client to Data Parrot's hosted MCP server. There is no Data Parrot server package to install, build, or run locally. Use the client's native remote HTTP and OAuth support.

**Documentation checked: September 11, 2026.** Each client section links to current provider documentation and the corresponding Data Parrot guide. Gemini's configuration was also checked against its latest stable release, 0.59.0. These are documentation and configuration checks: client installation, authenticated OAuth, workspace access, token refresh, and successful business-tool execution have not been tested as part of this package review.

## Choose the client

| AI client | Installation instructions |
| --- | --- |
| Claude.ai / Claude Desktop | [Custom connector](#claudeai--claude-desktop) |
| Claude Code | [Native HTTP connection](#claude-code) |
| ChatGPT | [Developer mode connection](#chatgpt) |
| Codex app | [Desktop MCP settings](#codex-app) |
| Codex CLI | [Terminal setup](#codex-cli) |
| Cursor | [Native remote connection](#cursor) |
| Grok.com | [Custom connector](#grokcom) |
| Grok CLI | [Terminal setup](#grok-cli) |
| Cline IDE extension | [Remote server settings](#cline-ide-extension) |
| Gemini CLI | [Direct connection or extension](#gemini-cli) |

## Service and prerequisites

- Name: `data-parrot`
- Endpoint: `https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp`
- Transport: Streamable HTTP
- Authentication: client-discovered OAuth with human browser sign-in and consent
- Access: a connected HubSpot account, a Data Parrot Pro or Max workspace, workspace membership, and MCP enabled for the user
- Client permission: the AI client or organization must allow this remote connection

Revenue data is read-only. The connection can access all Data Parrot data in the selected workspace, including synced HubSpot data. HubSpot per-user permissions are not synchronized or enforced through MCP.

Selecting or switching a workspace changes the connection binding. Requesting access records a request and attempts to notify workspace administrators. Do not choose a workspace for the user or automatically request access.

## Before changing client settings

Identify the intended client, installed version, and configuration scope. If the client is unspecified, ask. Inspect existing settings and installed plugins first. Reuse a Data Parrot connection for the same endpoint, even if its name differs; use that existing name in subsequent commands. Preserve unrelated settings, server entries, credentials, and approval policies. Ask before replacing a same-name entry that points elsewhere or removing an existing connection.

Use user-level configuration for a new CLI or IDE connection unless the user requests project scope. Every JSON or TOML example below is an entry to merge, not a replacement settings file. Add only the intended connection; do not execute every client section.

Use native OAuth discovery. Do not request API keys, HubSpot private-app tokens, browser cookies, or pasted access tokens. Do not add `mcp-remote`, a local bridge, shell startup commands, environment variables, hardcoded OAuth endpoints, or blanket tool approval. Let the user complete browser sign-in and consent. If a documented command or control is missing, check the installed version and current provider guide before proceeding.

## Claude.ai / Claude Desktop

1. Open **Customize → Connectors**. Reuse Data Parrot if already present.
2. On an individual Claude Pro or Max account, select **+ → Add custom connector**. Enter **Data Parrot** and the endpoint above. Leave advanced OAuth client credentials unset, then select **Add**.
3. On Claude Team or Enterprise, an owner must first add the endpoint through **Organization settings → Connectors → Add → Custom → Web**. Members then find it in **Customize → Connectors**.
4. Select **Connect** and complete Data Parrot browser sign-in.
5. In a conversation, open **+ → Connectors** and enable Data Parrot. Continue to [verify a real call](#check-access-and-verify-a-real-call).

Use the remote connector flow for Claude Desktop as well; do not add a local process to `claude_desktop_config.json`. If an organization owner must enable the connector, explain that requirement rather than changing organization settings automatically.

Sources: [Claude custom connector documentation](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) · [Data Parrot Claude guide](https://dataparrot.ai/docs/mcp/connect/anthropic#connect-the-data-parrot-mcp-server-to-claudeai-or-claude-desktop).

## Claude Code

Inspect `claude mcp list` and the session's `/mcp` menu first, including any connector or plugin that already supplies Data Parrot. If absent, run:

```bash
claude mcp add --transport http --scope user data-parrot https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp
```

Open Claude Code, enter `/mcp`, select Data Parrot, and complete browser authentication. Current Claude Code also supports `claude mcp login data-parrot` from the terminal (introduced in 2.1.186). Use the `/mcp` flow if the installed version predates that command.

Check the connection with `/mcp`, then [verify a real call](#check-access-and-verify-a-real-call). An “Added” message only confirms the configuration was saved.

Sources: [Claude Code MCP reference](https://code.claude.com/docs/en/mcp) · [Data Parrot Claude Code guide](https://dataparrot.ai/docs/mcp/connect/anthropic#connect-the-data-parrot-mcp-server-to-claude-code).

## ChatGPT

1. In ChatGPT web, open **Settings → Security and login** and enable **Developer mode**. Availability depends on the account and workspace policy; an administrator may need to enable access.
2. Open [ChatGPT Plugins](https://chatgpt.com/plugins), inspect existing connections, and select **+** if Data Parrot is absent.
3. Enter **Data Parrot** and the description: **Data Parrot brings AI revenue analysis of your HubSpot data into your AI tools.** Under **Connection**, use the public HTTPS endpoint above.
4. Use OAuth if the form asks for an authentication method. Leave optional OAuth client credentials unset, create the connection, and complete Data Parrot browser sign-in.
5. Review the discovered tools. Start a conversation, add Data Parrot from the tools menu, and [verify a real call](#check-access-and-verify-a-real-call).

This configures a personal or workspace-authorized custom connection; it does not require a public Data Parrot directory listing. Do not publish a workspace-wide connection as an incidental setup step.

Sources: [OpenAI's current connection guide](https://developers.openai.com/plugins/deploy/connect-chatgpt) · [Data Parrot ChatGPT guide](https://dataparrot.ai/docs/mcp/connect/openai#connect-the-data-parrot-mcp-server-to-chatgpt).

## Codex app

1. Open **Settings** and locate **MCP servers**. In versions with the older settings layout, this is under **Plugins → MCPs**.
2. Reuse an existing Data Parrot connection; otherwise select **Add server**, enter `data-parrot`, choose **Streamable HTTP**, and paste the endpoint above.
3. Save, restart the connection when prompted, and select **Authenticate** to complete browser sign-in.
4. Enter `/mcp` in a conversation and [verify a real call](#check-access-and-verify-a-real-call).

OpenAI's current MCP reference labels the desktop setup as ChatGPT desktop. The shared local configuration remains `~/.codex/config.toml` by default. The app and Codex CLI do not need separate entries when using the same configuration home.

Sources: [OpenAI's desktop MCP reference](https://learn.chatgpt.com/docs/extend/mcp) · [Data Parrot Codex app guide](https://dataparrot.ai/docs/mcp/connect/openai#connect-the-data-parrot-mcp-server-to-the-codex-app).

## Codex CLI

Inspect `codex mcp list` first. If Data Parrot is absent, run:

```bash
codex mcp add data-parrot --url https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp
```

Complete sign-in if the add command starts it. If authentication is still required, run:

```bash
codex mcp login data-parrot
```

Alternatively, merge this into the active user configuration, normally `~/.codex/config.toml`, and use the login command above:

```toml
[mcp_servers.data-parrot]
url = "https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp"
```

Use one configuration method. Open Codex and check `/mcp`, then [verify a real call](#check-access-and-verify-a-real-call). For a Mac authentication failure, consult the [Data Parrot Mac troubleshooting guide](https://dataparrot.ai/docs/mcp/connect/codex-macos-workaround); do not apply certificate or OAuth overrides preemptively.

Sources: [OpenAI's MCP configuration and OAuth reference](https://learn.chatgpt.com/docs/extend/mcp) · [Data Parrot Codex CLI guide](https://dataparrot.ai/docs/mcp/connect/openai#connect-the-data-parrot-mcp-server-to-codex-cli).

## Cursor

If the separate Data Parrot Cursor/Grok Bot plugin is already installed, use its connection. Do not add a duplicate or replace the plugin.

For a new direct remote connection, merge this into `~/.cursor/mcp.json` for user scope. Use project `.cursor/mcp.json` only when requested:

```json
{
  "mcpServers": {
    "data-parrot": {
      "url": "https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp"
    }
  }
}
```

Open **Customize** and inspect Data Parrot under MCP servers. Complete the OAuth prompt when connecting or first using its tools, then [verify a real call](#check-access-and-verify-a-real-call). Keep existing tool-approval settings. Do not add static OAuth credentials or a local bridge.

The [Data Parrot Cursor guide](https://dataparrot.ai/docs/mcp/connect/cursor#connect-data-parrot-to-cursor) describes the separate GitHub plugin installation path. The direct URL configuration above follows [Cursor's current MCP documentation](https://cursor.com/docs/mcp). Either path uses the hosted endpoint; use only one.

## Grok.com

1. Open [Grok Connectors](https://grok.com/connectors) and inspect existing connections.
2. Select **New Connector → Custom**. Enter **Data Parrot** and the endpoint above.
3. Complete Data Parrot browser authentication. On Grok Business or Enterprise, a team administrator must first provision the connector for the organization.
4. Return to Grok, confirm the connector and its tools are available, and [verify a real call](#check-access-and-verify-a-real-call).

Grok.com is separate from Grok Bot and does not use the Cursor/Grok Bot plugin package.

Sources: [xAI's custom connector instructions](https://docs.x.ai/grok/connectors) · [Data Parrot Grok.com guide](https://dataparrot.ai/docs/mcp/connect/xai#connect-the-data-parrot-mcp-server-to-grokcom).

## Grok CLI

Use the official xAI Grok CLI. Inspect `grok mcp list` first; `grok inspect` shows loaded configuration origins. Grok can also load Claude and Cursor MCP settings, so reuse an imported Data Parrot connection when present.

If absent, add the remote server:

```bash
grok mcp add --transport http data-parrot https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp
```

Open Grok and enter `/mcps`. Select Data Parrot and use the authentication action (`i` in the current interface), then complete browser sign-in. If configuration was edited while Grok was open, refresh the MCP list with `r`.

For a connection problem, run `grok mcp doctor data-parrot` and inspect the result. Continue to [verify a real call](#check-access-and-verify-a-real-call). Do not add project scope unless requested.

Sources: [xAI's MCP and CLI reference](https://docs.x.ai/build/features/mcp-servers) · [Data Parrot Grok CLI guide](https://dataparrot.ai/docs/mcp/connect/xai#connect-the-data-parrot-mcp-server-to-grok-cli).

## Cline IDE extension

1. Open **MCP Servers → Remote Servers** in Cline.
2. Enter `data-parrot` and the endpoint above, choose **Streamable HTTP**, and select **Add Server**.
3. When the server reports authentication is required, select **Authenticate** in its MCP settings. Complete browser sign-in, then [verify a real call](#check-access-and-verify-a-real-call).

For manual configuration instead, open **MCP Servers → Configure → Configure MCP Servers**. This opens the active extension settings file without assuming an operating-system-specific path. Merge:

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

Use the exact `streamableHttp` spelling. In current Cline, omitting `type` selects legacy SSE. Leave `autoApprove` empty and do not add an Authorization header; Data Parrot uses browser OAuth.

Sources: [Cline's current MCP setup and configuration reference](https://docs.cline.bot/mcp/mcp-overview) · [Cline's native OAuth flow](https://github.com/cline/cline/blob/main/apps/vscode/src/services/mcp/McpOAuthManager.ts). Data Parrot's [general connection guide](https://dataparrot.ai/docs/mcp/connect) covers service prerequisites; there is no dedicated Cline website guide yet.

## Gemini CLI

The checked stable release is [Gemini CLI 0.59.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.59.0). Inspect `gemini mcp list`, installed extensions, and the active settings first. A same-name server in `settings.json` takes precedence over an extension. Choose one of the following paths.

### Direct connection

For a new user-level connection, run:

```bash
gemini mcp add --transport http --scope user data-parrot https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp
```

Alternatively, merge this into `mcpServers` in `~/.gemini/settings.json`:

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

The explicit `type: "http"` and `url` match the released 0.59.0 transport implementation and this repository's manifest. Some Gemini documentation examples still use `httpUrl`; use the release-checked configuration above. Do not add `--trust` or enable automatic approval.

### Extension installation

If the user chooses this package instead of direct configuration, run from a terminal:

```bash
gemini extensions install https://github.com/data-parrot/data-parrot-mcp
```

Git must be available. While the repository is private, the user needs repository access and working Git authentication. Let the user review the installation prompt. This downloads connection configuration, not a Data Parrot server runtime. Do not bypass prompts or enable automatic updates as part of setup.

### Authenticate and verify

Restart Gemini CLI. Use `/mcp` to inspect the server and `/mcp auth data-parrot` when authentication is needed. Let the user finish sign-in and consent in the browser, then [verify a real call](#check-access-and-verify-a-real-call). A local browser and a reachable OAuth callback are required for this documented flow; report headless or remote callback problems instead of extracting credentials from another client.

Sources: [Gemini MCP documentation](https://geminicli.com/docs/tools/mcp-server/) · [Extension reference](https://geminicli.com/docs/extensions/reference/) · [0.59.0 HTTP transport](https://github.com/google-gemini/gemini-cli/blob/v0.59.0/packages/core/src/tools/mcp-client.ts#L2237) · [0.59.0 add-command implementation](https://github.com/google-gemini/gemini-cli/blob/v0.59.0/packages/cli/src/commands/mcp/add.ts).

Data Parrot's [general connection guide](https://dataparrot.ai/docs/mcp/connect) covers service prerequisites; there is no dedicated Gemini website guide yet.

## Other AI clients

For a client not listed here, check its current official documentation for native Streamable HTTP and browser OAuth support, then use the [Data Parrot custom connection guide](https://dataparrot.ai/docs/mcp/connect/other-clients). Do not copy another client's JSON schema or introduce a local bridge without a separately approved setup approach.

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

Only remove a connection when the user requests it. Preserve all unrelated configuration and use the actual configured name:

- Claude.ai/Desktop: use the connector's **Remove** control in **Customize → Connectors**.
- Claude Code: `claude mcp remove data-parrot --scope user` for the user-level entry created above.
- ChatGPT: open the connection in **Plugins** and use its disconnect/remove control.
- Codex app/CLI: remove the server in MCP settings or use `codex mcp remove data-parrot`. With shared local configuration, this affects both clients.
- Cursor: remove only the direct `data-parrot` entry from the configuration file you edited; manage a plugin-provided connection through that plugin's controls.
- Grok.com: open the connector's management controls and disconnect/remove it.
- Grok CLI: `grok mcp remove data-parrot`.
- Cline: remove the server in MCP settings or remove only its JSON entry.
- Gemini direct connection: remove only its entry from the settings file you edited. Gemini extension: `gemini extensions uninstall data-parrot`.

Report what was configured, which checks actually ran, and any remaining access requirement. Never claim installation, OAuth, workspace access, token refresh, or a business call was tested unless it was observed.

For service requirements, see the [MCP FAQ](https://dataparrot.ai/docs/mcp/faq). Contact [support@dataparrot.ai](mailto:support@dataparrot.ai) with the client version and error, excluding credentials and customer data.
