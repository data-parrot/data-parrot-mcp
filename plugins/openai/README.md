# Data Parrot for OpenAI

This package connects OpenAI clients to the hosted Data Parrot MCP server.
The descriptions, starter questions, and permissions disclosure come from the
[public README](../../README.md). Keep that README as the copy source.

## Build

From the repository root, run:

```bash
python3 plugins/openai/build.py
```

The script uses the Python standard library and writes
`dist/data-parrot-openai-0.1.0.zip`. It prints the archive's SHA-256 hash.
The ZIP contains `plugin.json`, `mcp.json`, `assets/icon.png`, and the root MIT
license. File order, timestamps, and permissions are fixed for reproducible
builds with the same Python/zlib version. Generated ZIPs stay out of Git.

The package has its own version in `plugin.json`, independent of the Gemini
extension and hosted MCP server versions.

## Connection

`mcp.json` uses the existing production endpoint, Streamable HTTP, and browser
OAuth with dynamic client registration. OAuth endpoints come from discovery.
Credentials and reviewer access belong in the secure OpenAI dashboard.

## Validation status

This package has not been uploaded, submitted, or published. Authenticated
installation and portal scans remain separate checks.

OpenAI's [package guide](https://developers.openai.com/plugins/build/plugins)
documents the per-server `extensions.com.openai.auth` declaration used here.
The published Agent Plugins 1.0.0 MCP schema currently rejects that extension.
Validate the portable core separately from the documented OpenAI auth fields;
portal validation is still required. See the
[submission guide](https://developers.openai.com/plugins/deploy/submission)
for the upload and review steps.
