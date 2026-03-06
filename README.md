# Autodesk Revit API AI Friendly Docs

Local markdown mirror of Autodesk Revit APIs documentation with scripts to re-crawl that enables more targeted prompts, reduces token usage, tool usage and speeds up agent discovery to improve performance on complex tasks.

## Where to Find Things

- [2026](2026/README.md) - Autodesk Revit 2026 API Docs

## Humans

Use this workflow to get the best results from AI tools:

1. Clone this repository locally.
2. Add this repo folder to your workspace in VS, VS Code, or Cursor.
3. In the project tree, right-click and choose `Add Folder to Workspace...`.
4. When prompting, include where the docs are located so the assistant can search the right files.

Example prompt:

```
Use the Revit API docs in ./2026/README.md as the starting point.
Write me an example of exporting all sheets to PDFs.
```