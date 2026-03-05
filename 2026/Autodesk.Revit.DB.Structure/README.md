# Autodesk.Revit.DB.Structure

**~336 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **model structural elements, place reinforcement, and work with the structural analytical model**. It is the second largest namespace in the Revit API and covers everything from rebar placement and shaping to analytical members and fabric reinforcement.

## Key outcomes

- **Place and configure rebar** — create `Rebar` elements in concrete members, assign `RebarBarType` and `RebarShape`, control bar sets, spacing, and cover with `RebarCoverType`.
- **Define rebar shapes** — build custom `RebarShape` definitions with bend angles, hook data (`RebarHookType`), and termination geometry using `RebarShapeTerminationsData`.
- **Model rebar cranking** — configure crank offsets and bar terminations using the rebar cranking API (new in Revit 2026).
- **Place fabric reinforcement** — add `FabricReinforcement` sheets to slabs with `FabricSheet` and `FabricWireRun` definitions.
- **Work with the analytical model** — read and write `AnalyticalMember`, `AnalyticalPanel`, `AnalyticalOpening`, and `AnalyticalElement` objects for structural analysis export.
- **Define end treatments** — assign `EndTreatmentType` to bar ends for standard structural detailing of lap splices, mechanical couplers, and headed bars.
- **Query bar termination data** — use `BarTerminationsData` and `RebarShapeTerminationsData` to inspect how bars terminate at their start and end.

## Key classes

| Class | Purpose |
|---|---|
| `Rebar` | Individual rebar element placed in a concrete host |
| `RebarBarType` | Type element defining bar diameter, material, and deformation |
| `RebarShape` | Parametric shape definition (bend geometry, hooks) |
| `RebarHookType` | Hook geometry type at rebar ends |
| `RebarCoverType` | Cover distance type assigned to a concrete member |
| `RebarContainer` | Container for multi-bar rebar elements |
| `FabricReinforcement` | Fabric reinforcement sheet element |
| `FabricSheet` | Type element defining the fabric wire layout |
| `FabricWireRun` | Configuration of major/minor wire runs in a fabric sheet |
| `AnalyticalMember` | Linear analytical structural member (beam, column, brace) |
| `AnalyticalPanel` | Planar analytical structural element (wall, slab) |
| `AnalyticalOpening` | Analytical opening in a panel |
| `EndTreatmentType` | Type defining how a rebar end is terminated (hook, coupler, headed) |
| `BarTerminationsData` | Data object for bar end treatment assignments |

## File naming conventions

Files follow the same patterns as `Autodesk.Revit.DB`:

| Pattern | Example |
|---|---|
| `{Class}-Class.md` | `Rebar-Class.md` |
| `{Class}-Methods.md` | `Rebar-Methods.md` |
| `{Class}-Properties.md` | `Rebar-Properties.md` |
| `{Class}-{Method}-Method.md` | `Rebar-Get-Hook-Orientation-Method.md` |
| `{Enum}-Enumeration.md` | `RebarHookOrientation-Enumeration.md` |

## Namespace listing

For a full class list see [`../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md`](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md).

## Revit 2026 changes

Rebar cranking API was added in 2026. See [`../ungrouped/Major-changes-and-renovations-to-the-Revit-API.md`](../ungrouped/Major-changes-and-renovations-to-the-Revit-API.md) for details.
