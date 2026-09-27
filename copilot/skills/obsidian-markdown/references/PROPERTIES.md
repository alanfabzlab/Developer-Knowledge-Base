# Properties reference

Properties are YAML frontmatter at the very start of a note.

| Property type | Example |
| --- | --- |
| Text | <code>title: My title</code> |
| Number | <code>rating: 4.5</code> |
| Checkbox | <code>completed: true</code> |
| Date | <code>date: 2026-07-21</code> |
| Date and time | <code>due: 2026-07-21T14:30:00</code> |
| List | <code>tags: [one, two]</code> or a YAML list |
| Link | <code>related: "[[Other Note]]"</code> |

Obsidian reserves <code>tags</code>, <code>aliases</code>, and
<code>cssclasses</code> for their built-in behaviors. Tags may contain letters,
numbers (not as the first character), underscores, hyphens, and forward slashes.
Prefer YAML lists when a property naturally has multiple values.
