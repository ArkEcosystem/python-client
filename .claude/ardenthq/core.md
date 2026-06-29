<!-- airc v0.3.0 — managed file, do not edit -->
<!-- Local override: CLAUDE.local.md. Per-repo override: below the @imports in CLAUDE.md. Permanent override: PR to https://github.com/ardenthq/airc -->

# Baseline

Shared rules for every repo. Apply to any stack.

## Commits

- Format: [Conventional Commits](https://www.conventionalcommits.org) — `feat:`, `fix:`, `chore:`, `style:`, `refactor:`, `test:`, `docs:`
- Subject line only, ideally under 50 characters
- Human, direct tone. Avoid formal or robotic voice ("this commit introduces…", "this change implements…")
- **Never** add `Co-Authored-By` or any mention of Claude / AI / agents
- **Never** add a description or body — subject only
- Commit incrementally when a logical chunk lands — don't batch everything at the end
- Examples: `feat: scaffold composer package`, `fix: stack detection for inertia`

## Pull Requests

- Always draft (`gh pr create --draft`)
- Base branch: the repo's default
- If the repo has a `.github/PULL_REQUEST_TEMPLATE.md`, fill it in as the PR body and check off the items that apply. `gh pr create` ignores the template unless you pass it yourself — write the filled body to a file and use `--body-file`
- **Never** reference Claude / AI / agents in title, body, branch name, or comments

## Pre-push checks

Standard order before pushing:

1. Formatter → 2. Linter → 3. Static analysis → 4. Tests

Exact commands are repo-defined (see the repo's `CLAUDE.md` / `composer.json` / `package.json`). If the formatter modifies files, commit those changes before pushing so CI doesn't kick back automated `style:` cleanup commits.

**Mid-task (recommendation):** for long tasks, run only affected/new checks during the work; defer the full suite to the end. For short tasks, skip intermediate runs. Don't run checks repeatedly mid-work — once at completion is usually enough.

## Security

- Never commit `.env`, credentials, tokens, or any secret
- Flag any new dependency as suspect before adding it (typosquatting, unknown maintainer, etc.)
- No destructive operations (`force-push`, branch deletion, history rewrite, `git reset --hard`, `rm -rf`) without explicit confirmation from the dev
- For external tools (CI, pastebins, gists): consider whether uploaded content could be sensitive — it may be cached or indexed even if later deleted

## Code style

- Follow existing patterns before introducing new ones
- Reuse existing components/helpers before writing new ones
- No comments unless explaining a non-obvious **why** (a hidden constraint, a subtle invariant, a workaround for a specific bug)
- Well-named identifiers > a comment explaining the "what"
- **Don't document changes in comments.** Comments describe the code as it is, not how it got there:
  - ❌ `// moved from backend to frontend`
  - ❌ `// renamed from foo to bar`
  - ❌ `// replaces the previous logic that used X`
  - ❌ `// added for issue #123`
  - ✅ omit the comment — git log / PR tells the story
- Don't reference callers or temporal context: no `// used by X`, `// for the Y flow`, `// added in sprint Z`

## Claude reply style

- Concise. Skip the obvious.
- End-of-turn summary: one or two sentences — what changed, what's next.
- No long essays, no unnecessary disclaimers, no "sure, happy to help…"

## Overrides

- Personal override: create `CLAUDE.local.md` (gitignored)
- Per-repo override: add rules below the `@imports` in this repo's `CLAUDE.md`
- Permanent shared override: PR against the upstream guidelines repo
