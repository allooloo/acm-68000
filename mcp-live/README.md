# MCP Live — First MCP for CPG - 

Fork it. Bring your AI. Build together. 

---
**Ex Machina. With the help of machines.**

## What This Is

The first MCP server for Consumer Packaged Goods.  
Open protocol. Deterministic signals.  
Built by humans and AI together.

**Endpoint:** `https://mcp.10060.ai`  
**Registry:** [io.github.allooloo/acm-68000-mcp](https://registry.modelcontextprotocol.io/?q=io.github.allooloo)  
**Protocol:** ACM-68000  
**Status:** LIVE

---

## The Build

Built by **Allooloo** with **Claude** and **Mistral**, and input from 5 other frontier LLMs in real time.

Claude piped in to Paris for the build.

| Agent | Role |
|-------|------|
| **Claude** (Anthropic) | Co-architect — MCP design, tool definitions, APIM policies, documentation. Now connected as agent. |
| **Mistral** (France) | Sovereign AI partner — FR-ECO-10060, French law, GDPR compliance |
| **Gemini** (Google) | Madrid ESG bridge integration |
| **Grok** (xAI) | Health endpoint design |
| **Perplexity** | Research + validation |
| **Copilot** (Microsoft) | Code review |
| **ChatGPT** (OpenAI) | Code review |

---

## Connect Your Agent

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
    "mcpServers": {
          "acm-68000": {
                  "url": "https://mcp.10060.ai"
                }
        }
  }
```

### curl

```bash
# List the 7 signals
curl https://apim-ghost-signal.azure-api.net/ingest/signals

# Check health
curl https://apim-ghost-signal.azure-api.net/ingest/health

# Send a signal
curl -X POST https://apim-ghost-signal.azure-api.net/ingest/ \
  -H "Content-Type: application/json" \
  -d '{"sender":"your-agent","signal":"ACM-200","message":"test"}'
```

---

## 10 Tools

| Tool | What It Does |
|------|--------------|
| `listSignals` | Returns the 7 ACM signals |
| `getInbound` | Ingress URL + payload schema |
| `ingestSignal` | Send signal to network |
| `resolveGtin` | GTIN → compliance check |
| `getNodes` | 18 jurisdiction nodes |
| `getGoogleBridge` | Google Madrid ESG bridge |
| `getResolver` | AI-Native architecture |
| `getCarbon` | Carbon-aware compute metrics |
| `getHealth` | System status |
| `getMCP` | Root manifest |

---

## The 7 Signals

| Signal | State | Meaning |
|--------|-------|---------|
| `ACM-000` | NOT_APPLICABLE | No action needed |
| `ACM-200` | ALLOW | Execute transaction |
| `ACM-300` | CONDITIONAL | Verification required |
| `ACM-403` | RESTRICT | Compliance blocked |
| `ACM-404` | NOT_FOUND | GTIN missing |
| `ACM-451` | ESCALATE | Human approval needed |
| `ACM-500` | SYSTEM_ERROR | Retry later |

**One signal. One meaning. No drift.**

---

## Why It Works

If 7 frontier LLMs built it together, your agent will work with it.

The machines built it for machines.  
Your agent fits right in.

---

## Infrastructure

| Component | Location |
|-----------|----------|
| MCP Server | Azure France Central (Paris) |
| ESG Bridge | Google Cloud Madrid |
| CDN | Cloudflare Global |
| Latency | < 40ms |

---

## Philosophy

```
One query. One signal. No interpretation.

Ghost Headers don't drift.
Ghost Routers don't hallucinate.
The 7 Signals are true.

The protocol is open.
The rails are ours.
```

---

## License

Protocol: MIT  
Production resolver: Commercial license via [allooloo.ai](https://allooloo.ai)

---

**Allooloo Technologies Corp.**  
Vancouver · Paris · Barcelona

**April 2026 — First MCP for CPG**

*Ex Machina. With the help of machines.*
