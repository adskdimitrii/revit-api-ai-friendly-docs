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

Each directory maps to a Revit API namespace. Files inside document classes, methods, properties, enumerations, and events for that namespace.

| Directory | Contents |
|---|---|
| `Autodesk.Revit.ApplicationServices/` | `Application` and `ControlledApplication` — app-wide settings, document access |
| `Autodesk.Revit.Creation/` | `Document` creation methods — union fittings, zones |
| `Autodesk.Revit.DB/` | Core database namespace (~450+ files) — elements, geometry, views, parameters, filters, import/export |
| `Autodesk.Revit.DB.Analysis/` | Energy analysis, MEP analytical segments, generic zones, building schedules |
| `Autodesk.Revit.DB.Architecture/` | Architectural elements — `StairsType`, `StairsPathType` |
| `Autodesk.Revit.DB.DirectContext3D/` | Direct 3D graphics — handle settings, color, visibility, `DrawContext.FlushBuffer` |
| `Autodesk.Revit.DB.Electrical/` | Electrical systems, cable/conductor/wire model, panel schedules, analytical bus data |
| `Autodesk.Revit.DB.Events/` | Event argument classes — `RevitAPISingleEventArgs`, pre/post doc event args |
| `Autodesk.Revit.DB.ExternalService/` | `BuiltInExternalServices` — `GeometryAugmentationService` |
| `Autodesk.Revit.DB.IFC/` | IFC import/export — `ExporterIFC`, `ImporterIFC`, hybrid import options, link enumerations |
| `Autodesk.Revit.DB.Macros/` | `ApplicationEntryPoint` properties |
| `Autodesk.Revit.DB.Mechanical/` | Mechanical systems — `Zone`, duct settings, pressure drop data |
| `Autodesk.Revit.DB.Plumbing/` | Plumbing — pipe fitting/accessory pressure drop, fluid temperature |
| `Autodesk.Revit.DB.Structure/` | Structural API (~200+ files) — rebar, analytical elements, fabric, connections |
| `Autodesk.Revit.UI/` | UI layer — `UIApplication`, `UIControlledApplication`, `PostableCommand` |
| `Autodesk.Revit.UI.Events/` | `FabricationPartBrowserOperation` enumeration |
| `Autodesk.Revit.UI.Macros/` | `ApplicationEntryPoint` events |

---

## `ungrouped/` Directory

Pages that don't belong to a single namespace:

| File | Description |
|---|---|
| `Major-changes-and-renovations-to-the-Revit-API.md` | **What's New in Revit 2026 API** — CefSharp removal, add-in isolation, rebar cranking, electrical overhaul, .NET 8, IFC changes, obsolete API removals |
| `Migrating-From-.NET-4.8-to-.NET-8.md` | Add-in migration guide from .NET 4.8 to .NET 8 |
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
4. **Looking for what changed in 2026?** Start with `ungrouped/Major-changes-and-renovations-to-the-Revit-API.md`.

---

## Regenerate

```bash
python docs/revit/2026/crawl_docs.py
```
