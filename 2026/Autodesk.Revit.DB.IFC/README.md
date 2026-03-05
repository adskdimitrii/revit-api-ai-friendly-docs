# Autodesk.Revit.DB.IFC

**38 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **import and export IFC (Industry Foundation Classes) files** programmatically. It covers both classic and hybrid IFC workflows, giving you fine-grained control over what gets exported, how it maps, and how imported IFC data is handled.

## Key outcomes

- **Export IFC from Revit** — use `ExporterIFC` to configure and execute IFC exports, control building storey mapping, manage level information, and call export utility helpers.
- **Import IFC into Revit** — use `ImporterIFC` and `IFCLink` types to import or link IFC files with configurable mapping options.
- **Use Hybrid IFC import** — configure `IFCHybridImport` and `IFCHybridImportOptions` for the new hybrid import workflow introduced in recent Revit versions, including grid import settings.
- **Control IFC link behavior** — use IFC link enumeration types to manage how linked IFC files reload and resolve.
- **Map Revit elements to IFC entities** — configure type and property set mappings in the export configuration.

## Key classes

| Class | Purpose |
|---|---|
| `ExporterIFC` | Drives an IFC export — access building storey info, level data, and utility methods during export |
| `ImporterIFC` | Drives an IFC import — provides access to the IFC file structure during import |
| `IFCHybridImport` | Manages a hybrid IFC import operation |
| `IFCHybridImportOptions` | Configuration for hybrid IFC import (grid handling, element mapping, etc.) |
| `IFCLinkOptions` | Options controlling how an IFC file is linked into a Revit project |

## Namespace listing

For a full class list see [`../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md`](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md).

## Revit 2026 changes

Hybrid IFC import received updates in 2026. See [`../ungrouped/Major-changes-and-renovations-to-the-Revit-API.md`](../ungrouped/Major-changes-and-renovations-to-the-Revit-API.md) for details.
