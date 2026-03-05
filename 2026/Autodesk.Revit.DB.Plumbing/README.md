# Autodesk.Revit.DB.Plumbing

**6 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **model and configure plumbing system properties**. It focuses on pipe fitting pressure drop calculations and piping system fluid temperature settings.

## Key outcomes

- **Read pipe fitting pressure drop data** — access `PipeFittingAndAccessoryPressureDropItem` to retrieve the calculated pressure loss for individual pipe fittings and accessories, including the connector indices and loss coefficient.
- **Configure fluid temperature** — set the `FluidTemperature` property on `PipingSystemType` to define the operating temperature used in flow and pressure calculations.

## Key classes

| Class | Purpose |
|---|---|
| `PipeFittingAndAccessoryPressureDropItem` | Represents calculated pressure drop data for a single pipe fitting or accessory |
| `PipingSystemType` | Piping system type element (defined in `Autodesk.Revit.DB`; `FluidTemperature` property added here) |

## Key properties on `PipeFittingAndAccessoryPressureDropItem`

| Property | Purpose |
|---|---|
| `BeginConnectorIndex` | Index of the upstream connector in the pressure drop calculation |
| `EndConnectorIndex` | Index of the downstream connector in the pressure drop calculation |
| `Coefficient` | The dimensionless loss coefficient (K-value) for this fitting |

## Files in this directory

| File | Contents |
|---|---|
| [`Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Class.md`](Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Class.md) | Class overview |
| [`Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Methods.md`](Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Methods.md) | Method listing |
| [`Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Properties.md`](Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Properties.md) | Property listing |
| [`Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Begin-Connector-Index-Property.md`](Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Begin-Connector-Index-Property.md) | `BeginConnectorIndex` detail |
| [`Pipe-Fitting-And-Accessory-Pressure-Drop-Item-End-Connector-Index-Property.md`](Pipe-Fitting-And-Accessory-Pressure-Drop-Item-End-Connector-Index-Property.md) | `EndConnectorIndex` detail |
| [`Piping-System-Type-Fluid-Temperature-Property.md`](Piping-System-Type-Fluid-Temperature-Property.md) | `FluidTemperature` property detail |
