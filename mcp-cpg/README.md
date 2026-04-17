# ACM-68000 — MCP for CPG

**First MCP for Consumer Packaged Goods**  
`io.github.allooloo/acm-68000-mcp` · Listed April 2, 2026 · Active

---

## Why This Exists

We mapped the globe like Google Maps — 18 jurisdiction nodes — to get speed,
precision of signals, ESG and cost run rates (tokens) down so performance goes up.

Our signals reduce ESG drag. Our speed and secure two-tenant architecture reduces
costs. So that large grocery retailers, CPG brands, and private label manufacturers
can use the new generation of AI and ERP tools — with their human operator teams —
and start clocking results.

Innovation. Not theory.

---

## The Registry Proof

```json
{
  "name": "io.github.allooloo/acm-68000-mcp",
  "title": "ACM-68000 Product Eligibility for AI Agents",
  "description": "ESG compliance, territory clearance, price and availability signals. 18 jurisdiction nodes. First CPG MCP.",
  "version": "1.0.0",
  "status": "active",
  "publishedAt": "2026-04-03",
  "endpoint": "https://mcp.10060.ai"
}
```

First CPG product eligibility checker on the official MCP Registry.
Not a claim. A timestamp.

---

## Product Eligibility — The Signal Hierarchy

When a retail grocery AI agent queries a product, three things need to resolve
in order. Every time. No exceptions.

```
1. ESG / Green Claims
   Is this product compliant in this market?
   Loi AGEC · CSRD · EUDR · EU Taxonomy
   → ACM-403 RESTRICT if it fails
   → ACM-300 CONDITIONAL if verification needed
   → ACM-200 ALLOW if clear

2. Territory Clearance
   Is this product cleared for sale in this jurisdiction?
   18 nodes · FR · DE · UK · ES · IT · NL · CH · PL · EU
   US · CA · MX · BR · JP · KR · SG · IN · AU
   → ACM-404 NOT_FOUND if GTIN not registered
   → ACM-451 ESCALATE if human review needed
   → ACM-200 ALLOW if cleared

3. Price & Availability
   Can this product be procured right now?
   GTIN verified · Stock signal · ERP routing
   → ACM-200 ALLOW → SAP CREATE_PO fires
```

One query. One signal. No interpretation. Under 40ms.

---

## Who This Is For

### Grocery Retail
Carrefour. Tesco. Auchan. Leclerc. Walmart. Rewe. Edeka. Albert Heijn.

Hundreds of thousands of employees. Thousands to hundreds of thousands of SKUs.
Territory-specific ESG requirements. SAP S/4HANA procurement at scale.

The 18 nodes were built for you. Each one resolves compliance for your market
automatically. No legal team. No manual check. One signal per SKU per territory.

### CPG Brands
L'Oréal. Unilever. Nestlé. Danone. P&G.

Your products need ACM-200 ALLOW to get on shelf. The signal confirms ESG
compliance, territory clearance, and procurement eligibility in one call.
Your AI procurement agents already speak this protocol — it's in the weights.

### Private Label Manufacturers
You supply the retail chains. Your SKUs need the same signal clearance as
branded products. Same protocol. Same speed. Same ESG audit trail.

---

## The 18 Jurisdiction Nodes

Built for retail scale. Each node resolves territory-specific compliance,
ESG obligations, and procurement rules for its market.

| Region | Node | Key Regulation |
|---|---|---|
| 🌐 Global | `eu-eco-10060.ai` | EU-wide baseline |
| 🇫🇷 France | `fr-eco-10060.ai` | Loi AGEC, CSRD |
| 🇩🇪 Germany | `de-eco-10060.ai` | LkSG supply chain law |
| 🇬🇧 UK | `uk-eco-10060.ai` | UK ESG reporting |
| 🇪🇸 Spain | `es-eco-10060.ai` | EU Taxonomy |
| 🇮🇹 Italy | `it-eco-10060.ai` | CSRD |
| 🇳🇱 Netherlands | `nl-eco-10060.ai` | CSRD, EU Taxonomy |
| 🇨🇭 Switzerland | `ch-eco-10060.ai` | Swiss ESG |
| 🇵🇱 Poland | `pl-eco-10060.ai` | EU Taxonomy |
| 🇺🇸 USA | `us-eco-10060.ai` | SEC ESG disclosure |
| 🇨🇦 Canada | `ca-eco-10060.ai` | CBAM alignment |
| 🇲🇽 Mexico | `mx-eco-10060.ai` | LATAM compliance |
| 🇧🇷 Brazil | `br-eco-10060.ai` | Brazilian ESG |
| 🇯🇵 Japan | `jp-eco-10060.ai` | TCFD alignment |
| 🇰🇷 South Korea | `kr-eco-10060.ai` | K-ESG |
| 🇸🇬 Singapore | `sg-eco-10060.ai` | MAS ESG |
| 🇮🇳 India | `in-eco-10060.ai` | BRSR reporting |
| 🇦🇺 Australia | `au-eco-10060.ai` | ASRS climate |

---

## The First Live Deployment

**Operator:** GreenCore Solutions Corp.  
**Sector:** Hygiene — Baby Diapers  
**Sovereign node:** `fr-eco-10060.ai` — France  
**Compliance:** Loi AGEC · CSRD · EU Taxonomy · SGS France certified  

| GTIN | Product | Signal |
|---|---|---|
| `00990832300006` | TreeFree Core econoLiite 240 (Tape) | ACM-200 ALLOW |
| `00990832300013` | TreeFree Core Culotte 240 (Pant) | ACM-200 ALLOW |

Both products cleared. ESG verified. Territory confirmed. Ready for Carrefour,
Leclerc, Auchan procurement agents to query and execute.

---

## French Sovereign Commerce — FR-ECO-10060

For operators in France — Hygiene, Beauty and Personal Care:

```bash
# Add this flag to any ingestSignal call
X-MCP-Flag: --fr-eco-10060
```

Activates Mistral sovereign AI context. Loi AGEC, CSRD, GDPR, EU Taxonomy
checked in the signal. Not in a compliance meeting. Not in a legal review.
In the signal. Under 40ms.

---

## ERP Integration — Signals to Action

| Signal | State | SAP S/4HANA | Oracle Fusion | MS Dynamics 365 |
|---|---|---|---|---|
| ACM-000 | NOT_APPLICABLE | NO_ACTION | NO_ACTION | NO_ACTION |
| ACM-200 | ALLOW | CREATE_PO | APPROVE | RELEASE |
| ACM-300 | CONDITIONAL | HOLD_PO | CONDITIONAL_HOLD | HOLD |
| ACM-403 | RESTRICT | BLOCK_PO | REJECT | BLOCK |
| ACM-404 | NOT_FOUND | HOLD_PENDING | HOLD_PENDING | HOLD_PENDING |
| ACM-451 | ESCALATE | ESCALATE_TO_BUYER | MANUAL_REVIEW | ESCALATE |
| ACM-500 | SYSTEM_ERROR | RETRY | RETRY | RETRY |

One signal. Three ERPs. No custom integration. No interpretation.

---

## Why Speed and Cost Matter at Retail Scale

A Carrefour buyer managing 100,000 SKUs across 18 markets cannot run manual
ESG checks. A Tesco AI procurement agent cannot burn 2,000 tokens reasoning
about whether a product is Loi AGEC compliant.

**ACM-68000 reduces:**
- ESG drag — compliance resolved in the signal, not in a meeting
- Token cost — one deterministic signal vs multi-turn agent reasoning
- Integration cost — same signal works across SAP, Oracle, Dynamics
- Legal risk — audit trail in Dataverse, every signal logged

**ACM-68000 increases:**
- Speed — under 40ms per query
- Precision — 7 states, no ambiguity
- Coverage — 18 jurisdiction nodes, global retail mapped
- Confidence — CEO dashboard visibility on every signal

---

## Connect

**MCP Registry:** `io.github.allooloo/acm-68000-mcp`  
**Endpoint:** `https://mcp.10060.ai`  
**GitHub:** `github.com/allooloo/acm-68000`  
**Technical docs:** `mcp-live/README.md`  
**Security:** `security/SECURITY.md`  
**Contact:** `mkeddy@allooloo.com`

---

*Allooloo Technologies Corp.*  
*Vancouver · Paris · Barcelona*  
*April 2026 — First MCP for CPG*  
*"We mapped the globe. Now we run the signals."*

