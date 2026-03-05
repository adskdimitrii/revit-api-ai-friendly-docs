# Autodesk.Revit.UI

**5 files** | Assembly: `RevitAPIUI.dll`

## What you can do here

Use this namespace to **interact with the Revit user interface from your add-in** — build ribbon UI, respond to UI events, invoke built-in Revit commands, and access the active view and selection.

## Key outcomes

- **Invoke built-in Revit commands** — use the `PostableCommand` enumeration with `UIApplication.PostCommand()` to trigger any built-in Revit command (e.g., open a dialog, start a tool) from your add-in code.
- **Access the active document and view** — use `UIApplication.ActiveUIDocument` to get the current document, active view, and selection.
- **Register ribbon UI at startup** — receive `UIControlledApplication` in `IExternalApplication.OnStartup` to add ribbon tabs, panels, and buttons.
- **Handle UI-level events** — subscribe to `UIApplication` events such as `ViewActivated`, `ApplicationClosing`, and `Idling` to react to UI state changes.
- **Display dialogs and task dialogs** — use `TaskDialog` (in `Autodesk.Revit.DB`) from within the `UIApplication` context.

## Key classes

| Class | Purpose |
|---|---|
| [`UIApplication`](UIApplication-Class.md) | The main UI-layer application object available inside external commands — active document, post commands, events |
| [`UIControlledApplication`](UIControlled-Application-Class.md) | Restricted UI app object passed to `IExternalApplication.OnStartup` — register ribbon and events |
| [`PostableCommand`](Postable-Command-Enumeration.md) | Enumeration of every built-in Revit command that can be invoked via `PostCommand()` |

## Key events on `UIApplication`

| Event | Fires when |
|---|---|
| `ViewActivated` | The active view changes |
| `Idling` | Revit is idle and available for API calls |
| `ApplicationClosing` | Revit is about to shut down |
| `DialogBoxShowing` | A Revit dialog box is about to appear |

## Typical usage pattern

```csharp
// In IExternalApplication.OnStartup — register ribbon
public Result OnStartup(UIControlledApplication app)
{
    RibbonPanel panel = app.CreateRibbonPanel("My Tools");
    panel.AddItem(new PushButtonData("MyCmd", "Run", assemblyPath, "MyNamespace.MyCommand"));
    return Result.Succeeded;
}

// In IExternalCommand.Execute — post a command or access active view
public Result Execute(ExternalCommandData data, ...)
{
    UIApplication uiApp = data.Application;
    View activeView = uiApp.ActiveUIDocument.ActiveView;
    uiApp.PostCommand(RevitCommandId.LookupPostableCommandId(PostableCommand.Save));
}
```

## Files in this directory

| File | Contents |
|---|---|
| [`UIApplication-Class.md`](UIApplication-Class.md) | Class overview and all members |
| [`UIApplication-Events.md`](UIApplication-Events.md) | Full event listing |
| [`UIControlled-Application-Class.md`](UIControlled-Application-Class.md) | Startup-time UI app class |
| [`UIControlled-Application-Events.md`](UIControlled-Application-Events.md) | Startup-time event listing |
| [`Postable-Command-Enumeration.md`](Postable-Command-Enumeration.md) | All `PostableCommand` enum values |
