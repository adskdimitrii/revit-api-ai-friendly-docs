# Autodesk.Revit.DB

**~586 files** | Assembly: `RevitAPI.dll`

## What you can do here

This is the **core namespace of the Revit API**. Nearly every interaction with a Revit model — reading, creating, modifying, or deleting elements — goes through this namespace. If you are working with geometry, parameters, views, filters, categories, or model elements of any kind, start here.

## Key outcomes

- **Read and modify model elements** — access any element by `ElementId`, query parameter values, change type assignments, move or rotate geometry.
- **Create elements** — place walls, floors, roofs, families, views, sheets, dimensions, and hundreds of other types.
- **Query with filters** — use `FilteredElementCollector` with element, parameter, and logical filters to efficiently find elements without iterating the whole model.
- **Work with geometry** — create and analyze `Arc`, `Curve`, `Line`, `Solid`, `Face`, `Mesh`, and other geometric primitives; perform boolean operations and intersection tests.
- **Manage views and sheets** — create `ViewPlan`, `ViewSection`, `View3D`; place viewports on sheets; apply view templates.
- **Control parameters** — read and write built-in parameters via `BuiltInParameter`, access shared parameters, create project parameters.
- **Organize by category** — use `BuiltInCategory` to target specific element types in collectors and filters.
- **Import and export** — configure IFC export templates, map parameters, handle DWG/DXF import settings.
- **Handle failures** — subscribe to failure events, suppress or resolve warnings using the failures API.
- **Work with radial and path arrays** — create and modify element arrays programmatically.
- **Model toposolids** — create and edit toposolid terrain elements (Revit 2024+).

## Key classes (selected)

| Class | Purpose |
|---|---|
| `Document` | The root object for any open Revit file — start all transactions here |
| `Element` | Base class for every object in the model |
| `ElementId` | Unique identifier for any element |
| `FilteredElementCollector` | Efficient query engine for finding elements by type, category, or parameter value |
| `Transaction` | Required wrapper for any model modification |
| `Parameter` | Read/write access to a parameter value on an element |
| `BuiltInParameter` | Enumeration of all built-in Revit parameter ids |
| `BuiltInCategory` | Enumeration of all built-in Revit categories |
| `Curve` / `Line` / `Arc` | Geometric curve types |
| `Solid` / `Face` / `Mesh` | 3D geometric bodies and surfaces |
| `XYZ` | 3D point or vector (Revit's fundamental coordinate type) |
| `Transform` | Coordinate-system transformation |
| `ViewPlan` | Floor plan or ceiling plan view |
| `View3D` | 3D perspective or orthographic view |
| `FamilyInstance` | Placed instance of a loadable family |
| `Wall` / `Floor` / `Roof` | Primary architectural element types |
| `Level` | Horizontal datum plane used to anchor elements |
| `Options` | Controls geometry detail level when extracting geometry |

## File naming conventions

Files follow predictable patterns so you can navigate directly:

| Pattern | Example |
|---|---|
| `{Class}-Class.md` | `Wall-Class.md` |
| `{Class}-Methods.md` | `Wall-Methods.md` |
| `{Class}-Properties.md` | `Wall-Properties.md` |
| `{Class}-Events.md` | `Document-Events.md` |
| `{Class}-{Method}-Method.md` | `Wall-Flip-Method.md` |
| `{Class}-{Property}-Property.md` | `Wall-Width-Property.md` |
| `{Enum}-Enumeration.md` | `BuiltInCategory-Enumeration.md` |

## Namespace listing

For a full alphabetical class list see [`../ungrouped/Autodesk.-Revit.-DB-Namespace.md`](../ungrouped/Autodesk.-Revit.-DB-Namespace.md).

## Related namespaces

Sub-namespaces extend `Autodesk.Revit.DB` for specific disciplines:

- [`../Autodesk.Revit.DB.Analysis/`](../Autodesk.Revit.DB.Analysis/README.md) — energy and systems analysis
- [`../Autodesk.Revit.DB.Architecture/`](../Autodesk.Revit.DB.Architecture/README.md) — architectural-specific types
- [`../Autodesk.Revit.DB.Electrical/`](../Autodesk.Revit.DB.Electrical/README.md) — electrical systems
- [`../Autodesk.Revit.DB.Mechanical/`](../Autodesk.Revit.DB.Mechanical/README.md) — mechanical / HVAC systems
- [`../Autodesk.Revit.DB.Plumbing/`](../Autodesk.Revit.DB.Plumbing/README.md) — plumbing systems
- [`../Autodesk.Revit.DB.Structure/`](../Autodesk.Revit.DB.Structure/README.md) — structural engineering
- [`../Autodesk.Revit.DB.IFC/`](../Autodesk.Revit.DB.IFC/README.md) — IFC import/export
