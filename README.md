<p align="center">
  <img src="https://dataparrot.ai/brand/data-parrot-icon-400.png" alt="Data Parrot" width="112">
</p>

# Data Parrot MCP

Data Parrot brings AI revenue analysis of your HubSpot data into your AI tools.

Data Parrot connects to HubSpot and learns how your company sells. Its MCP server brings deal health, sales forecasting, pipeline analysis, customer health, and win/loss analysis into your AI tools.

This repository contains connection instructions and a Gemini CLI extension for the hosted Data Parrot MCP server. There is no local server to build or run.

**Private review package:** public release requires Chris's explicit sign-off. The configuration targets Gemini CLI 0.59.0. Cline and Gemini installation, authenticated OAuth, workspace access, and a successful business-tool call have not been tested for this package.

[MCP overview](https://dataparrot.ai/docs/mcp) · [Connection guide](https://dataparrot.ai/docs/mcp/connect) · [Agent installation guide](llms-install.md)

## Connection details

| Setting | Value |
| --- | --- |
| Server name | `data-parrot` |
| Endpoint | `https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth through your browser, discovered by the client |

The normal connection flow requires no API key, HubSpot private-app token, or pasted bearer token.

## Before connecting

You need a connected HubSpot account, a Data Parrot Pro or Max workspace, and access to that workspace with MCP enabled for your user. Your organization may also need to allow the connection in your AI client. See the [MCP FAQ](https://dataparrot.ai/docs/mcp/faq).

Revenue-data access is read-only. The connection can access all Data Parrot data in the selected workspace, including synced HubSpot data; Data Parrot cannot synchronize or enforce HubSpot per-user permissions in MCP.

Connection setup has separate effects: selecting or switching a workspace changes the connection binding. Requesting workspace access records a request and contacts workspace administrators. Choose the workspace yourself and request access only when you intend to do so.

## Connect with Cline

1. Open **MCP Servers** in the Cline IDE extension, then **Remote Servers**.
2. Enter `data-parrot` and the endpoint above. Choose **Streamable HTTP** and add the server.
3. Complete browser sign-in and consent when Cline prompts you. Choose the Data Parrot workspace you want to use if asked.
4. Confirm the connection and available tools, then try the smoke prompt below.

For manual configuration, use Cline's **Configure MCP Servers** control to open the active settings file. Merge this entry into its existing `mcpServers` object; preserve unrelated entries. If Data Parrot is already configured for this endpoint, use that entry instead of creating a duplicate.

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

The Cline transport spelling is `streamableHttp`. Keep tool approvals enabled. See [Cline's MCP documentation](https://docs.cline.bot/mcp/mcp-overview).

## Connect with Gemini CLI

These instructions target **Gemini CLI 0.59.0**. Use either the extension or direct configuration, not both.

### Install the extension

While this repository is private, your GitHub account must have repository access and your local Git authentication must be configured. From your terminal, run:

```bash
gemini extensions install https://github.com/data-parrot/data-parrot-mcp
```

Review the installation prompt, restart Gemini CLI, and use `/mcp` to inspect the connection. Complete the requested browser sign-in; if authentication is needed, run `/mcp auth data-parrot`. Choose the workspace if asked.

The CLI downloads the extension's configuration files. It does not run a local Data Parrot server. An existing same-name entry in Gemini settings takes precedence over the extension; inspect an existing configuration before adding the extension.

### Configure the endpoint directly

Alternatively, merge this entry into `mcpServers` in your chosen Gemini settings file, such as `~/.gemini/settings.json` for user-level configuration. Preserve other settings and use any existing Data Parrot connection rather than adding a duplicate.

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

Restart Gemini CLI and complete authentication as above. The explicit `http` transport is supported by the [Gemini 0.59.0 source](https://github.com/google-gemini/gemini-cli/blob/v0.59.0/packages/core/src/tools/mcp-client.ts#L2237). See the [extension reference](https://geminicli.com/docs/extensions/reference/) for installation and removal.

## Verify the connection

Check that Data Parrot tools are available. If workspace access is unclear, ask the client to call `get_data_parrot_access_status`. Then ask:

> Where will we land this month?

Confirm that the client actually called a Data Parrot business tool successfully and used the intended workspace and period. A chat answer alone is not proof of a connection. If the workspace has no applicable data, the answer should say so.

If sign-in succeeds but revenue tools are unavailable, check the returned access status: membership, paid-plan eligibility, the HubSpot connection, MCP access for your user, or workspace selection may need attention. Follow the returned setup guidance; do not change permissions or send access requests automatically.

## Other clients and support

Use the [connection guide](https://dataparrot.ai/docs/mcp/connect) for other AI tools. The [Cursor/Grok Bot package](https://github.com/data-parrot/cursor-grok-bot-mcp) is maintained separately.

For connection problems, use the client's reconnect/authentication controls and review the [MCP FAQ](https://dataparrot.ai/docs/mcp/faq). A browser GET to the MCP endpoint can return HTTP 405; that is not a complete MCP health check.

To remove the connection, remove its entry through your client's MCP settings. For the Gemini extension, run `gemini extensions uninstall data-parrot`. Contact [support@dataparrot.ai](mailto:support@dataparrot.ai) with the client version and error message, excluding credentials and customer data.

## License

The files distributed in this repository are available under the [MIT License](LICENSE). This repository does not distribute the hosted Data Parrot service or its private server implementation.
