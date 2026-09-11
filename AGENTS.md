# Maintainer instructions

- This repository contains connection documentation and Gemini CLI metadata for Data Parrot's hosted MCP service. Do not add a server implementation, local bridge, dependencies, or build system.
- Preserve approved product copy. Do not rephrase Data Parrot's positioning or capabilities unless explicitly requested.
- Keep README setup summaries concise. Maintain complete client instructions in `llms-install.md`, with current official sources and exact Data Parrot documentation links. Keep section anchors stable.
- Use `https://api-v3.dataparrot.ai/api/v3/data-parrot/mcp` with native HTTP transport and OAuth discovery. Preserve existing client settings; never embed credentials or enable automatic tool approval.
- Preserve the workspace-wide access disclosure: revenue data is read-only, HubSpot per-user visibility is not enforced, and workspace selection/access requests have setup effects.
- Keep Gemini examples consistent with `gemini-extension.json`. The manifest version belongs to this connection package; documentation-only changes do not require a version bump.
- Parse JSON/TOML examples, check links and anchors, and run the commands below. Report static validation separately from observed authenticated client tests.

```bash
python3 -m json.tool gemini-extension.json > /dev/null
git diff --check
git diff --cached --check
```
