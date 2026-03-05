# Autodesk.Revit.DB.Macros

**2 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace when writing **Revit macro add-ins** (code embedded directly in a `.rvt` or `.rfa` file via the Macro Manager). The `ApplicationEntryPoint` class is the entry point that Revit instantiates when a macro module is loaded.

## Key outcomes

- **Access the macro application entry point** — read properties from `ApplicationEntryPoint` to get the `Application` and `UIApplication` objects available to the macro.
- **Bootstrap macro code** — use the entry point to set up any initialization needed before macro methods are called.

## Key class

| Class | Purpose |
|---|---|
| [`ApplicationEntryPoint`](Application-Entry-Point-Class.md) | Entry point class for Revit macro modules — provides access to the running Revit application |

## Note

This namespace covers only the **DB-layer properties** of the macro entry point. For the **UI-layer events** (e.g., the macro module load/unload events), see [`../Autodesk.Revit.UI.Macros/`](../Autodesk.Revit.UI.Macros/README.md).

## Files in this directory

| File | Contents |
|---|---|
| [`Application-Entry-Point-Class.md`](Application-Entry-Point-Class.md) | Class overview and member list |
| [`Application-Entry-Point-Properties.md`](Application-Entry-Point-Properties.md) | Full property listing |
