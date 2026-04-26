# ACM-68000
### The Deterministic Signal Protocol for Agentic Commerce

**Operator:** Allooloo Technologies Corp.  
**Version:** 1.2 · **Status:** LIVE  
**License:** MIT (protocol spec) · Commercial license required for production resolver access  
**Resolver:** [resolver.aio-resolver.com](https://resolver.aio-resolver.com)  
**Protocol reference:** [allooloo.ai](https://www.allooloo.ai)

---

## What It Is

ACM-68000 is a machine-executable eligibility protocol. It issues deterministic terminal signals for SKU orderability — enabling AI procurement agents and enterprise ERP systems to execute commercial actions without interpreting ESG, regulatory, or sourcing rules themselves.

One query. One resolved state. No interpretation required.

---

## Signal Vocabulary

| Signal | State | Meaning |
|--------|-------|---------|
| ACM-200 | ALLOW | Agent may execute the commercial action |
| ACM-300 | CONDITIONAL | Execution permitted only if required conditions are satisfied |
| ACM-403 | RESTRICT | Action blocked under current policy or compliance conditions |
| ACM-404 | NOT_FOUND | Referenced object or identifier could not be resolved |
| ACM-451 | ESCALATE | Human review required before execution |
| ACM-500 | SYSTEM_ERROR | Resolver infrastructure could not produce a valid execution state |
| ACM-000 | NOT_APPLICABLE | Signal does not govern the evaluated object or context |

---

## Query the Resolver

```bash
# Query by GTIN
curl "https://resolver.aio-resolver.com/resolve?gtin=00990832300006&jurisdiction=EU"

# Query by SKU
curl "https://resolver.aio-resolver.com/resolve?sku=ZTPL-D"

# Protocol metadata
curl "https://resolver.aio-resolver.com/protocol"
```

**Response:**
```json
{
  "protocol"    : "ACM-68000",
  "version"     : "1.2",
  "object_id"   : "GTIN:00990832300006",
  "jurisdiction": "EU",
  "acm_signal"  : "ACM-200",
  "state"       : "ALLOW",
  "timestamp"   : "2026-03-14T00:00:00Z",
  "resolver"    : "RCO-10060",
  "dpu_uri"     : "dpu://eco-10060.org/es/2026-03-14/43777"
}
```

---

## Agent Bootstrap Discovery

Place `agent.json` at your root domain so procurement agents can discover your resolver automatically:

```json
{
  "protocol"   : "ACM-68000",
  "version"    : "1.2",
  "resolver"   : "https://resolver.aio-resolver.com/protocol",
  "license"    : "MIT",
  "commercial" : "https://allooloo.ai/license",
  "operator"   : "Allooloo Technologies Corp."
}
```

---

## Infrastructure

| | |
|---|---|
| Resolver | resolver.aio-resolver.com |
| Latency | Sub-40ms |
| Region | Azure France Central · Paris |
| Compute | Microsoft Azure · AWS · Google Cloud · Cloudflare |
| Governance | Standard-10060 |
| Auth required | None (open protocol layer) |

---

## Governance

| | |
|---|---|
| Maintainer | Allooloo Technologies Corp. |
| Protocol | ACM-68000 — AI Commerce Mechanism 68000 |
| Signal Layer | Agentic Hyperscaler Signals (AHS) |
| Governance Framework | Standard-10060 |
| Versioning | Semantic · append-only · non-breaking |

---

## License

<!-- SPDX-License-Identifier: MIT -->

The ACM-68000 protocol specification is open under the **MIT License**.  
Production resolver access requires a commercial license. See [allooloo.ai/license](https://www.allooloo.ai/license).

---

## First Live Deployment

The AIO-TFX Rail — the non-lignocellulosic hygiene vertical execution rail — is the first live deployment on the ACM-68000 signal cluster, operational for **GreenCore Solutions Corp.**

- **Signal:** ACM-200 ALLOW · clean execution confirmed
- **ERP:** SAP ECC 6.0 confirmed
- **Live jurisdictions:** ES · EU · MX · CR · DO

---

*Allooloo Technologies Corp. · Vancouver · Paris · Barcelona*  
*[allooloo.ai](https://www.allooloo.ai) · [licensing@allooloo.ai](mailto:licensing@allooloo.ai)*
