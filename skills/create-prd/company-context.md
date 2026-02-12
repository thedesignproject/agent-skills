# Company Product & Architecture Context

<!--
==========================================================================
CUSTOMIZE THIS FILE for your product and codebase.

This file is read by the PRD generator skill to ground PRDs in your
actual product, architecture, and conventions. Replace all [YOUR ...]
placeholders with your real information.

The more specific you are here, the better your generated PRDs will be.
==========================================================================
-->

## Core Product Concepts

<!--
List the key domain concepts in your product. These help the PRD generator
use correct terminology and understand how features relate to each other.

Example for a scheduling app:
- **Event Types**: Templates for bookable meetings
- **Bookings**: Instances of scheduled meetings
- **Availability**: When a user is bookable
-->

- **[YOUR CONCEPT 1]**: [What it is and why it matters]
- **[YOUR CONCEPT 2]**: [What it is and why it matters]
- **[YOUR CONCEPT 3]**: [What it is and why it matters]
- **[YOUR CONCEPT 4]**: [What it is and why it matters]

## Architecture Layers

<!--
Describe the layers of your application so the PRD generator can map
feature changes to the right parts of the codebase.

Example:
  Browser → Next.js App Router → tRPC Router → Service → Repository → Prisma → PostgreSQL
-->

```
[YOUR ARCHITECTURE FLOW, e.g.: Browser → API Gateway → Backend Service → Database]
```

| Layer | Location | Purpose |
|-------|----------|---------|
| **[YOUR LAYER 1]** | `[directory path]` | [Purpose] |
| **[YOUR LAYER 2]** | `[directory path]` | [Purpose] |
| **[YOUR LAYER 3]** | `[directory path]` | [Purpose] |
| **[YOUR LAYER 4]** | `[directory path]` | [Purpose] |
| **[YOUR LAYER 5]** | `[directory path]` | [Purpose] |

## Key Directories

<!--
List the directories the PRD generator should know about when researching
the codebase. Be specific — real paths help the generator find real code.
-->

```
[YOUR KEY DIRECTORIES, e.g.:]
src/app/                    # Routes / pages
src/components/             # Shared UI components
src/services/               # Business logic
src/db/                     # Database schema and migrations
src/api/                    # API routes
tests/                      # Test files
```

## Tech Stack Summary

<!--
List your actual tech stack so PRDs reference the right technologies.
-->

| Technology | Usage |
|-----------|-------|
| [YOUR FRAMEWORK] | [e.g., Next.js 14, App Router] |
| [YOUR LANGUAGE] | [e.g., TypeScript, strict mode] |
| [YOUR DATABASE] | [e.g., PostgreSQL with Prisma ORM] |
| [YOUR API LAYER] | [e.g., tRPC, REST, GraphQL] |
| [YOUR AUTH] | [e.g., NextAuth.js, Clerk, Auth0] |
| [YOUR STYLING] | [e.g., Tailwind CSS] |
| [YOUR TESTING] | [e.g., Vitest for unit, Playwright for E2E] |
| [YOUR LINTER] | [e.g., ESLint, Biome] |

## Project-Specific PRD Requirements

<!--
These are conventions and checklists that every PRD's Technical Scope
section should address. Delete any that don't apply, add your own.
-->

### Feature Flags
<!-- How does your team handle feature flags? Delete if not applicable. -->
- All new features ship behind a feature flag
- Flag naming convention: [YOUR CONVENTION, e.g., kebab-case]
- Default: `off`
- Rollout phases: [YOUR PHASES, e.g., internal → percentage → GA]

### Internationalization (i18n)
<!-- Delete this section if your product is English-only. -->
- All UI strings must be translation keys in `[YOUR TRANSLATIONS FILE PATH]`
- Never hardcode user-facing strings
- Estimate the number of new translation keys in each PRD

### PR Size Limits
<!-- Adjust to match your team's conventions. -->
- Each PR: <[YOUR LIMIT, e.g., 500] lines changed, <[YOUR LIMIT, e.g., 10] files
- Break implementations into incremental, reviewable PRs
- Each PR should be independently mergeable

### Database Conventions
<!-- Add your ORM/database conventions. -->
- [YOUR CONVENTION 1, e.g., "Always use `select` (never `include`) in Prisma queries"]
- [YOUR CONVENTION 2, e.g., "New fields should be nullable or have defaults"]
- [YOUR CONVENTION 3, e.g., "Never expose sensitive fields in API responses"]

### Error Handling
<!-- How does your team handle errors? -->
- [YOUR CONVENTION, e.g., "Use TRPCError in routers, custom AppError in services"]
- [YOUR CONVENTION, e.g., "Descriptive error messages with context"]

### Testing Expectations
<!-- What level of test coverage does your team expect for new features? -->
- Unit tests for: [YOUR EXPECTATION, e.g., "business logic and state machines"]
- Integration tests for: [YOUR EXPECTATION, e.g., "API endpoints"]
- E2E tests for: [YOUR EXPECTATION, e.g., "critical user-facing flows"]

<!--
==========================================================================
ADD YOUR OWN SECTIONS BELOW

Common additions:
- Accessibility requirements
- Mobile/responsive considerations
- Self-hosted / on-prem considerations
- Security review requirements
- Performance budgets
- API versioning conventions
==========================================================================
-->
