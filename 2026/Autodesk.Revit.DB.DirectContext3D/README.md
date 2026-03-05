# Autodesk.Revit.DB.DirectContext3D

**7 files** | Assembly: `RevitAPI.dll`

## What you can do here

Use this namespace to **render custom 3D graphics directly in the Revit viewport** without creating persistent model elements. It is the low-level drawing API for add-ins that need to display overlays, decorators, or visualization geometry that lives outside the Revit model database.

## Key outcomes

- **Draw custom 3D geometry** in any Revit view — lines, meshes, and solid geometry rendered as viewport overlays.
- **Control handle appearance** — configure per-handle color and visibility using `DirectContext3DHandleSettings` to distinguish multiple graphic objects.
- **Flush draw buffers** — explicitly flush pending draw calls via `DrawContext.FlushBuffer` to control rendering timing.
- **Build visualization add-ins** — implement `IDirectContext3DServer` to provide a persistent custom graphics server that Revit queries each frame.

## Key classes

| Class | Purpose |
|---|---|
| [`DirectContext3DHandleSettings`](Direct-Context-3DHandle-Settings-Class.md) | Per-handle settings for color and visibility of custom graphic objects |
| `DrawContext` | Static context for issuing draw calls; `FlushBuffer` commits pending geometry |

## Key members

| Member | Class | Purpose |
|---|---|---|
| `Color` | `DirectContext3DHandleSettings` | Sets the display color for a handle's geometry |
| `Visibility` | `DirectContext3DHandleSettings` | Controls whether the handle's geometry is visible |
| [`FlushBuffer`](Draw-Context-Flush-Buffer-Method.md) | `DrawContext` | Flushes buffered draw calls to the viewport |

## Typical usage pattern

```csharp
// Implement IDirectContext3DServer, then in RenderScene:
public void RenderScene(View view, DisplayStyle displayStyle)
{
    DrawContext.SetWorldTransform(Transform.Identity);
    // ... build VertexBuffer and IndexBuffer ...
    DrawContext.FlushBuffer(vertexBuffer, vertexCount,
                            indexBuffer, indexCount,
                            VertexFormatBits.Position,
                            effectInstance, PrimitiveType.TriangleList, 0, triangleCount);
}
```

## Files in this directory

| File | Contents |
|---|---|
| [`Direct-Context-3DHandle-Settings-Class.md`](Direct-Context-3DHandle-Settings-Class.md) | Class overview |
| [`Direct-Context-3DHandle-Settings-Methods.md`](Direct-Context-3DHandle-Settings-Methods.md) | Method listing |
| [`Direct-Context-3DHandle-Settings-Properties.md`](Direct-Context-3DHandle-Settings-Properties.md) | Property listing |
| [`Direct-Context-3DHandle-Settings-Color-Property.md`](Direct-Context-3DHandle-Settings-Color-Property.md) | `Color` property detail |
| [`Direct-Context-3DHandle-Settings-Visibility-Property.md`](Direct-Context-3DHandle-Settings-Visibility-Property.md) | `Visibility` property detail |
| [`Draw-Context-Flush-Buffer-Method.md`](Draw-Context-Flush-Buffer-Method.md) | `FlushBuffer` overloads and parameters |
