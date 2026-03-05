# Autodesk.Revit.DB.Events

**3 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **build event handler methods that respond to Revit document lifecycle events**. It provides the base event argument classes that all document-level API events use, giving you access to the originating document and control over whether the event can be cancelled.

## Key outcomes

- **Handle document events with type-safe arguments** — use `RevitAPIPreDocEventArgs` for pre-action events (where you can cancel) and `RevitAPIPostDocEventArgs` for post-action events.
- **Write reusable event handler base logic** — `RevitAPISingleEventArgs` is the common base giving access to the event's `Cancellable` flag and the `Document`.
- **Cancel in-progress operations** — pre-doc event args expose `Cancel()` to abort actions such as document close or synchronize before they execute.

## Class hierarchy

```
RevitAPISingleEventArgs
├── RevitAPIPreDocEventArgs    ← raised before an action; may be cancellable
└── RevitAPIPostDocEventArgs   ← raised after an action has completed
```

## Key classes

| Class | Purpose |
|---|---|
| [`RevitAPISingleEventArgs`](Revit-APISingle-Event-Args-Class.md) | Base class — provides `Document`, `Cancellable`, and `Cancel()` |
| [`RevitAPIPreDocEventArgs`](Revit-APIPre-Doc-Event-Args-Class.md) | Pre-action event args — subscribe to `Application.DocumentOpening`, `DocumentSaving`, etc. |
| [`RevitAPIPostDocEventArgs`](Revit-APIPost-Doc-Event-Args-Class.md) | Post-action event args — subscribe to `Application.DocumentOpened`, `DocumentSaved`, etc. |

## Typical usage pattern

```csharp
app.DocumentSaving += (sender, e) =>
{
    RevitAPIPreDocEventArgs args = e;
    if (ShouldBlockSave(args.Document))
        args.Cancel();
};
```

## Files in this directory

| File | Contents |
|---|---|
| [`Revit-APISingle-Event-Args-Class.md`](Revit-APISingle-Event-Args-Class.md) | Base event args class |
| [`Revit-APIPre-Doc-Event-Args-Class.md`](Revit-APIPre-Doc-Event-Args-Class.md) | Pre-document event args |
| [`Revit-APIPost-Doc-Event-Args-Class.md`](Revit-APIPost-Doc-Event-Args-Class.md) | Post-document event args |
