# PR and Branch Naming Conventions

When working on a client codebase as a designer or developer contributor, clear naming for pull requests and branches makes our work easier to track, review, and identify — both for the client team and for us.

This guide proposes a simple convention to follow when the client doesn't already have one in place, and offers a way to make TDP-authored work easy to spot at a glance.

## Why naming matters

Branch and PR names are read far more often than they're written. A descriptive name communicates the purpose of the work without anyone having to open the diff or scroll through commits. When multiple contributors are pushing to the same repo, consistent naming reduces ambiguity and helps reviewers prioritize.

This becomes especially relevant for us as design contributors: when our PRs sit alongside the client's engineering work, a clear naming pattern makes it obvious which changes are ours and what they're meant to accomplish.

## PR naming

Use the format:

```
<type>(<scope>): <short description>
```

- **type** — what kind of work this is (`feat`, `fix`, `docs`, `refactor`, `experimental`, etc.)
- **scope** — the area of the product affected (`playground`, `dashboard`, `auth`, etc.)
- **description** — a concise summary in plain language

**Example:**

```
feat(playground): v1 prototype — patient-based messaging flow
```

For our work as designers, the most common types will be `feat` or `feature` for new UI work, and `experimental` for prototypes or explorations. More developer-specific types (`refactor`, `chore`, `perf`) usually won't apply.

## Branch naming

Following the same logic, branches benefit from a prefix that communicates their purpose. The most common pattern is:

```
<prefix>/<short-description>
```

**Example:**

```
feature/patient-based-messaging
```

Common prefixes include:

- `feature/` — new features or UI work
- `bugfix/` — fixing existing functionality
- `hotfix/` — urgent production fixes
- `docs/` — documentation changes
- `experimental/` — prototypes and explorations

For more detail on branch naming basics (lowercase, hyphen-separated, no trailing hyphens, etc.), Abhay Amin's cheatsheet on Medium is a useful reference.

## When the client doesn't have conventions

If the client repo has no documented conventions, this is a good opportunity to propose the structure above. From experience on a recent client project, the developer responded well to a PR named using this format — it made the intent of the change immediately clear and didn't require any back-and-forth.

A few things to keep in mind when proposing:

- **Frame it as a suggestion, not a requirement.** The client owns the repo; we're contributors.
- **Match what's already there if anything exists.** If past PRs follow a loose pattern, adapt to it rather than introducing something entirely new.
- **Lead by example.** Sometimes it's easier to use the convention in our own PRs and let it speak for itself than to push for adoption upfront.

## Optional: a TDP prefix for our work

When our contributions sit alongside the client's internal team, prefixing branches with `tdp/` can make our work easy to identify:

```
tdp/feature/patient-based-messaging
```

This is entirely optional and depends on the client's preferences, but it can be a nice touch for repos where multiple teams contribute. It also gives the client a clean way to filter or audit our work later.

## Quick reference

| Element | Format | Example |
|---------|--------|---------|
| PR title | `type(scope): description` | `feat(playground): v1 prototype — patient-based messaging flow` |
| Branch | `prefix/short-description` | `feature/patient-based-messaging` |
| Branch (with TDP prefix) | `tdp/prefix/short-description` | `tdp/feature/patient-based-messaging` |

---

**Reference:** [Naming conventions for Git Branches — a Cheatsheet](https://medium.com/@abhay.pixolo/naming-conventions-for-git-branches-a-cheatsheet-8549feca2534) by Abhay Amin
