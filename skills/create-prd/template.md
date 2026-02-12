# PRD Template

Use this template to generate PRDs. Each section includes guidance on what to write. Remove the guidance comments in the final output — they're instructions for you, not content for the PRD.

---

```markdown
# PRD: {Feature Name}

## Metadata

| Field | Value |
|-------|-------|
| **Author** | [TODO — PRD author name] |
| **Status** | Draft |
| **Created** | {today's date, YYYY-MM-DD} |
| **Last Updated** | {today's date, YYYY-MM-DD} |
| **Version** | 0.1 |
| **Related Docs** | {List transcripts, meeting notes, design docs, prototypes, and other references mentioned in the input} |

---

## 1. Problem Statement

<!--
Write a clear problem statement following this structure:
- **Who** is affected (specific persona, not "users")
- **What need** is unmet (concrete, not abstract)
- **Why** the current state is insufficient

Then provide **Evidence** — data points, user quotes, support tickets, competitive analysis,
or stakeholder observations from the transcript. Use bullet points. Cite sources.

End with a **Key Insight** paragraph — the non-obvious realization that frames the solution
direction. This should be the "aha" that someone reading the PRD needs to understand before
the solution makes sense.

If the transcript doesn't provide enough evidence, use [TODO] markers for specific data
points that need to be gathered.
-->

**Who** is affected and **what need** is unmet?

> {One-paragraph problem statement — specific persona + unmet need + why it matters now}

**Evidence:**
- {Evidence point 1 — data, quote, or observation with source}
- {Evidence point 2}
- {Evidence point 3}

**Key Insight:**
{The non-obvious realization that frames the solution direction}

---

## 2. Goals

<!--
Use the Goal/Metric/Target table format. Each goal should be:
- Measurable (tied to a specific metric)
- Time-bound (has a target timeline)
- Realistic but ambitious

Include 3-5 goals. Mark baselines as [TODO] if not available from the transcript.
-->

| # | Goal | Metric | Target |
|---|------|--------|--------|
| G1 | {Goal description} | {Specific metric} | {Target value + timeline} |
| G2 | {Goal description} | {Specific metric} | {Target value + timeline} |
| G3 | {Goal description} | {Specific metric} | {Target value + timeline} |

---

## 3. Non-Goals

<!--
Explicitly state what this feature is NOT doing. Categories:
- "Not building:" — things that sound related but are out of scope
- "Not solving for:" — user segments or use cases excluded from this version
- "Not changing:" — existing systems/features that remain untouched
- "Deferred to future:" — good ideas that belong in a later version, with brief rationale

Be specific. Each non-goal should preempt a question someone might ask after reading the
Goals section.
-->

- **Not building:** {Feature or capability that's explicitly out of scope}
- **Not solving for:** {User segment or use case excluded}
- **Not changing:** {Existing system that remains untouched}
- **Deferred to future:** {Good idea for later, with brief rationale for deferral}

---

## 4. Target Users

<!--
Define Primary Persona, Secondary Persona (if applicable), and Anti-Persona.
For each persona include:
- **Who:** Specific role/title, not generic "users"
- **Context:** Their situation when they encounter this feature
- **Motivation:** What they're trying to accomplish (Jobs to be Done framing)
- **Current workaround:** How they handle this today without the feature
- **Jobs to be done:** A quote-style JTBD statement
-->

### Primary Persona
- **Who:** {Specific role — e.g., "Team admin at a 50-person SaaS company"}
- **Context:** {Their situation when they encounter this feature}
- **Motivation:** {What they're trying to accomplish}
- **Current workaround:** {How they handle this today}
- **Jobs to be done:** "{JTBD statement in first person}"

### Secondary Persona
- **Who:** {Role}
- **How they're impacted:** {How this feature affects them differently than primary persona}
- **Context:** {Their situation}

### Anti-Persona
- **Who is this NOT for:**
  - {User type 1 and why they're excluded}
  - {User type 2 and why they're excluded}

---

## 5. User Stories & Key Flows

<!--
Write 3-6 user stories covering:
1. Happy path (primary use case, most detail)
2. Key alternative paths (skip flows, error cases, edge cases)
3. Each story uses the format: As a [persona], I want to [action], so that [outcome]
4. Each story has a numbered step-by-step Flow section
5. End with "Flows NOT Covered" listing what's explicitly excluded

The happy path should be very detailed (15-20 steps). Alternative paths can be shorter.
-->

### Story 1: {Happy Path Title}
**As a** {persona}, **I want to** {action}, **so that** {outcome}.

**Flow:**
1. {Step 1}
2. {Step 2}
...

### Story 2: {Alternative Path Title}
**As a** {persona}, **I want to** {action}, **so that** {outcome}.

**Flow:**
1. {Step 1}
2. {Step 2}
...

### Flows NOT Covered
- {Flow 1 and why it's excluded}
- {Flow 2 and why it's excluded}

---

## 6. Solution Overview

<!--
Start with an **Approach** paragraph summarizing the overall solution in 2-3 sentences.

Then list **Key Design Decisions** — numbered, each with:
- A bold title stating the decision
- A paragraph explaining the rationale (why this approach, not just what)
- Trade-offs considered

These decisions should be opinionated and specific to your product's context.
Reference existing patterns, code, and conventions where relevant.
-->

**Approach:** {2-3 sentence overview of the solution}

**Key Design Decisions:**

1. **{Decision title}.** {Rationale paragraph explaining why this approach was chosen,
   what alternatives were considered, and how this fits existing patterns.}

2. **{Decision title}.** {Rationale paragraph.}

**Wireframes/Mockups:** {Reference to designs or [TODO — mockups needed]}

---

## 7. Technical Scope

<!--
IMPORTANT: This section must reference REAL code paths from your codebase research.
Never hallucinate file paths or module names.

Fill in the Affected Architecture Layers table and any project-specific checklists
from company-context.md.
-->

### Affected Architecture Layers

| Layer | Changes | Details |
|-------|---------|---------|
| **Database** | {None / Minor / Major} | {What models, fields, or tables change} |
| **Backend** | {None / New / Modified} | {Which services, APIs, or routes are affected} |
| **Frontend** | {None / New / Modified} | {Which components, pages, or views} |
| **API** | {None / New endpoints / Modified} | {Which endpoints} |
| **Integrations** | {None / Affected} | {Which third-party integrations} |

### Database Changes
- [ ] New tables/models: {List or "None"}
- [ ] New fields on existing tables: {List with types}
- [ ] New enum values: {List}
- [ ] Migration strategy: {Forward-only / backfill needed / etc.}

### API Surface
- [ ] New endpoints/procedures: {List with input/output types}
- [ ] Modified endpoints/procedures: {List}
- [ ] Webhook events: {New/modified events or "None"}

### Feature Flag Strategy
- Flag name: `{feature-flag-name}`
- Default: `off`
- Implementation: {Where the flag is checked}
- Rollout plan: {Phased rollout description}

<!--
Add any project-specific technical checklists here.
See company-context.md for sections your team requires (e.g., i18n, self-hosted,
mobile impact, accessibility, etc.)
-->

---

## 8. Hypotheses & Assumptions

<!--
Use the format: "We believe [hypothesis] because [reasoning]. We'll know we're right
if [measurable validation criteria]."

List 3-5 hypotheses. Mark each as Unvalidated, Partially Validated, or Validated.

Then list "Key assumptions that could invalidate this plan" with mitigations.
-->

| # | Hypothesis | Validation Method | Status |
|---|-----------|-------------------|--------|
| H1 | We believe {hypothesis} because {reasoning} | We'll know we're right if {measurable criteria} | Unvalidated |
| H2 | We believe {hypothesis} because {reasoning} | We'll know we're right if {measurable criteria} | Unvalidated |

**Key assumptions that could invalidate this plan:**

- **{Assumption 1}.** {Why it matters and what happens if it's wrong.} **Mitigation:** {How to de-risk.}
- **{Assumption 2}.** {Why it matters.} **Mitigation:** {How to de-risk.}

---

## 9. Success Metrics

<!--
Structure: Primary KPI, Secondary KPIs, Guardrail Metrics, Release Criteria.
Each metric needs: metric name, baseline (or [TODO]), target, timeline.
Guardrail metrics are things that must NOT regress.
Release criteria are pass/fail gates before launch.
-->

### Primary KPI
- **Metric:** {Primary success metric}
- **Baseline:** {Current value or [TODO — need data from {source}]}
- **Target:** {Target value}
- **Timeline:** {When to measure}

### Secondary KPIs
- **Metric:** {Secondary metric 1}
- **Baseline:** {Value or [TODO]}
- **Target:** {Target}
- **Timeline:** {When}

### Guardrail Metrics (must not regress)
- {Metric 1}: must stay above {threshold}
- {Metric 2}: must not increase beyond {threshold}

### Release Criteria
- [ ] {Criterion 1}
- [ ] {Criterion 2}
- [ ] {Criterion 3}

---

## 10. Risk Assessment (SVPG Framework)

<!--
Assess four risk types from SVPG (Silicon Valley Product Group):
- Value: Will users want this?
- Usability: Can users figure out how to use it?
- Feasibility: Can engineering build it with current resources/timeline?
- Viability: Does it work for the business (legal, compliance, cost, etc.)?

Rate each as Low/Medium/High with description and mitigation.
-->

| Risk Type | Level | Description | Mitigation |
|-----------|-------|-------------|------------|
| **Value** | {Low/Medium/High} | {Will users want this? What's uncertain?} | {How to de-risk} |
| **Usability** | {Low/Medium/High} | {Can users figure it out?} | {How to de-risk} |
| **Feasibility** | {Low/Medium/High} | {Can we build it?} | {How to de-risk} |
| **Viability** | {Low/Medium/High} | {Does it work for the business?} | {How to de-risk} |

---

## 11. Dependencies & Risks

<!--
List dependencies in categories relevant to your project:
- Cross-Team Dependencies (people/teams that must do something)
- Third-Party Dependencies (external services, APIs)
- Any project-specific categories from company-context.md
-->

### Cross-Team Dependencies
- [ ] {Team/Person} — {What's needed and timing}

### Third-Party Dependencies
- [ ] {Service/API} — {Dependency and risk level}

---

## 12. Implementation Approach

<!--
Break the implementation into small, reviewable PRs.
Adjust size limits to match your team's conventions.
-->

### PR Breakdown Strategy

| # | PR Scope | Estimated Size | Dependencies | Labels |
|---|----------|---------------|--------------|--------|
| 1 | {PR description} | ~{N} lines | {None or PR #} | `{labels}` |
| 2 | {PR description} | ~{N} lines | {None or PR #} | `{labels}` |

**Total estimated size:** ~{N} lines across {N} PRs.

### Testing Plan

- **Unit tests:** {What to test and in which PR}
- **Integration tests:** {What to test and in which PR}
- **E2E tests:** {What to test and in which PR}

### Rollout Plan

1. **Development:** Feature flag `off`. Build behind flag.
2. **Internal dogfooding ({duration}):** Flag on for internal accounts.
3. **Partial rollout ({percentage}, {duration}):** A/B test with metrics.
4. **GA:** Flag on for all users.

### Rollback Criteria
- {Condition 1 that triggers rollback}
- {Condition 2 that triggers rollback}
- **Rollback procedure:** {How to roll back safely}

---

## 13. Stakeholder Sign-Off

| Role | Name | Status |
|------|------|--------|
| PM | {Name or [TODO]} | [ ] Approved |
| Eng Lead | {Name or [TODO]} | [ ] Approved |
| Design | {Name or [TODO]} | [ ] Approved |

---

## Appendix

### Change Log
| Date | Version | Changes |
|------|---------|---------|
| {today's date} | 0.1 | Initial draft generated from {source description} |

### FAQ

<!--
Include 3-8 FAQ entries addressing questions someone would likely ask after reading the PRD.
Format: Q/A pairs. Good FAQs preempt objections and clarify ambiguities.
-->

- **Q:** {Anticipated question}
- **A:** {Clear answer with rationale}

### Research & References
- {Reference 1 — transcript, doc, or resource with description}
- {Reference 2}
```
