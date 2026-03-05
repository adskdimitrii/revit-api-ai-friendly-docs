# Draw Context Flush Buffer Method

Source: https://www.revitapidocs.com/2026/e216a4c0-6a88-cf2c-35fa-8f43019db61d.htm

---

| Draw Context Flush Buffer Method |
| --- |

Submits geometry for rendering. 
**Namespace:** [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static void FlushBuffer(
	VertexBuffer vertexBuffer,
	int vertexCount,
	IndexBuffer indexBuffer,
	int indexCount,
	VertexFormat vertexFormat,
	EffectInstance effectInstance,
	PrimitiveType primitiveType,
	int start,
	int primitiveCount
)
```

```
Public Shared Sub FlushBuffer ( 
	vertexBuffer As VertexBuffer,
	vertexCount As Integer,
	indexBuffer As IndexBuffer,
	indexCount As Integer,
	vertexFormat As VertexFormat,
	effectInstance As EffectInstance,
	primitiveType As PrimitiveType,
	start As Integer,
	primitiveCount As Integer
)
```

```
public:
static void FlushBuffer(
	VertexBuffer^ vertexBuffer, 
	int vertexCount, 
	IndexBuffer^ indexBuffer, 
	int indexCount, 
	VertexFormat^ vertexFormat, 
	EffectInstance^ effectInstance, 
	PrimitiveType primitiveType, 
	int start, 
	int primitiveCount
)
```

```
static member FlushBuffer : 
        vertexBuffer : VertexBuffer * 
        vertexCount : int * 
        indexBuffer : IndexBuffer * 
        indexCount : int * 
        vertexFormat : VertexFormat * 
        effectInstance : EffectInstance * 
        primitiveType : PrimitiveType * 
        start : int * 
        primitiveCount : int -> unit 
```

#### Parameters

vertexBuffer [VertexBuffer](329e5617-ce46-a993-1131-85c64f0842f2.htm)
:   The vertex buffer that contains vertex data.

vertexCount Int32
:   The number of vertices in the vertex buffer.

indexBuffer [IndexBuffer](186f6b15-38c7-cee7-6163-396cfdea43ee.htm)
:   The index buffer that contains indices into the vertex buffer.

indexCount Int32
:   The number of indices in the index buffer.

vertexFormat [VertexFormat](a946fa2b-bb1f-202c-38dc-8ae0307bedac.htm)
:   The format of the vertices in the vertex buffer.

effectInstance [EffectInstance](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.htm)
:   The effect instance to be used for drawing this piece of geometry.

primitiveType [PrimitiveType](f0b47a17-85be-d631-10c1-76358114f7dc.htm)
:   The type of geometry primitive used in the index buffer.

start Int32
:   The first index to use for drawing.

primitiveCount Int32
:   The number of primitives to draw.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | A change in the graphics state has made the vertex buffer vertexBuffer invalid for rendering.  \-or\-  A change in the graphics state has made the indexBuffer invalid for rendering, or indexBuffer is null and indexCount is not zero.  \-or\-  A change in the graphics state has made the vertex format vertexFormat invalid for rendering.  \-or\-  A change in the graphics state has made the effect instance effectInstance invalid for rendering.  \-or\-  The vertex format vertexFormat and the effect instance effectInstance do not match. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This DrawContext is not available because Revit is not currently rendering. In general, this DrawContext must be used in the scope of the RenderScene() callback of IDirectContext3DServer. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[DrawContext Class](b9244325-08c8-8bbd-a9f3-5d91d638d85d.htm) [Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)
