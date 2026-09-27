# JSON Canvas examples

## Connected notes

~~~json
{
  "nodes": [
    {
      "id": "8a9b0c1d2e3f4a5b",
      "type": "text",
      "x": 0,
      "y": 0,
      "width": 300,
      "height": 140,
      "text": "# Main idea"
    },
    {
      "id": "1a2b3c4d5e6f7a8b",
      "type": "file",
      "x": 400,
      "y": 0,
      "width": 300,
      "height": 200,
      "file": "Notes/Supporting note.md",
      "subpath": "#Evidence"
    }
  ],
  "edges": [
    {
      "id": "3c4d5e6f7a8b9c0d",
      "fromNode": "8a9b0c1d2e3f4a5b",
      "fromSide": "right",
      "toNode": "1a2b3c4d5e6f7a8b",
      "toSide": "left",
      "label": "supported by"
    }
  ]
}
~~~

## Grouped board

~~~json
{
  "nodes": [
    {
      "id": "5e6f7a8b9c0d1e2f",
      "type": "group",
      "x": 0,
      "y": 0,
      "width": 320,
      "height": 500,
      "label": "In progress",
      "color": "3"
    },
    {
      "id": "8b9c0d1e2f3a4b5c",
      "type": "text",
      "x": 30,
      "y": 60,
      "width": 260,
      "height": 100,
      "text": "## Task\n\nImplement the feature"
    }
  ],
  "edges": []
}
~~~
