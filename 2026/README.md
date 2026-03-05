# Revit API Docs 2026 — Folder Guide

This folder contains a local markdown crawl of the Revit API 2026 reference, sourced from `https://www.revitapidocs.com/2026/sitemap.xml`. 1,273 pages are organized into namespace-based subdirectories.

---

## Root-Level Files

| File | Description |
|---|---|
| `index.md` | Landing page — links to "What's New in Revit 2026 API" and the official Autodesk reference guide |
| `_url_index.md` | Auto-generated map of every source URL to its local markdown file path |
| `crawl_docs.py` | Python script that crawled the sitemap and generated this folder |

---

## Namespace Directories

Each directory maps to a Revit API namespace and has its own `README.md` explaining what you can accomplish with it.

### Application and UI Layer

| Directory | What you can do | Files |
|---|---|---|
| [`Autodesk.Revit.ApplicationServices/`](Autodesk.Revit.ApplicationServices/README.md) | Access Revit version info, locate shared content paths, and subscribe to document lifecycle events. The `ControlledApplication` is your entry point in `IExternalApplication.OnStartup`. | 6 |
| [`Autodesk.Revit.UI/`](Autodesk.Revit.UI/README.md) | Build ribbon UI, access the active document and view, invoke built-in Revit commands via `PostableCommand`, and react to UI events like `ViewActivated` and `Idling`. | 5 |
| [`Autodesk.Revit.UI.Events/`](Autodesk.Revit.UI.Events/README.md) | Identify operations in the fabrication part browser using the `FabricationPartBrowserOperation` enumeration. | 1 |
| [`Autodesk.Revit.UI.Macros/`](Autodesk.Revit.UI.Macros/README.md) | Handle load/unload lifecycle events for Revit macro modules. | 2 |

### Core Model Layer

| Directory | What you can do | Files |
|---|---|---|
| [`Autodesk.Revit.DB/`](Autodesk.Revit.DB/README.md) | **The heart of the Revit API.** Create, read, modify, and delete any model element. Work with geometry (`Curve`, `Solid`, `XYZ`), query elements with `FilteredElementCollector`, manage parameters, control views and sheets, and handle failures. Start here for almost any model operation. | ~586 |
| [`Autodesk.Revit.Creation/`](Autodesk.Revit.Creation/README.md) | Programmatically create MEP connectivity elements — union fittings between connectors, and HVAC zones from sets of spaces — using the `Document` factory object. | 4 |
| [`Autodesk.Revit.DB.Events/`](Autodesk.Revit.DB.Events/README.md) | Build event handlers for document lifecycle events (open, save, sync). Pre-document event args let you cancel operations before they execute. | 3 |
| [`Autodesk.Revit.DB.ExternalService/`](Autodesk.Revit.DB.ExternalService/README.md) | Look up well-known external service IDs (such as the Geometry Augmentation Service) without hardcoding GUIDs. | 3 |
| [`Autodesk.Revit.DB.Macros/`](Autodesk.Revit.DB.Macros/README.md) | Access the `Application` and `UIApplication` objects from within a Revit macro module via `ApplicationEntryPoint`. | 2 |

### Discipline-Specific Namespaces

| Directory | What you can do | Files |
|---|---|---|
| [`Autodesk.Revit.DB.Architecture/`](Autodesk.Revit.DB.Architecture/README.md) | Customize stair path annotation symbols (arrowhead and start symbol) and configure middle stringer support types. | 3 |
| [`Autodesk.Revit.DB.Structure/`](Autodesk.Revit.DB.Structure/README.md) | Place and shape rebar in concrete members, define rebar shapes with hooks and bends, model fabric reinforcement, configure analytical structural members and panels, and assign bar end treatments. Includes rebar cranking (new in 2026). | ~336 |
| [`Autodesk.Revit.DB.Mechanical/`](Autodesk.Revit.DB.Mechanical/README.md) | Configure HVAC zones with heating/cooling setpoints, air changes, and humidity targets. Set duct sizing friction methods and read pressure drop data from fittings. | 46 |
| [`Autodesk.Revit.DB.Electrical/`](Autodesk.Revit.DB.Electrical/README.md) | Define cable and conductor types, build electrical wire types, read analytical load and power flow data (bus, equipment, transformer, transfer switch), retrieve per-phase current and voltage, and generate panel schedules. Received a major overhaul in 2026. | 135 |
| [`Autodesk.Revit.DB.Plumbing/`](Autodesk.Revit.DB.Plumbing/README.md) | Read K-value pressure drop data for pipe fittings and accessories, and set the fluid temperature on piping system types for accurate flow calculations. | 6 |
| [`Autodesk.Revit.DB.Analysis/`](Autodesk.Revit.DB.Analysis/README.md) | Extract energy analysis surfaces, spaces, zones, and openings. Query MEP analytical segment flow and pressure data. Manage generic zones and building operating schedules. Generate systems analysis reports. | 80 |
| [`Autodesk.Revit.DB.IFC/`](Autodesk.Revit.DB.IFC/README.md) | Export Revit models to IFC with `ExporterIFC`, import IFC files (classic and hybrid), configure IFC exchange options, and manage IFC links. | 38 |

### Graphics Extension

| Directory | What you can do | Files |
|---|---|---|
| [`Autodesk.Revit.DB.DirectContext3D/`](Autodesk.Revit.DB.DirectContext3D/README.md) | Render custom 3D geometry directly in Revit viewports as non-persistent overlays. Control per-handle color and visibility, and flush draw buffers at the right time. | 7 |

---

## `ungrouped/` Directory

[`ungrouped/`](ungrouped/README.md) — Cross-cutting reference pages for migration and namespace browsing.

| File | Purpose |
|---|---|
| [`Major-changes-and-renovations-to-the-Revit-API.md`](ungrouped/Major-changes-and-renovations-to-the-Revit-API.md) | **What's New in Revit 2026 API** — CefSharp removal, add-in isolation, rebar cranking, electrical overhaul, .NET 8, IFC changes, obsolete API removals |
| [`Migrating-From-.NET-4.8-to-.NET-8.md`](ungrouped/Migrating-From-.NET-4.8-to-.NET-8.md) | Add-in migration guide from .NET 4.8 to .NET 8 |
| `Autodesk.-Revit.-DB-Namespace.md` | Full class listing for `Autodesk.Revit.DB` |
| `Autodesk.-Revit.-DB.-Electrical-Namespace.md` | Full class listing for the Electrical sub-namespace |
| `Autodesk.-Revit.-DB.-IFC-Namespace.md` | Full class listing for the IFC sub-namespace |
| `Autodesk.-Revit.-DB.-Events-Namespace.md` | Full class listing for the DB Events sub-namespace |
| `Autodesk.-Revit.-DB.-Analysis-Namespace.md` | Full class listing for the Analysis sub-namespace |
| `Autodesk.-Revit.-DB.-Structure-Namespace.md` | Full class listing for the Structure sub-namespace |
| `Autodesk.-Revit.-DB.-Mechanical-Namespace.md` | Full class listing for the Mechanical sub-namespace |

---

## Finding a Specific Class or Method

1. **Know the namespace?** Go directly to the matching directory and look for a file named after the class.
2. **Know the URL?** Search `_url_index.md` for the URL to get the local file path.
3. **Unsure of namespace?** Check the namespace listing files in `ungrouped/` (e.g., `Autodesk.-Revit.-DB-Namespace.md`) to locate the class, then navigate to its directory.
4. **Looking for what changed in 2026?** Start with [`ungrouped/Major-changes-and-renovations-to-the-Revit-API.md`](ungrouped/Major-changes-and-renovations-to-the-Revit-API.md).
5. **Not sure where to start?** See each namespace's `README.md` for outcome-oriented guidance on what you can accomplish.

---

## Regenerate

```bash
python docs/revit/2026/crawl_docs.py
```
