# Autodesk.Revit.DB.Analysis

**80 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **run and consume energy analysis, MEP systems analysis, and generic zone management**. It provides access to the analytical layer that sits beneath MEP and architectural models, enabling data extraction for energy simulation, flow balancing, and systems performance reporting.

## Key outcomes

- **Build energy models** — access energy analysis surfaces, openings, spaces, and zones to assemble data for energy simulation export (e.g., gbXML).
- **Query MEP analytical data** — read pressure drop coefficients, flow characteristics, and segment data from analytical MEP models.
- **Manage generic zones** — create and modify `GenericZone` elements either from sketch boundaries or from sets of spaces.
- **Configure building schedules** — set up building operating schedules (occupied/unoccupied hours, setpoints) for energy analysis inputs.
- **Generate systems analysis reports** — use `ViewSystemsAnalysisReport` to produce and style MEP systems performance reports.
- **Control energy analysis settings** — adjust `EnergyDataSettings` to configure the project's energy analysis parameters including building type, location, and construction.

## Key classes

| Class | Purpose |
|---|---|
| `EnergyAnalysisDetailModel` | Top-level model for energy analysis — access all surfaces, spaces, zones, and openings |
| `EnergyAnalysisSurface` | Represents a wall/floor/roof surface in the energy model |
| `EnergyAnalysisSpace` | An enclosed space in the energy model |
| `EnergyAnalysisZone` | A zone grouping spaces for energy simulation |
| `EnergyAnalysisOpening` | A window, door, or other opening in the energy model |
| `EnergyDataSettings` | Project-level energy analysis configuration (building type, ground reflectance, etc.) |
| `GenericZone` | A groupable zone element, either sketch-based or space-aggregated |
| `MEPAnalyticalSegment` | Duct or pipe segment with flow and pressure-drop analytical data |
| `BuildingOperatingSchedule` | Occupied/unoccupied time schedule used as energy analysis input |
| `ViewSystemsAnalysisReport` | A view type that displays MEP systems analysis results |

## Namespace listing

For a full class list see [`../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md`](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md).
