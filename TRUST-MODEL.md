# ACM-68000 Trust Model

## Overview

Agentic Ghost Headers provide deterministic signals for AI commerce decisions. This document defines the **Trust Model** that allows agents to verify header authenticity without cryptographic signatures.

---

## Infrastructure Trust Anchors

The ACM-68000 protocol relies on **infrastructure trust** rather than per-request cryptographic signatures:

| Anchor | Provider | Purpose |
|--------|----------|---------|
| **Azure Paris** | Microsoft | EU sovereign hosting, GDPR compliance |
| **Cloudflare** | Cloudflare | TLS 1.3, WAF, DDoS protection, edge delivery |
| **Domain Control** | Allooloo | Exclusive control of all .ai signal domains |

---

## Verification Headers (Phase 2)

### New Headers

```
X-GSC-Timestamp: Mon, 06 Apr 2026 12:00:00 GMT
X-GSC-Nonce: unique-request-id
X-GSC-Trust-Anchor: dpuone.ai
X-GSC-Verify: /.well-known/acm-68000.json
```

### Header Definitions

| Header | Purpose |
|--------|---------|
| `X-GSC-Timestamp` | Server timestamp for freshness verification |
| `X-GSC-Nonce` | Unique request ID to prevent replay attacks |
| `X-GSC-Trust-Anchor` | Points to DPU for cross-verification |
| `X-GSC-Verify` | Path to verification endpoint |

---

## Verification Endpoint

All ACM-68000 nodes expose:

```
/.well-known/acm-68000.json
```

This RFC 8615 compliant endpoint returns:

- Protocol version
- - Operator identity
  - - Trust anchors
    - - Allowed domains list
      - - Signal definitions
        - - Verification steps
         
          - ---

          ## Agent Verification Flow

          ```
          1. Agent hits acm-200.ai
          2. Check TLS certificate is valid ✓
          3. Verify domain is in allowed_domains ✓
          4. Confirm X-GSC-Protocol = "ACM-68000" ✓
          5. Read X-GSC-Signal for state ✓
          6. Optional: Cross-check with MCP Registry ✓
          7. Execute based on signal
          ```

          ---

          ## Allowed Domains

          Only these domains are authorized ACM-68000 signal sources:

          ### Signal Nodes
          - `acm-000.ai` — NOT_APPLICABLE
          - - `acm-200.ai` — ALLOW
            - - `acm-300.ai` — CONDITIONAL
              - - `acm-403.ai` — RESTRICT
                - - `acm-404.ai` — NOT_FOUND
                  - - `acm-451.ai` — ESCALATE
                    - - `acm-500.ai` — SYSTEM_ERROR
                     
                      - ### Infrastructure
                      - - `gsc-em.com` — GreenCore Solutions
                        - - `mcp.10060.ai` — MCP Server
                          - - `dpuone.ai` — Digital Proof Unit
                            - - `aio-tfx-rail.ai` — AIO Rail
                              - - `resolver.aio-resolver.com` — Global Resolver
                                - - `10060.ai` — Core infrastructure
                                  - - `allooloo.ai` — Allooloo Technologies
                                    - - `sri-10060.ai` — SRI Resolver
                                     
                                      - ---

                                      ## Security Mitigations

                                      ### Spoofing Prevention

                                      | Risk | Mitigation |
                                      |------|------------|
                                      | **Domain Spoofing** | TLS certificate validation + allowed domain list |
                                      | **Man-in-the-Middle** | TLS 1.3 + Cloudflare encrypted tunnel |
                                      | **Replay Attacks** | X-GSC-Timestamp + X-GSC-Nonce |
                                      | **Header Injection** | Cloudflare WAF strips malicious headers |

                                      ### High-Value Transaction Protection

                                      For transactions above threshold, agents should:

                                      1. Verify signal with multiple nodes
                                      2. 2. Cross-check with MCP Registry
                                         3. 3. If `ACM-451` (ESCALATE), require human approval
                                           
                                            4. ---
                                           
                                            5. ## Trust Levels
                                           
                                            6. | Level | Description | Action |
                                            7. |-------|-------------|--------|
                                            8. | **Full Trust** | Valid TLS + Known domain + Correct protocol | Execute immediately |
                                            9. | **Partial Trust** | Valid TLS + Unknown domain | Cross-verify with MCP |
                                            10. | **No Trust** | Invalid TLS or suspicious headers | Reject, log, alert |
                                           
                                            11. ---
                                           
                                            12. ## Why Not Cryptographic Signatures?
                                           
                                            13. 1. **Latency** — Signing adds 5-10ms per request
                                                2. 2. **Complexity** — Key management across 7+ nodes
                                                   3. 3. **Infrastructure Already Trusted** — Azure + Cloudflare provide equivalent security
                                                      4. 4. **Cache-Friendly** — Unsigned headers cache at edge indefinitely
                                                        
                                                         5. ---
                                                        
                                                         6. ## Future: Optional JWT Signing
                                                        
                                                         7. For enterprise deployments requiring cryptographic proof:
                                                        
                                                         8. ```json
                                                            {
                                                              "X-GSC-JWT": "eyJhbGciOiJFUzI1NiIs..."
                                                            }
                                                            ```

                                                            This signed JWT would contain:
                                                            - All Ghost Header values
                                                            - - Timestamp
                                                              - - Signature from DPU private key
                                                               
                                                                - Agents verify against public key at:
                                                                - ```
                                                                  https://dpuone.ai/.well-known/jwks.json
                                                                  ```

                                                                  ---

                                                                  ## Conclusion

                                                                  The ACM-68000 Trust Model provides:

                                                                  - **Infrastructure-grade security** via Azure + Cloudflare
                                                                  - - **Domain verification** via allowed list
                                                                    - - **Freshness** via timestamp headers
                                                                      - - **Cross-verification** via MCP Registry
                                                                       
                                                                        - This is sufficient for autonomous agent commerce at scale.
                                                                       
                                                                        - ---

                                                                        ## License

                                                                        MIT Licensed — Allooloo Technologies Corp.

                                                                        **github.com/allooloo/acm-68000**
