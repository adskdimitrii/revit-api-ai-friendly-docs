# Autodesk.Revit.DB.Electrical

**135 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **model, configure, and analyze electrical systems** in Revit. It covers the full stack from cable and conductor definitions through panel schedules to analytical power flow data. This namespace saw significant expansion in Revit 2026 as part of the electrical API overhaul.

## Key outcomes

- **Define cable sizes** — create, read, update, and delete `CableSize` definitions that drive wire sizing in electrical circuits.
- **Configure conductors and insulation** — assign `ConductorMaterial` and `InsulationMaterial` to wiring types to accurately model electrical properties.
- **Perform electrical analysis** — access `AnalyticalBusData`, `AnalyticalEquipmentLoadData`, `AnalyticalPowerSourceData`, `AnalyticalTransformerData`, and `AnalyticalTransferSwitchData` to retrieve calculated load and power flow results.
- **Model per-phase power** — use `ElectricalPerPhaseData` to read current and voltage on individual phases for balanced and unbalanced systems.
- **Build and format panel schedules** — use `PanelSchedule` types to generate, template, and populate electrical panel schedules on sheets.
- **Define wire types** — configure `WireType` conductor count, material, temperature rating, and conduit type.

## Key classes

| Class | Purpose |
|---|---|
| `CableSize` | A named cable size definition (AWG, kcmil, or mm²) |
| `ConductorMaterial` | Copper, aluminum, or custom conductor specification |
| `InsulationMaterial` | THHN, XHHW, or custom insulation specification |
| `AnalyticalBusData` | Analytical results for a bus element (voltage, current, short-circuit data) |
| `AnalyticalEquipmentLoadData` | Calculated load data for electrical equipment |
| `AnalyticalPowerSourceData` | Analytical data for a power source in the distribution system |
| `AnalyticalTransformerData` | Transformer analytical results (kVA, impedance, losses) |
| `AnalyticalTransferSwitchData` | Analytical data for an automatic transfer switch |
| `ElectricalPerPhaseData` | Per-phase current and voltage for a circuit or equipment |
| `PanelScheduleTemplate` | Template controlling the format and content of panel schedules |
| `WireType` | Electrical wire type with conductor and insulation properties |

## Namespace listing

For a full class list see [`../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md`](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md).

## Revit 2026 changes

The electrical namespace received a major overhaul in 2026. If upgrading an add-in, review [`../ungrouped/Major-changes-and-renovations-to-the-Revit-API.md`](../ungrouped/Major-changes-and-renovations-to-the-Revit-API.md) for details on API changes and replacements.
