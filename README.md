# ACM-68000

**ACM-68000 defines the clearance rule reference and signal vocabulary for listed issuers' records. Its rule register binds every rule_version used in a receipt to an immutable revision of a duty, its jurisdiction, legal reference, sources and effective dates. Each family publishes how its evidence-backed outcomes map to the clearance signals for a specified read or action. The producing node signs rule and outcome records under the ECO-10060 contract; the RCO door separately signs the receipt of the cleared read. ACM makes the governing revision and the meaning of clearance recoverable, and keeps three distinctions: lookup is not permission, missing evidence is not a negative finding, and system failure is not a resolved restriction.**

Reference site: **https://acm-68000.org/** — canonical text v1.0 (30 October 2026).

## The contract

ACM-68000 defines the clearance rule reference and the signal vocabulary used when an artificial-intelligence (AI) agent reads or acts on a listed issuer's record. It makes a clearance outcome interpretable: which duty applied, in which jurisdiction, under which revision, on what evidence and within what scope. Its central object is the rule register. Every rule_version value written into a receipt resolves to an immutable revision of that register.

A rule family names a duty. A registered revision identifies the particular statement of that duty, and its clearance bindings, that governed the read. A family name alone does not satisfy the historical contract: the rule_version in a receipt identifies the revision that was applied, never an alias whose meaning changes when the register is updated.

Each registered revision binds the duty, the jurisdiction, the legal reference, the revision identity, the sources and the effective dates. It also states the applicability conditions and the mapping from the family's resolved outcomes to the clearance signals. A later reader recovers the rule as it stood, without substituting today's text for the revision used at the time.

The register preserves an attributable representation of the rule and the evidence used to encode it. A source reference leads to identifiable source material; a bare label is not a source. Source publication, source observation, rule effectiveness and register publication are four distinct events and are represented distinctly.

A clearance applies to an identified subject, action and context. Clearance to read a record does not clear an order, a distribution decision or a venue handoff. The same signal vocabulary may be used by different families only where each family publishes the scope and prerequisites of its binding.

## What the standard does not do

It does not make a record true, certify a product, approve a firm, or guarantee that a proposed action complies with every applicable obligation. It records a determinate outcome under a named revision and a declared scope; responsibilities outside that scope remain outside the result.

A successful lookup is not permission to act. Finding a subject or fetching a revision establishes availability. Permission requires the applicable clearance evaluation and its evidence, and a cleared response says what was cleared, so that success at the read boundary is never mistaken for permission at the order boundary.

Missing evidence is not a negative finding. A missing filing, an incomplete client classification or an unavailable source remains an evidence gap. It never becomes a restriction because the evaluator could not finish its work. Where the binding calls for a filing to be read, ACM-451 states that next step; it establishes no adverse finding.

A system failure is not a resolved restriction. A timeout, an invalid response, a failed signature check or an unavailable evaluator is never converted into ACM-403. Operational failure is reported explicitly, outside any clearance result, and the absence of a valid result is never treated as clearance.

A clearance is time-bound by its facts, its revision and its conditions. It does not promise that a later action remains permitted after a halt, a rule amendment, a changed entitlement or a changed record. Historical receipts preserve what was supplied under the earlier context.

Artificial intelligence makes mistakes. A clearance signal states the outcome of a defined check under a named revision — nothing more. Read the regulator.

## Who signs

Two objects are signed in this family, by two keys, and neither key signs the other's object.

Rule-register records and clearance records are signed by their producing node under the record key, following the ECO-10060 content contract: attributable content, sources, dates, a verifiable signature. A national family's revision is produced by that market's node; a shared family's revision is produced by the apex. The signature binds the node's representation of the rule and the outcome; it does not make the node the authority that issued the rule.

The receipt of a cleared read is signed by the RCO door under the receipt key. The receipt carries rule_version, which names the immutable revision used, and answer_hash, which binds the receipt to the signed answer supplied. The door signs neither the rule record nor the outcome, and verifies nothing about the rule's interpretation.

A receipt signature alone does not verify the rule record; a rule-record signature alone does not prove that a particular agent received it. A complete check verifies both objects with their own key sets and compares the answer hash between them.

## The arrow

listed security  →  record (ECO-10060, the node)  →  market (SM-ECO-10060)  →  rule (ACM-68000)  →  whether (AIO)  →  where (AMP)  →  receipt (RCO-10060, under every door)

This is a dependency model, not a ladder. It names the responsibilities that support an action without requiring every request to traverse the sequence. ECO defines the signed record and its evidence; SM-ECO binds the jurisdiction; ACM identifies the revision and the meaning of the outcome; AIO resolves whether a product may be ordered for a client class in a market; AMP resolves the venue and permitted route for an instrument, actor and action; RCO receipts each cleared read wherever it occurs; CPG-68000 is the umbrella.

AIO may need venue restrictions before it can resolve orderability. AMP may discover candidate venues before a clearance exists. An actionable route depends on the applicable clearance and orderability results, while reference information may be retrieved earlier. The register makes these dependencies explicit; discovery never grants access.

Venue identity, rules, calendars, halts and clearing relationships can form a sourced venue record. A permitted endpoint additionally requires evidence connecting the actor, the instrument, the action and the endpoint under the applicable rules. Without that evidence AMP returns reference information and unresolved gates; ACM cannot manufacture a permission the venue record does not establish.

Sustainability disclosure (ESG) is a specialised record under ECO-10060 and a rule family within this register. It supplies disclosure evidence and rule conditions. It is not a tier, and an ESG record never produces a generic sustainable outcome: any sustainability-related condition used by AIO is defined by the family and supported by its evidence.

## The thing ACM owns

ACM-68000 owns rule_version in the receipt and the clearance signal vocabulary. The rule register gives rule_version a durable referent; the signal bindings give the outcome a stable meaning. Neither responsibility belongs to listing status, to content identity or to the receipt signature.

An immutable revision is never edited in place. An amendment, a corrected interpretation or a changed binding produces a new revision. Earlier revisions remain resolvable for historical receipts. Successor and withdrawal relationships are published in later immutable records; they never rewrite the earlier signed object.

Effective dates say when a revision applies; publication dates say when the register made it available. The two are never conflated. Historical selection accounts for both the applicable interval and the evidence available at the read time. An open-ended interval means no end has been recorded, not perpetual applicability.

A family alias may support discovery of the current revision, but is never written into a receipt as though it were a revision. The resolver returns the exact rule_version selected, its signed revision record and the reasons it applies to the requested context.

Where several duties govern a clearance, the receipt's single rule_version names an immutable composite revision that lists its component revisions. The resolver never silently selects one duty and omits the others, and never constructs an unversioned mixture at verification time.

## The clearance vocabulary

Signal | Reading | Boundary
ACM-200 | Cleared | The specified read or action has cleared the applicable registered checks in the stated context.
ACM-403 | Restricted or halted | Evidence establishes a restriction or an applicable halt under the selected revision.
ACM-404 | Not on the register | The named lookup target is absent from the identified register. This establishes neither global absence nor prohibition.
ACM-451 | Read the filing | The binding requires the identified filing or source to be read before a conclusion or a progression.

ACM-200 means cleared. It never means a listing state. A listing attribute — trading, suspended, delisted — belongs in its own field on the record. A sourced halt may be an input to a family's restriction rule; the raw listing attribute and the resolved signal remain distinct, including when both appear in one response.

ACM-404 names the register and the lookup target: an absent rule revision and an absent subject registration are different failures and never share an unexplained message. ACM-451 names the required filing or evidence when known, and never disguises a service outage as a request to read.

### 6.1 Family binding table

The bindings below are the common interpretation. Each immutable family revision supplies its own source-backed prerequisites, applicability and reason codes before a binding is applied. A listed duty name is a register seed, not a completed rule.

Family | ACM-200 | ACM-403 | ACM-404 | ACM-451
Duty clearance (national and shared families) | Declared action clears the duty checks | An applicable duty condition restricts the action | Requested duty revision absent from the register | A specified filing must be read to complete the check
AIO orderability | Product, market and client-class action clears the orderability checks | Evidence establishes a distribution or target-market restriction | Requested product or rule registration absent from its register | Required product or target-market material must be read
AMP route clearance | Actor, instrument, action and endpoint clear the route gates | An applicable venue restriction, entitlement failure or halt is established | Requested venue, route or rule registration absent from its register | Required venue notice or filing must be read
ESG duty family | The named disclosure check clears its defined criteria | Evidence establishes a restriction under the applicable disclosure rule | Requested disclosure or rule registration absent from its register | Required disclosure material must be read

An ESG ACM-200 clears the named check; it is not a sustainability claim. An AMP ACM-200 requires route-gate evidence; it is never produced because an endpoint is discoverable. An unresolved prerequisite stays visible: no evaluation issues ACM-200 while hiding an unmet condition. Evidence gaps, operational errors and unresolved conflicts have explicit representations, and a family uses ACM-451 only where its published binding calls for the named source to be read.

## Publication discipline

One approved source. The canonical text, the register schema, the family bindings, the machine descriptors and the reading guide are generated from the same approved definitions. A human page never broadens the promise of the machine contract; a descriptor never advertises a capability the service does not provide.

Register before page. The sequence is mission, schema, source reading, field population, validation, publication. A page cannot create a revision by paraphrasing a family label; each revision is independently recoverable and attributable.

No counts in prose. No coverage total or member ordinal appears in authored text; generated presentation reads the current record. Routing follows the fleet registry; historical route patterns are never authority for a current endpoint.

Semantic change is a new revision. Changes to scope, bindings or required evidence produce new immutable revisions. Editorial corrections to a presentation never change a referenced signed object. Standard version, schema version, family revision and deployment version stay distinguishable.

## Machine files

- https://acm-68000.org/signals.json — the four signals of §6
- https://acm-68000.org/register.json — the register and its Book of Markets attachments
- https://acm-68000.org/.well-known/acm-68000.json

---

Standard held by Allooloo Technologies Corp. · Open standard, MIT licence.
