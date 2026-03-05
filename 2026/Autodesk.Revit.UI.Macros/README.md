# Autodesk.Revit.UI.Macros

**2 files** | Assembly: `RevitAPIUI.dll`

## What you can do here

Use this namespace to **handle UI-level lifecycle events for Revit macro modules**. It extends the macro entry point with events that fire when the macro application starts and stops.

## Key outcomes

- **React to macro module load/unload** — subscribe to events on `ApplicationEntryPoint` to run initialization or cleanup logic when a macro module is loaded into or unloaded from Revit.

## Key class

| Class | Purpose |
|---|---|
| [`ApplicationEntryPoint`](Application-Entry-Point-Class.md) | UI-layer macro entry point — provides events for module lifecycle |

## Note

This namespace covers only the **UI-layer events** of the macro entry point. For the **DB-layer properties**, see [`../Autodesk.Revit.DB.Macros/`](../Autodesk.Revit.DB.Macros/README.md).

## Files in this directory

| File | Contents |
|---|---|
| [`Application-Entry-Point-Class.md`](Application-Entry-Point-Class.md) | Class overview and member list |
| [`Application-Entry-Point-Events.md`](Application-Entry-Point-Events.md) | Full event listing |
