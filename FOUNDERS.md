# ACM-68000 — Founder's Document

**Allooloo Technologies Corp.**  
Version 1.1 — April 2026  
Operating Design Reference & White Paper

*First Enterprise-Grade MCP with Security Stack*

---

## 1. Thesis

Large Language Models on hyperscaler fabric have known drift. The web they navigate is 90% synthetic content and 51% bot traffic. Traditional agent-to-agent communication requires interpretation — a liability when instruments are unreliable and the environment is hostile.

ACM-68000 solves this by applying the same principles mariners used for millennia: fixed trusted anchors for triangulation against drift, and counterparty verification to confirm signals arrived intact.

### The Navigation Metaphor

In celestial navigation, you don't trust the ocean — it moves, it lies, it kills. You trust fixed points in the sky that have been there for millennia. Sailors could cross oceans because Polaris doesn't move.

In shortwave radio and cryptography, you need counterparties — known trusted stations with verified call signs. A signal isn't valid until the receiver confirms it.

ACM-68000 combines both: fixed infrastructure anchors (two geographically separate Azure tenants) that LLMs can triangulate against, plus a receiver station that confirms every signal. The result is deterministic commerce execution in <40ms, with zero interpretation required.

### Two Byproducts

1. **Trust anchoring for drifting LLMs** — External fixed points that agents can triangulate against, preventing hallucination and confabulation in commerce decisions.
2. **Elevation above the noise floor** — Business-critical signals travel via Ghost Headers, invisible to the garbage web, elevated above the layer where 90% of content is synthetic and 51% of traffic is automated.

---

## 2. Problem Statement

### The Three Failures

| Failure | Description |
|---|---|
| **Hyperscaler Drift** | LLMs on cloud fabric hallucinate, lose context, confabulate. The instruments are unreliable. You cannot trust an agent's reasoning for commerce decisions. |
| **Hostile Web** | 90% of web content is now synthetic. 51% of traffic is automated bots. Agents navigating this environment are interpreting garbage. Interpretation is a liability. |
| **No Counterparty** | Traditional A2A has no verification. Agents discuss purchases, reason about intent. There's no receiver station confirming the signal arrived. No proof of transmission. |

### Traditional A2A vs. ACM-68000

| Traditional A2A | ACM-68000 |
|---|---|
| Agent discusses purchase | Agent issues machine-executable signal |
| LLM reasons about intent | Keyword-to-schema mapping (<40ms) |
| Variable text response | Fixed 7-signal vocabulary |
| Requires interpretation | Pipes directly to ERP/Dataverse |
| No audit trail | Every signal logged in InboundEvents |
| Hope-based execution | CEO dashboard visibility |

---

## 3. The Solution: Two Tenants, One Loop

### Infrastructure Overview

| Tenant | Role | Key URLs |
|---|---|---|
| **#1 — Broadcast** | Signals OUT | `dpuone.ai`, `mcp.10060.ai`, `acm-000.ai` → `acm-500.ai` |
| **#2 — Receiver** | Signals BACK | `7signalingress.ai`, `aio-router.ai`, `7signalrefinery.ai` |

### Tenant #1 — Signal Source / Broadcast

**Resource Group:** `rg-waypoint-10060-fr`  
**Region:** Azure France Central (EU sovereign)

| Host | Role |
|---|---|
| `dpuone.ai` | Digital Proof Unit — GTIN origin, jurisdiction verification |
| `mcp.10060.ai` | MCP Server — first CPG MCP in official registry |
| `acm-000.ai` → `acm-500.ai` | The 7 Signal nodes |

### Tenant #2 — Receiver + Security Stack

**Resource Group:** `rg-7signalfoundry-fr`  
**Program:** Microsoft AI Partner Program

| Host | Role |
|---|---|
| `7signalfoundry.ai` | Forges signal infrastructure |
| `7signalingress.ai` | Receives agent POST-backs (/ingest endpoint) |
| `aio-router.ai` | CEO Dashboard — real-time signal visibility |
| `7signalrefinery.ai` | Enterprise signal processing |
| `7signalrefinery.org` | MIT Protocol specification |
| `7signalstack.ai` | Protocol standard documentation |

### Why Two Tenants?

Broadcast ≠ Receiver. Separate trust domains. Like shortwave radio: the transmitting station and receiving station are independent. If Tenant #1 is compromised, Tenant #2 can still validate. If an agent spoofs a signal, the receiver on Tenant #2 won't match. No single point of failure.

---

## 4. The 7 Signals

Every commerce decision resolves to exactly one of seven deterministic states. No interpretation. No reasoning. Just execution.

| Signal | Domain | State | Meaning | Color |
|---|---|---|---|---|
| ACM-000 | `x-000.ai` | NOT_APPLICABLE | Idle / No state | `#888888` |
| ACM-200 | `x-200.ai` | ALLOW | Execute transaction | `#1D9E75` |
| ACM-300 | `x-300.ai` | CONDITIONAL | Verify / Audit required | `#EF9F27` |
| ACM-403 | `x-403.ai` | RESTRICT | Blocked | `#E24B4A` |
| ACM-404 | `x-404.ai` | NOT_FOUND | Product missing | `#444444` |
| ACM-451 | `x-451.ai` | ESCALATE | Human in the loop | `#E24B4A` |
| ACM-500 | `x-500.ai` | SYSTEM_ERROR | Retry later | `#7F77DD` |

**One signal. One meaning. No drift.**

### Why 7 Signals?

- **Minimal** — Covers all possible agentic commerce outcomes
- **Universal** — Maps to HTTP status codes developers already understand
- **Deterministic** — No ambiguity, no interpretation required
- **Cacheable** — Can be cached at edge indefinitely
- **Machine-readable** — HTTP headers, not prose

---

## 5. Agentic Ghost Headers

HTTP response headers that every ACM-68000 node returns. Called "Ghost" because they are invisible to humans (not rendered in browsers) and instantly readable by AI agents (programmatic header access).

### The Complete Header Set

| Header | Value / Purpose |
|---|---|
| `X-GSC-Protocol` | `ACM-68000` |
| `X-GSC-Signal` | `ACM-200` (current state) |
| `X-GSC-State` | `ALLOW` (human-readable state) |
| `X-GSC-Router` | `aio-router.ai` |
| `X-GSC-Stack` | `7SignalStack` |
| `X-GSC-Operator` | `Allooloo Technologies Corp.` |
| `X-GSC-Node` | `<node-identifier>` |
| `X-GSC-Version` | `1.2.1` |
| `X-GSC-Registry` | `io.github.allooloo/acm-68000-mcp` |
| `X-GSC-Inbound` | `https://7signalingress.ai/ingest` (return address) |
| `X-GSC-Trust-Anchor` | `dpuone.ai` |
| `X-GSC-Verify` | `/.well-known/acm-68000.json` |
| `X-GSC-Timestamp` | `<ISO-8601>` (freshness) |
| `X-GSC-Nonce` | `<unique-request-id>` (anti-replay) |
| `X-MCP-Server` | `https://mcp.10060.ai` |
| `X-MCP-Registry` | `io.github.allooloo/acm-68000-mcp` |
| `X-Agent-Access` | `Claude,Mistral,Gemini,Grok,OpenAI` |

---

## 6. Signal Round Trip

### Outbound — Signals OUT (Tenant #1)

```
Agent → mcp.10060.ai → dpuone.ai → Returns 1 of 7 signals + Ghost Headers + X-GSC-Inbound return address
```

The broadcast tenant sends deterministic signals. Every response includes the return beacon (`X-GSC-Inbound`) pointing to Tenant #2.

### Inbound — Signals BACK (Tenant #2)

```
Agent POSTs to https://7signalingress.ai/ingest
  → Azure Front Door
  → WAF
  → Logic App (ingest-signal)
  → Dataverse (InboundEvents)
  → aio-router.ai (CEO Dashboard)
```

### The Receiver Station — Technical Flow

| Step | Action |
|---|---|
| **1. INPUT** | AI Agent sends: "Need 4 pallets diapers Madrid" |
| **2. PARSE** | Parser extracts: `cluster=HYGIENE`, `qty=4`, `region=ES-MAD`, `gtin=null` |
| **3. RESOLVE** | Signal resolver → ACM-300 (CONDITIONAL) — GTIN missing |
| **4. WRITE** | OData client POSTs to Dataverse (`cr1e4_inboundeventses` table) |
| **5. DISPLAY** | CEO sees signal in Power Apps dashboard with colour coding |

The signal lands in the CEO dashboard before a traditional A2A system would finish its first reasoning step. Target latency: **<40ms total**.

---

## 7. MCP Server — seven-signal-foundry

The `seven-signal-foundry` MCP server is the agent-facing entry point into the 7SignalStack. It exposes the full signal infrastructure as callable tools via JSON-RPC 2.0 over Server-Sent Events.

**Endpoint:** `https://apim-ghost-signal.azure-api.net/seven-signal-foundry/mcp`  
**Public endpoint:** `https://mcp.10060.ai`  
**Registry:** `io.github.allooloo/acm-68000-mcp`  
**Transport:** JSON-RPC 2.0 / SSE  
**Infrastructure:** Azure APIM Premium — France Central

### 12 Tools

| Tool | Method | What It Does |
|---|---|---|
| `listSignals` | GET `/signals` | Returns all 7 ACM signals + domains |
| `getInbound` | GET `/inbound` | Ingress URL + full payload schema |
| `ingestSignal` | POST `/` | Send signal → Logic App → Dataverse |
| `resolveGtin` | GET `/resolve/{gtin}` | GTIN → ACM signal + compliance |
| `getHealth` | GET `/health` | Live system status + signal integrity |
| `getDpu` | GET `/dpu` | Digital Proof Unit — GTIN notary (Paris) |
| `getEsgReport` | GET `/esg` | ESG compliance — CSRD, Loi AGEC, EU Taxonomy |
| `getNodes` | GET `/nodes` | 18 jurisdiction nodes status |
| `getGoogleBridge` | GET `/bridge/google` | Google Cloud Madrid ESG bridge |
| `getResolver` | GET `/resolver` | AI-native signal resolver |
| `getCarbon` | GET `/carbon` | Carbon-aware compute metrics |
| `getMcp` | GET `/` | Root MCP manifest |

### Signal Payload Schema (16 fields)

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

### Connect Your Agent

**Claude Desktop** — add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "acm-68000": {
      "url": "https://mcp.10060.ai"
    }
  }
}
```

**Claude Project** — add MCP connector:

```
URL:  https://apim-ghost-signal.azure-api.net/seven-signal-foundry/mcp
Auth: Ocp-Apim-Subscription-Key header
```

**curl — tools/list handshake:**

```bash
curl -X POST https://apim-ghost-signal.azure-api.net/seven-signal-foundry/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/list","id":1}'
```

---

## 8. Security Stack — First Ever for MCP

All security infrastructure is deployed on Tenant #2 (the receiver). This is the first MCP server with enterprise-grade security.

| Layer | Function |
|---|---|
| **Azure Front Door Premium** | Global load balancing, CDN, edge delivery, entry point for all inbound signals |
| **WAF** | DDoS protection, bot filtering, OWASP ruleset, rate limiting |
| **Managed Identity** | No secrets in code — Azure handles authentication |
| **Key Vault (HSM)** | `kv-ghost-signal` — HSM-backed, cert expires April 2029 |
| **Dataverse** | InboundEvents table, row-level security, enterprise audit trail |
| **Power Apps** | CEO Dashboard at `aio-router.ai`, RBAC |

### Trust Model

| Anchor | Provider | Purpose |
|---|---|---|
| **Azure Paris** | Microsoft | EU sovereign hosting, GDPR compliance |
| **Cloudflare** | Cloudflare | TLS 1.3, WAF, DDoS protection, edge delivery |
| **Domain Control** | Allooloo | Exclusive control of all `.ai` signal domains |

### Security Mitigations

| Risk | Mitigation |
|---|---|
| Domain Spoofing | TLS certificate validation + allowed domain list |
| Man-in-the-Middle | TLS 1.3 + Cloudflare encrypted tunnel |
| Replay Attacks | `X-GSC-Timestamp` + `X-GSC-Nonce` |
| Header Injection | Cloudflare WAF strips malicious headers |

---

## 9. Compliance

| Standard | Status |
|---|---|
| Loi AGEC (France) | ✅ COMPLIANT |
| CSRD (EU) | ✅ COMPLIANT |
| GDPR | ✅ Azure France Central sovereign hosting |
| EU Taxonomy | ✅ ALIGNED |
| EUDR | NOT_APPLICABLE (current product set) |

### Live Registered Products

| GTIN | Product | Signal | Certifications |
|---|---|---|---|
| `00990832300006` | TreeFree Core econoLiite 240 (Tape) | ACM-200 ALLOW | SGS France 52583 |
| `00990832300013` | TreeFree Core Culotte 240 (Pant) | ACM-200 ALLOW | SGS France 51912 |

---

## 10. Complete URL Reference

### Tenant #1 — Broadcast Infrastructure

| URL | Role |
|---|---|
| `dpuone.ai` | Digital Proof Unit — GTIN origin, jurisdiction verification |
| `mcp.10060.ai` | MCP Server — first CPG MCP in official registry |
| `acm-000.ai` | NOT_APPLICABLE signal node |
| `acm-200.ai` | ALLOW signal node |
| `acm-300.ai` | CONDITIONAL signal node |
| `acm-403.ai` | RESTRICT signal node |
| `acm-404.ai` | NOT_FOUND signal node |
| `acm-451.ai` | ESCALATE signal node |
| `acm-500.ai` | SYSTEM_ERROR signal node |

### Tenant #2 — Receiver Infrastructure

| URL | Role |
|---|---|
| `7signalfoundry.ai` | Forges signal infrastructure |
| `7signalingress.ai` | Receives agent POST-backs (/ingest endpoint) |
| `aio-router.ai` | CEO Dashboard — real-time signal visibility |
| `7signalrefinery.ai` | Enterprise signal processing |
| `7signalrefinery.org` | MIT Protocol specification |
| `7signalstack.ai` | Protocol standard documentation |

### Signal Flow Order

```
7signalfoundry.ai → 7signalingress.ai → aio-router.ai → 7signalrefinery.ai → 7signalrefinery.org → 7signalstack.ai
```

### X-GS* Namespace (22 Domains)

| Header | Domain | Purpose |
|---|---|---|
| `X-GSC-*` | `x-gsc.ai` | Ghost Signal Commerce (outbound) |
| `X-GSI-*` | `x-gsi.ai` | Ghost Signal Ingress (catcher) |
| `X-GSR-*` | `x-gsr.ai` | Ghost Signal Receiver (router) |
| `X-GSX-*` | `x-gsx.ai` | Ghost Signal Finance |
| `X-GSH-*` | `x-gsh.ai` | Ghost Signal Network Health |
| `X-GSG-*` | `x-gsg.ai` | Ghost Signal Government lane |
| `X-GSE-*` | `x-gse.ai` | Ghost Signal Education lane |
| `X-FAF-*` | `x-faf.ai` | Fast As Fuck labs |
| `X-MCP-*` | `x-mcp.ai` | MCP integration |
| `X-UCP-*` | `x-ucp.ai` | Universal Commerce Protocol |
| `X-ADM-*` | `x-adm.ai` | Admin dashboard |
| `X-DEV-*` | `x-dev.ai` | DevOps authority |
| `X-SMS-*` | `x-sms.ai` | Short Message Service |
| `X-DPU-*` | `x-dpu.ai` | Digital Proof Units |
| `X-ERP-*` | `x-erp.ai` | ERP bridge (SAP/Oracle/Dynamics) |

---

## 11. Conclusion

ACM-68000 is the first Model Context Protocol with enterprise-grade security, counterparty verification, and deterministic signal execution. It applies the principles of celestial navigation and shortwave radio to the problem of LLM drift on hyperscaler fabric.

### What Was Built

- **Two-tenant trust architecture** — Broadcast (Tenant #1) and Receiver (Tenant #2) are separate trust domains
- **Fixed trusted anchors** — Like shortwave radio stations with known call signs
- **Counterparty verification** — The receiver station (`7signalingress.ai`) confirms every signal
- **Agentic Ghost Headers** — Invisible to humans, visible to AI agents, machine-readable identity
- **MCP Server** — `seven-signal-foundry`, 12 tools, JSON-RPC 2.0, live on Azure APIM Premium
- **Enterprise security stack** — First MCP with Front Door Premium, WAF, Managed Identity, Dataverse, Power Apps
- **CEO visibility** — Real-time dashboard showing every signal as it lands
- **Claude connected as live agent** — Calling tools directly from this Claude Project

### The Result

Deterministic commerce execution targeted at <40ms. Zero interpretation. Zero reasoning. Signals out from Tenant #1, signals back to Tenant #2. Full loop. First ever for MCP.

### Live Status (April 2026)

```
Stack:          OPERATIONAL
Signal QR:      98.2%
Latency avg:    38ms
Drift:          NONE
Active agents:  Claude, Mistral
Azure Paris:    LIVE
GCP Madrid:     LIVE
Nodes healthy:  18/18
```

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

`github.com/allooloo/acm-68000`  
`mkeddy@allooloo.com`

*April 2026 — First MCP for CPG*  
*Ex Machina. With the help of machines.*

