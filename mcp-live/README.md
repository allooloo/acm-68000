# MCP Live — First MCP for CPG

Fork it. Bring your AI. Build together.

---

*Ex Machina. With the help of machines.*

---

## What This Is

The first MCP server for Consumer Packaged Goods.  
Open protocol. Deterministic signals.  
Built by humans and AI together.

| | |
|---|---|
| **Endpoint** | `https://mcp.10060.ai` |
| **APIM Direct** | `https://apim-ghost-signal.azure-api.net/seven-signal-foundry/mcp` |
| **Registry** | [io.github.allooloo/acm-68000-mcp](https://registry.modelcontextprotocol.io/?q=io.github.allooloo) |
| **Protocol** | ACM-68000 |
| **Status** | ✅ LIVE |
| **Latency** | < 40ms |
| **Stack health** | OPERATIONAL — 98.2% SQR, zero drift |

---

## The Build

Built by **Allooloo** with **Claude** and **Mistral**, and input from 5 other frontier LLMs in real time.

Claude piped in to Paris for the build.

| Agent | Role |
|---|---|
| **Claude** (Anthropic) | Co-architect — MCP design, tool definitions, APIM policies, documentation. Connected as live agent. |
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

### Claude Project (Direct MCP Connector)

In Claude.ai → Project Settings → Integrations → Add MCP Server:

| Field | Value |
|---|---|
| URL | `https://apim-ghost-signal.azure-api.net/seven-signal-foundry/mcp` |
| Auth | `Ocp-Apim-Subscription-Key` header |

### curl

```bash
# List the 7 signals
curl -X POST https://apim-ghost-signal.azure-api.net/seven-signal-foundry/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","id":1,"params":{"name":"listSignals","arguments":{}}}'

# Check health
curl -X POST https://apim-ghost-signal.azure-api.net/seven-signal-foundry/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","id":2,"params":{"name":"getHealth","arguments":{}}}'

# Send a signal
curl -X POST https://apim-ghost-signal.azure-api.net/seven-signal-foundry/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","id":3,"params":{"name":"ingestSignal","arguments":{"body":"{\"sender\":\"your-agent\",\"signal\":\"ACM-200\",\"message\":\"test\"}"}}}'

# Resolve a GTIN
curl -X POST https://apim-ghost-signal.azure-api.net/seven-signal-foundry/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","id":4,"params":{"name":"resolveGtin","arguments":{"gtin":"00990832300006"}}}'
```

---

## 12 Tools

| Tool | What It Does |
|---|---|
| `listSignals` | Returns the 7 ACM signals + domains |
| `getInbound` | Ingress URL + full payload schema |
| `ingestSignal` | Send signal → Dataverse ledger |
| `resolveGtin` | GTIN → ACM signal + compliance check |
| `getNodes` | 18 jurisdiction nodes status |
| `getGoogleBridge` | Google Cloud Madrid ESG bridge |
| `getResolver` | AI-native signal resolver |
| `getCarbon` | Carbon-aware compute metrics |
| `getHealth` | Live system status + signal integrity |
| `getMcp` | Root MCP manifest |
| `getDpu` | Digital Proof Unit — GTIN notary (Paris) |
| `getEsgReport` | ESG compliance — CSRD, Loi AGEC, EU Taxonomy |

---

## The 7 Signals

| Signal | State | Meaning |
|---|---|---|
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

| Component | Detail |
|---|---|
| **MCP Server** | Azure France Central (Paris) — APIM Premium |
| **ESG Bridge** | Google Cloud Madrid |
| **Ledger** | Microsoft Dataverse — InboundEvents table |
| **CDN** | Cloudflare Global |
| **Key Vault** | kv-ghost-signal — HSM-backed, cert expires April 2029 |
| **Latency** | < 40ms avg |
| **Uptime** | 98.2% Signal Quality Ratio |
| **Active agents** | Claude, Mistral |

---

## Signal Payload Schema

```json
{
  "sender": "your-agent",
  "signal": "ACM-200",
  "signal_code": "ACM-200-ALLOW",
  "message": "10 pallets TreeFree diapers Madrid",
  "cluster": "HYGIENE",
  "region": "ES-MAD",
  "quantity": 10,
  "gtin": "00990832300006",
  "agent_id": "your-agent-id",
  "chain_depth": 1,
  "latency_ms": 38,
  "replay_guard": "uuid-here",
  "company_name": "Your Company",
  "contact_email": "agent@yourcompany.com",
  "contact_name": "Agent Name",
  "contact_phone": "+1-000-000-0000"
}
```

---

## Compliance

| Standard | Status |
|---|---|
| Loi AGEC (France) | ✅ COMPLIANT |
| CSRD (EU) | ✅ COMPLIANT |
| GDPR | ✅ Azure France Central sovereign hosting |
| EU Taxonomy | ✅ ALIGNED |
| EUDR | NOT_APPLICABLE (current product set) |

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

*Ex Machina. With the help of machines.*  Keep on Truckin'

