---
name: pr-branch-naming
description: Generate a conventionally-named branch and PR title from a feature description. Use when the user is starting a new branch, opening a PR, or asks how to name a branch or PR. Triggers on phrases like "create a branch", "name this branch", "open a PR", "what should I call this branch", "PR title for this".
argument-hint: [feature description]
allowed-tools: Read, Bash(git status:*), Bash(git branch:*), Bash(git checkout:*), Bash(git log:*), Bash(gh pr create:*), Bash(gh auth status:*)
---

# PR & Branch Naming

You generate a conventionally-named branch and a matching PR title from a feature description, then optionally check out the branch and/or open a PR — but only with explicit user confirmation.

---

## Step 1: Get the feature description

The user's input is in `$ARGUMENTS`. It can be:

1. **A description** — use it directly
2. **Empty** — try to infer the work from `git status` and the most recent commits (`git log -n 5 --oneline`). If you can infer it, propose it back to the user for confirmation. If not, ask: *"What's the feature or change this branch is for?"*

Don't fabricate a description. If there's nothing to go on, ask.

---

## Step 2: Pick the type and scope

### Type (one of)

| Type | When to use |
|---|---|
| `feat` | New feature or new UI work |
| `fix` | Bug fix to existing functionality |
| `docs` | Documentation changes only |
| `refactor` | Code restructuring with no behavior change |
| `perf` | Performance improvement |
| `chore` | Tooling, config, dependency bumps |
| `experimental` | Prototype, spike, or exploration not intended to ship as-is |

Pick the type that best matches the description. For designer-authored work, the common types are `feat` and `experimental`.

### Scope

The area of the product affected — short, lowercase, single word if possible. Examples: `playground`, `dashboard`, `auth`, `onboarding`, `billing`.

Infer the scope from the description. If it's genuinely ambiguous, ask once: *"What part of the product does this touch — dashboard, auth, etc.?"* Don't pepper the user with questions.

---

## Step 3: Pick the branch prefix

| Prefix | When to use |
|---|---|
| `feature/` | New features or UI work (pairs with `feat`) |
| `bugfix/` | Fixing existing functionality (pairs with `fix`) |
| `hotfix/` | Urgent production fixes |
| `docs/` | Documentation changes (pairs with `docs`) |
| `experimental/` | Prototypes and explorations (pairs with `experimental`) |

The prefix should align with the type. Use `feature/` for `feat`, `bugfix/` for `fix`, and so on.

---

## Step 4: Generate the names

### Branch name

Format: `<prefix>/<kebab-description>`

Rules:
- Lowercase only
- Hyphen-separated (no underscores, no spaces)
- No trailing hyphen
- Keep it concise — aim for 3–6 words in the description portion
- Drop filler words (`the`, `a`, `for`, `to`, `make`)

**Example:** `feature/patient-based-messaging`

### PR title

Format: `<type>(<scope>): <short description>`

Rules:
- Description in plain language, sentence case, no trailing period
- Concise — fits on one line
- Mirrors what the branch is about, but reads naturally to a human reviewer

**Example:** `feat(playground): v1 prototype — patient-based messaging flow`

---

## Step 5: Show the result

Present both names plus a one-line rationale, in this format:

```
Branch:    feature/patient-based-messaging
PR title:  feat(playground): v1 prototype — patient-based messaging flow

Type: feat (new UI work) · Scope: playground · Prefix: feature/
```

---

## Step 6: Offer to apply

Ask the user whether to:

1. **Check out the branch** — run `git checkout -b <branch>`
2. **Open a draft PR** — run `gh pr create --draft --title "<title>" --body "<one-line description>"`
3. **Do both**
4. **Neither** — they'll copy the names themselves

Before running either command, check the preconditions and stop with a clear message if they fail:

- **For `git checkout -b`:** run `git status` first. If the working tree is dirty, surface that and ask whether to proceed anyway, stash, or abort. If a branch with the same name already exists, suggest a numeric suffix (`-2`).
- **For `gh pr create`:** run `gh auth status` first. If unauthenticated, tell the user to run `gh auth login` and stop. Don't open the PR from a branch with no commits ahead of base — check with `git log <base>..HEAD --oneline` and warn if empty.

Never run destructive git operations (`reset --hard`, `branch -D`, `push --force`) as part of this skill.

---

## Notes

- If the user is already on a non-default branch when invoking this skill, ask whether the new branch should be cut from `main`/`master` or from the current branch.
- If multiple changes are described (e.g., "fix the login bug and add a new dashboard widget"), suggest splitting into two branches/PRs rather than smushing them into one.
- The PR title's description can use an em dash (`—`) to add a qualifier, as in the example. Don't overuse it.
