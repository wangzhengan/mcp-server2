# ChatGPT MCP Integration

## Install

```bash
pip install -e .
```

## Configure MCP Client

Example configuration:

```json
{
  "mcpServers": {
    "local-files": {
      "command": "python",
      "args": ["-m", "mcp_server.main"],
      "cwd": "/path/to/mcp-server2"
    }
  }
}
```

## Available Tools

- read_file
- list_directory
- search_files

## Security

The server uses a sandbox root directory and only exposes configured file types.
Write operations are disabled by default.
