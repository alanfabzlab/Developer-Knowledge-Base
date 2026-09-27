---
name: openartifacts-publish
description: Publish an existing Markdown note or local HTML file, update a published Markdown note, or withdraw an OpenArtifacts page. Use when the user asks to publish, share, update, delete, remove, or withdraw an OpenArtifacts page.
metadata:
  copilot-enabled-agents: opencode, claude, codex
  copilot-builtin-version: "5"
---

# Publish Markdown or HTML to OpenArtifacts

Copilot supplies everything this skill needs through the environment:
`$OPENARTIFACTS_WORKSPACE_ROOT` is the vault root, and `COPILOT_PLUS_LICENSE_KEY`
is the credential the bundled wrapper sends. Do not read Copilot settings or credential
files, print the key, install anything, or run Node, npm, npx, or the Obsidian CLI.

If `COPILOT_PLUS_LICENSE_KEY` is unset or empty, stop before generating anything and tell
the user: Publishing to OpenArtifacts needs a Copilot Plus license key. Add it in Copilot Settings and try again.

## 1. Prepare the page

### Existing Markdown note

Read one existing Markdown source note. Treat YAML frontmatter as metadata, never as page
content. Note its `openartifacts` property, or on older notes the `symposium` property:
an `https://…/d/<docId>` value means the note is already published and this task updates
that page; pass that `docId` to the wrapper. Compare document ids, not urls: an older
`symposium.site` link and an `openartifacts.site` link with the same id are the same page.
If either property holds any other value, or the two name different ids, stop and ask the
user before touching them.

Write complete UTF-8 HTML (at most `10485760` bytes) to a new file
under `$OPENARTIFACTS_WORKSPACE_ROOT/.openartifacts/handoffs/`, creating
the directory if needed. Preserve the note's content; render Obsidian-specific syntax such
as wikilinks, callouts, embeds, Mermaid, and Bases into static HTML or SVG. CSS, scripts,
and external resources are allowed and are published unchanged.

Use the note's file name without `.md` as its page title. Convert the filename-derived title to
title case while preserving recognizable acronyms and proper names. Put that title in both the HTML
`<title>` and a visible `<h1>` above the rendered note body. If the user explicitly asks for no
title, do not add the `<h1>`. Keep the HTML `<title>` as browser metadata, and preserve any
authored opening heading as note content. Otherwise, if the rendered note body already starts with an
equivalent `<h1>` containing the same visible title text, use that heading as the page-body title
and do not add another heading. Preserve all remaining note content below it, and do not edit the
source Markdown to add the heading. Keep normal text wrapping on the `<h1>` so long titles wrap
naturally on narrow screens. Never truncate the title, hide its overflow, or apply single-line or
ellipsis styling. The review and publish steps must use this same complete HTML file so its title
and body match in preview and after publishing.

Themes are optional. For a named theme, check
`$OPENARTIFACTS_WORKSPACE_ROOT/.openartifacts/themes/<name>.md`, then
`themes/<name>.md` next to this skill. Check each path independently. If neither
exists, continue with readable defaults; a missing theme must never block publishing.
The bundled `research-memo` is an optional example.

### Existing HTML file

For an existing local `.html` file, confirm that it exists and is at most
`10485760` bytes. Pass that original HTML file path directly to
the wrapper. Treat the file as the complete page: do not convert it to Markdown, and do
not render, rewrite, or copy it into `.openartifacts/handoffs/`. Use its file
name without `.html` as the wrapper title without changing the document's own title or
visible content. Skip the Markdown frontmatter, generated-title, and theme instructions
above. Check the HTML, including inline CSS, for every reference to a local file. Examples
include relative `src`, `href`, `srcset`, `poster`, or CSS `url(...)` references.
If any exist, keep the file unchanged; name each reference in the review message and say it
will not load on the published page because only the HTML file is uploaded. This warning
does not block publication: let the user make the file self-contained or approve publishing
anyway. The original file remains user-owned; never delete the original HTML file.

## 2. Let the user review

Tell the user the absolute path of the HTML file and that, subject to any relative-asset
warning above, opening it in a browser shows the page as it will be uploaded; OpenArtifacts
adds its own header and footer bylines when it serves the page. Then end your turn.

Never publish in the same turn that generated the HTML. Publish only when a later
message from the user clearly asks to publish this page. Treat anything else as feedback
(revise the generated Markdown handoff and repeat this step; for existing HTML, relay the
feedback and wait for the user to update the file, then repeat steps 1 and 2 before accepting
publication approval) or as a cancellation. When unsure whether a message is an approval,
ask once. Never simulate the user's approval.

## 3. Publish

Run the wrapper next to this SKILL.md with the HTML file, its filename-derived title, and
the existing `docId` when updating a Markdown note. On macOS or Linux, the Markdown path
uses its generated handoff:

```bash
sh "/absolute/path/to/this/skill/directory/openartifacts-publish.sh" publish "$OPENARTIFACTS_WORKSPACE_ROOT/.openartifacts/handoffs/unique.html" "Note title" [docId]
```

An existing HTML file uses its original path directly:

```bash
sh "/absolute/path/to/this/skill/directory/openartifacts-publish.sh" publish "/absolute/path/to/page.html" "Page title"
```

On Windows, use the `.cmd` wrapper (prefix with `&` in PowerShell):

```powershell
& "/absolute/path/to/this/skill/directory/openartifacts-publish.cmd" publish "$env:OPENARTIFACTS_WORKSPACE_ROOT/.openartifacts/handoffs/unique.html" "Note title" [docId]
```

For an existing HTML file on Windows, replace the handoff path with the original absolute
`.html` path and omit the `docId`.

Success returns the same server receipt, `{"docId", "url", "version"}`, for either
input. For a Markdown note, set its `openartifacts` frontmatter property to that `url`
(create the frontmatter block if needed, keep every other property), remove a `symposium`
property whose link has the same document id, and delete the generated HTML file from
`.openartifacts/handoffs/`. For an existing HTML file, leave the source file
unchanged. Then report the URL. Publishing the same Markdown note again updates the same page.

On failure the wrapper prints the HTTP status and the server's message to stderr and
exits 1. Report that message verbatim. Do not retry on your own, invent a cause, strip
styling, or publish another way. For a 401, the license key was refused or the plan
cannot publish; point the user at Copilot Settings. For `not_found` on an update, stop;
do not create a replacement page unless the user explicitly asks.

## 4. Withdraw

For delete, remove, or withdraw requests, take the `docId` from an OpenArtifacts link the
user supplies or the receipt URL reported earlier. Otherwise, read it with the same rules as
step 1: `openartifacts` first, `symposium` on older notes, compared by document id, and
stop to ask on any other value or on two properties naming different ids. If there is no link
or property, say nothing is published. Otherwise tell the user the link will stop working and
that copies people already saved cannot be recalled, then end your turn. On a clear yes, run
the wrapper with `unshare <docId>`, remove each `openartifacts` or `symposium` property
only when that property's own link has the same document id, and report that the page is gone.
Never tell the user to delete the page at its public URL.
