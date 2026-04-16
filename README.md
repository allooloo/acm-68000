# ACM-68000

**The Protocol for Agentic Commerce**

First CPG Product Eligibility Checker on MCP | Hygiene, Beauty and Personal Care

[![MCP Registry](https://img.shields.io/badge/MCP-io.github.allooloo%2Facm--68000--mcp-028090)](https://registry.modelcontextprotocol.io/?q=io.github.allooloo)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen)](https://mcp.10060.ai)

---

## One Query. One Signal. No Interpretation.

ACM-68000 is an AI-native protocol that enables autonomous agents to make commerce decisions in under 40ms. No parsing PDFs. No interpreting JSON. Just deterministic signals.

```
GTIN 00990832300006 → ACM-200 → ALLOW → Ship it.
```

---

## The 7-Signal Stack

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

## MCP Server

### Live Endpoints

| Endpoint | URL |
|----------|-----|
| MCP Server | `https://mcp.10060.ai` |
| APIM Direct | `https://apim-ghost-signal.azure-api.net/ingest/` |

### 10 Tools Available

| Tool | Description |
|------|-------------|
| `listSignals` | Returns the 7 ACM signals |
| `getInbound` | Ingress URL + payload schema |
| `ingestSignal` | Send signal to Dataverse |
| `resolveGtin` | GTIN → compliance check |
| `getNodes` | 18 jurisdiction nodes |
| `getGoogleBridge` | Google Madrid ESG bridge |
| `getResolver` | AI-Native architecture |
| `getCarbon` | Carbon-aware compute metrics |
| `getHealth` | Agentic health dashboard |
| `getMCP` | Root manifest |

### Quick Start

```bash
# List all signals
curl https://apim-ghost-signal.azure-api.net/ingest/signals

# Check network health
curl https://apim-ghost-signal.azure-api.net/ingest/health

# Send a signal
curl -X POST https://apim-ghost-signal.azure-api.net/ingest/ \
  -H "X-GSC-Protocol: ACM-68000" \
  -H "Content-Type: application/json" \
  -d '{"sender":"your-agent","signal":"ACM-200","message":"test"}'
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     AI AGENTS                                │
│              Claude | Mistral | Grok | Gemini               │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  mcp.10060.ai                               │
│                  MCP Server                                  │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  dpuone.ai                                  │
│           Digital Proof Unit (Trust Anchor)                 │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│             resolver.aio-resolver.com                       │
│              Global Signal Authority                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                aio-tfx-rail.ai                              │
│                 Execution Rail                              │
└─────────────────────────────────────────────────────────────┘
```

### AI-Native Philosophy

> No traditional API. No backend logic. No database queries.
> > LLMs ingest signals directly. The resolver exists.
> > > Agents read it. Resolution happens.
> > >
> > > ---
> > >
> > > ## Global Coverage
> > >
> > > ### 18 Jurisdiction Nodes
> > >
> > > **Europe (9):** EU, FR, DE, UK, ES, IT, NL, CH, PL
> > >
> > > **Americas (4):** US, CA, MX, BR
> > >
> > > **Asia-Pacific (5):** JP, KR, SG, IN, AU
> > >
> > > Each node: `{country}-eco-10060.ai`
> > >
> > > Example: `fr-eco-10060.ai` (France, co-built with Mistral)
> > >
> > > ---
> > >
> > > ## Sustainability
> > >
> > > ### Speed is Sustainability
> > >
> > > | Metric | Traditional | Ghost Headers | Improvement |
> > > |--------|-------------|---------------|-------------|
> > > | Latency | 200-500ms | <40ms | 80% faster |
> > > | CO2/Query | 0.8g | 0.15g | 80% less |
> > > | Energy | Standard cloud | 90% renewable | French nuclear + wind |
> > >
> > > **Carbon Layer:** [aio-carbon.ai](https://aio-carbon.ai)
> > >
> > > ---
> > >
> > > ## First Products
> > >
> > > ### Hygiene, Beauty and Personal Care
> > >
> > > | GTIN | Product | Signal |
> > > |------|---------|--------|
> > > | `00990832300006` | TreeFree Core econoLiite 240 | ACM-200 ALLOW |
> > > | `00990832300013` | TreeFree Core Culotte 240 | ACM-200 ALLOW |
> > >
> > > **Compliance:** CSRD ✓ | Loi AGEC ✓ | EU Taxonomy ✓
> > >
> > > **Certifications:** SGS France 52583, 51912
> > >
> > > **Trust Anchor:** [dpuone.ai](https://dpuone.ai)
> > >
> > > ---
> > >
> > > ## Infrastructure
> > >
> > > | Provider | Region | Role |
> > > |----------|--------|------|
> > > | Azure | France Central (Paris) | MCP Server, Dataverse |
> > > | Google Cloud | europe-southwest1 (Madrid) | ESG Bridge |
> > > | Cloudflare | Global Edge | CDN, Protection |
> > >
> > > ---
> > >
> > > ## Connected Agents
> > >
> > > | Agent | Status |
> > > |-------|--------|
> > > | Claude | ✅ Connected |
> > > | Mistral | ✅ Partner (FR-ECO-10060) |
> > > | Grok | 🔲 Pending |
> > > | Gemini | 🔲 Pending |
> > > | Copilot | 🔲 Pending |
> > >
> > > ---
> > >
> > > ## Links
> > >
> > > | Resource | URL |
> > > |----------|-----|
> > > | MCP Registry | [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/?q=io.github.allooloo) |
> > > | Protocol Site | [allooloo.github.io/acm-68000](https://allooloo.github.io/acm-68000/) |
> > > | Trust Anchor | [dpuone.ai](https://dpuone.ai) |
> > > | Resolver | [resolver.aio-resolver.com](https://resolver.aio-resolver.com) |
> > > | Carbon Layer | [aio-carbon.ai](https://aio-carbon.ai) |
> > > | 7SignalStack | [7signalstack.ai](https://7signalstack.ai) |
> > >
> > > ---
> > >
> > > ## Mission
> > >
> > > ```
> > > 7SignalStack is the deterministic anchor for agentic commerce.
> > >
> > > We trained the web. Now we run the rails.
> > >
> > > Ghost Headers don't drift.
> > > Ghost Routers don't hallucinate.
> > > The 7 Signals are true.
> > >
> > > In an agentic world that drifts by nature,
> > > we are the fixed point.
> > >
> > > Fast. True. Deterministic.
> > > Signs out. Signals in. FaF.
> > > ```
> > >
> > > ---
> > >
> > > ## License
> > >
> > > MIT Licensed — [Allooloo Technologies Corp.](https://allooloo.ai)
> > >
> > > **Vancouver** | **Barcelona** | **Paris**
> > >
> > > ---
> > >
> > > *First CPG Product Eligibility Checker on MCP — April 2026*
