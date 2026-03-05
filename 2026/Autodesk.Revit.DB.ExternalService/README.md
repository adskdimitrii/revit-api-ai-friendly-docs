# Autodesk.Revit.DB.ExternalService

**3 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **access and reference Revit's built-in external service identifiers**. It provides the static `BuiltInExternalServices` class, which exposes well-known `ExternalServiceId` values that you pass to `ExternalServiceRegistry` when registering a server or retrieving a service.

## Key outcomes

- **Look up the Geometry Augmentation Service ID** — get the `ExternalServiceId` needed to register a server that provides augmented geometry to Revit's graphics pipeline.
- **Avoid hardcoding GUIDs** — use the named property instead of embedding raw GUID strings in your add-in code.

## Key class

| Class | Purpose |
|---|---|
| [`ExternalServices.BuiltInExternalServices`](External-Services-Built-In-External-Services-Class.md) | Static class holding well-known `ExternalServiceId` values for built-in Revit services |

## Key property

| Property | Type | Purpose |
|---|---|---|
| [`GeometryAugmentationService`](External-Services-Built-In-External-Services-Geometry-Augmentation-Service-Property.md) | `ExternalServiceId` | ID of the geometry augmentation service — pass to `ExternalServiceRegistry.GetService()` or when registering a custom geometry server |

## Typical usage pattern

```csharp
ExternalServiceId serviceId =
    ExternalServices.BuiltInExternalServices.GeometryAugmentationService;

IExternalService service = ExternalServiceRegistry.GetService(serviceId);
IList<IGuidedObject> servers = service.GetRegisteredServerIds();
```

## Files in this directory

| File | Contents |
|---|---|
| [`Built-In-External-Services-Properties.md`](Built-In-External-Services-Properties.md) | Full property listing |
| [`External-Services-Built-In-External-Services-Class.md`](External-Services-Built-In-External-Services-Class.md) | Class overview |
| [`External-Services-Built-In-External-Services-Geometry-Augmentation-Service-Property.md`](External-Services-Built-In-External-Services-Geometry-Augmentation-Service-Property.md) | `GeometryAugmentationService` property detail |
