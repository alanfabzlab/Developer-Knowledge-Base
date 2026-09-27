# Bases functions reference

## Global functions

| Function | Purpose |
| --- | --- |
| <code>date(value)</code> | Parse a date string |
| <code>duration(value)</code> | Parse a duration string |
| <code>now()</code> / <code>today()</code> | Current date-time / date |
| <code>if(condition, yes, no?)</code> | Conditional value |
| <code>number(value)</code> | Convert to number |
| <code>link(path, display?)</code> | Create a link |
| <code>file(path)</code> | Resolve a file object |
| <code>list(value)</code> | Normalize a value to a list |
| <code>image(path)</code> / <code>icon(name)</code> | Create renderable values |

## Common methods

- String: <code>contains</code>, <code>startsWith</code>, <code>endsWith</code>,
  <code>lower</code>, <code>trim</code>, <code>replace</code>,
  <code>split</code>, <code>isEmpty</code>.
- Number: <code>abs</code>, <code>ceil</code>, <code>floor</code>,
  <code>round</code>, <code>toFixed</code>.
- List: <code>contains</code>, <code>containsAll</code>,
  <code>containsAny</code>, <code>filter</code>, <code>map</code>,
  <code>reduce</code>, <code>flat</code>, <code>join</code>,
  <code>sort</code>, <code>unique</code>.
- File: <code>asLink</code>, <code>hasLink</code>, <code>hasTag</code>,
  <code>hasProperty</code>, <code>inFolder</code>.
- Link: <code>asFile</code>, <code>linksTo</code>.
- Object: <code>keys</code>, <code>values</code>, <code>isEmpty</code>.
- Regular expression: <code>matches</code>.

Date fields include <code>year</code>, <code>month</code>, <code>day</code>,
<code>hour</code>, <code>minute</code>, and <code>second</code>. Date methods
include <code>date()</code>, <code>format()</code>, <code>time()</code>, and
<code>relative()</code>.

Duration fields are <code>days</code>, <code>hours</code>,
<code>minutes</code>, <code>seconds</code>, and <code>milliseconds</code>.
Duration does not directly support number rounding methods.
