# Autodesk.Revit.Creation

**4 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **programmatically create new Revit MEP elements** using the `Document` factory object. This is a focused creation sub-namespace for MEP connectivity elements.

## Key outcomes

- **Create union fittings** between two connectors to programmatically join piping or duct runs.
- **Create HVAC/MEP zones** from a set of spaces to group them for analysis or scheduling.

## Key class

| Class | Purpose |
|---|---|
| [`Document`](Document-Class.md) | Factory class — access via `Document.Create` to call element creation methods |

## Key creation methods

| Method | What it creates |
|---|---|
| [`NewUnionFitting`](Document-New-Union-Fitting-Method.md) | A union fitting between two connectors in a piping or duct system |
| [`NewZone`](Document-New-Zone-Method.md) | A new zone from a phase and a set of spaces |

## Typical usage pattern

```csharp
// Access the creation document from your active document
Autodesk.Revit.Creation.Document creDoc = doc.Create;

// Create a zone
Phase phase = ...; // get from document phases
IList<Space> spaces = ...; // spaces to include
Zone zone = creDoc.NewZone(phase, spaces);
```

## Files in this directory

| File | Contents |
|---|---|
| [`Document-Class.md`](Document-Class.md) | Class overview and all members |
| [`Document-Methods.md`](Document-Methods.md) | Full method listing |
| [`Document-New-Union-Fitting-Method.md`](Document-New-Union-Fitting-Method.md) | `NewUnionFitting` signature and parameters |
| [`Document-New-Zone-Method.md`](Document-New-Zone-Method.md) | `NewZone` signature and parameters |
