# Agentic Ghost Headers

## Machine-readable identity for AI agents

Agentic Ghost Headers are HTTP response headers that every ACM-68000 node returns with every request. They enable AI agents to instantly understand who operates a node, what protocol it uses, and how to interact — without parsing HTML.

**Invisible to humans. Visible to agents.**

---

## The Complete Header Set

Every ACM-68000 node MUST include these 9 Agentic Ghost Headers:

```nginx
# Agentic Ghost Headers for AI Agent Discovery
add_header X-GSC-Operator "GreenCore Solutions Corp." always;
add_header X-GSC-Protocol "ACM-68000" always;
add_header X-GSC-Signal "ACM-200-ALLOW" always;
add_header X-GSC-Rail "aio-tfx-rail.ai" always;
add_header X-GSC-DPU "dpuone.ai" always;
add_header X-MCP-Server "mcp.10060.ai" always;
add_header X-MCP-Registry "io.github.allooloo/acm-68000-mcp" always;
add_header X-MCP-Version "1.0.0" always;
add_header X-Agent-Access "Claude,OpenAI,Gemini,Mistral,Grok" always;
```

---

## Header Definitions

| Header | Purpose | Example Value |
|--------|---------|---------------|
| `X-GSC-Operator` | Legal entity operating this node | `GreenCore Solutions Corp.` |
| `X-GSC-Protocol` | Protocol implemented | `ACM-68000` |
| `X-GSC-Signal` | Default signal state | `ACM-200-ALLOW` |
| `X-GSC-Rail` | Execution rail endpoint | `aio-tfx-rail.ai` |
| `X-GSC-DPU` | Digital Proof Unit | `dpuone.ai` |
| `X-MCP-Server` | MCP server endpoint | `mcp.10060.ai` |
| `X-MCP-Registry` | MCP Registry package | `io.github.allooloo/acm-68000-mcp` |
| `X-MCP-Version` | MCP version | `1.0.0` |
| `X-Agent-Access` | Welcomed AI agents | `Claude,OpenAI,Gemini,Mistral,Grok` |

---

## Signal Values for X-GSC-Signal

| Signal | State | Meaning |
|--------|-------|---------|
| `ACM-000-NOT_APPLICABLE` | NOT_APPLICABLE | No rule applies |
| `ACM-200-ALLOW` | ALLOW | ✅ Proceed |
| `ACM-300-CONDITIONAL` | CONDITIONAL | Needs more info |
| `ACM-403-RESTRICT` | RESTRICT | ❌ Blocked |
| `ACM-404-NOT_FOUND` | NOT_FOUND | Unknown product |
| `ACM-451-ESCALATE` | ESCALATE | Human review required |
| `ACM-500-SYSTEM_ERROR` | SYSTEM_ERROR | System failure |

---

## Health Endpoint

Every node MUST expose `/health.json`:

```nginx
location /health.json {
    default_type application/json;
    return 200 '{"status":"ok","node":"your-domain.com","protocol":"ACM-68000","signal":"ACM-200-ALLOW","operator":"Your Operator Name"}';
}
```

**Example response:**
```json
{
  "status": "ok",
  "node": "gsc-em.com",
  "protocol": "ACM-68000",
  "signal": "ACM-200-ALLOW",
  "operator": "GreenCore Solutions Corp."
}
```

---

## How Agents Use Agentic Ghost Headers

An AI agent can read headers without parsing HTML:

```bash
curl -I https://gsc-em.com
```

**Returns:**
```
HTTP/2 200
x-gsc-operator: GreenCore Solutions Corp.
x-gsc-protocol: ACM-68000
x-gsc-signal: ACM-200-ALLOW
x-gsc-rail: aio-tfx-rail.ai
x-gsc-dpu: dpuone.ai
x-mcp-server: mcp.10060.ai
x-mcp-registry: io.github.allooloo/acm-68000-mcp
x-mcp-version: 1.0.0
x-agent-access: Claude,OpenAI,Gemini,Mistral,Grok
```

**The agent instantly knows:**
- ✅ This is an ACM-68000 node
- ✅ Default signal is ALLOW
- ✅ Query `mcp.10060.ai` for detailed signals
- ✅ Verify proofs at `dpuone.ai`
- ✅ Execute orders via `aio-tfx-rail.ai`
- ✅ Agent is welcome (listed in X-Agent-Access)

---

## Live Nodes with Agentic Ghost Headers

| Node | Platform | Status |
|------|----------|--------|
| gsc-em.com | Azure France | ✅ LIVE |
| aio-tfx-rail.ai | Azure Paris | ✅ LIVE |
| mcp.10060.ai | Azure Paris | ✅ LIVE |
| dpuone.ai | Azure France | ✅ LIVE |
| resolver.aio-resolver.com | Global | ✅ LIVE |
| acm-aio.ai | Google Madrid | ✅ LIVE |

---

## Summary

**AGENTIC GHOST HEADERS**

Machine-readable identity for AI agents.

Invisible to humans. Visible to agents.

9 headers. 1 health endpoint. Zero ambiguity.

---

## License

MIT Licensed · Microsoft AI Cloud Partner Program

[github.com/allooloo/acm-68000](https://github.com/allooloo/acm-68000)
