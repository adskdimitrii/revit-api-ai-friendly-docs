# Autodesk.Revit.ApplicationServices

**6 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to access **application-wide settings and resources** at the Revit session level — before any specific document is involved. This is your entry point for reading Revit version info, language, shared component paths, and managing the document lifecycle via events.

## Key outcomes

- **Inspect the running Revit environment** — read the version number, build number, language, and install paths without opening a document.
- **Locate shared component paths** — find where Revit's shared templates, families, and content libraries are installed on disk.
- **Control document lifecycle** — subscribe to events for document open, close, save, and synchronize to react programmatically.
- **Bootstrap an add-in** — the `ControlledApplication` is the object passed to `IExternalApplication.OnStartup`; use it to register your ribbon, events, and services at startup.

## Key classes

| Class | Purpose |
|---|---|
| [`Application`](Application-Class.md) | Full application access available inside external commands — version, language, shared paths, open documents, events |
| [`ControlledApplication`](Controlled-Application-Class.md) | Restricted application object passed to `IExternalApplication.OnStartup` — register events and services before a document is open |

## Notable properties

| Property | Class | What it gives you |
|---|---|---|
| `SharedComponentsLocation` | `Application` | Path to Revit's shared content directory |
| `SharedComponentsLocation` | `ControlledApplication` | Same path, available at startup before any document loads |

## Typical usage pattern

```csharp
// In IExternalApplication.OnStartup
public Result OnStartup(UIControlledApplication app)
{
    app.ControlledApplication.DocumentOpened += OnDocumentOpened;
    return Result.Succeeded;
}

// In IExternalCommand.Execute
public Result Execute(ExternalCommandData data, ...)
{
    Application app = data.Application.Application;
    string version = app.VersionNumber;        // e.g. "2026"
    string sharedPath = app.SharedComponentsLocation;
}
```

## Files in this directory

| File | Contents |
|---|---|
| [`Application-Class.md`](Application-Class.md) | Class overview, inheritance, all members |
| [`Application-Properties.md`](Application-Properties.md) | Full property listing |
| [`Application-Shared-Components-Location-Property.md`](Application-Shared-Components-Location-Property.md) | `SharedComponentsLocation` property detail |
| [`Controlled-Application-Class.md`](Controlled-Application-Class.md) | Class overview for startup-time access |
| [`Controlled-Application-Properties.md`](Controlled-Application-Properties.md) | Full property listing |
| [`Controlled-Application-Shared-Components-Location-Property.md`](Controlled-Application-Shared-Components-Location-Property.md) | `SharedComponentsLocation` property detail |
