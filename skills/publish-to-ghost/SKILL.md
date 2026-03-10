---
name: publish-to-ghost
description: Publish a markdown blog post to Ghost CMS. Use when the user wants to publish content to Ghost, upload a blog post, or push an article to the TDP Ghost blog.
argument-hint: [markdown-file-path]
disable-model-invocation: true
allowed-tools: Bash(node *)
---

# Publish to Ghost

Publish a markdown file to the TDP Ghost blog as a draft.

## Usage

Run the publish script with the markdown file path:

```bash
node ~/.claude/skills/publish-to-ghost/scripts/publish.mjs $ARGUMENTS
```

## What the script does

1. Reads the markdown file
2. Extracts the title from the first H1 heading
3. Converts markdown to HTML
4. Creates a draft post in Ghost with:
   - Author: Dianne Alter
   - Proper HTML content (using `?source=html` parameter)
   - Meta description from excerpt if available
   - Tags if specified in frontmatter

## Configuration

The script uses these Ghost API credentials (update in the script if needed):
- API URL: https://ghost.designproject.io
- Admin API Key: Configured in the script

## Expected markdown format

```markdown
# Post Title

- **Category:** Product Development
- **Tags:** AI, Design
- **Excerpt:** SEO description here

---

Your content here...

---

## Content Brief
(This section is stripped from published content)
```

## Output

Returns the Ghost editor URL where you can review and publish the draft.
