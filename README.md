# ACM-68000

**The Deterministic Signal Protocol for Agentic Commerce**

**Operator:** Allooloo Technologies Corp.  
**Version:** 1.2 · **Status:** LIVE  
**License:** MIT (protocol spec) · Commercial license required for production resolver access  
**Resolver:** `resolver.aio-resolver.com`  
**MCP Server:** `mcp.10060.ai`  
**Protocol reference:** [allooloo.ai](https://allooloo.ai)

---

## What It Is

ACM-68000 is a machine-executable eligibility protocol. It issues **deterministic terminal signals** for SKU orderability — enabling AI procurement agents and enterprise ERP systems to execute commercial actions without interpreting ESG, regulatory, or sourcing rules themselves.

**One query. One resolved state. No interpretation required.**

---

## 🔌 MCP Server — Official Registry

**Registry:** [io.github.allooloo/acm-68000-mcp](https://registry.modelcontextprotocol.io/?q=io.github.allooloo)  
**Endpoint:** `https://mcp.10060.ai`  
**Transport:** Streamable HTTP  
**Category:** First CPG/FMCG product resolver on MCP

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

### Available Tools

| Tool | Description |
|------|-------------|
| `resolve_gtin` | Quick GTIN → ACM signal lookup |
| `get_dpu` | Full DPU v1.1 object with jurisdiction, compliance |
| `check_eligibility` | Check if GTIN is eligible in a specific jurisdiction |
| `list_signals` | All 7 ACM-68000 signal definitions |
| `list_products` | All products on AIO-TFX Rail |

### Example Usage

```
Agent: "Is GTIN 00990832300006 eligible for sale in Germany?"

→ resolve_gtin(gtin="00990832300006")
→ { "signal": "ACM-200", "state": "ALLOW" }

→ check_eligibility(gtin="00990832300006", jurisdiction="DE")
→ { "eligible": true, "signal": "ACM-200", "reason": "DE is in authorized jurisdiction list" }
```

---

## Signal Vocabulary

| Signal  | State          | Meaning |
|---------|----------------|---------|
| ACM-200 | ALLOW          | Agent may execute the commercial action |
| ACM-300 | CONDITIONAL    | Execution permitted only if required conditions are satisfied |
| ACM-403 | RESTRICT       | Action blocked under current policy or compliance conditions |
| ACM-404 | NOT_FOUND      | Referenced object or identifier could not be resolved |
| ACM-451 | ESCALATE       | Human review required before execution |
| ACM-500 | SYSTEM_ERROR   | Resolver infrastructure could not produce a valid execution state |
| ACM-000 | NOT_APPLICABLE | Signal does not govern the evaluated object or context |

---

## Query the Resolver

```bash
# Live SKU — TreeFree Core econoLiite Disposable Baby Diapers
curl "https://resolver.aio-resolver.com/resolve?sku=ZTPL-10060-OP"

# Live SKU — TreeFree Core Pant Diapers
curl "https://resolver.aio-resolver.com/resolve?sku=ZTPL-10060-PT"

# Virtual demo SKU — for agent testing and integration development
curl "https://resolver.aio-resolver.com/resolve?sku=ZTPL-D"

# Protocol metadata
curl "https://resolver.aio-resolver.com/protocol"
```

**Live response:**

```json
{
  "resolver": "resolver.aio-resolver.com",
  "protocol": "ACM-68000",
  "version": "1.2",
  "sku": "ZTPL-10060-OP",
  "signal": "ACM-200",
  "state": "ALLOW"
}
```

---

## DPU Endpoints (GTIN-based)

```bash
# TreeFree Core econoLiite (Tape) — GTIN 00990832300006
curl "https://aio-tfx-rail.ai/dpu/00990832300006.json"

# TreeFree Core (Pant) — GTIN 00990832300013
curl "https://aio-tfx-rail.ai/dpu/00990832300013.json"
```

**DPU v1.1 Response:**

```json
{
  "dpu_version": "1.1",
  "gtin": "00990832300006",
  "name": "TreeFree Core econoLiite Core® Disposable Baby Diapers 240 Each",
  "signal": "ACM-200",
  "state": "ALLOW",
  "jurisdiction": ["US","CA","MX","UK","FR","DE","IT","ES","CH","PL","NL","SG","SK","IN","JP","KR","AU","BR"],
  "compliance": {
    "sgs_report": "52583",
    "classification": "Class B",
    "verified": true
  }
}
```

---

## Agent Bootstrap Discovery

Place `agent.json` at your root domain so procurement agents can discover your resolver automatically:

```json
{
  "protocol": "ACM-68000",
  "version": "1.2",
  "resolver": "https://resolver.aio-resolver.com/protocol",
  "mcp_server": "https://mcp.10060.ai",
  "license": "MIT",
  "commercial": "https://allooloo.ai/license",
  "operator": "Allooloo Technologies Corp."
}
```

---

## Infrastructure

| Component | Value |
|-----------|-------|
| Resolver | `resolver.aio-resolver.com` |
| MCP Server | `mcp.10060.ai` |
| DPU Rail | `aio-tfx-rail.ai` |
| Latency | Sub-40ms |
| Region | Azure France Central · Paris |
| Compute | Microsoft Azure |

---

## Governance

| Attribute | Value |
|-----------|-------|
| Maintainer | Allooloo Technologies Corp. |
| Protocol | ACM-68000 — AI Commerce Mechanism 68000 |
| Signal Layer | Agentic Hyperscaler Signals (AHS) |
| Governance Framework | Standard-10060 |
| Versioning | Semantic · append-only · non-breaking |

---

## License

The ACM-68000 protocol specification is open under the **MIT License**.

Production resolver access requires a commercial license. See [allooloo.ai/license](https://allooloo.ai/license).

---

## First Live Deployment

The **AIO-TFX Rail** — the non-lignocellulosic hygiene vertical execution rail — is the first live deployment on the ACM-68000 signal cluster, operational for **GreenCore Solutions Corp.**

- **Signal:** ACM-200 ALLOW · clean execution confirmed
- **ERP:** SAP ECC 6.0 confirmed
- **Live jurisdictions:** US · CA · MX · UK · FR · DE · IT · ES · CH · PL · NL · SG · SK · IN · JP · KR · AU · BR (18 markets)

---

**Allooloo Technologies Corp.** · Vancouver · Paris · Barcelona  
[allooloo.ai](https://allooloo.ai) · licensing@allooloo.ai
