# Compound Structure Set Layer Priority Method

Source: https://www.revitapidocs.com/2026/f3a56c5b-5aaa-5a45-5090-94e6f94e4d97.htm

---

| Compound Structure Set Layer Priority Method |
| --- |

Sets the priority of the specific layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetLayerPriority(
	int layerIdx,
	int priority
)
```

```
Public Sub SetLayerPriority ( 
	layerIdx As Integer,
	priority As Integer
)
```

```
public:
void SetLayerPriority(
	int layerIdx, 
	int priority
)
```

```
member SetLayerPriority : 
        layerIdx : int * 
        priority : int -> unit 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

priority Int32
:   The priority of the layer.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The priority of the layer is not valid. |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The effective priority value should be between 1\-5\. Membrane layers should not have a priority, the value should be 999\.
 You should set the layer priority if you want a customized priority value rather than the default one by function.
 In shell, a non\-membrane layer which is closer to the core should not have a lower priority. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
