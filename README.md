# ACM-68000 — the seven canonical signals

**State determines behavior.** ACM-68000 is the base deterministic execution vocabulary for agentic commerce: seven states, fixed meanings, no scoring, ranking or narrative interpretation. An agent does not need to infer what a state means. The number is the contract.

Reference site: **https://acm-68000.org/** (Agentic KG Holdings, reference operator). Licence: MIT (see `LICENSE`).

## The seven signals

| Signal | State | Action |
|---|---|---|
| ACM-000 | NOT_APPLICABLE | No action required. |
| ACM-200 | ALLOW | Execute the transaction. |
| ACM-300 | CONDITIONAL | Evaluate before proceeding. |
| ACM-403 | RESTRICT | Halt transaction. |
| ACM-404 | NOT_FOUND | Abort transaction. |
| ACM-451 | ESCALATE | Human-in-the-loop required. |
| ACM-500 | SYSTEM_ERROR | Retry or fallback. |

## Rules of the vocabulary

1. **Append-only.** A code, once published, keeps its meaning forever. New codes may be added; none is renamed, renumbered or removed.
2. **Non-breaking.** An agent written against today's seven keeps working against every later version.
3. **Non-substitutable.** A code is never reused for a different state, and a state is never carried by a different code.
4. **Deterministic.** The same inputs give the same signal. A signal carries a state, not an opinion.
5. **Domain profiles apply, never redefine.** A domain (for example CPG-68000 for consumer packaged goods, or the issuer states on the Electronic Compliance Object pages) maps its situations onto these seven meanings; it does not change them.

## Machine form

The signals of record, with their per-signal hosts, are served at https://acm-68000.org/signals.json. Every implementation names the code and the state together, for example:

```json
{ "signal": "ACM-404", "state": "NOT_FOUND" }
```

## Implemented by

- GreenCore Solutions Corp. — hubs (A2A Grocery, A2A Cosmetics, A2A Peptides) and gtinfetch.ai, under the CPG-68000 profile.
- Allooloo Technologies Corp. — the Capital Markets Knowledge Graph nodes and the Electronic Compliance Object pages (https://allooloo.ai/markets): ACM-200 trading · ACM-403 halted · ACM-404 not on the register · ACM-451 read the filing.

© 2026 Agentic KG Holdings · MIT licence. This repository restores the URL https://allooloo.github.io/acm-68000/ cited in the March 25 2026 release; the reference site is https://acm-68000.org/.
