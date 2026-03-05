# Compound Structure Set Layer Method

Source: https://www.revitapidocs.com/2026/3a7e18fd-fcd4-1335-ce10-841d2bfd2322.htm

---

| Compound Structure Set Layer Method |
| --- |

Sets a single layer for this CompoundStructure. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetLayer(
	int layerIdx,
	CompoundStructureLayer layer
)
```

```
Public Sub SetLayer ( 
	layerIdx As Integer,
	layer As CompoundStructureLayer
)
```

```
public:
void SetLayer(
	int layerIdx, 
	CompoundStructureLayer^ layer
)
```

```
member SetLayer : 
        layerIdx : int * 
        layer : CompoundStructureLayer -> unit 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

layer [CompoundStructureLayer](Compound-Structure-Layer-Class.md)
:   The layer to be set.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The layer is not valid for this operation. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is valid only for non\-vertically compound structures. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This function does not support addition of new layers, use SetLayers() to change the number of layers. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
