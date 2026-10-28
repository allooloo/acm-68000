# ACM-68000 — the seven canonical signals

Reference site: **https://acm-68000.org/** — this repository is the signal protocol as a document. Operator: Allooloo Technologies Corp. Licence: MIT (see `LICENSE`).

**State determines behavior.** ACM-68000 is the base deterministic execution vocabulary for agentic commerce: seven states, fixed meanings, no scoring, ranking or narrative interpretation. An agent does not need to infer what a state means. The number is the contract.

## The seven signals

| Signal | State | Action | Page |
|---|---|---|---|
| ACM-000 | NOT_APPLICABLE | No action required. | https://acm-000.org/ |
| ACM-200 | ALLOW | Execute the transaction. | https://acm-200.org/ |
| ACM-300 | CONDITIONAL | Evaluate before proceeding. | https://acm-300.org/ |
| ACM-403 | RESTRICT | Halt transaction. | https://acm-403.org/ |
| ACM-404 | NOT_FOUND | Abort transaction. | https://acm-404.org/ |
| ACM-451 | ESCALATE | Human-in-the-loop required. | https://acm-451.org/ |
| ACM-500 | SYSTEM_ERROR | Retry or fallback. | https://acm-500.org/ |

## Rules of the vocabulary

1. **Append-only.** A code, once published, keeps its meaning forever. New codes may be added; none is renamed, renumbered or removed.
2. **Non-breaking.** An agent written against today's seven keeps working against every later version.
3. **Non-substitutable.** A code is never reused for a different state, and a state is never carried by a different code.
4. **Deterministic.** The same inputs give the same signal. A signal carries a state, not an opinion.
5. **Domain profiles apply, never redefine.** A domain — for example the issuer states on the Electronic Compliance Object pages (fr-eco.ai, de-eco.ai …) — maps its own conditions onto these seven; it never changes what a code means.

## Where the signals are served

- Listed issuers: `get_signal` at **https://mcp.getissuer.ai/mcp** (the Allooloo door; one signed record per listed company, served from the issuer's own country) and on every market's Electronic Compliance Object page.
- The jurisdiction layer the signals pair with: **https://sm-eco-10060.org/** (github.com/allooloo/sm-eco-10060).
- Receipts for decisions cleared: **https://rco-a2a.ai/**.

## Files

- `signals.json` — the seven signals: code, state, action, page.
- `schema/signal.schema.json` — the signal record's schema.
