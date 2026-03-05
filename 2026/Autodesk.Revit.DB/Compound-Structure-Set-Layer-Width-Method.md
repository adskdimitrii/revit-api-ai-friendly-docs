# Compound Structure Set Layer Width Method

Source: https://www.revitapidocs.com/2026/9b801ee8-b10b-dbef-313d-b0ef0d555ea4.htm

---

| Compound Structure Set Layer Width Method |
| --- |

Sets the width of a specified layer. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetLayerWidth(
	int layerIdx,
	double width
)
```

```
Public Sub SetLayerWidth ( 
	layerIdx As Integer,
	width As Double
)
```

```
public:
void SetLayerWidth(
	int layerIdx, 
	double width
)
```

```
member SetLayerWidth : 
        layerIdx : int * 
        width : float -> unit 
```

#### Parameters

layerIdx Int32
:   Index of a layer in the CompoundStructure. The layer index is zero based. It counts from the exterior of wall and from the top of roofs, floors and ceilings.

width Double
:   The new width of the specified layer.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The width of the layer is not valid. |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | If the region of the layer is not a simple region. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If the structure is vertically compound, and the layer is associated to a single simple region,
 the width of that region is adjusted. If layerIdx is 0 or LayerCount\-1,
 and there is no associated region in the VerticalRegionsStructure, one will be created and associated to the layer.
 If the specified layer index is associated to a simple region, and the width is set to 0\.0, that region will be deleted. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[CompoundStructure Class](Compound-Structure-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
