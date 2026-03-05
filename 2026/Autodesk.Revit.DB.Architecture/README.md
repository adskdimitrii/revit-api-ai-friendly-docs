# Autodesk.Revit.DB.Architecture

**3 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **control architectural stair appearance and type properties**. It exposes a small set of properties for customizing stair path annotations and support configurations.

## Key outcomes

- **Customize stair path annotation symbols** — set the arrowhead type and start symbol for stair path annotations to match project standards.
- **Configure middle stringer support** — control the structural support type used for the middle stringer of stair types.

## Key properties

| Property | Class | Purpose |
|---|---|---|
| [`ArrowheadTypeId`](Stairs-Path-Type-Arrowhead-Type-Id-Property.md) | `StairsPathType` | `ElementId` of the arrowhead family used on the stair path annotation |
| [`StartSymbolTypeId`](Stairs-Path-Type-Start-Symbol-Type-Id-Property.md) | `StairsPathType` | `ElementId` of the symbol placed at the start of the stair path |
| [`MiddleSupportType`](Stairs-Type-Middle-Support-Type-Property.md) | `StairsType` | Enumeration value controlling the middle stringer support geometry |

## Note

The base `Stairs`, `StairsType`, `StairsPathType`, and related classes are defined in the parent `Autodesk.Revit.DB` namespace. This sub-namespace only adds the three specific properties listed above.

## Files in this directory

| File | Contents |
|---|---|
| [`Stairs-Path-Type-Arrowhead-Type-Id-Property.md`](Stairs-Path-Type-Arrowhead-Type-Id-Property.md) | `ArrowheadTypeId` detail |
| [`Stairs-Path-Type-Start-Symbol-Type-Id-Property.md`](Stairs-Path-Type-Start-Symbol-Type-Id-Property.md) | `StartSymbolTypeId` detail |
| [`Stairs-Type-Middle-Support-Type-Property.md`](Stairs-Type-Middle-Support-Type-Property.md) | `MiddleSupportType` detail |
