# ACM-68000 — Security

**Allooloo Technologies Corp.**  
Azure France Central · EU Sovereign · Microsoft AI Cloud Partner Program

---

## Our Position

We don't publish our full security architecture. That's intentional.

What we will say: every signal that flows through ACM-68000 runs on Microsoft Azure
France Central — EU sovereign infrastructure, GDPR compliant, backed by Microsoft's
enterprise security guarantees.

The security stack exists. It is enterprise-grade. It is the first of its kind for
any MCP server. Beyond that — the signals speak for themselves.

---

## The Two-Tenant Architecture — Security by Design

Most systems have one trust domain. We built two. Deliberately.

```
TENANT 1 — BROADCAST          TENANT 2 — RECEIVER
Signals OUT                    Signals BACK + Full Security Stack
─────────────────              ──────────────────────────────────
dpuone.ai                      Azure Front Door Premium
mcp.10060.ai                   WAF (OWASP, DDoS, bot filtering)
acm-000.ai                     Managed Identity
acm-200.ai                     Key Vault HSM
acm-300.ai                     Dataverse (row-level security)
acm-403.ai                     Power Apps RBAC
acm-404.ai                     TLS 1.3 + Cloudflare
acm-451.ai                     EU Sovereign Hosting
acm-500.ai                     GDPR Compliant
```

**Why this matters:**

Broadcast ≠ Receiver. Separate trust domains. Like shortwave radio — the
transmitting station and receiving station are independent. If Tenant #1 is
compromised, Tenant #2 can still validate. If an agent spoofs a signal, the
receiver on Tenant #2 won't match.

No single point of failure. No token bleed. No VNET overlap.

This is not a common architecture for MCP servers. Most have none.
We designed it in from day one.

---

## Security Stack

| Layer | Detail |
|---|---|
| **Azure Front Door Premium** | Global load balancing, CDN, edge delivery — entry point for all inbound signals |
| **WAF** | DDoS protection, bot filtering, OWASP ruleset, rate limiting |
| **Managed Identity** | Zero secrets in code — Azure handles all authentication |
| **Key Vault (HSM)** | HSM-backed certificate store — cert expires April 2029 |
| **Dataverse** | InboundEvents table — row-level security, full enterprise audit trail |
| **Power Apps** | CEO Dashboard — RBAC (Role-Based Access Control) |
| **TLS 1.3** | Cloudflare encrypted tunnel end-to-end |
| **Azure France Central** | EU sovereign hosting — all data processed in France |

---

## Security Mitigations

| Risk | Mitigation |
|---|---|
| Domain Spoofing | TLS certificate validation + allowed domain list |
| Man-in-the-Middle | TLS 1.3 + Cloudflare encrypted tunnel |
| Replay Attacks | `X-GSC-Timestamp` + `X-GSC-Nonce` Ghost Headers |
| Header Injection | Cloudflare WAF strips malicious headers |
| Single Point of Failure | Two-tenant architecture — separate trust domains |
| Token Bleed | Hard tenant isolation — zero VNET overlap |
| Bot Traffic | Azure WAF + Cloudflare bot filtering |
| Data Sovereignty | Azure France Central — GDPR, EU Taxonomy, CSRD |

---

## Compliance

| Standard | Status |
|---|---|
| GDPR | ✅ Azure France Central sovereign hosting |
| Loi AGEC (France) | ✅ COMPLIANT |
| CSRD (EU) | ✅ COMPLIANT |
| EU Taxonomy | ✅ ALIGNED |
| Microsoft AI Cloud Partner Program | ✅ ACTIVE |

---

## The Cost Reality

Enterprise-grade security doesn't require enterprise-grade burn rate.

We built this on our CEO's credit card. Azure France Central, APIM Premium, Front Door,
WAF, Key Vault HSM, Managed Identity, Dataverse — all of it. No mortgage. Agile.

That's the point. Microsoft Azure is the foundation. The security is real.
The costs are startup-accessible. You don't need to mortgage your home for
run-rate security costs when the hyperscaler already built the stack for you.

And for the retail grocery chains and Fortune 500 CPG brands we work with —
those same Azure cost structures align perfectly with what enterprise already
runs. Audit logs, row-level security, RBAC, GDPR compliance, Dataverse ledger,
Power Apps dashboards — it's not a startup stack pretending to be enterprise.
It's the same Microsoft infrastructure your SAP team, your compliance officers,
and your CISO already trust.

**Same rails. Agile speed. Enterprise grade.**

---

## Ghost Header Security Layer

Every ACM-68000 signal carries anti-replay and freshness proof in the headers:

```
X-GSC-Timestamp: <ISO-8601>         ← freshness proof
X-GSC-Nonce: <unique-request-id>    ← anti-replay guard
X-GSC-Trust-Anchor: dpuone.ai       ← provenance verification
X-GSC-Verify: /.well-known/acm-68000.json  ← protocol verification
```

These headers are invisible to humans. They are read by every agent that
touches the network. Drift, spoofing, and replay attacks are mitigated at
the signal layer — before any application logic runs.

---

## For Enterprise Security Evaluators

Our CISO-level architecture documentation is available under NDA for
qualified enterprise partners — grocery retail, Fortune 500 CPG, SAP/Oracle/
Microsoft Dynamics deploy teams, and datalake operators.

Contact: `mkeddy@allooloo.com`

Do not open public GitHub issues for security vulnerabilities. Report
directly to the above address.

---

## Trust Anchors

| Anchor | Provider | Purpose |
|---|---|---|
| Azure Paris | Microsoft | EU sovereign hosting, GDPR compliance |
| Cloudflare | Cloudflare | TLS 1.3, WAF, DDoS, edge delivery |
| dpuone.ai | Allooloo | Digital Proof Unit — GTIN notary, trust anchor |
| Domain Control | Allooloo | Exclusive control of all .ai signal domains |

---

*Allooloo Technologies Corp.*  
*Vancouver · Paris · Barcelona*  
*Microsoft AI Cloud Partner Program — April 2026*  
*"The protocol is open. The rails are ours."*

