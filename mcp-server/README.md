# ACM-68000 MCP Server

Official MCP server for the ACM-68000 deterministic signal protocol.

**Registry:** [io.github.allooloo/acm-68000-mcp](https://registry.modelcontextprotocol.io/?q=io.github.allooloo)  
**Endpoint:** `https://mcp.10060.ai`  
**Transport:** Streamable HTTP

## Quick Start

### Connect in Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "acm-68000": {
      "url": "https://mcp.10060.ai"
    }
  }
}
```

### Run Locally

```bash
cd mcp-server
pip install -r requirements.txt
python main.py
```

Server runs at `http://localhost:8000`

### Docker

```bash
cd mcp-server
docker build -t acm-mcp-server .
docker run -p 8000:8000 acm-mcp-server
```

## Available Tools

| Tool | Endpoint | Description |
|------|----------|-------------|
| `resolve_gtin` | `/tools/resolve_gtin?gtin={gtin}` | Quick GTIN → ACM signal lookup |
| `get_dpu` | `/tools/get_dpu?gtin={gtin}` | Full DPU v1.1 object |
| `check_eligibility` | `/tools/check_eligibility?gtin={gtin}&jurisdiction={code}` | Jurisdiction eligibility check |
| `list_signals` | `/tools/list_signals` | All 7 ACM-68000 signal definitions |
| `list_products` | `/tools/list_products` | All products on AIO-TFX Rail |

## Example Queries

```bash
# Resolve GTIN to signal
curl "https://mcp.10060.ai/tools/resolve_gtin?gtin=00990832300006"

# Check eligibility in Germany
curl "https://mcp.10060.ai/tools/check_eligibility?gtin=00990832300006&jurisdiction=DE"

# List all signals
curl "https://mcp.10060.ai/tools/list_signals"

# Health check
curl "https://mcp.10060.ai/health"
```

## License

MIT License — Allooloo Technologies Corp.
