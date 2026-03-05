# Autodesk.Revit.DB.Mechanical

**46 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **model, configure, and query HVAC and mechanical systems**. It covers duct network settings, zone thermal parameters, pressure drop data, and system zone element types used in heating and cooling calculations.

## Key outcomes

- **Configure duct systems** — set friction method, sizing preferences, and routing preferences through `DuctSettings` to control how Revit calculates duct sizing.
- **Read duct fitting pressure drop** — access `DuctFittingAndAccessoryPressureDropData` to retrieve calculated pressure loss coefficients (C-values) for fittings and accessories.
- **Define HVAC zones** — create and configure `Zone` elements with heating/cooling setpoints, air change rates, and humidification/dehumidification targets via `SystemZoneElementType`.
- **Model zone elements** — use `SystemZoneElementType` to specify heating set points, cooling set points, air changes per hour, and humidity control bounds for a thermal zone.

## Key classes

| Class | Purpose |
|---|---|
| `Zone` | An HVAC zone grouping spaces for load calculations |
| `SystemZoneElementType` | Type element that holds heating/cooling setpoints and air quality targets for a zone |
| `DuctSettings` | Document-level settings for duct sizing, friction, and routing |
| `DuctFittingAndAccessoryPressureDropData` | Calculated pressure drop coefficient data for a duct fitting or accessory |
| `DuctPressureDropData` | Pressure drop results for a duct segment |

## Key properties on `SystemZoneElementType`

| Property | Purpose |
|---|---|
| `HeatingSetPoint` | Target temperature for heating mode |
| `CoolingSetPoint` | Target temperature for cooling mode |
| `OutsideAirPerPerson` | Outside air flow per occupant |
| `OutsideAirPerArea` | Outside air flow per unit floor area |
| `AirChangesPerHour` | Minimum air change rate |
| `HumidificationSetPoint` | Minimum relative humidity target |
| `DehumidificationSetPoint` | Maximum relative humidity target |

## Namespace listing

For a full class list see [`../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md`](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md).
